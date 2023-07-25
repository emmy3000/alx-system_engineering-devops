#!/usr/bin/python3
"""
Retrieve and display an employee's data using a REST API.
"""
import requests
import sys


def main():
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    user_data = requests.get(base_url + 'users/{}'
                             .format(employee_id)).json()
    todo_data = requests.get(base_url + 'todos',
                             params={'userId': employee_id}).json()
    completed_tasks = [title.get("title") for title in todo_data
                       if title.get('completed')]

    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_task_count = len(completed_tasks)

    print("Employee {} is done with tasks ({}/{})"
          .format(employee_name, completed_task_count, total_tasks))

    for title in completed_tasks:
        print("\t{}".format(title))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py EMPLOYEE_ID")
    else:
        main()
