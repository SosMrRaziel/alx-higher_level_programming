#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data).encode("utf-8")

    with urllib.request.urlopen(url, data) as r:
        read = e.read().decode("utf-8")
        print(read)
