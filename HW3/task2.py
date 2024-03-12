# def get_bitcoin_value():
#     # https://bitpay.com/api/rates
#     # /bitcoin_rate?currency=UAH&convert=100
#     # input parameter currency code
#     # default is USD
#     # default count is 1
#     # return value currency of bitcoin
#     # add one more input parameter count and multiply by currency (int)
#     # * https://bitpay.com/api/
#     # * $, €, ₴
#     # * return symbol of input currency code
#     pass

import httpx
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello World!</p>"


@app.route('/bitcoin_rate')
# @use_kwargs(
#     {
#         'currency': fields.Str(
#             missing='USD'
#         ),
#         'convert': fields.Int(
#             missing=1
#         )
#     },
#     location='query'
# )
def get_bitcoin_value():
    currency_value = request.args.get('currency', 'USD')
    convert_value = float(request.args.get('convert', 1))

    url = 'https://bitpay.com/api/rates'
    bitcoin = httpx.get(url)
    bitcoin_rates = bitcoin.json()

    for i in bitcoin_rates:
        if i['code'] == currency_value:
            bitcoin_value = i['rate'] * convert_value

            return f"{convert_value} BTC  равно {str(bitcoin_value)} {currency_value}"


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
