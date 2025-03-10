#!/usr/bin/python3
"""
Lists all states where the name matches in the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s", (state_name,))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
