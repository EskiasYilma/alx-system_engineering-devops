#!/usr/bin/python3
"""
Python script to export data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME",\
    "TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv

"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = str(sys.argv[1])
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        end_points = ["posts", "comments", "albums",
                      "photos", "todos", "users"]

        r = requests.get(url).json()
        name = r.get("name")
        td = requests.get("http://jsonplaceholder.typicode.com/todos").json()
        todos = list(filter(lambda i: i.get('userId') == user_id, td))
        with open("{}.csv".format(user_id), 'w') as f:
            for i in todos:
                t_csv = '"{}","{}","{}","{}"\n'.format(i.get("userId"),
                                                     name,
                                                     i.get("completed"),
                                                     i.get("title"))
                f.write(t_csv)
