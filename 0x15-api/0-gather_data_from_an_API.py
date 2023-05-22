#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID, \
returns information about his/her TODO list progress.
"""
import requests
import urllib
import sys


def api_0():
    """
    A script that, using this REST API, for a given employee ID, \
    returns information about his/her TODO list progress.
    """
    if len(sys.argv) < 2:
        sys.exit(0)
    else:
        user_id = str(sys.argv[1])

    end_points = ["posts", "comments", "albums",
                  "photos", "todos", "users"]
    n = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(user_id)).json()['name']
    tda = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                       format(user_id)).json()
    total_tasks = len(tda)
    completed_tasks = [i['title'] for i in tda if i['completed'] is True]
    tcp = len(completed_tasks)
    output = "Employee {} is done with tasks({}/{}):\n\t ".format(
                                                                  n,
                                                                  tcp,
                                                                  total_tasks)
    for i, j in enumerate(completed_tasks):
        output = output + j
        if i < len(completed_tasks)-1:
            output += "\n\t "
    print(output)


if __name__ == "__main__":
    api_0()
