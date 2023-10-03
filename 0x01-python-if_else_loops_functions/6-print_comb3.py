#!/usr/bin/python3
for index in range(10):
    for jndix in range(index + 1, 10):
        if index == 8 and jndix == 9:
            print("{}{}".format(index, jndix))
        else:
            print(f"{}{}".format(index, jndix), end=", ")

