#!/usr/bin/python3
"""Returns information about an employee's TODO list progress given an ID."""
import requests
from sys import argv

def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for an employee."""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        # Fetch user data
        user_response = requests.get(url + f"users/{employee_id}")
        user_response.raise_for_status()  # Raise an error for bad responses
        user_data = user_response.json()
        employee_name = user_data.get('name')
        
        if not employee_name:
            print("Employee not found.")
            return
        
        # Fetch TODO list data
        todos_response = requests.get(url + f"todos?userId={employee_id}")
        todos_response.raise_for_status()  # Raise an error for bad responses
        todos_list = todos_response.json()
        
        # Calculate task completion
        total_tasks = len(todos_list)
        completed_tasks = [task for task in todos_list if task.get('completed')]
        completed_count = len(completed_tasks)
        
        # Display results
        print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
    
    except requests.RequestException as e:
        print(f"An error occurred with the request: {e}")
    except ValueError:
        print("Failed to decode JSON from the response.")
    except KeyError as e:
        print(f"Missing expected data: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_id>")
        exit(1)
    
    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        exit(1)
    
    get_employee_todo_progress(employee_id)

