#By Amrit Gautam

import csv
import pandas as pd
import os
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

class Book:
    def __init__(self):
        self.book = ""
        self.author = ""
        self.content = ""
        self.note = ""

    def saver(self):
        with open("books.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["Book", "Author", "Note"])
            writer.writerow([self.book, self.author, self.note])

    def book_creater(self):
        with open(f"{self.book}.txt", 'w', encoding='utf-8') as f:
            f.write(self.content)

def search(name):
    with open("books.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if name in row:
                system = platform.system() #To get the info which system is this code running.
                if system == "Windows":
                    os.startfile(f"{name}.txt") #To give commands to system to do specific task.
                elif system == "Darwin":
                    subprocess.run(["open", f"{name}.txt"])
                else:
                    subprocess.run(["xdg-open", f"{name}.txt"])

def view_books():
    try:
        df = pd.read_csv("books.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "No books found!!") #To display a popup if smt happens.
        return 

    win = tk.Toplevel(root) #tk.TopLevel: window for each popup or new independent window.
    win.title("Books Library")
    win.geometry("500x300")

    tree = ttk.Treeview(win, columns=("Book","Author","Note"), show="headings") #Table like widget to display smt in tAble.
    tree.heading("Book", text="Book") #To create a label which shows at top of each column.
    tree.heading("Author", text="Author")
    tree.heading("Note", text="Note")
    tree.pack(fill=tk.BOTH, expand=True) #To let widget expand and occupy space when window resizes.

    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(row["Book"], row["Author"], row["Note"]))

def add_book():
    win = tk.Toplevel(root)
    win.title("Add a Book")
    win.geometry("400x500")

    tk.Label(win, text="Book").pack()
    book_entry = tk.Entry(win) # To take single line text input from user.
    book_entry.pack()

    tk.Label(win, text="Author").pack()
    author_entry = tk.Entry(win)
    author_entry.pack()

    tk.Label(win, text="Content").pack()
    content_entry = tk.Text(win, height=10, width=40)   # To take multi line text input from user.
    content_entry.pack()

    tk.Label(win, text="Note").pack()
    note_entry = tk.Entry(win)
    note_entry.pack()

    def save_book():
        name = book_entry.get().strip().capitalize()
        author = author_entry.get().strip().capitalize()
        content = content_entry.get("1.0", tk.END).strip().capitalize()
        note = note_entry.get().strip().capitalize()

        if name and author and content:
            book = Book()
            book.book = name
            book.author = author
            book.content = content
            book.note = note
            book.saver()
            book.book_creater()
            messagebox.showinfo("Success", f"'{name}' added!")
            win.destroy()
        else:
            messagebox.showwarning("Error", "All fields are required!!!")

    tk.Button(win, text="Save book", command=save_book).pack(pady=10)

def read_book():
    try:
        pd.read_csv("books.csv")  # just check file exists
    except FileNotFoundError:
        messagebox.showerror("Error", "No books found!")
        return

    win = tk.Toplevel(root)  
    win.title("Read Book")
    win.geometry("300x200")

    tk.Label(win, text="Enter book name to read").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    def open_book():
        name = name_entry.get().strip().capitalize()
        search(name)
    
    tk.Button(win, text="Read", command=open_book).pack(pady=10)

root = tk.Tk() #tk.Tk(): main application window, or an instance having other windows inside.
root.title("Digital Library") #title which appears at the top left side
root.geometry("400x300") #to set the size of the pixels

tk.Label(root, text="Welcome to your library", font=("Arial", 16)).pack(pady=20) #tk.Label: simple text displayed at front.
tk.Button(root, text="Add Book", width=20, command=add_book).pack(pady=5) # A clickable button.
tk.Button(root, text="View Books", width=20, command=view_books).pack(pady=5)
tk.Button(root, text="Read a book", width=20, command=read_book).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

root.mainloop()
