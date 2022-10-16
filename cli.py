"""
This is the View module in the MVC Pattern.
As you may notice, this module is highly dependent
the underneath technology. In this case CLI.

If our application is to be used with a different
interface, this module will change significantly, but
hopefully the controller and the model modules will
remain the same.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

import sys
import logging

# set up logger
for handler in logging.root.handlers[:]:  # make sure all handlers are removed
    logging.root.removeHandler(handler)

logging_level = logging.DEBUG
logging.root.setLevel(logging_level)
logging.root.addHandler(logging.StreamHandler())


class CLI:

    @staticmethod
    def show_menu():
        print("Please enter one of the following options:")
        print("[1]  add student")
        print("[2]  add faculty")
        print("[3]  list people")
        print("[4]  remove person")
        print("[5]  exit")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except IOError as e:
            return f"{e}"

    @staticmethod
    def add_student():
        print("In the same line, add the following:")
        print("FirstName LastName DateOfBirth(yyyy-mm-dd) StudentID")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except IOError as e:
            return f"{e}"

    @staticmethod
    def add_faculty():
        print("In the same line, add the following")
        print("FirstName LastName DateOfBirth(yyyy-mm-dd) OfficeNo")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except IOError as e:
            return f"{e}"

    @staticmethod
    def remove_person():
        print("In the same line, add the following")
        print("LastName")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except IOError as e:
            return f"{e}"

    @staticmethod
    def list_people(persons: list):
        for p in persons:
            logging.info(f"{p}")

    @staticmethod
    def show_error(error: str):
        logging.error(f"Error: {error}")
