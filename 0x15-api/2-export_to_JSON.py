#!/usr/bin/python3
"""Python script to gather data from an API and convert it to JSON"""

import json
import requests

REST_API = "https://jsonplaceholder.typicode.com"


def gather_data():
    # Fetch all users and todos from the API
    users = requests.get(f'{REST_API}/users').json()
    todos = requests.get(f'{REST_API}/todos').json()

    data = {}

    # Iterate through each user to gather their tasks
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Collect tasks for the current user
        user_tasks = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos if task.get('userId') == user_id
        ]

        # Ensure each user ID has a list of tasks
        data[user_id] = user_tasks

    return data


if __name__ == '__main__':
    # Gather all data
    data = gather_data()

    # Save the JSON data to a file named 'todo_all_employees.json'
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
