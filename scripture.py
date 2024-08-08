"""
Choong Min Um <choongmin.um@unh.edu>

This module determines which verses of the scriptures to read today.
"""

import datetime


def get_days():
    num_days_per_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
            }

    # Determine the month and the date of today.
    month = int(datetime.datetime.now().strftime('%m'))
    day = int(datetime.datetime.now().strftime('%d'))

    # Count the number of days from 01/01 to today.
    num_days = 0
    for index in range(month):
        num_days = num_days + num_days_per_month[index + 1]
    num_days = num_days + day

    return num_days
 

def get_verses():
    # Enter the number of verses per scripture.
    num_verses = {
            'Sutta-Nipata': 16,
            'Dhammapada': 26,
            }

    # Determine which verses to read.
    num_days = get_days()
    to_read = {}
    for scripture in num_verses:
        if num_days % num_verses[scripture] == 0:
            to_read[scripture] = num_verses[scripture]
        else:
            to_read[scripture] = num_days % num_verses[scripture]

    return to_read


def main():
    print(get_verses())


if __name__ == '__main__':
    main()
