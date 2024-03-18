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
def find_city_genre(genre):
    if genre:
        query = """
        --sql
        SELECT 
            customers.City, 
            genres.Name, 
            COUNT(*)
        FROM 
            customers
        JOIN 
            invoices ON customers.CustomerId = invoices.CustomerId
        JOIN 
            invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        JOIN 
            tracks ON invoice_items.TrackId = tracks.TrackId
        JOIN 
            genres ON tracks.GenreId = genres.GenreId
        WHERE 
            genres.Name = ?
        ;
        """
        result = execute_query(query=query, args=(genre,))
    else:
        query = """
        --sql
        SELECT genres.Name FROM genres
        GROUP BY genres.Name;
        """
        table = execute_query(query=query)
        result = f"Input one of genre names: {table}"
    return result


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
