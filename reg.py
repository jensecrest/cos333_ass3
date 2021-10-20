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

    number = request.args.get('coursenum')
    if number == None:
        number = ''

    area = request.args.get('area')
    if area == None:
        area = ''

    title = request.args.get('title')
    if title == None:
        title = ''

    search = Search(dept, number, area, title)
    print('here')

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

    response.set_cookie('prev_dept', dept)
    response.set_cookie('prev_num', number)
    response.set_cookie('prev_area', area)
    response.set_cookie('prev_title', title)

    return response

#-----------------------------------------------------------------------

@app.route('/regdetails', methods=['GET'])
def reg_details():

    class_id = request.args.get('classid')

    prev_dept = request.cookies.get('prev_dept')
    if prev_dept == None:
        prev_dept = ''

    prev_num = request.cookies.get('prev_num')
    if prev_num == None:
        prev_num = ''

    prev_area = request.cookies.get('prev_area')
    if prev_area == None:
        prev_area = ''

    prev_title = request.cookies.get('prev_title')
    if prev_title == None:
        prev_title = ''

    try:
        details = get_class_details(class_id)
    # TODO: check the exception handling
    except ValueError as ex:
        print(str(ex), file=stderr)
        return make_response(render_template('index.html'))
        # dump(str(ex), write_flo)

    except sqlite3.DatabaseError as ex:
        print(str(ex), file=stderr)

        return make_response(render_template('index.html'))
        # dump('A server error occurred. '+\
        #    'Please contact the system administrator.', write_flo)

    html = render_template('classdetails.html', class_id=class_id,
        course_id=details.get_course_id(),
        days=details.get_days(), start_time=details.get_start_time(), 
        end_time=details.get_end_time(), building=details.get_bldg(), 
        room=details.get_room_num(), depts_and_nums=details.get_depts_and_nums(), 
        area=details.get_area(), title=details.get_title(), descrip=details.get_descrip(),
        prereqs=details.get_prereqs(), profs=details.get_profs(), 
        search_dept=prev_dept, search_num=prev_num, search_area=prev_area, 
        search_title=prev_title)

    response = make_response(html)

    return response
