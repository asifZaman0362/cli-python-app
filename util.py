"""
All the utility functions needed to easily complete this
project!

Author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from datetime import datetime

def convert_string_to_datetime(date: str) -> datetime:
    """
    Takes a date in a string format (e.g., `2022-10-05`) and returns a datetime
    object using the format. If the string given is wrong, it throws and error.

    Hint: Search for "python split a string by delimiter"!

    :param date: a string representing the date.
    :return: A datetime object reflecting the date given as a string.
    """
    tokens = date.split('-')
    if len(tokens) == 3:
        year, month, day = tokens
        try:
            if len(year) == 4 and len(month) == 2 and len(day) == 2:
                year = int(year)
                month = int(month)
                day = int(day)
                date = datetime(year=year, day=day, month=month)
                return date
            else:
                raise SyntaxError("Invalid date format! Accepted format is: YYYY-MM-DD")
        except ValueError:
                raise SyntaxError("Invalid date format! Accepted format is: YYYY-MM-DD")
    else:
        raise SyntaxError("Invalid date format! Accepted format is: YYYY-MM-DD")

