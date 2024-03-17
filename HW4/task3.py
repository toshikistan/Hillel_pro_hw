# 3.def get_all_info_about_track():
#     # *
#     # show time of all tracks of all albums in hours
#     # use info about all tracks
#     pass

from flask import Flask
from process_request import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/album-hours")
@use_kwargs(
    {
        'albumid': fields.Int(
            missing=None,
        )
    },
    location='query'
)
def get_album_hours_info(albumid):
    if albumid:
        query = """
        --sql
        SELECT 
            albums.AlbumId, 
            albums.Title, 
            SUM(tracks.Milliseconds) / 3600000.0 AS Hours
        FROM 
            albums
        JOIN 
            tracks ON albums.AlbumId = tracks.AlbumId
        WHERE 
            tracks.AlbumID = ?
        GROUP BY 
            albums.AlbumId, 
            albums.Title
        ;
        """
        result = execute_query(query=query, args=(albumid,))
    else:
        query = """
        --sql
        SELECT 
            albums.AlbumId, 
            albums.Title, 
            SUM(tracks.Milliseconds) / 3600000.0 AS Hours
        FROM 
            albums
        JOIN 
            tracks ON albums.AlbumId = tracks.AlbumId
        GROUP BY 
            albums.AlbumId, 
            albums.Title
        ;
        """
        result = execute_query(query=query)
    return result


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
