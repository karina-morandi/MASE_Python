import tkinter as tk
from tkinter import font
from DatabaseObj_GUI_MySQL import DBConnection_MySQL
#from DatabaseObj_GUI_SQLAlchemy import DBConnection_Alchemy

class AppGUI(tk.Tk):
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)

        self.hostVar = tk.StringVar()
        self.guestVar = tk.StringVar()
        self.passVar = tk.StringVar()
        self.portVar = tk.StringVar()
        self.DBVar = tk.StringVar()
        self.TableVar = tk.StringVar()

        self.hostVar.set('relational.fit.cvut.cz')
        self.guestVar.set('guest')
        self.passVar.set('relational')
        self.portVar.set('3306')
        self.DBVar.set('financial')
        self.TableVar.set('')

        self.relationalDB = None


        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF3 = font.Font(family="Calibri", size=12, weight="normal")
        self.l1 = tk.Label(master, text="Database Connector", font=self.ComicF1).grid(row=0,column=0,columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.labelHost = tk.Label(master, text="Host: ", font=self.ComicF3).grid(row=1, column=0,sticky=tk.W)
        self.entryHost = tk.Entry(master, textvariable=self.hostVar, font=self.ComicF3)
        self.entryHost.grid(row=1, column=1, sticky=tk.W)

        self.labelUser = tk.Label(master, text="User: ", font=self.ComicF3).grid(row=2, column=0,sticky=tk.W)
        self.entryUser = tk.Entry(master, textvariable=self.guestVar, font=self.ComicF3)
        self.entryUser.grid(row=2, column=1, sticky=tk.W)

        self.labelPass = tk.Label(master, text="Password: ", font=self.ComicF3).grid(row=3, column=0,sticky=tk.W)
        self.entryPass = tk.Entry(master, textvariable=self.passVar, font=self.ComicF3)
        self.entryPass.grid(row=3, column=1, sticky=tk.W)

        self.labelPort = tk.Label(master, text="Port: ", font=self.ComicF3).grid(row=4, column=0,sticky=tk.W)
        self.entryPort = tk.Entry(master, textvariable=self.portVar, font=self.ComicF3)
        self.entryPort.grid(row=4, column=1, sticky=tk.W)

        self.labelDB = tk.Label(master, text="Database: ", font=self.ComicF3).grid(row=5, column=0,sticky=tk.W)
        self.entryDB = tk.Entry(master, textvariable=self.DBVar, font=self.ComicF3)
        self.entryDB.grid(row=5, column=1, sticky=tk.W)

        self.labelTable = tk.Label(master, text="Table Name: ", font=self.ComicF3).grid(row=6, column=0,sticky=tk.W)
        self.entryTable = tk.Entry(master, textvariable=self.TableVar, font=self.ComicF3)
        self.entryTable.grid(row=6, column=1, sticky=tk.W)
        self.entryTable.config(state= "disabled")

        self.Connect_Button = tk.Button(master, text="Connect", command=self.ConnectToDB, font=self.ComicF3).grid(
            row=7, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.Connect_Button = tk.Button(master, text="Table Info", command=self.TableInfo, font=self.ComicF3).grid(
            row=7, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.GenerVis_Button = tk.Button(master, text="Display Gender", command=self.VisualiseGender, font=self.ComicF3).grid(
            row=8, column=0, columnspan=2,  sticky=tk.N + tk.S + tk.E + tk.W)

        self.log = tk.Text(master, state='disabled', height=30, width=80)
        self.log.grid(row=16, column=0, columnspan=2, sticky=tk.W)
        self.scrollY = tk.Scrollbar(master, command=self.log.yview)
        self.scrollY.grid(row=16, column=4, sticky=tk.N + tk.S + tk.E + tk.W)
        #self.scrollX = tk.Scrollbar(master, command=self.log.yview)
        #self.scrollX.grid(row=16, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

        self.close_button = tk.Button(master, text="Close", command=self.CloseApplication, font=self.ComicF3).grid(
            row=17, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    def writeToLog(self, msg):
        self.log['state'] = 'normal'
        if self.log.index('end-1c') != '1.0':
            self.log.insert('end', '\n')
        self.log.insert('end', msg)
        self.log['state'] = 'disabled'
        self.log.see('end')

    def TableInfo(self):
        self.relationalDB.selectTable(self.TableVar.get().strip())
        file = open("tableInfo.txt")
        data = file.read()
        file.close()
        self.writeToLog(data)

    def ConnectToDB(self):
        print('Connecting to DB')
        db_Info = (self.hostVar.get(), self.guestVar.get(), self.passVar.get(), int(self.portVar.get()), self.DBVar.get())

        # I have commented out one of the following instances, in this lab the MySQL works when bundled,
        # DBConnection_Alchemy will experience a compatability error.
        # self.relationalDB = DBConnection_Alchemy(db_Info);

        # The following will work when bundeling
        self.relationalDB = DBConnection_MySQL(db_Info);
        self.writeToLog(self.relationalDB.getConnectionProgress())
        self.entryTable.config(state="normal")

    def VisualiseGender(self):
        # values, labels = self.relationalDB.visualiseClient()
        # print(values)
        self.relationalDB.visualiseClient()

    def CloseApplication(self):
        print('closing')
        self.relationalDB.disposeConnection()
        self.master.destroy()
