import os
from flask import Flask, render_template, current_app as app
import json, urllib.request

app = Flask(__name__)

filename = os.path.join(app.static_folder, 'data', 'funnel_data.json')

#url = "https://raw.githubusercontent.com/FabienH27/projet-d3js/main/data/funnel_data.json"

@app.route('/')
def hello_world():
    funnel_list = []
    #Read from source
    #with urllib.request.urlopen(url) as f:
        #data = json.loads(f.read().decode('utf-8'))
    #Read locally
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
