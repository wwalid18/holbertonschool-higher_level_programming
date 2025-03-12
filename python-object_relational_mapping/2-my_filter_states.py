#!/usr/bin/python3
"""
Lists all states where the name matches
in the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to MySQL and retrieves states where
    name matches user input.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
