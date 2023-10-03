#!/usr/bin/python3
def fizzbuzz():
    for index in range(1, 100):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz ", end='')
        elif index % 3 == 0:
            print("fizz ", end='')
        elif index % 5 == 0:
            print("buzz ", end="")
        else:
            print(f"{index:d} ", end="")