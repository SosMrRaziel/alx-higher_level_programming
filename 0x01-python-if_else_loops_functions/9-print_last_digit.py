#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        num = -number % 10
        print(str(num), end='')
        return (str(num))
    else:
        num = number % 10
        print(str(num), end='')
        return (str(num))
