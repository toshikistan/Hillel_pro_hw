import csv
from flask_apispec import use_kwargs
from flask import Flask, Response
from faker import Faker
from webargs import fields, validate
import httpx
from http import HTTPStatus

app = Flask(__name__)
faker = Faker()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate-students")
@use_kwargs(
    {
        'count': fields.Int(
            missing=10,
            validate=[validate.Range(
                min_inclusive=True, min=1, max=1000, max_inclusive=True)]
        )
    },
    location='query'
)
def generate_student(count: int):
    # count = request.args.get('count', '10')
    # count = int(count)
    # if count > 1000:
    #     return "Слишком много значений, введите до 1000"

    students = []
    for _ in range(count):
        student = {
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email': faker.email(),
            'password': faker.password(),
            'birthday': faker.date_of_birth(minimum_age=18, maximum_age=60)
        }
        students.append(student)

    with open('generated_students.csv', 'w') as f:
        fieldnames = ['first_name', 'last_name',
                      'email', 'password', 'birthday']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    return students


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
