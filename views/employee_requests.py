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
    """_summary_
    """
    return EMPLOYEES

def get_single_employee(id):
    """Docstring
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee
