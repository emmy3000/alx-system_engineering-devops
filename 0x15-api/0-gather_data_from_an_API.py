#!/usr/bin/python3
"""
Retrieve and display an employee's TODO list progress using a REST API.
"""
import requests as rq
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    user_data = rq.get(base_url + 'users/{}'
                       .format(employee_id)).json()
    todo_data = rq.get(base_url + 'todos',
                       params={'userId': employee_id}).json()
    completed_tasks = [title.get("title") for title in todo_data
                       if title.get('completed')]

    print("Employee Name: {}".format(user_data.get("name")))
    print("To Do Count: {}/{}".format(len(completed_tasks), len(todo_data)))

    for title in completed_tasks:
        print("\t{}".format(title))
