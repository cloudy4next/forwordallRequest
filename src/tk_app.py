import tkinter
import tkinter.messagebox
from tkinter import *
import webbrowser
import urllib.request
from PIL import ImageGrab
import os

        
def app():
        root = tkinter.Tk()

        root.geometry('800x500')
        root.title('TIB HRMS')
        # root.iconbitmap('icon.ico')
        canvas= Canvas(root, width= 1000, height= 800, bg="white")

        new = 1
        url = 'https://127.0.0.1:8888/login'

        def urls():
             webbrowser.open(url,new=new)

        def message():
            tkinter.messagebox.showinfo( "Hello Applicant ", "Please Turn of Dual monitor ")

        def helloCallBack():
            tkinter.messagebox.showinfo( "Hello", "I'm TIB The GOD-Father of Crime")

        snapshot = ImageGrab.grab()
        wid, hgt = snapshot.size
        print(hgt,wid)
        if wid>1920 & hgt > 1200:
            button = Button(root, text = "Go To exam",command=message)
            button.place(relx=0.6, rely=0.5, anchor=CENTER)

        else:
            button = Button(root, text = "Go To exam",command=urls)
            button.place(relx=0.6, rely=0.5, anchor=CENTER)



        li ="This is a Demo app, Follow the instructions to give Examination"
        canvas.create_text(400, 50, text= li,fill=
        "black",font=('Helvetica 15 bold'))
        canvas.pack()



        button0 = tkinter.Button(text ="Instrauctions", command = helloCallBack,height = 1, 
                width = 10)

        button0.place(relx=0.4, rely=0.5, anchor=CENTER)

        root.mainloop()