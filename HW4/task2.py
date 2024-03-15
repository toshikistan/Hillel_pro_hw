# 2.def get_all_info_about_track():
#     # join all possible tables and show all possible info about all tracks
#     # as input track ID
#     pass

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/track-info")
def get_all_info_about_track():
    pass

if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
