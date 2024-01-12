#!/usr/bin/env python3
"""
flask app render html
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    function index
    """
    return render_template('0-index.html')
