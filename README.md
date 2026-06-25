# 🌱 Growify

**Growify** is a sleek, modern Command-Line Interface (CLI) application built in Python. It acts as your Personal Learning Dashboard, allowing you to track tasks, log study sessions, and gamify your learning journey with an XP system.

## ✨ Features

- **Modern UI**: Clean console interface with box-drawing characters and emojis.
- **Task Management**: Add, view, complete, and delete tasks.
- **Gamification**: Earn XP by completing tasks based on their difficulty (Easy, Medium, Hard). Level up as you learn!
- **Study Tracker**: Log the hours you spend studying different subjects.
- **Data Persistence**: Automatically saves your progress to a `.json` file so you never lose your data.
- **CSV Export**: Generate a spreadsheet-friendly report (`report.csv`) of all your tasks and study sessions.

---

## 💻 Sample Output

### Main Menu
Growify features a clean, bordered main menu that clears the screen between interactions:

```text
╭──────────────────────────────────────────────────╮
│               GrowthOS - Main Menu               │
├──────────────────────────────────────────────────┤
│                                                  │
│  [1] Add Task          [5] Add Study Session     │
│  [2] View Tasks        [6] View Study Sessions   │
│  [3] Complete Task     [7] View Dashboard        │
│  [4] Delete Task       [8] Export CSV Report     │
│                                                  │
│  [9] Exit                                        │
╰──────────────────────────────────────────────────╯
```

### Dashboard
The Dashboard displays your current level, a visual XP progress bar, and your overall statistics:

```text
╭──────────────────────────────────────────────────╮
│                    DASHBOARD                     │
├──────────────────────────────────────────────────┤
│ User:  Rohit                                     │
│ Level: 1                                         │
│ XP:    15 / 50 [######--------------]            │
│                                                  │
│ Tasks:     1 completed / 3 total                 │
│ Studying:  4.5h across 2 session(s)              │
╰──────────────────────────────────────────────────╯
```

---

## 🛠️ Installation & Usage

1. **Prerequisites**: Make sure you have Python 3.x installed on your computer.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the application:

```bash
python main.py
```

## 📂 Project Structure

- `main.py` — The core application loop and interactive menu logic.
- `helpers.py` — Contains the `Task` and `UserProfile` classes, and UI utilities like `clear_screen()`.
- `storage.py` — Handles reading and writing data safely to `data/growify_date.json`.
- `data/` — An automatically generated folder where the JSON save file and CSV exports are stored safely.

## 🧠 Concepts Practiced
- **Object-Oriented Programming (OOP)**
- **Data Structures (Lists & Dictionaries)**
- **File I/O (JSON & CSV)**
- **Exception Handling (`try/except`)**
- **Terminal UI Formatting**
