# -*- coding: utf-8 -*-

import json

from flask import Flask, request, g

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

print config


@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)
