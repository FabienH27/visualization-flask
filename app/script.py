import json
import os

from flask import Flask, render_template

app = Flask(__name__)

filename = os.path.join(app.static_folder, 'data', 'funnel_data.json')


@app.route('/')
def hello_world():
    funnel_list = []
    with open(filename) as f:
        data = json.load(f)
        for d in data:
            sublist = [d]
            datalist = []
            for line in data[d]:
                datalist.append(line)
            sublist.append(datalist)
            funnel_list.append(sublist)

    return render_template('index.html', data=funnel_list)
