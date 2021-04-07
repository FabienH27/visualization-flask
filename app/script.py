import os
from flask import Flask, render_template, current_app as app

app = Flask(__name__)

import json, urllib.request

filename = os.path.join(app.static_folder, 'data','funnel_data.json')

@app.route('/')
def hello_world():
    funnel_list = []
    with open(filename) as f:
        data = json.load(f)
        for f in data:
            sublist = []
            sublist.append(f)
            datalist = []
            for line in data[f]:
                datalist.append(line)
            sublist.append(datalist)
            funnel_list.append(sublist)

    return render_template('index.html',data = funnel_list)