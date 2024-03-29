#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import random

from flask import Flask

HERE = os.path.dirname(__file__)
app = Flask(__name__)

with open(os.path.join(HERE, 'classe-americaine.json')) as ca:
    quotes = json.load(ca)

@app.route('/')
def index():
    q = random.choice(quotes)
    return (q, 200, [('content-type', 'text/plain; charset=utf-8')])


if __name__ == '__main__':
    app.run()
