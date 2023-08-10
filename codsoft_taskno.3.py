import tkinter as tk
import random
import string

def generate_password(length, complexity):
    if complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "very strong":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.digits + string.punctuation

    if not characters:
        return "Error: Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(entry_length.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_text.delete("1.0", tk.END)  # Clear previous text
    password_text.insert(tk.END, password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the desired length of the password:")
entry_length = tk.Entry(root)

complexity_label = tk.Label(root, text="Select the complexity level:")

complexity_var = tk.StringVar()
complexity_var.set("medium")

complexity_radios = [
    ("Medium", "medium"),
    ("Strong", "strong"),
    ("Very Strong", "very strong")
]

for text, value in complexity_radios:
    radio = tk.Radiobutton(root, text=text, variable=complexity_var, value=value)
    radio.pack(anchor=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)

password_label = tk.Label(root, text="Generated Password:")
password_text = tk.Text(root, height=1, width=30)

length_label.pack()
entry_length.pack()

complexity_label.pack()

generate_button.pack()

password_label.pack()
password_text.pack()

root.mainloop()