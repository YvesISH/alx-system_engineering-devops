#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
from sys import argv


def to_csv():
    """
    get the API data
    """
    users = requests.get(
        "http://jsonplaceholder.typicode.com/users").json()
    for user in users:
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos").json()
    for todo in todos:
        if todo.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append(
                (todo.get('completed'), todo.get('title')))

    """
    export to csv
    """
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
