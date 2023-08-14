import tkinter as tk
from tkinter import *
import sqlite3

def fetch_db():
    connection = sqlite3.connect("My_Sql/Database.db")
    cursor = connection.cursor()
    cursor.execute("SELCT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    print(all_tables[0])
    connection.close()


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

# Defining the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)


root.mainloop()
