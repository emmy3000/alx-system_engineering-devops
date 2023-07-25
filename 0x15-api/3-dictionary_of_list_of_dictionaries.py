#!/usr/bin/python3
"""
Retrieve and display employees' TODO list progress using a REST API.
Export data in JSON format.
"""
import json
import requests as rq

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users_data = rq.get(base_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in rq.get(base_url + "todos",
                                 params={"userId": user.get("id")}).json()]
            for user in users_data}, jsonfile)
