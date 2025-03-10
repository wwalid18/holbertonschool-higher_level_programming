#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.

The script connects to a MySQL database, retrieves all states whose name starts with 'N',
and prints them in ascending order based on the state's id.

Usage: ./1-filter_states.py mysql_username mysql_password db_name
"""

import MySQLdb
import sys

def list_states_with_n(username, password, db_name):
    """
    Connects to the MySQL database, retrieves states starting with 'N', 
    and prints them in ascending order of their ID.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database to connect to.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_n(username, password, db_name)
