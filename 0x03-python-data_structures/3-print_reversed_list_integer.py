#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for elm in my_list[::-1]:
            print("{:g}".format(elm))
