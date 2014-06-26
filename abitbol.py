#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

from flask import Flask
import simplejson

HERE = os.path.dirname(__file__)
app = Flask(__name__)

with open(os.path.join(HERE, 'classe-americaine.json')) as ca:
    quotes = simplejson.load(ca)

@app.route('/')
def index():
    q = random.choice(quotes)
    return (q, 200, [('content-type', 'text/plain')])

if __name__ == '__main__':
    app.run(debug=True)
