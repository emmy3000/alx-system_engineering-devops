#!/usr/bin/python3
"""
Retrieve and display employees' TODO list progress using a REST API.
Export data in JSON format.
"""
import json
import requests


def get_all_employees_todo_progress():
    """
    Retrieve and display all employees' TODO list progress.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    employees_url = "{}".format(base_url)

    try:
        employees_res = requests.get(employees_url)
        employees_data = employees_res.json()

        all_data = {}
        for employee in employees_data:
            employee_id = employee["id"]
            employee_name = employee["name"]

            todos_url = "{}/todos?userId={}".format(base_url, employee_id)
            todos_res = requests.get(todos_url)
            todos_data = todos_res.json()

            completed_tasks = [
                {
                    "username": employee_name,
                    "task": task["title"],
                    "completed": task["completed"],
                }
                for task in todos_data
            ]

            all_data[str(employee_id)] = completed_tasks

        filename = "todo_all_employees.json"
        with open(filename, 'w') as json_file:
            json.dump(all_data, json_file, indent=2)

        print("Data exported to {} successfully.".format(filename))

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


if __name__ == "__main__":
    get_all_employees_todo_progress()
