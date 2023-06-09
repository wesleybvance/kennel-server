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
    """_summary_
    """
    return CUSTOMERS

def get_single_customer(id):
    """_summary_

    Args:
      id (_type_): gets id from path to match to customer data
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
