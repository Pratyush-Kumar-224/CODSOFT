import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        listbox_tasks.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

label = tk.Label(root, text="Enter task:")
entry_task = tk.Entry(root)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

listbox_tasks = tk.Listbox(root)

label.pack()
entry_task.pack()

add_button.pack()
remove_button.pack()

listbox_tasks.pack()

root.mainloop()