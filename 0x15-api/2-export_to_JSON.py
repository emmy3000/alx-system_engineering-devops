#!/usr/bin/python3
"""
Retrieve and display an employee's TODO list progress using a REST API.
Export data in JSON format.
"""
import requests
import json


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users/{}".format(base_url, employee_id)
    todos_url = "{}todos?userId={}".format(base_url, employee_id)

    try:
        employee_res = requests.get(employee_url)
        employee_data = employee_res.json()
        employee_name = employee_data.get('name', 'Unknown Employee')

        todos_res = requests.get(todos_url)
        todos_data = todos_res.json()

        completed_tasks = [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in todos_data
        ]

        data = {str(employee_id): completed_tasks}

        print(json.dumps(data, indent=2))

        filename = "{}.json".format(employee_id)
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        print("Data exported to {} successfully.".format(filename))

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
