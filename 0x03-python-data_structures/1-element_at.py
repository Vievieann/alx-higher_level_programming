#!/usr/bin/python3
def element_at(my_list, vdx):
    if vdx < 0:
        return None
    elif vdx >= len(my_list):
        return None
    return my_list[vdx]
