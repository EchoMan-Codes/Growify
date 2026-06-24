# Growify - JSON storage
# Handles saving and loading data from JSON files.

import json, os

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