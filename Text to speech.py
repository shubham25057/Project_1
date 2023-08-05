# speak the word
from tkinter import *
import pyttsx3

root= Tk()
root.title = ("codemy")
root.geometry("1200x600")

def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.setProperty('rate',625) # Speed of voice
    engine.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root,font=("Helvetica",28))
my_entry.pack(pady=20)

my_button = Button(root,text="speak",command=talk)
my_button.pack(pady=28)
root.mainloop()