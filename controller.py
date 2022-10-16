"""
This is the Controller Module.
Although we might not implement it to be perfect,
the hope is that most of the methods here will not
change with any UI changes.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

from cli import CLI
from persons import PersonList
from person import Student, Faculty


class Controller:

    def __init__(self):
        self._persons = PersonList()
        self._view = CLI()

    def run(self, args: list):
        """

        :param args:
        :return:
        """
        while True:
            inp = self._view.show_menu()
            if inp == "1":  # add student
                self.add_student(self._view.add_student())
            elif inp == "2":  # add teacher
                self.add_faculty(self._view.add_faculty())
            elif inp == "3":  # list people
                self._view.list_people(self._persons.get_people())
            elif inp == "4":  # remove person
                self.remove_person(self._view.remove_person())
            elif inp == "5":  # exit
                break
            else:
                self._view.show_error("Invalid Input!")

    def add_student(self, inp: str):
        """
        Add a student information using the CLI passed inputs.
        :param inp: the student information as given in the command line.
        """
        data = inp.split(" ")
        try:
            p = Student(data[0], data[1], data[2], int(data[3]))
            self._persons.append(p)
        except SyntaxError as e:
            # notify the view of the error!
            self._view.show_error(f"Unable to parse input! {e}")

    def add_faculty(self, inp: str):
        """
        Add a student information using the CLI passed inputs.
        :param inp: the student information as given in the command line.
        """
        data = inp.split(" ")
        try:
            p = Faculty(data[0], data[1], data[2], int(data[3]))
            self._persons.append(p)
        except SyntaxError as e:
            # notify the view of the error!
            self._view.show_error(f"Unable to parse input! {e}")

    def remove_person(self, inp: str):
        """
        Remove a person from the list of persons using their last name
        This should call the remove function on the PersonList class.
        """
        self._persons.remove(inp)
