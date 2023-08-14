
from tkinter import *
import time

root= Tk()
root.title = ("codemy")
root.geometry("1200x600")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label.config(text=hour + ":" + minute + ":" + second + " "+am_pm)
    my_label.after(1000,clock)

    my_label2.config(text=time_zone  + " " + day)
def update():
    my_label.config(text="New Text")

my_label = Label(root, text="", font=("Helvetica",48),fg="red",bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica",48))
my_label2.pack(pady=20)

clock()

my_label.after(5000,update)
root.mainloop()