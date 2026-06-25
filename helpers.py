# Growify - Helpers functions
# Contains Task class and utility functions

from datetime import datetime
import os

# XP reward for each difficulty level
XP_TABLE = {
    'easy': 10,
    'medium': 20,
    'hard': 30,
}

def clear_screen():
    """Clear the terminal screen."""
    # 'cls' for Windows, 'clear' for macOS and Linux
    os.system("cls" if os.name == "nt" else "clear")

class Task:
    """Represents a single task in GROWIFY."""

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.completed = False
        self.xp = XP_TABLE.get(difficulty, 10)
        self.date_created = datetime.now().strftime('%Y-%m-%d')

    def __str__(self):
        status = '[X]' if self.completed else '[ ]'
        return f' {status} {self.name} | {self.difficulty.capitalize()} | {self.xp} XP'
    

class UserProfile:
    """Stores the user's name and calculations level from XP."""

    XP_PER_LEVEL = 50   # Every 50 XP = 1 Level up

    def __init__(self, name):
        self.name = name

    def get_level(self, total_xp):
        """Calculate level based on total XP."""

        return (total_xp // UserProfile.XP_PER_LEVEL) + 1
