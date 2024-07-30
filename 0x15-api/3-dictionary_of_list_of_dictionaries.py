#!/usr/bin/python3
'''
Gather employee data from API and export it to JSON
'''

import json
import requests

REST_API = "https://jsonplaceholder.typicode.com"


def gather_data():
    users_req = requests.get('{}/users'.format(REST_API)).json()
    todos_req = requests.get('{}/todos'.format(REST_API)).json()

    data = {}

    for user in users_req:
        user_id = user.get('id')
        username = user.get('username')

        # Collect tasks for the current user
        tasks = [task for task in todos_req if task.get('userId') == user_id]
        user_tasks = [{
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in tasks]

        # Add the tasks to the dictionary under the user's ID
        data[user_id] = user_tasks

    return data


if __name__ == '__main__':
    data = gather_data()

    # Ensure the JSON output meets the checker requirements
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
