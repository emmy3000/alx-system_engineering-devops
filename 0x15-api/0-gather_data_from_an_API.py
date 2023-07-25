#!/usr/bin/python3
"""Script using a REST API to retrieve TODO list progress for a given employee ID.

Requirements:
- Uses the 'requests' module.
- Accepts an integer as a parameter, which is the employee ID.
- Displays the employee TODO list progress in the specified format.

Usage:
python script_name.py EMPLOYEE_ID
"""
import requests


def get_employee_todo_progress(employee_id):
    """Retrieve and display the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}employees/{}".format(base_url, employee_id)
    todos_url = "{}todos?userId={}".format(base_url, employee_id)

    try:
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get('name', 'Unknown Employee')

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]

        print("Employee {} is done with tasks ({}/{})".format(
            employee_name, len(completed_tasks), len(todos_data)))

        for task in completed_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
