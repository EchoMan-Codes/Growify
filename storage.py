# Growify - JSON storage
# Handles saving and loading data from JSON files.

import json, os

from helpers import Task

DATA_FILE = os.path.join('data', 'growify_date.json')

def save_data(profile, tasks, study_sessions, total_xp):
    """Saves all app data to a JSON file"""

    # Converts Task objects to dictionaries for JSON
    tasks_data = []
    for task in tasks:
        task_dict = {
            'name': task.name,
            'difficulty': task.difficulty,
            'completed': task.completed,
            'xp': task.xp,
            'date_created': task.date_created,
        }
        tasks_data.append(task_dict)

    # Build the full data structure
    data = {
        'profile': {
            'name': profile.name,
        },
        'tasks': tasks_data,
        'study_sessions': study_sessions,
        'total_xp': total_xp,
    }

    # Write to JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent = 4)

    print('[*] Data saved successfully.')


def load_data():
    """Load app data from the JSON file"""

    if not os.path.exists(DATA_FILE):
        return None
    
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, ValueError):
        print('[!] Save file is corrupted. Starting fresh.')
        return None
    
    return data

def restore_tasks(tasks_data):
    """Converts a list of task dictionarires back into Task object."""

    tasks = []

    for item in tasks_data:
        task = Task(item['name'], item['difficulty'])
        task.completed = item['completed']
        task.data_created = item['date_created']
        tasks.append(task)

    return tasks