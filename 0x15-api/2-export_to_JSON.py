#!/usr/bin/python3
"""Python script to gather data from an API and convert it to JSON"""

import json
import requests

REST_API = "https://jsonplaceholder.typicode.com"

def gather_data():
    users_req = requests.get(f'{REST_API}/users').json()
    todos_req = requests.get(f'{REST_API}/todos').json()

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

    # Save the JSON data to a file named 'todo_all_employees.json'
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
