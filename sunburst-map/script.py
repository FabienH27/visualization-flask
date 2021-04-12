from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('data.json',encoding='utf-8') as json_file:
        data = json.load(json_file)
    return render_template('index.html',data=data)