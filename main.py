# Growify - Personal Learning Dashboard

# ---- Data Storage (List of dictionaries) ----
tasks = []
study_sessions = []

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


# ---- Handle Choices ----
def handle_choices(choice):
    """Process the user's menu selection."""
    if choice == "1":
        print("\n>> Add Task (coming soon)")
    elif choice == "2":
        print("\n>> View Tasks (coming soon)")
    elif choice == "3":
        print("\n>> Complete Task (coming soon)")
    elif choice == "4":
        print("\n>> Delete Task (coming soon)")
    elif choice == "5":
        print("\n>> Add Study Session (coming soon)")
    elif choice == "6":
        print("\n>> View Study Sessions (coming soon)")
    elif choice == "7":
        print("\n>> View Dashboard (coming soon)")
    elif choice == "8":
        print("\n>> Export CSV Report (coming soon)")
    elif choice == "9":
        print("\nGoodbye! Keep growing!")
        return False
    else:
        print("\n[!] Invalid choice. Please enter a number from 1 to 9.")

    return True


# ---- Main Program ----
def main():
    """Main function that runs the Growify application."""
    running = True

    while running:
        show_menu()
        choice = input('\nEnter your choice (1-9): ')
        running = handle_choices(choice)

if __name__ == '__main__':
    main()