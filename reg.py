#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Jennifer Secrest and AnneMarie Caballero
#-----------------------------------------------------------------------

from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from regclass import RegClass
# TODO: adapt this
# from database import search

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

# TODO: any of our methods

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html', classes=[])
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/regsearch', methods=['GET'])
def search_results():

    # TODO: send this info as query to what you ma call it

    dept = request.args.get('dept')
    area = request.args.get('area')
    number = request.args.get('number')
    title = request.args.get('title')

    # TODO: PERFORM SEARCH 
    # E.g. books = search(author)  # Exception handling omitted
    # TODO: we should include the exception handling when we perform search

    # TODO: fix ugly values - also get more recent RegClass?
    classes = [RegClass('8321', dept, number, area, title)]

    html = render_template('index.html',
        classes=classes)
    response = make_response(html)
    # TODO: set form to previous search
    # TODO??: response.set_cookie('prev_author', author)
    return response
