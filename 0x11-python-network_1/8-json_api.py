#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]
    
    data = {"q" : q}
    r = requests.post(url, data)
    if r == "application/json":
        r_js = r.json()
        if r_js == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_js["id"], r_js["name"]))
    else:
        print("Not a valid JSON")