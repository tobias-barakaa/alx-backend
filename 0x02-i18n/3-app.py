#!/usr/bin/env python3
"""
get_locale: function
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    class config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """index"""
    return render_template('3-index.html', translate=translate)
