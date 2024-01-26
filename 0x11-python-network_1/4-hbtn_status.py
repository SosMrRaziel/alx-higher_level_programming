#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    content = resp.content
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(resp.text))
