# Tkinter Calculator

A simple desktop calculator built with Python's Tkinter library. This was a fun mini-project to practice GUI programming — working with widgets, button click events, and basic state management using global variables.

## What it does

- Number pad (0–9) to enter values
- Basic arithmetic: addition, subtraction, multiplication, division
- `=` to calculate the result
- `Clear` to reset the entry field
- A single-line entry box where input and output are displayed

## How it works

The calculator uses Tkinter's `place()` geometry manager to position buttons on a fixed-size window (800x600). Each number button appends its digit to the entry field using string concatenation. The operator buttons (`+`, `-`, `*`, `/`) store the first number and the chosen operation in global variables, then the `=` button picks up the second number, runs the calculation, and displays the result.

## Tech used

- Python 3
- Tkinter (comes built-in with Python, no extra install needed)

## Running it

Just make sure Python is installed, then run:

```bash
python Claculator_app.py
```

A window should pop up with the calculator UI.

## Known limitations

This was built as a learning project, so it's not bulletproof:

- Only supports one operation at a time (no chaining like `2 + 3 * 4`)
- No decimal point support — only whole numbers
- Dividing by zero will crash the app instead of showing an error
- No keyboard input support — you have to click the buttons

## What I'd improve next

- Add a decimal/point button
- Handle divide-by-zero gracefully instead of crashing
- Support continuous calculations (chaining operators)
- Add keyboard bindings so you can type instead of clicking
- Maybe switch from `place()` to `grid()` for cleaner, more responsive layout

---

Built while learning GUI development in Python. Feedback and suggestions are welcome!
