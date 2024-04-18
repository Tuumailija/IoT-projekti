from flask import Flask, jsonify, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def hmtl_kutsu():

    return render_template("tieto.html")
   



if __name__ == '__main__':
    app.run(debug=True)