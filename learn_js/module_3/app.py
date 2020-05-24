import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/a/*": {"origins": "*"}})


@app.route("/a")
def get_a():
    a={
        1 : "One",
        2 : "Two",
        3 : "Three"
    }
    json_a = json.dumps(a)
    #print(type(json_a))
    return json_a


if __name__ == "__main__":
    app.run()