#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idex in my_list:
        if idex == search:
            new_list.append(replace)
        else:
            new_list.append(idex)
    return new_list
