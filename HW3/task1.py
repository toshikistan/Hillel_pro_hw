# def generate_students():
#     # count should be as input GET parameter
#     # first_name, last_name, email, password, birthday (18-60)
#     # save to csv and show on web page
#     # set limit as 1000
#     pass

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


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
