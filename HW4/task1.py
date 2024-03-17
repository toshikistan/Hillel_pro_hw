# 1.def order_price():
#     # UnitPrice * Quantity - sales.
#     # Calculate sales
#     # Add possibility to get sum of sales data by Country
#     # by default all countries
#     # join two tables invoices and invoices_items
#     pass
#     # show sales by country on page / if no country show all sales by all counties.

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
        SELECT customers.Country, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS TotalSales
        FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        JOIN customers ON invoices.CustomerId = customers.CustomerId WHERE customers.Country = ?
        GROUP BY customers.Country;
        """
        result = execute_query(query=query, args=(country,))
    else:
        query = """
        SELECT customers.Country, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS TotalSales
        FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        JOIN customers ON invoices.CustomerId = customers.CustomerId
        GROUP BY customers.Country;
        """
        result = execute_query(query=query)

    return f"{result}"


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
