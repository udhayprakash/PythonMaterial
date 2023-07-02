import os

import flask
import flask.views
import utils


class Music(flask.views.MethodView):
    @utils.login_required
    def get(self):
        songs = os.listdir("static/music")
        return flask.render_template("music.html", songs=songs)
