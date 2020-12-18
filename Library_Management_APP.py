#################        IMPORTING THE LIBRARIES          ################



import tkinter as tk
from tkinter import ttk
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import *
from PIL import Image, ImageTk      # PILLOW
import sqlite3
from tkinter import messagebox
import time
import datetime
from datetime import date
from twilio.rest import Client      # TWILIO



################                  Student Database                     ################


conn0 = sqlite3.connect("Student.db")
cursor0 = conn0.cursor()
cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
conn0.commit()
    

################                   Admin Database                      ###############


conn = sqlite3.connect("Admin.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
conn.commit()

################                   Books Database                      ################


conn1 = sqlite3.connect('books.db')
cursor1 = conn1.cursor()
cursor1.execute((''' create table if not exists book
        (Name text not null,
        Author text not null,
        Genre text not null,
        Copies text not null,
        Location text not null)'''))
conn1.commit()
print('Table Created')



###############                    RECORDS DATABASE                  ###############


conn2 = sqlite3.connect("issue_record.db")
cursor2 = conn2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS record (Book_id int primary key, username TEXT , mobile_no TEXT, book_name TEXT, issue_date TEXT, return_date TEXT)")
conn2.commit()


#################                 Finding dates   (Twilio)             #################

def dates():

    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()
    cursor2.execute('select Book_id,username,mobile_no,book_name,issue_date,return_date from record')


    x = datetime.datetime.now()

    today = date.today()
    now_date = today.strftime("%d/%m/%Y")
    
    now_day = int(x.strftime('%d'))
    now_month = int(x.strftime('%m'))
    now_year = int(x.strftime('%Y'))
    
    for row in cursor2:
        #print(row[5])
        due_date = str(row[5])

        due_dayy = int(due_date[0:2])
        due_month = int(due_date[3:5])
        due_year = int(due_date[6:])

        if now_year == due_year and now_month == due_month and (due_dayy - now_day) == 1:

            mob_nu = str(row[2])

            print(str(mob_nu))

            account_sid = 'ACf9abce9b0251b69885fde795d42dfdb1'

            auth_token = '0231ece7baa2db0f2c13ec1b66c4d034'

            client = Client(account_sid,auth_token)

            message = client.messages.create(
                body = 'This is a gentle reminder, Tomorrow is the last date for returning the book you borrowed from UEL',
                from_ = '+12284564378',
                to = row[2]
                )
            messagebox.showinfo('Success','Reminder has been sent')
            print(message.sid)


        




#################              CLOSE FINE WINDOW               ###################


def close_fine():
    root1.destroy()

    
################             STUDENT CHECKING FINE           ##################


def stu_fine_check():
    global root1
    

    stu_fine = my_tree3.focus()
    dictt = my_tree3.item(stu_fine)
    stu_return_vals = dictt.get('values')

    root1 = tk.Tk()
    root1.title('Fine Calculation')
    root1.geometry('350x350')
    root1.resizable(0,0)
    root1.rowconfigure(0,weight=1)
    root1.columnconfigure(0,weight=1)

    due_date = str(stu_return_vals[5])
    due_day = int(due_date[0:2])
    due_mon = int(due_date[3:5])
    due_year = int(due_date[6:])

    
    print(due_day)
    print(due_mon)
    print(due_year)

    
    x = datetime.datetime.now()

    today = date.today()
    return_date = today.strftime("%d/%m/%Y")
    
    return_day = int(x.strftime('%d'))
    return_month = int(x.strftime('%m'))
    return_year = int(x.strftime('%Y'))
    
    print(return_date)

    
    days_31 = [1,3,5,7,8,10,12]

    if return_year == due_year and return_month < due_mon:
        extra_days = int(0)

    elif return_year == due_year and return_month == due_mon and return_day <= due_day:
        extra_days = int(0)
        
    elif return_year == due_year and return_month == due_mon and return_day > due_day:
        extra_days = return_day - due_day
        fine = 1*extra_days
        print(fine)
        
    elif return_year == due_year and return_month > due_mon:
        extra_month = return_month - due_mon
        if extra_month == int(1):
            extra_days = (30 - due_day) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(2):
            extra_days = (30 - due_day) + int(30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(3):
            extra_days = (30 - due_day) + int(30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(4):
            extra_days = (30 - due_day) + int(30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(5):
            extra_days = (30 - due_day) + int(30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(6):
            extra_days = (30 - due_day) + int(30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(7):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(8):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(9):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(10):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(11):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31+31) + return_day
            print('Extra Days :',extra_days)

    Label(root1, text = 'Book Due Date :').place(x=50,y=50)
    Label(root1, text = due_date).place(x=200,y=50)

    Label(root1, text = 'Book Returning Date :').place(x=50,y=100)
    Label(root1, text = return_date).place(x=200,y=100)

    Label(root1, text = 'Total extra days :').place(x=50,y=150)
    Label(root1, text = (extra_days,'days')).place(x=200,y=150)
    

    Label(root1, text = 'Total Fine :').place(x=50,y=200)
    Label(root1, text = ('£1','x',extra_days,'=','£',extra_days)).place(x=200,y=200)

    Button(root1, text ='OK',command = close_fine).place(x=150,y=300)

    root1.mainloop()



#####################        ADMIN CHECKING FINE            #######################



def Fine():
    global root1
    
    curItems = my_tree1.focus()
    dic = my_tree1.item(curItems)
    return_vals = dic.get('values')


    root1 = tk.Tk()
    root1.title('Fine Calculation')
    root1.geometry('350x350')
    root1.resizable(0,0)
    root1.rowconfigure(0,weight=1)
    root1.columnconfigure(0,weight=1)

    due_date = str(return_vals[5])
    due_day = int(due_date[0:2])
    due_mon = int(due_date[3:5])
    due_year = int(due_date[6:])

    
    print(due_day)
    print(due_mon)
    print(due_year)

    
    x = datetime.datetime.now()

    today = date.today()
    return_date = today.strftime("%d/%m/%Y")
    
    return_day = int(x.strftime('%d'))
    return_month = int(x.strftime('%m'))
    return_year = int(x.strftime('%Y'))
    
    print(return_date)

    
    days_31 = [1,3,5,7,8,10,12]

    if return_year == due_year and return_month < due_mon:
        extra_days = int(0)

    elif return_year == due_year and return_month == due_mon and return_day <= due_day:
        extra_days = int(0)    
        
    elif return_year == due_year and return_month == due_mon and return_day > due_day:
        extra_days = return_day - due_day
        
    elif return_year == due_year and return_month > due_mon :
        extra_month = return_month - due_mon
        if extra_month == int(1):
            extra_days = (30 - due_day) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(2):
            extra_days = (30 - due_day) + int(30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(3):
            extra_days = (30 - due_day) + int(30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(4):
            extra_days = (30 - due_day) + int(30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(5):
            extra_days = (30 - due_day) + int(30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(6):
            extra_days = (30 - due_day) + int(30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(7):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(8):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(9):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(10):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31+30) + return_day
            print('Extra Days :',extra_days)
        elif extra_month == int(11):
            extra_days = (30 - due_day) + int(30+31+30+31+30+31+30+31+31) + return_day
            print('Extra Days :',extra_days)

    Label(root1, text = 'Book Due Date :').place(x=50,y=50)
    Label(root1, text = due_date).place(x=200,y=50)

    Label(root1, text = 'Book Returning Date :').place(x=50,y=100)
    Label(root1, text = return_date).place(x=200,y=100)

    Label(root1, text = 'Total extra days :').place(x=50,y=150)
    Label(root1, text = (extra_days,'days')).place(x=200,y=150)
    

    Label(root1, text = 'Total Fine :').place(x=50,y=200)
    Label(root1, text = ('£1','x',extra_days,'=','£',extra_days)).place(x=200,y=200)

    Button(root1, text ='OK',command = close_fine).place(x=150,y=300)

    root1.mainloop()
        




##################             RETURNING BOOK           #################



def return_book():
    global return_values
    
    curItem1 = my_tree1.focus()
    dic1 = my_tree1.item(curItem1)
    return_values = dic1.get('values')

    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute('select Name,Author,Genre,Copies,Location from book')

    
    
    for rows in cursor1:
        if rows[0] == return_values[3]:
            curr_copies = int(rows[3])+1
            cursor1.execute('update book set Copies = ?  where Name=?',(curr_copies,rows[0]))
            conn1.commit()
    
    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()
    cursor2.execute('select Book_id,username,mobile_no,book_name,issue_date,return_date from record')

    for row in cursor2:
        if row[0]==return_values[0]:
            cursor2.execute('delete from record where (Book_id,username,book_name)=(?,?,?)',(return_values[0],return_values[1],return_values[3]))
            conn2.commit()
            
            x = my_tree1.selection()[0]
            my_tree1.delete(x)
            messagebox.showinfo('Success','Book Returned')


    


##################          ADMIN SEARCHING IN THE RECORDS          #################



def search_records():
    search_re = record_search.get()
    
    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()
    cursor2.execute("select Book_id,username,mobile_no,book_name,issue_date,return_date from record WHERE username LIKE '%"+search_re+"%' or book_name LIKE '%"+search_re+"%'")
    rows = cursor2.fetchall()
    
    for data in my_tree1.get_children():
        my_tree1.delete(data)

    for i in rows:
        my_tree1.insert('','end',values=i)

    


##################          STUDENTS CHECKING THEIR RECORDS          #################



def student_check_records():

    global conn2,cursor2

    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()

    cursor2.execute('select Book_id,username,mobile_no,book_name,issue_date,return_date from record')

            
    Frame11()



##################          ADMIN CHECKING ALL THE RECORDS          #################



        
def check_records():

    global conn2,cursor2,rec

    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()
    rec = cursor2.execute('select Book_id,username,mobile_no,book_name,issue_date,return_date from record')

    Frame8()



    
##############          CREATING BOOK TRANSACTIONS DATABASE         ################



def create_record_db():

    conn2 = sqlite3.connect("issue_record.db")
    cursor2 = conn2.cursor()
    cursor2.execute("CREATE TABLE IF NOT EXISTS record (Book_id int primary key, username TEXT , mobile_no TEXT, book_name TEXT, issue_date TEXT, return_date TEXT)")

    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()

    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.execute('select username from login')

    username_list = []
    
    for u in cursor0:
        username_list.append(u[0])

    if (bookid and borr_n and borr_p and issued  and returnd)=="":
        messagebox.showinfo("Error","Fields cannot be empty.")
        
    elif int(get_values[3]) == 0:
        messagebox.showinfo('Error','Not Enough Books')

    elif borr_n not in username_list:
        messagebox.showinfo('Error','Username not in records')

    else:
        try:
            cursor2.execute("INSERT INTO record (Book_id,username,mobile_no,book_name,issue_date,return_date) VALUES(?,?,?,?,?,?)",(bookid,borr_n,borr_p,get_values[0],issued,returnd))
            conn2.commit()
            messagebox.showinfo("Success","Issued successfully")
            
            current_copies = int(get_values[3])
            #print(current_copies)
            remaining_copies = current_copies - 1
        
            cursor1.execute('update book set Copies = ?  where Name=?',(remaining_copies,get_values[0]))
            conn1.commit()
        except:
            messagebox.showinfo('Error','Book id already exists, It should be Unique')
            
    clear_treeview()


        
##################      GETTING BOOK BORROWER DETAILS       #################



def get_issue_details():
    global bookid,borr_n,borr_p,issued,returnd
    
    bookid = id_book.get()
    borr_n = borr_name.get()
    borr_p = borr_phn.get()
    issued = issue_d.get()
    returnd = return_d.get()

    
    create_record_db()
        



##################              SELECTING BOOK             #################    



def select_book():
    global get_values
    
    curItem = my_tree.focus()
    dic = my_tree.item(curItem)
    get_values = dic.get('values')

    Frame7()




##################          STUDENT SEARCHING THE DESIRED BOOK          #################



def student_search_books():
    stu_search_book = search_b.get()

    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute("select Name,Author,Genre,Copies,Location from book WHERE Name LIKE '%"+stu_search_book+"%' \
                                or Author LIKE '%"+stu_search_book+"%' or Genre LIKE '%"+stu_search_book+"%'")
    rows = cursor1.fetchall()
    
    for data in my_tree2.get_children():
        my_tree2.delete(data)

    for i in rows:
        my_tree2.insert('','end', values=i)




##################             ADMIN SEARCHING THE DESIRED BOOK          #################




def search_books():
    search_bo = search_b.get()

    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute("select Name,Author,Genre,Copies,Location from book WHERE Name LIKE '%"+search_bo+"%' or Author LIKE '%"+search_bo+"%' or Genre LIKE '%"+search_bo+"%'")
    rows = cursor1.fetchall()
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    
    for i in rows:
        my_tree.insert('','end',values=i)
            


    

##################    STUDENT READING THE BOOKS FROM BOOKS DATABASE      ######################



def student_check_books():
    global books_list1
    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute('select Name,Author,Genre,Copies,Location from book')

    books_list1 = []
    for rows in cursor1:
        books_list1.append(rows)
    Frame10()



##################    ADMIN READING THE BOOKS FROM BOOKS DATABASE      ######################
        


def check_books():
    global books_list
    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute('select Name,Author,Genre,Copies,Location from book')

    books_list = []
    for rows in cursor1:
        books_list.append(rows)
    Frame6()
    



##################         USER REGISTERING BY THEMSELVES        #######################


def stu_self_in():
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    
    if (unames and pws and phs)=='':
        messagebox.showinfo('Error', 'Fields cannot be empty')
    else:
        cursor0.execute("INSERT INTO login (username, password,mobile_no) VALUES(?,?,?)",(unames,pws,phs))
        conn0.commit()
        messagebox.showinfo("Success","Registered Successfully")
        show_frame(frame1)




def Stu_self_register():
    global unames,pws,phs
    
    unames = stu_unames.get()
    pws = stu_pws.get()
    phs = stu_phs.get()

    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor0.execute('select username from login')

    s=[]
    
    for row in cursor0:
        if row[0] == unames:
            s.append(row[0])
    
    if len(s)>=1:
        messagebox.showinfo('Error', 'Username Already Exists, Choose Another One!')
        s.clear()
    else:
        stu_self_in()


        

################          ADDING THE REGISTRATION DETAILS INTO DATABSE         ################


    
def stu_in():
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    
    if (uname and pw and ph)=='':
        messagebox.showinfo('Error', 'Fields cannot be empty')                           #      THIS BLOCK IS ACCESSED WHEN ADMIN WANTS TO ADD NEW MEMBERS
    else:
        cursor0.execute("INSERT INTO login (username, password,mobile_no) VALUES(?,?,?)",(uname,pw,ph))
        conn0.commit()
        messagebox.showinfo("Success","Registered Successfully")
        show_frame(frame3)



        
##################        CHECKING IF THE USERNAME ALREADY EXISTS BEFORE REGISTRATION          ##############



def Stu_register():
    global uname,pw,ph
    
    uname = stu_uname.get()
    pw = stu_pw.get()
    ph = stu_ph.get()

    conn0 = sqlite3.connect("Student.db")                                          #        THIS BLOCK IS ACCESSED WHEN ADMIN WANTS TO ADD NEW MEMBERS
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor0.execute('select username from login')

    s=[]
    
    for row in cursor0:
        if row[0] == uname:
            s.append(row[0])
            
    if len(s)>=1:
        messagebox.showinfo('Error', 'Username Already Exists, Choose Another One!')
        s.clear()
    else:
        stu_in()
        
          
##################          STUDENT LOGIN DATABASE           ##############


def student_Database():
    global conn0, cursor0
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    conn0.commit()

    login_stu()



##################          ADMIN LOGIN DATABASE              ##############


def admin_Database():
    global conn, cursor
    conn = sqlite3.connect("Admin.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor.execute('DELETE FROM login')
    cursor.execute("INSERT INTO login (username, password,mobile_no) VALUES('uellibrary', 'uel123',+447388397814)")
    conn.commit()
    login()




##################        INSERT BOOK INTO DATABASE         ##############



def insert_books():
    bookname = book_name.get()
    bookauthor = book_author.get()
    bookgenre = book_genre.get()
    bookcopies = book_copies.get()
    bookloc = book_location.get()

    if (bookname and bookauthor and bookgenre  and bookcopies and bookloc) == "":
        messagebox.showinfo("Error","Fields cannot be empty.")
    else:
        cursor1.execute('insert into book(Name,Author,Genre,Copies,Location) \
        values(?,?,?,?,?)',(bookname,bookauthor,bookgenre,bookcopies,bookloc))
        conn1.commit()
        messagebox.showinfo("Success","Book added successfully")
        show_frame(frame3)





##################        BOOKS DETAILS DATABASE         ##############

        
def books_database():
    global conn1, cursor1
    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute((''' create table if not exists book
        (Name text not null,
        Author text not null,
        Genre text not null,
        Copies text not null,
        Location text not null)'''))
    print('Table Created')
    Frame4()




##################       STUDENT LOGIN AUTHORIZATION        ##############



def login_stu():
    global name, password
    name = name_entry.get()
    password = password_entry.get()

    conn0 = sqlite3.connect('Student.db')
    cursor0 = conn0.cursor()
    cursor0.execute('select username, password from login')
    k = []
    for row in cursor0:
        if row[0] == name and row[1] == password:
            k.append(row[0])
            k.append(row[1])

    if len(k) == 2:
        Frame9()
        k.clear()
    else:
        messagebox.showinfo('Error','Username or Password Incorrect')
        


        
##################        ADMIN LOGIN AUTHORIZATION         ##############


def login():
    name = name_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('Admin.db')
    cursor = conn.cursor()
    cursor.execute('select username, password from login')
    k = []
    for row in cursor:
        if row[0] == name and row[1] == password:
            k.append(row[0])
            k.append(row[1])

    if len(k) == 2:
        Frame3()
        k.clear()
    else:
        messagebox.showinfo('Error','Username or Password Incorrect')





##################       FUNCTION TO CLEAR TREEVIEW ON STUDENT PAGE       ##############
        

def clear_student_treeview():
    for widgett in frame10.winfo_children():
        widgett.destroy()
    for widgets in frame11.winfo_children():
        widgets.destroy()
        
    Frame9()



##################        FUNCTION TO CLEAR TREEVIEW ON ADMIN PAGE         ##############
        

def clear_treeview():
    for widget in frame6.winfo_children():
        widget.destroy()
    for widgets in frame8.winfo_children():
        widgets.destroy()
    Frame3()
    



##################                          FRAME-11    (STUDENT CHECKING HIS OWN RECORDS)                    ##############



def Frame11():

    global record_search, my_tree3
    
    show_frame(frame11)
    
    style = ttk.Style(frame11)
    style.configure('Treeview', rowheight=40)

    my_tree3 = ttk.Treeview(frame11, columns = (0,1,2,3,4,5), show = 'headings')

    h_s_b = ttk.Scrollbar(frame11, orient="horizontal", command=my_tree3.xview)
    h_s_b.pack(side='bottom', fill='x')

    my_tree3.configure(xscrollcommand=h_s_b.set)

    my_tree3.heading(0,text = 'Book Id')
    my_tree3.heading(1,text = 'Name')
    my_tree3.heading(2,text = 'mobile')
    my_tree3.heading(3,text = 'book name')
    my_tree3.heading(4,text = 'issue date')
    my_tree3.heading(5,text = 'return date')

    
    q = 0
    
    for records in cursor2:
        if records[1] == name:
            my_tree3.insert(parent='',index = 'end',iid = q,text = '',values=(records[0],records[1],records[2],records[3],records[4],records[5]))
            q = q+1


    fine_but = Button(frame11, text = 'Check Fine',command = stu_fine_check,font = ('times',17,'bold italic')).place(x=400,y=100)

    Button(frame11,text = 'Go Back',command = clear_student_treeview, font = ('times',17,'bold italic')).place(x=600,y=100)
    
    my_tree3.bind('<ButtonRelease-1>',fine_but)
    
    my_tree3.pack(side = 'bottom', fill = X)




##################                          FRAME-10   (STUDENT CHECKING AVAILABLE BOOKS)                     ##############



def Frame10():
    global my_tree2, search_b
    
    show_frame(frame10)

    style = ttk.Style(frame10)
    style.configure('Treeview', rowheight=40)

    my_tree2 = ttk.Treeview(frame10, columns = (1,2,3,4,5), show = 'headings')


    my_tree2.heading(1,text = 'Name')
    my_tree2.heading(2,text = 'Author')
    my_tree2.heading(3,text = 'Genre')
    my_tree2.heading(4,text = 'Copies')
    my_tree2.heading(5,text = 'Location')


    
    m = 0
    for l in books_list1:
        my_tree2.insert(parent='',index = 'end',iid = m,text = '',values=(l[0],l[1],l[2],l[3],l[4]))
        m = m+1


    search_b = StringVar()
    Entry(frame10, textvariable = search_b).place(x=50,y=100,width=400,height=40)
    
    Button(frame10,text = 'Search',command = student_search_books, font = ('times',15,'bold italic')).place(x=500,y=100)

    
    Button(frame10,text = 'Back',command = clear_student_treeview,font = ('times',15,'bold italic')).place(x=600,y=100)


    my_tree2.pack(side = 'bottom', fill = X)




##################                          FRAME-9   (STUDENT OPERATIONS)                      ##############


def Frame9():
    show_frame(frame9)

    Button(frame9, text = 'Check Available Books', command = student_check_books, bg = '#FFFFFF', font = ('times',15,'bold italic')).place(x=400,y=200)
    Button(frame9, text = 'Check Records',command = student_check_records, bg = '#FFFFFF',font = ('times',15,'bold italic')).place(x=430,y=300)

    Button(frame9, text = 'Logout',command = Frame1,bg = '#FFFFFF', font = ('times',15,'bold italic')).place(x=460,y=400)




##################                          FRAME-8   (CHECK AND RETURN RECORD)  (Admin)                    ##############


def Frame8():

    global record_search, my_tree1
    
    show_frame(frame8)
    
    style = ttk.Style(frame8)
    style.configure('Treeview', rowheight=40)

    my_tree1 = ttk.Treeview(frame8, columns = (0,1,2,3,4,5), show='headings')

    h_s_b = ttk.Scrollbar(frame8, orient="horizontal", command=my_tree1.xview)
    h_s_b.pack(side='bottom', fill='x')

    my_tree1.configure(xscrollcommand=h_s_b.set)

    my_tree1.heading(0,text = 'Book Id')
    my_tree1.heading(1,text = 'Name')
    my_tree1.heading(2,text = 'mobile')
    my_tree1.heading(3,text = 'book name')
    my_tree1.heading(4,text = 'issue date')
    my_tree1.heading(5,text = 'return date')


    
    q = 0
    for records in cursor2:
        my_tree1.insert(parent='',index = 'end',iid = q,text = '',values=(records[0],records[1],records[2],records[3],records[4],records[5]))
        q = q+1


    record_search=StringVar()
    Entry(frame8, textvariable = record_search).place(x=50,y=100,width=400,height=40)
    
    Button(frame8,text = 'Search',command = search_records, font = ('times',15,'bold italic')).place(x=500,y=100)

    b2 = Button(frame8,text = 'Return',command = return_book, font = ('times',15,'bold italic')).place(x=600,y=100)

    fine_button = Button(frame8,text = 'check fine', command =Fine, font = ('times',15,'bold italic')).place(x=700,y=100)

    Button(frame8,text = 'Back',command = clear_treeview, font = ('times',15,'bold italic')).place(x=850,y=100)

    my_tree1.bind('<ButtonRelease-1>',fine_button)

    my_tree1.bind('<ButtonRelease-1>', b2)
    
    my_tree1.pack(side = 'bottom', fill = X)




##################                          FRAME-7    (ISSUE DETAILS)                     ##############



def Frame7():
    global id_book,borr_name, borr_phn, issue_d, return_d

    show_frame(frame7)
    
    Label(frame7,text = 'Book Id : ',font = ('times',15,'bold italic')).place(x=100,y=100)
    id_book = StringVar()
    Entry(frame7, textvariable = id_book).place(x=280,y=100)

    Label(frame7,text = 'Username : ',font = ('times',15,'bold italic')).place(x=100,y=150)
    borr_name = StringVar()
    Entry(frame7, textvariable = borr_name).place(x=280,y=150)

    Label(frame7,text = 'Mobile number : ',font = ('times',15,'bold italic')).place(x=100,y=200)
    borr_phn = StringVar()
    Entry(frame7, textvariable = borr_phn).place(x=280,y=200)

    Label(frame7,text = 'Issue Date : ',font = ('times',15,'bold italic')).place(x=100,y=250)
    issue_d = StringVar()
    Entry(frame7, textvariable = issue_d).place(x=280,y=250)

    Label(frame7,text = 'Return Date : ',font = ('times',15,'bold italic')).place(x=100,y=300)
    return_d = StringVar()
    Entry(frame7, textvariable = return_d).place(x=280,y=300)

    Button(frame7,text = 'Issue',command = get_issue_details,font = ('times',15,'bold italic')).place(x=250,y=370)

    Button(frame7,text = 'Back',command = clear_treeview, font = ('times',15,'bold italic')).place(x=180,y=370)





##################                          FRAME-6   (CHECK AND ISSUE AVAILABLE BOOKS)  (Admin)                    ##############



def Frame6():
    
    global my_tree, search_b
    show_frame(frame6)

    style = ttk.Style(frame6)
    style.configure('Treeview', rowheight=40)

    my_tree = ttk.Treeview(frame6,columns=(1,2,3,4,5), show='headings')


    my_tree.heading(1,text = 'Name')
    my_tree.heading(2,text = 'Author')
    my_tree.heading(3,text = 'Genre')
    my_tree.heading(4,text = 'Copies')
    my_tree.heading(5,text = 'Location')


    
    m = 0
    for l in books_list:
        my_tree.insert(parent='',index = 'end',iid = m,text = '',values=(l[0],l[1],l[2],l[3],l[4]))
        m = m+1


    search_b=StringVar()
    Entry(frame6, textvariable = search_b).place(x=50,y=100,width=400,height=40)
    
    Button(frame6,text = 'Search',command = search_books, font = ('times',15,'bold italic')).place(x=500,y=100)

    b1 = Button(frame6,text = 'Issue Book',command = select_book,font = ('times',15,'bold italic')).place(x=600,y=100)
    
    Button(frame6,text = 'Back',command = clear_treeview,font = ('times',15,'bold italic')).place(x=750,y=100)

    my_tree.bind('<ButtonRelease-1>', b1)

    my_tree.pack(side = 'bottom', fill = X)




##################                          FRAME-5A (USERS SELF-REGISTRATION)                    ##############



def Frame5a():
    show_frame(frame5a)
    
    global stu_unames, stu_pws, stu_phs

    Label(frame5a,text = 'Username : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=150)
    stu_unames=StringVar()
    Entry(frame5a, textvariable = stu_unames).place(x=280,y=150)

    Label(frame5a,text = 'Password : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=200)
    stu_pws = StringVar()
    Entry(frame5a, textvariable = stu_pws).place(x=280,y=200)

    Label(frame5a,text = 'Phone number : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=250)
    stu_phs = StringVar()
    Entry(frame5a, textvariable = stu_phs).place(x=280,y=250)

    Button(frame5a, text = 'Submit',command = Stu_self_register,font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=300,y=300)

    Button(frame5a, text = 'Back', command = Frame1, font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=220,y=300)



##################                          FRAME-5  (ADMIN REGISTERING NEW MEMBERS)                       ##############


    
def Frame5():
    show_frame(frame5)
    global stu_uname, stu_pw, stu_ph

    Label(frame5,text = 'Username : ',font = ('times',15,'bold italic')).place(x=100,y=150)
    stu_uname=StringVar()
    Entry(frame5, textvariable = stu_uname).place(x=280,y=150)

    Label(frame5,text = 'Password : ',font = ('times',15,'bold italic')).place(x=100,y=200)
    stu_pw=StringVar()
    Entry(frame5, textvariable = stu_pw).place(x=280,y=200)

    Label(frame5,text = 'Phone number : ',font = ('times',15,'bold italic')).place(x=100,y=250)
    stu_ph=StringVar()
    Entry(frame5, textvariable = stu_ph).place(x=280,y=250)

    Button(frame5, text = 'Submit',command = Stu_register,font = ('times',15,'bold italic')).place(x=300,y=300)

    Button(frame5, text = 'Back', command = Frame3,font = ('times',15,'bold italic')).place(x=220,y=300)



##################                          FRAME-4  (ADDING BOOK PAGE)                       ##############


def Frame4():
    show_frame(frame4)
    global book_name,book_author,book_genre,book_copies,book_location
    
    Label(frame4, text = 'Book Name : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=150)
    book_name=StringVar()
    Entry(frame4, textvariable = book_name).place(x=280,y=150)

    Label(frame4, text = 'Author : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=200)
    book_author=StringVar()
    Entry(frame4, textvariable = book_author).place(x=280,y=200)

    Label(frame4, text = 'Genre : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=250)
    book_genre=StringVar()
    Entry(frame4, textvariable = book_genre).place(x=280,y=250)

    Label(frame4, text = 'Copies : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=300)
    book_copies=StringVar()
    Entry(frame4, textvariable = book_copies).place(x=280,y=300)

    Label(frame4, text = 'Location : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=350)
    book_location=StringVar()
    Entry(frame4, textvariable = book_location).place(x=280,y=350)


    Button(frame4, text = 'Submit', command= insert_books, font = ('times',15,'bold italic'),bg = '#ffedf9').place(x=300,y=425)

    Button(frame4, text = 'Back', command = Frame3, font = ('times',15,'bold italic'),bg = '#ffedf9').place(x=200,y=425)



##################                          FRAME-3  (ADMIN OPERATIONS)                       ##############

    
def Frame3():
    show_frame(frame3)
    
    Button(frame3, text = 'Add Book',command=books_database, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=100)
    Button(frame3, text = 'Add Members',command = Frame5, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=170)
    Button(frame3, text = 'Issue Book',command = check_books, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=240)
    Button(frame3, text = 'Check Record',command = check_records, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=310)
    Button(frame3, text = 'Reminder', command = dates, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=370)


    Button(frame3, text = 'Logout',command = Frame1, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=450)

    

##################                          FRAME-2A  (STUDENT LOGIN PAGE)                      ##############


def Frame2a():
    show_frame(frame2a)

    global name_entry
    global password_entry

    Label(frame2a, text = 'Username : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=170)
    Label(frame2a, text = 'Password : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=240)

    name_entry=StringVar()
    Entry(frame2a,textvariable=name_entry).place(x=170,y=170)

    password_entry=StringVar()
    Entry(frame2a,textvariable=password_entry, show = '*').place(x=170,y=240)
    
    Button(frame2a, text = 'Sign In',command = student_Database ,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=320)
    Button(frame2a, text = 'Go Back',command = Frame1 ,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=380)



##################                          FRAME-2  (ADMIN LOGIN PAGE)                       ##############


def Frame2():
    show_frame(frame2)
    global name_entry
    global password_entry

    Label(frame2, text = 'Username : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=170)
    Label(frame2, text = 'Password : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=240)

    name_entry=StringVar()
    Entry(frame2,textvariable=name_entry).place(x=170,y=170)

    password_entry=StringVar()
    Entry(frame2,textvariable=password_entry, show = '*').place(x=170,y=240)
    
    Button(frame2, text = 'Sign In',command = admin_Database ,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=320)
    Button(frame2, text = 'Go Back',command = Frame1 ,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=380)



##################                          FRAME-1  (HOME PAGE)                       ##############


def Frame1():
    show_frame(frame1)
    Label(frame1, text = 'Login as Admin : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=170)
    Button(frame1, text = 'Sign In', command = Frame2,bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=170)

    Label(frame1, text = 'Login as Student : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=270)
    Button(frame1, text = 'Sign In', command = Frame2a,bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=270)

    Label(frame1,text = 'Have  to Register?',font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=370)
    Button(frame1, text = 'Sign Up',command = Frame5a,font = ('times',15,'bold italic'),bg='#E0FFFF').place(x=800,y=370)

    Button(frame1, text = 'Exit',command = close,bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=700,y=450)


    
##################              FUNCTION TO EXIT THE APPLICATION             ##############


def close():
    root.destroy()


###########################################################################################

##################              FUNCTION TO RAISE DESIRED FRAMES             ##############

     
def show_frame(frame):
    frame.tkraise()


##################                       MAIN WINDOW                         ##############


root = tk.Tk()
root.title('UEL Library')
root.geometry('1000x650')
root.resizable(0,0)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)





##################                         FRAMES                            ##############


frame1 = Frame(root)                                  
frame2 = Frame(root)
frame2a = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame5a = Frame(root,bg='#8BB7FF')
frame6 = Frame(root)
frame7 = Frame(root)
frame8 = Frame(root)
frame9 = Frame(root,bg='#8BFFF1')
frame10 = Frame(root)
frame11 = Frame(root)

for frame in (frame1,frame2,frame2a,frame3,frame4,frame5,frame5a,frame6,frame7,frame8,frame9,frame10,frame11):
    frame.place(relheight=1,relwidth=1)

    

##################                 F R A M E - BACKGROUNDS                   ##############


    
F1_img = ImageTk.PhotoImage(Image.open('home_img.png'))
F1_background = tk.Label(frame1, image = F1_img)
F1_background.pack(side = "bottom", fill = "both", expand = "yes")


F2_img = ImageTk.PhotoImage(Image.open('admin_login.png'))
F2_background = tk.Label(frame2, image = F2_img)
F2_background.pack(side = "bottom", fill = "both", expand = "yes")

F2a_img = ImageTk.PhotoImage(Image.open('admin_login.png'))
F2a_background = tk.Label(frame2a, image = F2a_img)
F2a_background.pack(side = "bottom", fill = "both", expand = "yes")

F3_img = ImageTk.PhotoImage(Image.open('F3_img.png'))
F3_background = tk.Label(frame3, image = F3_img)
F3_background.pack(side = 'bottom', fill = 'both',expand = 'yes')


F4_img = ImageTk.PhotoImage(Image.open('F4_img.png'))
F4_background = tk.Label(frame4, image = F4_img)
F4_background.pack(side = "bottom", fill = "both", expand = "yes")



################################################################################


Frame1()                    # Running first frame


root.mainloop()

