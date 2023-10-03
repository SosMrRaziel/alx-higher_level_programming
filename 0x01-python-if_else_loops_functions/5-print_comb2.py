#!/usr/bin/python3
for index in range(0, 100):
    if index == 99:
       print(f"{index}")
    else:
       print(f"{index:02}", end=", ")