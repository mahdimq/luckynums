from flask import Flask, render_template, request, jsonify
import requests
from forms import UserInput
from werkzeug.datastructures import MultiDict

app = Flask(__name__)

BASE_URL = "http://numbersapi.com/"


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def get_num():
    """get lucky num api"""
    req = request.json  #<-- Get request from user input

    #
    form = UserInput(MultiDict(mapping=req), csrf_enabled=False)
    from random import randint
    rand_num = randint(0, 100)

    if form.validate_on_submit(): #<-- validate form

        response = {
            "num": {
                "fact": requests.get(f"{BASE_URL}{rand_num}/trivia").text,
                "num": rand_num,
            },
            "year": {
                "fact": requests.get(f"{BASE_URL}{req['year']}/year").text,
                "year": req["year"],
            },
        }
        # print(dir(requests.get(BASE_URL))) -> to check what methods are returned
        # print("RESPONSE: ", response) -> verify if response is correct
        return jsonify(response)

    else:
        error = {"errors": {}} #<-- create json data for errors
        for err in form.errors: #<-- loop through errors dict
            error['errors'][err] = eval(f'form.{err}.errors') #<-- populate errors to dict
            return jsonify(error) #<-- jasonify dict to use in JavaScript


# REQUEST:  {'data': {'name': 'Bubba', 'email': 'jon@jon.com', 'year': '1998', 'color': 'blue'}}