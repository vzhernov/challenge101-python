#!/usr/bin/env python

"""
    Generate a file with random data separated by comma.
    Data contains alphabetical strings, integer numbers,
    alphanumerics strings with spaces and real numbers in every row.
"""
import os
import string
import random

MIN_FILE_SIZE = 10 * 1024 * 1024

MIN_ALPHABETICAL_LEN = 10
MAX_ALPHABETICAL_LEN = 20

MIN_REAL_INT_LEN = 2
MAX_REAL_INT_LEN = 6

MIN_REAL_FRACT_LEN = 3
MAX_REAL_FRACT_LEN = 6

MIN_INT_LEN = 3
MAX_INT_LEN = 10

MIN_ALNUM_SPACE = 1
MAX_ALNUM_SPACE = 10
MIN_ALNUM_LEN = 10
MAX_ALNUM_LEN = 20


def get_alphabetical():
    """
        Get a random alphabetical string

    :return: string
    """
    return ''.join(random.sample(string.ascii_lowercase,
                                 random.randint(
                                     MIN_ALPHABETICAL_LEN,
                                     MAX_ALPHABETICAL_LEN
                                 )))


def get_real():
    """
        Get a random real number
    :return: string
    """
    return str(round(random.random() *
                     10 ** random.randrange(MIN_REAL_INT_LEN,
                                            MAX_REAL_INT_LEN),
                     random.randrange(MIN_REAL_FRACT_LEN,
                                      MAX_REAL_FRACT_LEN)
                     ))


def get_integer():
    """
        Get a random integer number

    :return: string
    """
    return random.randint(10 ** (MIN_INT_LEN - 1), 10 ** MAX_INT_LEN - 1)


def get_alphanumerics():
    """
        Get a random alphanumerics

    :return: string
    """
    alphanumerics = ''.join(random.sample(string.lowercase + string.digits,
                                          random.randint(
                                              MIN_ALNUM_LEN,
                                              MAX_ALNUM_LEN
                                          )))
    alphanumerics = alphanumerics.ljust(
        len(alphanumerics) + random.randint(MIN_ALNUM_SPACE, MAX_ALNUM_SPACE)
    )
    alphanumerics = alphanumerics.rjust(
        len(alphanumerics) + random.randint(MIN_ALNUM_SPACE, MAX_ALNUM_SPACE)
    )
    return alphanumerics


def generate(file="out.data"):
    """
    Generate file with random alphabetical strings, integer numbers,
    alphanumerics strings with spaces and real numbers in every row.
    These data separated by comma.

    Row example: prmrdskrkjhgypplgbmp, 602152193,     7xebeditl75       , 72.8818,

    :param file: output filename
    :return:
    """
    with open(file, "w") as f:
        file_size = 0

        print 'Start...'

        while file_size < MIN_FILE_SIZE:
            f.write("{0}, {1}, {2}, {3},\n".format(get_alphabetical(),
                get_integer(),
                get_alphanumerics(),
                get_real()
            ))
            f.flush()
            file_size = os.stat(file).st_size

        print "Done. File size:", file_size, "bytes"


if __name__ == "__main__":
    generate()
