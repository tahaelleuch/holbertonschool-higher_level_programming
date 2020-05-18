#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return False
    else:
        return True
