# 2. Створити view яка на вхід приймає стиль музики. Має вивести місто
# в якому найбільше слухають цей стиль музики. Якшо жанра немає вивести повідомлення.
# genre - обов'язковий параметер.
# /stats_by_city?genre=HipHop

from flask import Flask
from process_request import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route('/')
def Hello_world():
    return "<p>Hello, world!</p>"


@app.route('/stats_by_city')
@use_kwargs(
    {
        'genre': fields.Str(
            missing=None
        )
    },
    location='query'
)
def find_city_genre(genre=None):
    if genre:
        query = """
        --sql
        SELECT
            City,
            Name,
            GenreCounts
        FROM
            (SELECT
                customers.City,
                genres.Name,
                COUNT(*) AS GenreCounts,
                DENSE_RANK() OVER (PARTITION BY genres.Name ORDER BY COUNT(*) DESC) AS DRank
            FROM
                customers
                JOIN invoices ON customers.CustomerId = invoices.CustomerId
                JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
                JOIN tracks ON invoice_items.TrackId = tracks.TrackId
                JOIN genres ON tracks.GenreId = genres.GenreId
            WHERE
                genres.Name = ?
            GROUP BY
                customers.City,
                genres.Name) AS ranked_cities
        WHERE
            DRank = 1
        ORDER BY
            GenreCounts DESC
        ;
        """
        result = execute_query(query=query, args=(genre,))
    else:
        result = "Input some genre name."
    return result


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
