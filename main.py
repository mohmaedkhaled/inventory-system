__author__ = "macaw"
import os
import subprocess
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("المخزن")
main.resizable(0, 0)

def Exit():
    sure = messagebox.askyesno("الخروج", "هل أنت متأكد أنك تريد الخروج؟", parent=main)
    if sure:
        main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    subprocess.call(["pythonw", "scripts/employee.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    main.deiconify()

def adm():
    main.withdraw()
    subprocess.call(["pythonw", "scripts/admin.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=120, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=110, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

main.mainloop()
