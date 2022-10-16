"""
A test module to validate the Controller class functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from controller import Controller
from cli import CLI
from persons import PersonList


class TestController(unittest.TestCase):

    def setUp(self):
        self.c = Controller()

    def test_initialization(self):
        """Validating the initialization
        """
        self.assertIsInstance(self.c._persons, PersonList)
        self.assertIsInstance(self.c._view, CLI)

    def test_add_student(self):
        """Validate we can add a student.
        """
        self.assertEqual(0, len(self.c._persons.people))
        self.c.add_student("Someone LastName 2000-10-10 9999999999")
        self.assertEqual(1, len(self.c._persons.people))

    def test_add_student_go_wrong(self):
        """Validate wrongly added information.
        """
        self.assertEqual(0, len(self.c._persons.people))
        with self.assertRaises(IndexError):
            self.c.add_student("LastName 2000-10-10 9999999999")

    def test_add_faculty(self):
        """Validate we can add a student.
        """
        self.assertEqual(0, len(self.c._persons.people))
        self.c.add_faculty("Someone LastName 2000-10-10 100")
        self.assertEqual(1, len(self.c._persons.people))

    def test_add_faculty_go_wrong(self):
        """Validate wrongly added information.
        """
        self.assertEqual(0, len(self.c._persons.people))
        with self.assertRaises(IndexError):
            self.c.add_faculty("LastName 2000-10-10 9999999999")

    def test_remove_existing_person(self):
        """Validate removing existing person
        """
        self.assertEqual(0, len(self.c._persons.people))
        self.c.add_faculty("Someone LastName 2000-10-10 100")
        self.c.add_faculty("Someone OtherName 2000-10-10 100")
        self.assertEqual(2, len(self.c._persons.people))
        self.c.remove_person("LastName")
        self.assertEqual(1, len(self.c._persons.people))

    def test_remove_non_existing_person(self):
        """Validate removing non-existing person
        """
        self.assertEqual(0, len(self.c._persons.people))
        self.c.add_faculty("Someone LastName 2000-10-10 100")
        self.c.add_faculty("Someone OtherName 2000-10-10 100")
        self.assertEqual(2, len(self.c._persons.people))
        self.c.remove_person("NotThere")
        self.assertEqual(2, len(self.c._persons.people))
