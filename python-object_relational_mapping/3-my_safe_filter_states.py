#!/usr/bin/python3
"""
Listing states from a db
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Check input arguments
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} "
              "<username> <password> <database> <state name>")
        sys.exit(1)

    # Catch db credentials
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to DB
    db = MySQLdb.connect(host=MY_HOST,
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB,
                         port=3306
                         )

    # Cursor creation to execute SQL queries
    cursor = db.cursor()

    # Print results in comma delimited format
    cursor.execute("SELECT * FROM states WHERE name = %s", (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection with db
    cursor.close()
    db.close()
