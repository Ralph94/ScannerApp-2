import tkinter as tk
import tkinter.messagebox as MessageBox
from tkinter import *
from tkinter import ttk
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sqlite3
from pyzbar.pyzbar import decode



def show_frame(frame):
    frame.tkraise()


#Login section

def validate():
    username1 = E_username.get()
    password1 = E_password.get()
    if username1 == 'Raffp737' and password1 == 'DHL':
        MessageBox.showinfo(username1, 'logged verified please press enter to proceed to next page!')  # messagebox is a small notafication
    else:
        MessageBox.showinfo(username1, 'error please try again')

def validate2():
    username1 = E_ID.get()
    password1 = E_ID2.get()
    username2 = E_ID3.get()
    password2 = E_ID4.get()
    if username1 == 'RNOSP01' and password1 == 'DHL' and username2 == "RNO" and password2 == "RNO" :
        MessageBox.showinfo(username1, 'logged verified please press enter to proceed to next page!')  # messagebox is a small notafication
    else:
        MessageBox.showinfo(username1, 'error please try again')




# mw = mainwindow
root = Tk() # Our blank window
root.title("Route")
#root.state('zoomed')
root.geometry("800x500")
root.configure(bg="black")
root.iconbitmap('icon_W8P_icon.ico')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


window1 = Frame(root)
window2 = Frame(root)
window3 = Frame(root)
window4 = Frame(root)
for frame in (window1, window2, window3, window4):
    frame.grid(row=0,column=0, sticky='nsew')

# Define image backgrounds
back_ground = PhotoImage(file='fw.png')
window1.configure(background='black')
back_ground2 = PhotoImage(file="route.png")
back_ground3 = PhotoImage(file="sp.PNG")
icon_img = PhotoImage(file='cis.png')
back_ground4 = PhotoImage(file="bg2.png")
my_label = Label(window1, image=back_ground,background='grey')
my_label.place(x=0, y=0, relwidth=1, relheight=1)
my_label2 = Label(window2, image=back_ground2,background='grey')
my_label2.place(x=0, y=0, relwidth=1, relheight=1)
my_label3 = Label(window3, image=back_ground3,background='grey')
my_label3.place(x=0, y=0, relwidth=1, relheight=1)
my_label4 = Label(window4, image=back_ground4,background='grey')
my_label4.place(x=0, y=0, relwidth=1, relheight=1)
img = Label(window4, image=icon_img,background='grey')
img.configure(width=245, height=225)
img.place(x=-43, y=50)



#Window 1
text = Label(window1, text='Login Page', fg="red", font=('bold',15))
text.pack(fill=X)
user_name = Label(window1, text='User Name', fg="red", font=('impact',12))
user_name.place(x=200, y=90, anchor='w')
E_username = Entry(window1) # this our entry for our user name or in other words your textbox
E_username.place(x=300, y=90, anchor='w')
pass_word = Label(window1, text='Password', fg="red", font=('impact',12))
pass_word.place(x=200, y=130, anchor='w')
E_password = Entry(window1) # this our password for our user name
E_password.place(x=300, y=134, anchor='w')# placing our entry for our password
window1_title = Label(window1, text='Login section!', bg="yellow", fg='red')
window1_title.pack(fill='x')
submit=Button(window1, text='Verify login', fg='black',command=validate)
submit.place(relx=.5, rely=.4, anchor='center')
window1_button = Button(window1, text='Enter',fg='red',bg="yellow",font=('impact',20) ,command=lambda:show_frame(window2))
window1_button.place(relx=.5, rely=.9, anchor='center')



# END OF WINDOW 1!
#-----------------------------------------------------------------------------------

#Window 2

#Text1
ID = Label(window2, text='Courier ID:', font=('bold',12))
ID.config(height=1, width=20)
ID.place(relx=.2, y=110, anchor='center')
E_ID = Entry(window2)
E_ID.place(x=400, y=110, anchor='center')

#Text2
ID2 = Label(window2, text='Courier Name:', font=('bold',12))
ID2.config(height=1, width=30)
ID2.place(x=180, y=155, anchor='center')
E_ID2 = Entry(window2)
E_ID2.place(relx=.5, y=155, anchor='center')

#Text3
ID3 = Label(window2, text='Service:',font=('bold',12))
ID3.config(height=1, width=20)
ID3.place(x=145, y=200, anchor='center')
E_ID3 = Entry(window2)
E_ID3.config(width=7)
E_ID3.place(x=212, y=200, anchor='center')

#Text4
ID4 = Label(window2, text='Facility:',font=('bold',12))
ID4.config(height=1, width=20)
ID4.place(x=350, y=200, anchor='center')
E_ID4 = Entry(window2)
E_ID4.config(width=7)
E_ID4.place(x=417, y=200, anchor='center')


#Text5
ID5 = Label(window2, text='Route I.D:',font=('bold',12))
ID5.config(height=1, width=20)
ID5.place(x=150, y=275, anchor='center')
E_ID5 = Entry(window2)
E_ID5.config(width=12)
E_ID5.place(x=300, y=278, anchor='center')

#Text6
ID6 = Label(window2, text='Cycle code:',font=('bold',12))
ID6.config(height=1, width=25)
ID6.place(x=510, y=276, anchor='center')
E_ID6 = Entry(window2)
E_ID6.config(width=12)
E_ID6.place(x=690, y=278, anchor='center')

# Checkbox
def display():
    if(x.get()==1):
        print("NICE")
x = IntVar()

check_button = Checkbutton(window2, text="Service Partner:", variable=x,onvalue=1,offvalue=0,command=display)
check_button.config(height=1, width=40)
check_button.place(x=610, y=200, anchor='center')
text = Label(window2, text='Route Page', fg="red", font=('bold',15))
text.pack(fill=X)

window2_title = Label(window2, text='Route Credentials!', bg="yellow", fg='red')
window2_title.pack(fill='x')
window2_button = Button(window2, text='Sign on',bg='yellow',fg='red',font=('impact',20), command=lambda:show_frame(window3))
window2_button.config(height=1)
window2_button.pack(fill='both',side=BOTTOM,pady=0)
submit=Button(window2, text='Verify login', fg='black',command=validate2)
submit.place(relx=.5, rely=.7, anchor='center')

# END OF WINDOW 2!
#-----------------------------------------------------------------------------------


#Window 3
frame = cv2.imread('QR2.png')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def scan():
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            print(barcode.data)
            myData = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
            print(myData)
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            # print("Data", obj.data)
            scanned.config(text=obj.data)
            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
            print("Barcode scan sucessful ")


        cv2.imshow("Frame",frame)

        key = cv2.waitKey(1)


        if cv2.getWindowProperty('Frame',cv2.WND_PROP_VISIBLE)<1:
            break
    cv2.destroyAllWindows()

def scan2():
    print('Route Data')

but3 = tk.Button(window3,text="PUT QR CODE IN FRONT OF CAMERA", width=50,font=("Ariel Bold",15),bg='red', fg='yellow', command=scan)
but3.place(x=120, y=260)
but4 = tk.Label(window3, text='Route Information', width=50,font=("Ariel Bold",15),bg='red', fg='yellow')
but4.place(x=120, y=100)
scanned = tk.Label(window3, text="RESULT", width=30,bg='red', fg='yellow', font=("Ariel Bold", 15))
scanned.place(x=230, y=309)
text = Label(window3, text='Scanner info', bg='red', fg='yellow',font=('impact',20))
text.pack()
window3_title = Label(window3, text='Route Data!', bg="yellow", fg='red')
window3_title.pack(fill='x')
window3_button = Button(window3, text='Enter', command=lambda:show_frame(window4))
window3_button.pack(side=BOTTOM)

show_frame(window4)




# END OF WINDOW 3!
#-----------------------------------------------------------------------------------

# Window 4

#tv = ttk.Treeview(window4, columns=(1,2,3), show='headings',height='5')
#tv.place(relx=.5,y=360,anchor='center')
#tv.heading(1, text='Name')
#tv.heading(2, text='Weight')
#tv.heading(3, text='Address')


name = Label(window4, text='Item')
name.place(x=380, y=70)
name_e = Entry(window4, width=30)
name_e.place(x=400,y=100, anchor='center')

weight= Label(window4, text='Weight')
weight.place(x=380, y=130)
weight_e = Entry(window4, width=30)
weight_e.place(x=400,y=160, anchor='center')

address = Label(window4, text='Address')
address.place(x=380, y=180)
address_e = Entry(window4, width=30)
address_e.place(x=400,y=210, anchor='center')


text = Label(window4, text='My Route', bg='red', fg='yellow',font=('impact',20))
text.place(x=80,y=45, anchor='center')
text2 = Label(window4,text='Deliveries & pickups',bg='red', fg='yellow', font=('impact',10))
text2.place(x=80,y=80, anchor='center')
window4_title = Label(window4, text='Scanned Barcode/QR Code!', bg="yellow", fg='red')
window4_title.pack(fill='x')
window4_button = Button(window4, text='Enter', command=lambda:show_frame(window1))
window4_button.place(x=80,y=235, anchor='center')
delete_box = Entry(window4, width=30)
delete_box.place(x=400,y=380, anchor='center')
delete_box_label = Label(window4, text="Select ID Number")
delete_box_label.place(x=250,y=380, anchor='center')

conn = sqlite3.connect('address_book2.db')

 # create cursor
c = conn.cursor()


 # create table
#c.execute(""" CREATE TABLE addresses2 (
        #name text,
        #weight text,
        #address text
        #)""")

def update():
    updater = Tk()  # Our New blank window
    updater.title("Updated Section")
    # updater.state('zoomed')
    updater.geometry("800x500")
    updater.configure(bg="yellow")
    updater.iconbitmap('icon_W8P_icon.ico')

    conn = sqlite3.connect('address_book2.db')

    # create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses2 WHERE oid = 'record_id';")
    #c.execute("SELECT * FROM addresses2 WHERE oid = " + record_id)
    records = c.fetchall()




    name_updated = Label(updater, text='Item')
    name_updated.place(x=250, y=90)
    name_e_updated = Entry(updater, width=30)
    name_e_updated.place(x=400, y=100, anchor='center')

    weight_updated = Label(updater, text='Weight')
    weight_updated.place(x=250, y=150)
    weight_e_updated = Entry(updater, width=30)
    weight_e_updated.place(x=400, y=160, anchor='center')

    address_updated = Label(updater, text='Address')
    address_updated.place(x=250, y=200)
    address_e_updated = Entry(updater, width=30)
    address_e_updated.place(x=400, y=210, anchor='center')


    text_updated = Label(updater, text='Updated Database', bg='red', fg='yellow', font=('impact', 20))
    text_updated.place(x=120, y=45, anchor='center')
    text2_updated = Label(updater, text='Inventory', bg='red', fg='yellow', font=('impact', 10))
    text2_updated.place(x=120, y=80, anchor='center')
    window4_title_updated = Label(updater, text='Upadated information!', bg="yellow", fg='red')
    window4_title_updated.pack()

    # Loop thur results
    for record in records:
        name_e.insert(0, record[0])
        weight_e.insert(0, record[1])
        address_e.insert(0, record[2])


    # Save Button
    save_button = Button(updater, text='Save Records', width=50, height=3, command=update)
    save_button.place(x=400, y=450, anchor='center')



    # commit changes
    conn.commit()

    # close connection
    conn.close()


def delete():
    conn = sqlite3.connect('address_book2.db')

    # create cursor
    c = conn.cursor()

    # Delete Record!
    #c.execute("SELECT * FROM addresses2 WHERE oid = 'delete_box.get()';")
    c.execute(" DELETE from addresses2 WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# Create Submit Function For Database
def submit():
    conn = sqlite3.connect('address_book2.db')

    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO addresses2 VALUES (:name_e, :weight_e, :address_e)",
            {'name_e': name_e.get(),
             'weight_e': weight_e.get(),
             'address_e': address_e.get()
            })
    # commit changes
    conn.commit()

    # close connection
    conn.close()


def query():
    conn = sqlite3.connect('address_book2.db')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses2")
    records = c.fetchall()
    #print(records)
    print_records = ""

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[3]) + "\n"
    query_label = Label(window4, text=print_records, width=30)
    query_label.place(x=200,y=200, anchor='center')

    # commit changes
    conn.commit()

    # close connection
    conn.close()


submit()
#query()

# Submit Button
submit_button = Button(window4, text='Add Record To Database', command=submit)
submit_button.place(x=400,y=290, anchor='center')

# Query Button
query_button = Button(window4, text='Show Records', command=query)
query_button.place(x=400,y=320, anchor='center')

# Delete Button
delete_button = Button(window4, text='Delete Records', command=delete)
delete_button.place(x=400,y=410, anchor='center')

# Update Button
update_button = Button(window4, text='Update Records', command=update)
update_button.place(x=400,y=450, anchor='center')

# commit changes
conn.commit()

# close connection
conn.close()

show_frame(window1)

# END OF WINDOW 4!
#-----------------------------------------------------------------------------------




"""
canvas = Canvas(mw, width=300,height=160)
frame_address = Frame(mw)
mw.title("DHL Route")
my_img = ImageTk.PhotoImage(Image.open("bg.png"))
bg = PhotoImage("bg.png")
pic = Label(frame_name, image=my_img)


pic.pack()
frame_name.pack(side=TOP, fill=X)
frame_name2.pack(side=TOP, fill=X)


m = Menu(frame_name)
mw.config(menu=m)
"""































root.mainloop()