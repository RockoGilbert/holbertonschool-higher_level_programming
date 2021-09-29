#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
    except:
        total = None
    finally:
        print("Inside total: {}".format(total))
    return result
