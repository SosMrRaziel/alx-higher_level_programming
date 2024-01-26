#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as r:
    html1 = r.read()
    html2 = html1.decode('utf-8')
    print("Body response:$")
    print("\t- type: {}".format(type(html1)))
    print("\t- content: {}".format(html1))
    print("\t- utf8 content: {}".format(html2))
