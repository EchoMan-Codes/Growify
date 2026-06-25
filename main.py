# Growify - Personal Learning Dashboard

from datetime import datetime

from helpers import Task, UserProfile
from storage import load_data, restore_tasks, save_data

# ---- Data Storage----
tasks = []
study_sessions = []
total_xp = 0
profile = None

# ---- Main Menu ----
def show_menu():
    """Displays the main menu options to the user"""
    print('\nWelcome to Growify - Personal Learning Dashborad')
    print("\n--- GROWIFY Menu ---")
    print('  1. Add Task')
    print('  2. View Tasks')
    print('  3. Complete Task')
    print('  4. Delete Task')
    print('  5. Add Study Session')
    print('  6. View Study Sessions')
    print('  7. View Dashboard')
    print('  8. Export CSV Report')
    print('  9. Exit')
    print('----------------------------')


# ---- Add Task ----
def add_task():
    """Ask the user for task details and add it to the tasks list."""
    print('\n--- Add New Task ---')

    name = input('Task name: ').strip()

    if not name:
        print('[!] Task name cannot be empty.')
        return

    print('Difficulty options: Easy, Medium, Hard')
    difficulty = input('Difficulty: ').strip().lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print('[!] Invalid difficulty. Using "easy" as default.')
        difficulty = 'easy'

    task = Task(name, difficulty)
    tasks.append(task)

    print(f'\n[+] Task "{task.name} added! ({task.difficulty.capitalize()} - {task.xp} XP)')


# ---- View Tasks ----
def view_tasks():
    """Display all tasks with their index number."""
    print('\n--- Your Tasks ---')

    if not tasks:
        print('  No tasks yet. Add one from the menu.')
        return
    
    for index, task in enumerate(task, start = 1):
        print(f'   {index}.{task}')

    print(f'\n   Total: {len(tasks)} taks(s)')


# ---- Complete Task ----
def complete_task():
    """Mark a task as completed and award XP."""
    global total_xp

    print('\n--- Complete a Task ---')

    if not tasks:
        print('  No tasks to complete.')
        return
    
    # Show tasks so user can pick one
    view_tasks()

    choice = input('\nEnter task number to complete: ').strip()

    # Validate: is it a number?
    if not choice.isdigit():
        print('[!] Please enter a valid number.')
        return
    
    index = int(choice) - 1    # Convert to 0-based index

    # Validate: is it in range?
    if index < 0 or index >= len(tasks):
        print('[!] Invalid task number.')
        return
    
    task = tasks[index]

    # Validate: is it already done?
    if task.completed:
        print(f'[!] "{task.name}" is already completed.')
        return
    
    task.completed = True
    total_xp += task.xp

    print(f'\n[+] "{task.name}" completed! + {task.xp} XP earned!')
    print(f'     Total XP: {total_xp}')


# ---- Delete Task ----
def delete_task():
    """Remove a task from the tasks list permanently."""
    global total_xp

    print('\n--- Delete a Task ---')

    if not tasks:
        print('No tasks to delete.')
        return
    
    view_tasks()

    choice = input('\nEnter task number to delete: ').strip()

    if not choice.isdigit():
        print('[!] Please enter a valid number.')
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print('[!] Invalid task number.')
        return
    
    task = tasks.pop(index)
    
    # If deleted task was completed, remove its xp
    if task.completed:
        total_xp -= task.xp

    print(f'\n[-] Task "{task.name}" deleted.' )


# ---- Study Session ----
def add_study_session():
    """Ask the user for study session details and save it."""
    print('\n--- Add Study Session ---')

    subject = input('Subject (e.g., Python, Math): ').strip()

    if not subject:
        print('[!] Subject cannot be empty.')
        return
    
    hours_input = input('Hours studied: ').strip()

    # Validate hours studied
    try:
        hours  = float(hours_input)
    except ValueError:
        print('[!] Hours must be greater than 0.')
        return
    
    # Date: use today if user presses Enter
    date_input = input('Date (YYYY-MM-DD) or press Enter for today: ').strip()

    if date_input:
        date = date_input
    else:
        date = datetime.now().strftime('%Y-%m-%d')

    # Store as a dictionary
    session = {
        'subject': subject,
        'hours': hours,
        'date': date,
    }

    study_sessions.append(session)

    print(f'\n[+] Study session added: {subject} | {hours}h | {date}')


# ---- View Study Sessions ----
def view_study_session():
    """Displays all study sessions and total hours"""
    print('\n--- Your Study Sessions ---')

    if not study_sessions:
        print('  No study sessions yet. Add one from the menu.')
        return
    
    total_hours = 0

    for index, session in enumerate(study_sessions, start = 1):
        sub = session['subject']
        hrs = session['hours']
        dt = session['date']
        print(f'   {index}. {sub} | {hrs}h | {dt}')
        total_hours += hrs
    
    print(f'\n   Total hours: {len(study_sessions)} session(s) | {total_hours}s studied')


# ---- View Dashboard ----
def view_dashboard():
    """Displays the full dashboard summary."""
    print('\n' + '-' * 50)
    print('           DASHBOARD')
    print('-' * 50)

    # User info
    level = profile.get_level(total_xp)
    print(f'  Name: {profile.name}')
    print(f'  Level: {level}')
    print(f'  XP: {total_xp} / {level * UserProfile.XP_PER_LEVEL}')

    # Task stats
    completed_count = 0
    for task in tasks:
        if task.completed:
            completed_count += 1

    print(f'\n Tasks:       {completed_count} completed / {len(tasks)} total')

    # Study stats
    total_hours = 0
    for session in study_sessions:
        total_hours += session['hours']

    print(f'  Studying:   {total_hours}h across {len(study_sessions)} session(s)')
    print('-' * 50)

# ---- Handle Choices ----
def handle_choices(choice):
    """Process the user's menu selection."""
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        add_study_session()
    elif choice == "6":
        view_study_session()
    elif choice == "7":
        view_dashboard()
    elif choice == "8":
        print("\n>> Export CSV Report (coming soon)")
    elif choice == "9":
        save_data(profile, tasks, study_sessions, total_xp)
        print("\nGoodbye! Keep growing!")
        return False
    else:
        print("\n[!] Invalid choice. Please enter a number from 1 to 9.")

    return True


# ---- Main Program ----
def main():
    """Main function that runs the Growify application."""
    global profile, tasks, study_sessions, total_xp

    saved = load_data()

    if saved:
        profile = UserProfile(saved['profile']['name'])
        tasks = restore_tasks(saved['tasks'])
        study_sessions = saved['study_sessions']
        total_xp = saved['total_xp']
        print(f'\nWelcome back, {profile.name}!')
        print(f'  Level {profile.get_level(total_xp)} | {total_xp} XP | {len(tasks)} task(s)')

    name = input('\nEnter your name: ').strip()
    if not name:
        name = 'Echo'
    profile = UserProfile(name)
    
    print(f'\nHello, {profile.name}! Lets grow today.')

    running = True

    while running:
        show_menu()
        choice = input('\nEnter your choice (1-9): ')
        running = handle_choices(choice)

if __name__ == '__main__':
    main()