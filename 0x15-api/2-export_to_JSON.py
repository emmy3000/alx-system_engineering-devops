#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID
to JSON format.
"""
import json
import requests as rq
import sys


def main():
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    employee_data = rq.get(base_url + "users/{}"
                           .format(employee_id)).json()
    if isinstance(employee_data, dict) and "username" in employee_data:
        username = employee_data["username"]
    else:
        print("Invalid response format. "
              "Could not retrieve employee data.")
        return

    todos_data = rq.get(base_url + "todos",
                        params={"userId": employee_id}).json()
    if not isinstance(todos_data, list) or not \
            all(isinstance(task, dict) for task in todos_data):
        print("Invalid response format. "
              "The todos_data must be a list of dictionaries.")
        return

    if len(todos_data) != 20:
        print("All tasks found: NOK")
        return

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos_data
        ]}, jsonfile, indent=2)

    print("All tasks found: OK")


if __name__ == "__main__":
    main()
