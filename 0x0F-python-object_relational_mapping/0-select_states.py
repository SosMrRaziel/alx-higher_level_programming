#!/usr/bin/python3
"""
script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           password=password,
                           db=database
                           )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
