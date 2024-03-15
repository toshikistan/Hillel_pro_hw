# 1.def order_price():
#     # UnitPrice * Quantity - sales.
#     # Calculate sales
#     # Add possibility to get sum of sales data by Country
#     # by default all countries
#     # join two tables invoices and invoices_items
#     pass
#     # show sales by country on page / if no country show all sales by all counties.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/order-price")
def order_price():
    pass

if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
