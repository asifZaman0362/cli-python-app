"""
A person list module where we keep track
of all the persons added to our database.

The class here should wrap the list class instead of
inheriting it.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

from typing import List
from person import Person


class PersonList:
    """
    A person list class. It wraps the built-in list class
    to keep track of all the person's information added
    """

    def __init__(self):
        """
        Start by initializing an empty list.
        Preferably indicate the type of the list and
        what it takes.
        """
        self.people: List[Person] = []

    def get_people(self) -> list:
        """
        Return all the person objects in the listed
        sorted based on their get_name().
        :return: A sorted list of the people variable.
        """
        return sorted(self.people, key=lambda person: person.get_name())

    def remove(self, last_name: str):
        """
        Given some person last_name, remove any matches to it.
        :param last_name: A person(s) last name to be removed if found in the list of people.
        """
        people_to_remove: List[Person] = [ 
            person for person in self.people if person._last_name == last_name 
        ]
        for person_to_remove in people_to_remove:
            self.people.remove(person_to_remove)

    # TODO: Add an "append" method that takes a Person and add it to the list. No Skeleton given!
    def append(self, person: Person):
        self.people.append(person)
