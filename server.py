from flask import Flask, abort, Response
from flask import request
from flask import jsonify
import requests
import json

app = Flask(__name__)





@app.route('/webhook', methods=['POST', "GET"])
def func():
    if request.method == "POST":
        r = request.get_json()
        print(request.json)
        return Response(status=200)
    else:
        abort(400)


if __name__ == '__main__':
    app.run()

