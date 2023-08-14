from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x820+100+100")
        self.root.title('Employee Management System')

        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 40, 'bold'),
                          fg='white', bg='blue')
        lbl_title.place(x=0, y=0, width=1550, height=100)

        # For resizing the image of Logo
        #img_logo = Image.open('Image/Image4.webp')
        #img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        #self.photo_logo = ImageTk.PhotoImage(img_logo)

        #self.logo = Label(self.root, image=self.photo_logo)
        #self.logo.place(x=225, y=25, width=50, height=50)

        # Frame for Image

        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=100, width=1550, height=180)

        # Image 1
        # img1 = Image.open('Image/Image1.png')
        # img1 = img1.resize((500, 180), Image.ANTIALIAS)
        # self.photo1 = ImageTk.PhotoImage(img1)
        #
        # self.image1 = Label(self.root, image=self.photo1)
        # self.image1.place(x=0, y=100, width=500, height=180)

        # Image 2
        # img2 = Image.open('Image/Image3.png')
        # img2 = img2.resize((500, 180), Image.ANTIALIAS)
        # self.photo2 = ImageTk.PhotoImage(img2)
        #
        # self.image2 = Label(self.root, image=self.photo2)
        # self.image2.place(x=510, y=100, width=500, height=180)

        # Image 3
        # img3 = Image.open('Image/Image2.png')
        # img3 = img3.resize((500, 180), Image.ANTIALIAS)
        # self.photo3 = ImageTk.PhotoImage(img3)
        #
        # self.image3 = Label(img_frame, image=self.photo3)
        # self.image3.place(x=1020, y=0, width=500, height=180)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=290, width=1510, height=530)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                 font=('times new roman', 14, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1490, height=260)

        # Label and Entry fields
        lbl_dep = Label(upper_frame, text='Department', font=('arial', 10, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=5, sticky=W)
        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('arial', 11, 'bold'), width=20)
        combo_dep['value'] = ('Select Department', 'HR', 'Software Engineer', 'Manager', 'Senior Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Name
        lbl_name = Label(upper_frame, text='Designition:', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=0, column=2, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=0, column=3, padx=5, pady=7)

        # Label_Designition
        lbl_Designition = Label(upper_frame, text='Name ', font=('arial', 10, 'bold'), bg='white')
        lbl_Designition.grid(row=1, column=0, padx=5, pady=7, sticky=W)

        txt_Designition = ttk.Entry(upper_frame, textvariable=self.var_designition, width=22,
                                    font=('arial', 11, 'bold'))
        txt_Designition.grid(row=1, column=1, padx=5, pady=7)

        # Email
        lbl_email = Label(upper_frame, text='Email:', font=('arial', 10, 'bold'), bg='white')
        lbl_email.grid(row=1, column=2, padx=5, pady=7, sticky=W)

        txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=('arial', 11, 'bold'))
        txt_email.grid(row=1, column=3, padx=5, pady=7)

        # Address
        lbl_name = Label(upper_frame, text='Address:', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=2, column=0, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=2, column=1, padx=5, pady=7)

        # Married
        lbl_married = Label(upper_frame, text='Married Satus', font=('arial', 10, 'bold'), bg='white')
        lbl_married.grid(row=2, column=2, padx=5, sticky=W)
        combo_married = ttk.Combobox(upper_frame, textvariable=self.var_married, font=('arial', 11, 'bold'), width=20)
        combo_married['value'] = ('Select Status', 'Married', 'Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # DOB
        lbl_name = Label(upper_frame, text='DOB', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=3, column=0, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=3, column=1, padx=5, pady=7)

        # DOJ
        lbl_name = Label(upper_frame, text='DOJ:', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=3, column=2, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=3, column=3, padx=5, pady=7)

        # Id Proof

        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb, font=('arial', 11, 'bold'), width=20)
        combo_dep['value'] = ('Select ID Proof', 'PAN CARD', 'AADHAR CARD', 'DRIVING LICENCE', 'VOTER ID')
        combo_dep.current(0)
        combo_dep.grid(row=4, column=0, padx=5, pady=10, sticky=W)

        txt_proof = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22, font=('arial', 11, 'bold'))
        txt_proof.grid(row=4, column=1, padx=5, pady=7)

        # Gender
        lbl_gen = Label(upper_frame, text='Gender', font=('arial', 10, 'bold'), bg='white')
        lbl_gen.grid(row=4, column=2, padx=5, sticky=W)
        combo_gen = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 11, 'bold'), width=20)
        combo_gen['value'] = ('Select Gender', 'Male', 'Female', 'Other')
        combo_gen.current(0)
        combo_gen.grid(row=4, column=3, padx=5, pady=10, sticky=W)

        # Phone
        lbl_name = Label(upper_frame, text='Phone No:', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=0, column=4, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=0, column=5, padx=5, pady=7)

        # Country
        lbl_name = Label(upper_frame, text='Country:', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=1, column=4, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_country, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=1, column=5, padx=5, pady=7)

        # CTC
        lbl_name = Label(upper_frame, text='Salary(CTC):', font=('arial', 10, 'bold'), bg='white')
        lbl_name.grid(row=2, column=4, padx=5, pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=2, column=5, padx=5, pady=7)

        # Image
        # img4 = Image.open('Image/Image5.jpg')
        # img4 = img4.resize((220, 220), Image.ANTIALIAS)
        # self.photo4 = ImageTk.PhotoImage(img4)
        #
        # self.image4 = Label(upper_frame, image=self.photo4)
        # self.image4.place(x=1020, y=0, width=220, height=220)

        # Button_Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1270, y=5, width=190, height=210)

        button_add = Button(button_frame, text="Save", command=self.save, font=("arial", 16, "bold"), width=13,
                            fg='white', bg='blue')
        button_add.grid(row=0, column=0, padx=1, pady=6)

        button_update = Button(button_frame, text="Update", command=self.update_data, font=("arial", 16, "bold"),
                               width=13, fg='white', bg='blue')
        button_update.grid(row=1, column=0, padx=1, pady=6)

        button_delete = Button(button_frame, text="Delete", command=self.delete, font=("arial", 16, "bold"), width=13,
                               fg='white', bg='blue')
        button_delete.grid(row=2, column=0, padx=1, pady=6)

        button_clear = Button(button_frame, text="Clear", command=self.clear, font=("arial", 16, "bold"), width=13,
                              fg='white', bg='blue')
        button_clear.grid(row=3, column=0, padx=1, pady=6)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table',
                                font=('times new roman', 14, 'bold'), fg='red')
        down_frame.place(x=10, y=270, width=1490, height=250)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information',
                                  font=('times new roman', 14, 'bold'), fg='red')
        search_frame.place(x=6, y=0, width=1470, height=60)

        # Search By
        search_by = Label(search_frame, text='Search By:', font=('arial', 10, 'bold'), bg='red', fg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        self.var_com_search = StringVar()
        combo_tex = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=('arial', 11, 'bold'), width=20)
        combo_tex['value'] = ('Select option', 'Phone', 'ID_Proof')
        combo_tex.current(0)
        combo_tex.grid(row=0, column=1, padx=5, sticky=W)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('arial', 11, 'bold'))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text="Search", command=self.search, font=("arial", 11, "bold"), width=14,
                            bg='green', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        btn_search = Button(search_frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"),
                            width=14, bg='green', fg='white')
        btn_search.grid(row=0, column=4, padx=5)

        # =================== EMployee Table =====================
        # Table Frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, columns=(
        'dep', 'name', 'degi', 'email', 'address', 'married', 'dob', 'doj', 'idproofcomb', 'idproof', 'gender', 'phone',
        'country', 'salary',), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('degi', text='Degignition')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('married', text='Married Status')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproofcomb', text='ID Type')
        self.employee_table.heading('idproof', text='ID Proof')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'
        self.employee_table.column("dep", width=100, )
        self.employee_table.column("name", width=100)
        self.employee_table.column("degi", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("married", width=120)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("idproofcomb", width=100)
        self.employee_table.column("idproof", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("phone", width=100)
        self.employee_table.column("country", width=100)
        self.employee_table.column("salary", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ++++++++++++++++++++++++ Save Function ++++++++++++++++++++++++++++

    def save(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Feilds are required!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Shubham@123',
                                               database='Employee')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designition.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Shubham@123', database='Employee')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from emp')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get cursor
    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    # Update Data
    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Feilds are required!')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure to update the Employee data')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Shubham@123',
                                                   database='Employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        'update emp set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',
                        (
                            self.var_dep.get(),
                            self.var_name.get(),
                            self.var_designition.get(),
                            self.var_email.get(),
                            self.var_address.get(),
                            self.var_married.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_idproofcomb.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_country.get(),
                            self.var_salary.get(),
                            self.var_idproof.get()
                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee Successfully Updated', parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error', f'Due to: {str(ex)}', parent=self.root)

    # Delete Data
    def delete(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                dele = messagebox.askyesno('Delete', 'Are you sure to delete this Employee', parent=self.root)
                if dele > 0:

                    conn = mysql.connector.connect(host='localhost', username='root', password='Shubham@123',
                                                   database='Employee')
                    my_cursor = conn.cursor()
                    sql = 'delete from emp where id_proof=%s'
                    value = (self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not dele:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee Successfully Deleted', parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error', f'Due to: {str(ex)}', parent=self.root)

    # Clear Data
    def clear(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Select status")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # Search Data
    def search(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Shubham@123',
                                               database='Employee')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from emp where ' + str(self.var_com_search.get()) + " LIKE'%" + str(
                    self.var_search.get() + "%'"))
                row = my_cursor.fetchall()
                if len(row) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in row:
                        self.employee_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)


if __name__ == "__main__":
    root = Tk()
    emp = Employee(root)
    root.mainloop()