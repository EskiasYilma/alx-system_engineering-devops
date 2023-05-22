#!/usr/bin/python3
"""
Python script to export data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME",\
    "TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv

"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = str(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users'
    end_points = ["posts", "comments", "albums",
                  "photos", "todos", "users"]

    r = requests.get(url).json()
    name = None
    for i in r:
        if i.get('id') == int(user_id):
            name = i['name']
    td = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    data = {}
    with open("{}.json".format(user_id), 'w') as f:

        temp_tasks = []
        for i in td:
            if i.get("userId") == int(user_id):
                task = {"task": i.get("title"),
                        "completed": i.get("completed"),
                        "username": name}
                temp_tasks.append(task)
        data[str(user_id)] = temp_tasks
        json.dump(data, f)
