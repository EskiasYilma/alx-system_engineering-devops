#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID, \
returns information about his/her TODO list progress.
"""

import requests
import urllib
import sys

if len(sys.argv) < 2:
    sys.exit(0)
else:
    user_id = str(sys.argv[1])

end_points = ["posts", "comments", "albums", "photos",
              "todos", "users"]
employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                             format(user_id)).json()['name']
todos_all = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(user_id)).json()
total_tasks = len(todos_all)
completed_tasks = [i['title'] for i in todos_all if i['completed'] is True]
tcp = len(completed_tasks)
output = "Employee {} is done with tasks({}/{}):\n\t ".format(
                                                              employee_name,
                                                              tcp,
                                                              total_tasks)
for i, j in enumerate(completed_tasks):
    output = output + j
    if i < len(completed_tasks)-1:
        output += "\n\t "
print(output)
