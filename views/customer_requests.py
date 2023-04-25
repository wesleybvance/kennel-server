import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Mortimer Goth"
    },
    {
        "id": 2,
        "name": "Bella Goth"
    }
]

def get_all_customers():
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
            c.id,
            c.name
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'])

            customers.append(customer.__dict__) # see the notes below
            # for an explanation on this line of code.

    return customers

def get_single_customer(id):
    """GET request for a single customer, pass the id 
    of the requested customer as a parameter"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a customer instance from the current row
        customer = Customer(data['id'], data['name'])

        return customer.__dict__

def create_customer(customer):
    """CREATE CUSTOMER

    Args:
        customer (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    """DELETE CUSTOMER

    Args:
        id (_type_): _description_
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """UPDATE CUSTOMER"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
