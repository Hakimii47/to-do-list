import tkinter as tk
from tkinter import messagebox
import os

# Function to add a task to the list
def add_task():
    task = task_input.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to remove the selected task
def remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Function to clear all tasks
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Function to save tasks to a file
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            tasks_listbox.insert(tk.END, task.strip())

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Input Field
task_input = tk.Entry(root, width=40)
task_input.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, width=15, bg="#6c5ce7", fg="white")
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=15, bg="#d63031", fg="white")
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", command=clear_tasks, width=15, bg="#fdcb6e", fg="black")
clear_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks, width=15, bg="#00cec9", fg="white")
save_button.pack(pady=5)

# Tasks Listbox
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Load tasks when the app starts
load_tasks()

# Run the application
root.mainloop()
