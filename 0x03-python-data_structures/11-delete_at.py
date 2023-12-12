#!/usr/bin/python3
def delete_at(my_list=[], vdx=0):
    if vdx < 0:
        return my_list
    elif vdx >= len(my_list):
        return my_list
    del my_list[vdx]
    return my_list
