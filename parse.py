#!/usr/bin/env python

"""
    Parse file with random data separated by comma.
    Data contains alphabetical strings, integer numbers,
    alphanumerics strings with spaces and real numbers in every row.
"""
import re


def parse(file="out.data"):
    """
    Parse file with random data separated by comma.
    Data contains alphabetical strings, real numbers, integer numbers and
    alphanumerics strings with spaces in every row.

    Row example: prmrdskrkjhgypplgbmp, 602152193,     7xebeditl75       , 72.8818,

    :param file: input filename
    :return:
    """
    mask_alphabetical = re.compile(r'^[a-zA-Z]+$')
    mask_real = re.compile(r'^\d+\.\d+$')
    mask_integer = re.compile(r'^\d+$')
    mask_alphanumerics = re.compile(r'^\w+$')

    with open(file, "r") as f:
        lines = f.read().split()
        for line in lines:
            for object in line.split(','):
                object = object.strip()
                if object != '':
                    if mask_alphabetical.match(object):
                        print object, "- alphabetical strings"
                    elif mask_real.match(object):
                        print object, "- real numbers"
                    elif mask_integer.match(object):
                        print object, "- integer"
                    elif mask_alphanumerics.match(object):
                        print object, "- alphanumeric"
                    else:
                        print object, "- unknown object"


if __name__ == "__main__":
    parse()