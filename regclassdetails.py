#!/usr/bin/env python

#-----------------------------------------------------------------------
# regclassdetails.py
# Author: AnneMarie Caballero and Jen Secrest
#-----------------------------------------------------------------------

class RegClassDetails:
    """
    Creates an object to represent all of the main details
    of a class from the reegistrar database. Does not have any
    public methods because the main use of this class is to
    store the details of a class and then print those details.
    """

    def __init__(self, class_details, cl_details,
        course_details, prof_details):
        self._class_details = class_details
        self._cl_details = cl_details
        self._course_details = course_details
        self._prof_details = prof_details

    def get_course_id(self):
        """
        Get the course id of this class
        """
        return self._class_details[0]

    def get_days(self):
        """
        Get the days that this class meets
        """
        return self._class_details[1]

    def get_start_time(self):
        """
        Get the start time for this class
        """
        return self._class_details[2]

    def get_end_time(self):
        """
        Get the end time for this class
        """
        return self._class_details[3]

    def get_bldg(self):
        """
        Get the bldg for this class
        """
        return self._class_details[4]

    def get_room_num(self):
        """
        Get the room number for this class
        """
        return self._class_details[5]

    def get_depts_and_nums(self):
        """
        Gets an array with the depts and numbers
        for this class
        """
        return self._cl_details

    def get_area(self):
        """
        Get the course area for this class
        """
        return self._course_details[0]

    def get_title(self):
        """
        Get the course title for this class
        """
        return self._course_details[1]

    def get_descrip(self):
        """
        Get the course description for this class
        """
        return self._course_details[2]

    def get_prereqs(self):
        """
        Get the course prereqs for this class
        """
        return self._course_details[3]

    def get_profs(self):
        """
        Get the professors for this class (as array)
        """
        return self._prof_details
