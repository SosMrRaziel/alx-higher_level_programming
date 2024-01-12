#!/usr/bin/python3
"""
A script that lists all cities of a specific
state in the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC", (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row != query_rows[-1]:
            print(row[0], end=', ')
        else:
            print(row[0])
