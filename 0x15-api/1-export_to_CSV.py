#!/usr/bin/python3
"""
Retrieve and display an employee's TODO list progress using a REST API.

Requirements:
- Uses the 'requests' module.
- Accepts an integer as a parameter (employee ID).
- Displays the employee's TODO list progress in the specified format.
- Exports the data to a CSV file with the format "USER_ID.csv".

Usage:
python script_name.py EMPLOYEE_ID
"""
import requests
import csv


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

        completed_tasks = [task for task in todos_data
                           if task.get('completed', False)]

        print("Employee {} is done with tasks ({}/{})".format(
            employee_name, len(completed_tasks), len(todos_data)))

        for task in completed_tasks:
            print("\t{}".format(task.get('title', 'N/A')))

        filename = "{}.csv".format(employee_id)
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                ["USER_ID",
                 "USERNAME",
                 "TASK_COMPLETED_STATUS",
                 "TASK_TITLE"
                 ])

            for task in todos_data:
                csvwriter.writerow([employee_id, employee_name,
                                    task["completed"], task["title"]])

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
