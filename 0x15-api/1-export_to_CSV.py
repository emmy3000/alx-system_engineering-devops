#!/usr/bin/python3
"""
Script to export data in the CSV format
"""
import csv
import requests as rq
import sys


def main():
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = rq.get(base_url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    todos_data = rq.get(base_url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csvwriter.writerow([user_id, 
                                username, 
                                task.get("completed"), 
                                task.get("title")]
                               )


if __name__ == "__main__":
    main()
