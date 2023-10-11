#!/usr/bin/python3
def uniq_add(my_list=[]):
    to_set = set()
    sum = 0
    for num in my_list:
        if num not in to_set:
            to_set.add(num)
            sum += num
    return sum
