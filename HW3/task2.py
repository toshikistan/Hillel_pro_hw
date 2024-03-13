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

from http import HTTPStatus
from flask_apispec import use_kwargs
import httpx
from flask import Flask, Response
from webargs import fields

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello World!</p>"


@app.route('/bitcoin_rate')
@use_kwargs(
    {
        'currency': fields.Str(
            missing='USD'
        ),
        'convert': fields.Float(
            missing=1
        )
    },
    location='query'
)
def get_bitcoin_value(currency, convert):

    url = 'https://bitpay.com/api/rates'
    bitcoin = httpx.get(url)
    bitcoin_rates = bitcoin.json()

    if bitcoin.status_code != HTTPStatus.OK:
        return Response('Error: something went wrong', status=bitcoin.status_code)

    for i in bitcoin_rates:
        if i['code'] == currency:
            bitcoin_value = i['rate'] * convert

            return f"{convert} BTC equal to {str(bitcoin_value)} {currency}"


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
