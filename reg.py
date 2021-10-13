#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Jennifer Secrest and AnneMarie Caballero
#-----------------------------------------------------------------------

import sqlite3
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from sys import stderr
from regclass import RegClass
# TODO: adapt this
from database import create_condition_and_prepared_values,\
    get_class_details, get_classes_with_condition
from search import Search


#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

# TODO: any of our methods

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    dept = request.args.get('dept')
    if dept == None:
        dept = ''

    number = request.args.get('number')
    if number == None:
        number = ''

    area = request.args.get('area')
    if area == None:
        area = ''

    title = request.args.get('title')
    if title == None:
        title = ''

    search = Search(dept, area, number, title)

    try:
        # if we're executing a search then data will be a Search
        db_values = create_condition_and_prepared_values(search)
        classes = get_classes_with_condition(db_values[0],\
            db_values[1])

    # TODO: check the exception handling
    except ValueError as ex:
        print(str(ex), file=stderr)
        # dump(False, write_flo)
        # dump(str(ex), write_flo)

    except sqlite3.DatabaseError as ex:
        print(str(ex), file=stderr)
        # dump(False, write_flo)
        # dump('A server error occurred. '+\
        #    'Please contact the system administrator.', write_flo)

    html = render_template('index.html', prev_dept=dept, prev_num=number,
        prev_area=area, prev_title=title, classes=classes)

    response = make_response(html)

    return response

#-----------------------------------------------------------------------

# TODO - get rid of this method - we do not need it anymore
@app.route('/regdetails', methods=['GET'])
def reg_details():
    # thoughts on cookies:
    # - not quite sure when we set the cookie
    #   maybe do it every time we do a search in the main
    # - get the cookie every time we eneter regdetails
    #   and use it to create the url for the click here 
    #   to do another class search method 
    # - this uses existing mechanism for saving values 

    return None

#-----------------------------------------------------------------------

# TODO - get rid of this method - we do not need it anymore
@app.route('/regsearch', methods=['GET'])
def search_results():

    # prev_dept = request.cookies.get('prev_dept')
    # if prev_dept == None:
    #     prev_dept = ''

    # prev_num = request.cookies.get('prev_num')
    # if prev_num == None:
    #     prev_num = ''

    # prev_area = request.cookies.get('prev_area')
    # if prev_area == None:
    #     prev_area = ''

    # prev_title = request.cookies.get('prev_title')
    # if prev_title == None:
    #     prev_title = ''

    dept = request.args.get('dept')
    number = request.args.get('number')
    area = request.args.get('area')
    title = request.args.get('title')

    search = Search(dept, area, number, title)

    try:
        # if we're executing a search then data will be a Search
        db_values = create_condition_and_prepared_values(search)
        classes = get_classes_with_condition(db_values[0],\
            db_values[1])

    # TODO: check the exception handling
    except ValueError as ex:
        print(str(ex), file=stderr)
        # dump(False, write_flo)
        # dump(str(ex), write_flo)

    except sqlite3.DatabaseError as ex:
        print(str(ex), file=stderr)
        # dump(False, write_flo)
        # dump('A server error occurred. '+\
        #    'Please contact the system administrator.', write_flo)

    return redirect(url_for('index', classes=classes))

        # if dept != None:
    #     prev_dept = dept
    # if number != None:
    #     prev_num = number
    # if area != None:
    #     prev_area = area
    # if title != None:
    #     prev_title = title

    # html = render_template('index.html', prev_dept=prev_dept, prev_num=prev_num,
    #     prev_area=prev_area, prev_title=prev_title, classes=classes)

    # response = make_response(html)

    # if dept != None:
    #     response.set_cookie('prev_dept', dept)
    # if number != None:
    #     response.set_cookie('prev_num', number)
    # if area != None:
    #     response.set_cookie('prev_area', area)
    # if title != None:
    #     response.set_cookie('prev_title', title)

    # html = render_template('index.html', prev_search = search,
    #     classes=classes)
    # response = make_response(html)

    # response.set_cookie('prev_dept', dept)
    # response.set_cookie('prev_num', number)
    # response.set_cookie('prev_area', area)
    # response.set_cookie('prev_title', title)

    # return response
