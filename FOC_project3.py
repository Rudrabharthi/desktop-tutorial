import os
import shutil
import tkinter as tk
from tkinter import filedialog

def input_path():
    input_path = filedialog.askdirectory()
    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, input_path)

def destination_folder():
    destination_folder = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder)

def organize():
    source_path = input_path_entry.get()
    destination_path = destination_folder_entry.get()

    if not source_path or not destination_path:
        status_label.config(text="Please select both input path and destination folder.")
        return

    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            extension = extension[1:].lower()
            destination_folder = os.path.join(destination_path, extension)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(item_path, os.path.join(destination_folder, item))
    status_label.config(text="Files organized successfully.")

# Create main window
root = tk.Tk()
root.title("File Organizer")

# Input path selection
input_path_label = tk.Label(root, text="Input Path:")
input_path_label.grid(row=0, column=0)
input_path_entry = tk.Entry(root, width=30)
input_path_entry.grid(row=0, column=1)
browse_input_button = tk.Button(root, text="Browse", command=input_path)
browse_input_button.grid(row=0, column=2)

# Destination folder selection
destination_folder_label = tk.Label(root, text="Destination Folder:")
destination_folder_label.grid(row=1, column=0)
destination_folder_entry = tk.Entry(root, width=30)
destination_folder_entry.grid(row=1, column=1)
browse_destination_button = tk.Button(root, text="Browse", command=destination_folder)
browse_destination_button.grid(row=1, column=2)

# Organize button
organize_button = tk.Button(root, text="Organize Files", command=organize)
organize_button.grid(row=2, column=1)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
