# 3.def get_all_info_about_track():
#     # *
#     # show time of all tracks of all albums in hours
#     # use info about all tracks
#     pass

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/track-hours")
def get_track_hours_info():
    pass

if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
    