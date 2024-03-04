# def generate_password():
#     """
#     from 10 to 20 chars
#     upper and lower case
#     """
#     # string
#     # ascii_lowercase
#     # ascii_uppercase
#     # int
#     # special symbols
#     # return password
#     pass

import string
import random
from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate-password")
def generate_password():

    password_length = random.randint(10, 20)
    password = random.choice(string.digits) + random.choice(string.ascii_uppercase) + \
        random.choice(string.ascii_lowercase) + random.choice(string.punctuation) + \
        ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                               string.digits + string.punctuation, k=password_length - 4))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


@app.route("/calculate-average")
def calculate_average():
    df = pd.read_csv('hw.csv')
    average_height = df[' Height(Inches)'].mean()
    average_weight = df[' Weight(Pounds)'].mean()
    return (f"Средний рост студентов равен {average_height} дюймов. \nСредний вес студентов равен {average_weight} фунтов.")


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
