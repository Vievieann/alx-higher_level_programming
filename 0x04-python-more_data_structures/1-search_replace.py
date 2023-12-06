#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(my_list)
    for t in range(len(n_list)):
        if n_list[t] == search:
            n_list[t] = replace
    return n_list
