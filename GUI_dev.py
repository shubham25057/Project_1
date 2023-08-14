# GUI->graphycs user interface
import tkinter as tk
import pymysql


def fun1():
    x = E1.get()
    y = E2.get()

    conn = PyMySQL.connect(host="localhost", user="root", passwd="", port=3306, db="aict")
    cur = conn.cursor()
    q1 = "insert into  `user`(`username`, `password`)  Values('" + x + "','" + y + "')"
    V1.set("Insert Sucessfully...")
    e1 = cur.execute(q1)
    conn.commit()
    conn.close()


frame1 = tk.Tk()
frame1.geometry("400x400")
frame1.resizable(False, False)
frame1.config(bg="#ccf381")
frame1.title("aict")
pic = tk.PhotoImage(file="D:\\gui\\Image\\download.png")
frame1.iconphoto(False, pic)

V1 = tk.StringVar()

L1 = tk.Label(text="User Id", fg="red", bg="white")
L1.place(relx=0.1, rely=0.2)

E1 = tk.Entry(text="", fg="blue", bd=3)
E1.grid(row=1, column=2, pady=2)

L2 = tk.Label(text="password", fg="red", bg="white")
L2.grid(row=2, column=0, pady=2)

E2 = tk.Entry(text="", fg="blue", bd=3)
E2.grid(row=2, column=1, pady=2)

b1 = tk.Button(frame1, text="DEV", fg="red", bg='white', bd=3, command=fun1)
b1.place(relx=0.3, rely=0.38, relwidth=0.3, relheight=0.1)

L3 = tk.Label(frame1, text="Result", fg="black", bg="#ccf381", bd=3, textvariable=V1)
L3.place(relx=0.2, rely=0.56, relwidth=0.4, relheight=0.1)

frame1.mainloop()