from flask import Flask, render_template, request, jsonify
import requests

# from forms import InfoForm
# from werkzeug.datastructures import MultiDict


app = Flask(__name__)

BASE_URL = "http://numbersapi.com/"


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def get_num():
    """get lucky num api"""
    data = request.get_json()

    # form = InfoForm(MultiDict(mapping=req["data"]), csrf_enabled=False)

    from random import randint
    rand_num = randint(0, 100)


    # if req.values() == None:
    #     errors = {
    #         "errors": {
    #             "color": ["Invalid value, must be one of: red, green, orange, blue."],
    #             "name": ["This field is required."],
    #         }
    #     }
    #     return jsonify(errors)

    # else:

    response = {
        "num": {
            "fact": requests.get(f"{BASE_URL}{rand_num}/trivia").text,
            "num": rand_num,
        },
        "year": {
            "fact": requests.get(f"{BASE_URL}{req['data']['year']}/year").text,
            "year": req["data"]["year"],
        },
    }
    # print(dir(requests.get(BASE_URL))) -> to check what methods are returned
    # print("RESPONSE: ", response) -> verify if response is correct
    return jsonify(response)


# REQUEST:  {'data': {'name': 'Bubba', 'email': 'jon@jon.com', 'year': '1998', 'color': 'blue'}}
