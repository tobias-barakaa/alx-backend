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
      # Check if the 'locale' parameter is present in the request's query string
    requested_locale = request.args.get('locale')
    
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    
    # If the parameter is not present or not a supported locale, resort to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """index"""
    return render_template('4-index.html')
