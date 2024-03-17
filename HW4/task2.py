# 2.def get_all_info_about_track():
#     # join all possible tables and show all possible info about all tracks
#     # as input track ID
#     pass

from flask import Flask
from process_request import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/track-info")
@use_kwargs(
    {
        'trackid': fields.Int(
            missing=None,
        )
    },
    location='query'
)
def get_all_info_about_track(trackid):
    if trackid:
        query = """
        --sql
    SELECT 
        tracks.TrackID, 
        tracks.Name,
        albums.Title AS Album, 
        tracks.Composer, 
        tracks.Milliseconds, 
        tracks.Bytes, 
        tracks.UnitPrice,
        genres.Name AS Genre,
        media_types.Name AS TypeID,
        playlists.Name AS PlaylistName,
        artists.Name AS ArtistName
    FROM 
        tracks
    JOIN 
        albums ON tracks.AlbumID = albums.AlbumID
    JOIN 
        genres ON tracks.GenreId = genres.GenreId
    JOIN 
        media_types ON tracks.MediaTypeId = media_types.MediaTypeId
    JOIN 
        playlist_track ON tracks.TrackID = playlist_track.TrackID
    JOIN 
        playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    JOIN
        artists ON albums.ArtistId = artists.ArtistId
    WHERE 
        tracks.TrackID = ?;
        """
        result = execute_query(query=query, args=(trackid,))
    else:
        query = """
        --sql
        SELECT tracks.TrackId, tracks.Name FROM tracks;
        """
        result = execute_query(query=query)
    return result


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
