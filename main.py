__author__ = "macaw"
import os
from tkinter import *
from tkinter import messagebox
import subprocess

main = Tk()
main.geometry("{0}x{1}+0+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))  # Full screen
main.title("ادارة المخزن")
main.resizable(0, 0)

def Exit():
    sure = messagebox.askyesno("خروج", "هل انت متاكد من الخروج", parent=main)
    if sure:
        main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    subprocess.run([".\scripts\employee.exe"], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
    main.deiconify()

def adm():
    main.withdraw()
    os.system("python admin.py")
    subprocess.run([".\scripts\admin.exe"], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=main.winfo_screenwidth(), height=main.winfo_screenheight())
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
