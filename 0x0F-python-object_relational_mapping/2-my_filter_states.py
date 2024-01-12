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
    state_name_searched = sys.argv[4]

    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           password=password,
                           db=database
                           )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
                ORDER BY id", (state_name_searched,))
    rows = cur.fetchall()
    for row in rows:
        if row [1] == (state_name_searched):
            print(row)
