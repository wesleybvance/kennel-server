import sqlite3
import json
from models import Location
from views.employee_requests import get_employee_by_location_id
from views.animal_requests import get_animal_by_location_id

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    """
    DOCSTRING 2023 TBD
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__) # see the notes below
            # for an explanation on this line of code.

    return locations

def get_single_location(id):
    """GET request for a single location, pass the id 
    of the requested location as a parameter"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        employees = get_employee_by_location_id(id)
        animals = get_animal_by_location_id(id)

        location.animals = animals
        location.employees = employees

        return location.__dict__

def create_location(location):
    """CREATE LOCATION"""
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location

def delete_location(id):
    """METHOD FOR DELETING LOCATION
    ROW BY ID"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    """UPDATE LOCATION WITH SQL QUERY"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()
        # ? parameter for each field in table
        # tuple argument contains corresponding key
        # in the dictionary for the request
        db_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
