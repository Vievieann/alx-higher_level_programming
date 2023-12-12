#!/usr/bin/python3
def replace_in_list(my_list, vdx, element):
    if vdx < 0:
        return my_list
    if vdx >= len(my_list):
        return my_list
    my_list[vdx] = element
    return my_list
