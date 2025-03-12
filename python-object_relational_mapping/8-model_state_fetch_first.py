#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
If the table is empty, prints "Nothing".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    # Validate argument count
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <sqlun> <sqlpw> <dbname>")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
