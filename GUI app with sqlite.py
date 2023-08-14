import tkinter as tk
import sqlite3

def fetch_db():
    connection = sqlite.connect("data/recipes.")
def load_frame2():
    print("Hello baby")

root = tk.Tk()
root.title("Recipe Picker")

frame1 = tk.Frame(root, width=500,height=600,bg="#3d6466")
frame1.grid(row=0, column=0)

tk.Button(
    frame1,
    text="Shuffle",
    font=("TKHeadingFont",20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    #activebackground="#badee2",
    #activeforeeground="black",
    command=load_frame2()).pack()




root.mainloop()