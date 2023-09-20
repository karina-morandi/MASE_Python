import tkinter as tk
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import *


# import pylab as plt


class AppGUI(tk.Tk):
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.ComicF1 = font.Font(family="Comic Sans MS", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Comic Sans MS", size=10, weight="normal")

        # Text variables for the values specified by the user
        self.firstName = StringVar()
        self.firstName.set(' ')
        self.lastName = StringVar()
        self.lastName.set(' ')
        self.addContact = IntVar()
        self.addContact.set(1)
        self.email = StringVar()
        self.email.set(' ')
        self.rating = StringVar()
        self.rating.set('3')

        self.l1 = (tk.Label(self.master, text="Basic Contact Registration", font=self.ComicF1)
                   .grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W))

        self.firstName_space = (tk.Label(self.master, text="First Name", font=self.ComicF2)
                                .grid(row=1, column=0, sticky=W))
        self.firstName_space = (tk.Entry(master, textvariable=self.firstName, font=self.ComicF2)
                                .grid(row=1, column=1, sticky=W))

        self.lastName_space = (tk.Label(self.master, text="Last Name", font=self.ComicF2)
                               .grid(row=2, column=0, sticky=W))
        self.lastName_space = (tk.Entry(master, textvariable=self.lastName, font=self.ComicF2)
                               .grid(row=2, column=1, sticky=W))

        # Radiobutton group
        self.rb1 = Radiobutton(self.master, variable=self.addContact, text="Contact me", font=self.ComicF2, value=1,
                               command=self.UpdateContact)
        self.rb1.grid(row=3, column=0, sticky=W)
        self.rb2 = Radiobutton(self.master, variable=self.addContact, text="Do not contact me", font=self.ComicF2,
                               value=2, command=self.UpdateContact)
        self.rb2.grid(row=3, column=1, sticky=W)

        self.labelEmail = (tk.Label(self.master, text="Email: ", font=self.ComicF2).grid(row=4, column=0, sticky=W))
        self.entryEmail = (
            tk.Entry(self.master, textvariable=self.email, font=self.ComicF2).grid(row=4, column=1, sticky=W))

        # Combobox area
        # Label
        self.labelRating = (tk.Label(self.master, text="Rating", font=self.ComicF2).grid(row=5, column=0, sticky=W))
        self.rating_choice = Combobox(self.master, textvariable=self.rating, font=self.ComicF2, state="enabled")
        self.rating_choice.grid(row=4, column=1, sticky=tk.W)
        self.rating_choice['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.rating_choice.current(0)
        self.rating_choice.grid(row=5, column=1, sticky=W)

        self.b1 = tk.Button(self.master, text="Register", command=self.LoadData, font=self.ComicF2)
        self.b1.grid(row=6, column=0, columnspan=2, sticky=N + S + E + W)

        self.log = tk.Text(self.master, state='disabled', height=20, width=60)
        self.log.grid(row=7, column=0, columnspan=2, sticky=W)
        self.scrollB = tk.Scrollbar(self.master, command=self.log.yview)
        self.scrollB.grid(row=7, column=3, sticky=N + S + E + W)

        self.close_button = (tk.Button(self.master, text="Close", command=self.CloseApplication, font=self.ComicF2)
                             .grid(row=17, column=0, columnspan=2, sticky=N + S + E + W))

        self.HelloMsg()

    def LoadData(self):
        name = "Name: \t\t" + self.firstName.get() + "" + self.lastName.get()
        contact = " "
        if self.addContact.get() == 1:
            contact = "Add\t\t" + self.entryEmail.get()
        else:
            contact = "Contact not to be included"
        self.writeToLog(name)
        self.writeToLog(contact)
        self.writeToLog("User Rating: \t\t"+self.rating.get())

    def HelloMsg(self):
        file = open("/Users/karina/PycharmProjects/MASE_Python/Contact_App/HelloMsg.txt")
        data = file.read()
        file.close()
        self.writeToLog(data)

    def writeToLog(self, msg):
        # num lines = self.log.index("end - 1 line").split(".")[0]
        self.log['state'] = 'normal'
        if self.log.index('end-1c') != '1.0':
            self.log.insert('end', '\n')
        self.log.insert('end', msg)
        self.log['state'] = 'disabled'
        self.log.see('end')

    def UpdateContact(self):
        if int(self.addContact.get()) == 2:
            self.entryEmail.config(state='DISABLED')
            print(self.addContact.get())
        else:
            self.entryEmail.config(state='NORMAL')
            print(self.addContact.get())

    def CloseApplication(self):
        print('closing')
        self.master.destroy()
