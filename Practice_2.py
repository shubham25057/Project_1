# dice simulator

import tkinter
import random

#create an object to create a window
window = tkinter.Tk()
window.geometry('450x300') #window geometry
window.configure(bg='black')  #window background #OPTIONAL
window.title('Dice Simulator')  #window title

#create dice
label = tkinter.Label(window, text='',font=('Helvetica',260),background='black',foreground='white')

#roll the dice
def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()


#button to command the application to roll the dice
button = tkinter.Button(window,text='Roll the dice!',width=20,font="times 20",
                        bg='yellow',bd=5,command=roll)
button.pack()

window.mainloop()#calling mainloop method which is used when your application is ready to run and it tells the code to keep displaying