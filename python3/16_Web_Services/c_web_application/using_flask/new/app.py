#!/usr/bin/python3
from flask import Flask
from uuid import uuid4


app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid4())


IDP_CONFIG = {
  "well_known_url": "Identity Provider wellknown url: https://{TENANT}.auth0.com/.well-known/openid-configuration",
  "client_id": "Your app client ID",
  "client_secret": "Your app client secret",
  "scope": ["profile", "email", "openid"]
}

import requests
from flask import url_for
from requests_oauthlib import OAuth2Session


def get_well_known_metadata():
    response = requests.get(IDP_CONFIG["well_known_url"])
    response.raise_for_status()
    return response.json()


def get_oauth2_session(**kwargs):
    oauth2_session = OAuth2Session(IDP_CONFIG["client_id"],
                                   scope=IDP_CONFIG["scope"],
                                   redirect_uri=url_for(".callback", _external=True),
                                   **kwargs)
    return oauth2_session


from flask import redirect, session


@app.route("/login")
def login():
    well_known_metadata = get_well_known_metadata()
    oauth2_session = get_oauth2_session()
    authorization_url, state = oauth2_session.authorization_url(well_known_metadata["authorization_endpoint"])
    session["oauth_state"] = state
    return redirect(authorization_url)


from flask import request


@app.route("/callback")
def callback():
    well_known_metadata = get_well_known_metadata()
    oauth2_session = get_oauth2_session(state=session["oauth_state"])
    session["oauth_token"] = oauth2_session.fetch_token(well_known_metadata["token_endpoint"],
                                                        client_secret=IDP_CONFIG["client_secret"],
                                                        code=request.args["code"])["id_token"]
    return "ok"


@app.route("/user/token")
def get_user_token():
    return session["oauth_token"]


import jwt
from jwt import PyJWKClient
from jwt.exceptions import DecodeError
from werkzeug.exceptions import InternalServerError, Unauthorized


def get_jwks_client():
    well_known_metadata = get_well_known_metadata()
    jwks_client = PyJWKClient(well_known_metadata["jwks_uri"])
    return jwks_client


jwks_client = get_jwks_client()


@app.before_request
def verify_and_decode_token():
    if request.endpoint not in {"login", "callback"}:
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        elif "oauth_token" in session:
            token = session["oauth_token"]
        else:
            return Unauthorized("Missing authorization token")

        try:
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            header_data = jwt.get_unverified_header(token)
            request.user_data = jwt.decode(token,
                                           signing_key.key,
                                           algorithms=[header_data['alg']],
                                           audience=IDP_CONFIG["client_id"])
        except DecodeError:
            return Unauthorized("Authorization token is invalid")
        except Exception:
            return InternalServerError("Error authenticating client")


@app.route("/user/id")
def get_user_id():
    return request.user_data["email"]


if __name__ == "__main__":
    app.run()
