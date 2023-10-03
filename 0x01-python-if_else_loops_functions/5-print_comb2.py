#!/usr/bin/python3
for index in range(0, 100):
    if index == 99:
        print("{}".format(index))
    else:
        print("{:02}".format(index), end=", ")
