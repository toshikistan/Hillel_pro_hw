from flask import Flask
from process_request import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/order-price")
@use_kwargs(
    {
        'country': fields.Str(
            missing=None
        )
    },
    location='query'
)
def show_order_price(country):
    if country:
        query = """
        SELECT 
            customers.Country, 
            SUM(invoice_items.UnitPrice * invoice_items.Quantity)
        FROM 
            invoice_items
        JOIN 
            invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        JOIN 
            customers ON invoices.CustomerId = customers.CustomerId
        WHERE 
            customers.Country = ?
        GROUP BY 
            customers.Country;
        """
        result = execute_query(query=query, args=(country,))
    else:
        query = """
        SELECT
            customers.Country, 
            SUM(invoice_items.UnitPrice * invoice_items.Quantity)
        FROM 
            invoice_items 
        JOIN 
            invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        JOIN 
            customers ON invoices.CustomerId = customers.CustomerId
        GROUP BY 
            customers.Country;
        """
        result = execute_query(query=query)

    return result


@app.route("/track-info")
@use_kwargs(
    {
        'trackid': fields.Int(
            missing=None,
        ),
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
        playlists.PlaylistId,
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


@app.route("/album-hours")
@use_kwargs(
    {
        'albumid': fields.Int(
            missing=None,
        ),
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
            SUM(tracks.Milliseconds) / 3600000.0
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
            SUM(tracks.Milliseconds) / 3600000.0
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
