from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:2244@localhost/pizza-delivery",
                       echo=True
                       )

"""
The create_engine function creates a new instance of the Engine class. The first argument is the database URL.
Here, we are using a PostgreSQL database with the following URL:
postgresql://postgres:2244@localhost/pizza-delivery

The URL contains the following parts:
postgresql: The database driver to use. In this case, we are using the PostgreSQL driver.
postgres: The username to connect to the database.
2244: The password to connect to the database.
localhost: The hostname of the database server. In this case, we are using the local machine.
pizza-delivery: The name of the database to connect to.

The echo argument is set to True, which means that the engine will log all the SQL statements it executes.
This is useful for debugging purposes.
"""

Base = declarative_base()
session = sessionmaker()




