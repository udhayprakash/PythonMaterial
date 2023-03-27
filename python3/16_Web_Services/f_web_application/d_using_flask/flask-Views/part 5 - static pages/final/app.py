import flask
import settings
from login import Login

# Views
from main import Main
from music import Music
from remote import Remote

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule("/", view_func=Main.as_view("main"), methods=["GET"])
app.add_url_rule("/<page>/", view_func=Main.as_view("page"), methods=["GET"])
app.add_url_rule("/login/", view_func=Login.as_view("login"), methods=["GET", "POST"])
app.add_url_rule(
    "/remote/", view_func=Remote.as_view("remote"), methods=["GET", "POST"]
)
app.add_url_rule("/music/", view_func=Music.as_view("music"), methods=["GET"])


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template("404.html"), 404


app.debug = True
app.run()
