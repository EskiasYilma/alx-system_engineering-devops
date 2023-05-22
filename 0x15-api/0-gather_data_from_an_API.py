#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID, \
returns information about his/her TODO list progress.
"""
import requests
import sys
import urllib


def api_0():
    """
    A script that, using this REST API, for a given employee ID, \
    returns information about his/her TODO list progress.
    """
    if len(sys.argv) < 2:
        sys.exit(0)
    else:
        user_id = str(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users'
    end_points = ["posts", "comments", "albums",
                  "photos", "todos", "users"]
    EMPLOYEE_NAME = requests.get(url + "/" + user_id).json().get('name')
    tda = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                       format(user_id)).json()
    total_tasks = len(tda)
    completed_tasks = [i.get('title') for i in tda if i['completed'] is True]
    tcp = len(completed_tasks)
    output = "Employee " + EMPLOYEE_NAME + " is done with tasks"
    output = output + "({}/{}):\n\t ".format(tcp,
                                             total_tasks)
    for i, j in enumerate(completed_tasks):
        output = output + j
        if i < len(completed_tasks)-1:
            output += "\n\t "
    print(output)


if __name__ == "__main__":
    api_0()
