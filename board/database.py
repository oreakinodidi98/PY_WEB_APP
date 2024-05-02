# import sqlite3 module for interacting with the SQLite database
import sqlite3
# import click module for creating command line commands
import click
# import current_app and g from flask module for creating the database
from flask import current_app, g

# defines the init_app() function, carries the core logic for database initialization, and integrates a new command into the Flask application’s CLI by adding init_db_command()
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command():
    # calls get_db() and receives a database connection
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        # executes the commands in the schema.sql file
        db.executescript(f.read().decode("utf-8"))
        # prints out a message to the console
    click.echo("You successfully initialized the database!")

#  defines get_db(), which returns a database connection. If the connection does not exist, it creates a new one
def get_db():
    if "db" not in g:
        # creates a new connection to the database, using  sqlite3 module to create a database connection, pointing to the database name that you defined in your environment variables
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        # sets the row_factory attribute of the connection to sqlite3.Row, which allows you to access the query results by column name
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()