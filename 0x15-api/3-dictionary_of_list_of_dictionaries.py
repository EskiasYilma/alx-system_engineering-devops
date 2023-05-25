#!/usr/bin/python3
"""
Python script to export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task":\
     "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": \
     "USERNAME", "task": "TASK_TITLE", "completed": \
     TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": \
     "USERNAME", "task": "TASK_TITLE", "completed": \
     TASK_COMPLETED_STATUS}, {"username": "USERNAME", \
     "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},\
      ... ]}
    File name must be: todo_all_employees.json

"""
import json
import requests
import sys


def get_user():
    """
    Get users
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(url).json()
    name = None
    data = {}
    with open("todo_all_employees.json", 'w') as f:
        for i in r:
            t_list = get_tasks(i.get("id"))
            for j in t_list:
                j['username'] = i.get("username")
            data[i.get("id")] = t_list
        json.dump(data, f)


def get_tasks(user_id):
    """
    Get todo data
    """
    td = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    temp_tasks = []
    with open("{}.json".format(user_id), 'w') as f:
        for i in td:
            if i.get("userId") == int(user_id):
                task = {"username": "",
                        "task": i.get("title"),
                        "completed": i.get("completed"),
                        }
                temp_tasks.append(task)
    return temp_tasks


if __name__ == "__main__":
    get_user()
