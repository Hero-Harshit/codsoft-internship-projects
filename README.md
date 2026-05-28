# Codsoft Internship Projects

This small collection contains simple Python projects built during an internship. Each script is standalone and runnable with Python 3.

**Prerequisites:**
- **Python:** 3.7+

**How to run:**
Open a terminal in this folder and run one of the scripts:

```bash
python calculator.py
python contactBook.py
python passwordGenerator.py
python rpsGame.py
python toDoApp.py
```

**Projects**

- **Calculator:** [calculator.py](calculator.py)
  - **What it does:** Basic interactive calculator that supports add, subtract, multiply, and divide.
  - **How to use:** Choose an operation and enter two numbers. Division by zero is handled with a friendly error.

- **Contact Book:** [contactBook.py](contactBook.py)
  - **What it does:** In-memory contact manager that can add, search, and display contacts.
  - **How to use:** Add contacts with name, surname, and phone; search by name; view all contacts.

- **Password Generator:** [passwordGenerator.py](passwordGenerator.py)
  - **What it does:** Generates a secure random password using the `secrets` module. Options include length, capitals, numbers, and symbols.
  - **How to use:** Provide desired length and yes/no options for character groups; the program ensures at least one character from each selected group.

- **Rock Paper Scissors:** [rpsGame.py](rpsGame.py)
  - **What it does:** Play a best-of-N rounds game against the computer with inputs `R`, `P`, or `S`.
  - **How to use:** Choose the number of rounds and enter choices each round; scores are tallied and final winner displayed.

- **To-Do List App:** [toDoApp.py](toDoApp.py)
  - **What it does:** Simple CLI to add, view, and delete tasks kept in memory during the program session.
  - **How to use:** Use the numbered menu to manage tasks. Task numbers are used when deleting.

**Notes & Ideas for Improvement**
- Persist data to files (JSON/CSV) for `contactBook.py` and `toDoApp.py` so entries survive restarts.
- Add input validation and unit tests for core functions (e.g., calculator operations).
- Package common helpers into modules and add a simple launcher script to pick a project.

If you'd like, I can:
- add a small test suite,
- persist contacts/tasks to files, or
- create a single menu script to choose which app to run.
