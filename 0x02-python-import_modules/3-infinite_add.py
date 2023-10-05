#!/usr/bin/python3
if __name__ == '__main__':
    import sys

args = sys.argv[1: ]
print(f"{sum(int(arg) for arg in args)}")
