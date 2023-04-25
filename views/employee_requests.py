import sqlite3
import json
from models import Employee

EMPLOYEES = [
  {
    "id": 1,
    "name": "Wesley Vance"
  },
  {
    "id": 2,
    "name": "Julia Stough"
  },
  {
    "id": 3,
    "name": "Emily Pace"
  }
]

def get_all_employees():
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
            e.id,
            e.name
        FROM employee e
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'])

            employees.append(employee.__dict__) # see the notes below
            # for an explanation on this line of code.

    return employees

def get_single_employee(id):
    """GET request for a single employee, pass the id 
    of the requested employee as a parameter"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a employee instance from the current row
        employee = Employee(data['id'], data['name'])

        return employee.__dict__

def create_employee(employee):
    """CREATE EMPLOYEE"""
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    """DELETE EMPLOYEE"""
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """UPDATE EMPLOYEE"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
