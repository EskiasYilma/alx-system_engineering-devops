#!/usr/bin/python3
"""
The script that displays on the standard output the employee TODO list \
progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done with \
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of \
        completed and non-completed tasks
    Second and N next lines display the title of completed tasks: \
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
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
    ttl_tasks = 0
    comp_tasks = []
    for i in td:
        if i.get("userId") == int(user_id):
            ttl_tasks += 1
            if i.get("completed") is True:
                comp_tasks.append(i.get('title'))

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(name, len(comp_tasks), ttl_tasks))

    for i in comp_tasks:
        print("\t {}".format(i))
