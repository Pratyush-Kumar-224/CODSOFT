import os
import platform
import tkinter as tk

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def on_number_click(number):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + number)

def on_operation_click(operation):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + " " + operation + " ")

def on_clear_click():
    entry_display.delete(0, tk.END)

def on_backspace_click():
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text[:-1])

def on_percent_click():
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, str(float(current_text) / 100))

def on_sign_change_click():
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, str(-float(current_text)))

def on_equal_click():
    expression = entry_display.get()
    try:
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"{expression} = {result}\n")
        history_text.config(state=tk.DISABLED)
    except Exception:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry_display = tk.Entry(root, font=("Helvetica", 20))
entry_display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=10)

# Button layout for numbers and operations
buttons = [
    ("AC", 1, 0), ("<-", 1, 1), ("+/-", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("%", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

for (text, row, column) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, command=on_equal_click, height=2, width=10)
    elif text == "AC":
        button = tk.Button(root, text=text, command=on_clear_click, height=2, width=10)
    elif text == "<-":
        button = tk.Button(root, text=text, command=on_backspace_click, height=2, width=10)
    elif text == "%":
        button = tk.Button(root, text=text, command=on_percent_click, height=2, width=10)
    elif text == "+/-":
        button = tk.Button(root, text=text, command=on_sign_change_click, height=2, width=10)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: on_number_click(t) if t.isnumeric() or t == "." else on_operation_click(t), height=2, width=10)
    button.grid(row=row, column=column, padx=5, pady=5)

history_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
history_text.grid(row=6, columnspan=6, padx=10, pady=10)

root.mainloop()