import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk
from tkinter import font
from DataBaseConnection import DBConnection
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
        self.DBVar.set('world')
        self.TableVar.set('')

        self.relationalDB = None

        left_frame = tk.Frame(master)
        left_frame.grid(row=1, column=0, sticky="nsew")

        # Create a frame for the right side (connection information)
        right_frame = tk.Frame(master)
        right_frame.grid(row=1, column=4, sticky="nsew")

        # Configure the grid to expand with the window
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF3 = font.Font(family="Calibri", size=12, weight="normal")
        self.l1 = tk.Label(master, text="Main Window", font=self.ComicF1).grid(row=0,column=0,columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.labelHost = tk.Label(right_frame, text="Host: ", font=self.ComicF3).grid(row=1, column=0,sticky=tk.W)
        self.entryHost = tk.Entry(right_frame, textvariable=self.hostVar, font=self.ComicF3)
        self.entryHost.grid(row=0, column=1, sticky=tk.W)

        self.labelUser = tk.Label(right_frame, text="User: ", font=self.ComicF3).grid(row=2, column=0,sticky=tk.W)
        self.entryUser = tk.Entry(right_frame, textvariable=self.guestVar, font=self.ComicF3)
        self.entryUser.grid(row=1, column=1, sticky=tk.W)

        self.labelPass = tk.Label(right_frame, text="Password: ", font=self.ComicF3).grid(row=3, column=0,sticky=tk.W)
        self.entryPass = tk.Entry(right_frame, textvariable=self.passVar, font=self.ComicF3)
        self.entryPass.grid(row=2, column=1, sticky=tk.W)

        self.labelPort = tk.Label(right_frame, text="Port: ", font=self.ComicF3).grid(row=4, column=0,sticky=tk.W)
        self.entryPort = tk.Entry(right_frame, textvariable=self.portVar, font=self.ComicF3)
        self.entryPort.grid(row=3, column=1, sticky=tk.W)

        self.labelDB = tk.Label(right_frame, text="Database: ", font=self.ComicF3).grid(row=5, column=0,sticky=tk.W)
        self.entryDB = tk.Entry(right_frame, textvariable=self.DBVar, font=self.ComicF3)
        self.entryDB.grid(row=4, column=1, sticky=tk.W)

        self.labelTable = tk.Label(right_frame, text="Table Name: ", font=self.ComicF3).grid(row=6, column=0,sticky=tk.W)
        self.entryTable = tk.Entry(right_frame, textvariable=self.TableVar, font=self.ComicF3)
        self.entryTable.grid(row=5, column=1, sticky=tk.W)
        self.entryTable.config(state= "disabled")

        self.Connect_Button = tk.Button(right_frame, text="Connect", command=self.ConnectToDB, font=self.ComicF3).grid(
            row=6, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.Connect_Button = tk.Button(right_frame, text="Table Info", command=self.TableInfo, font=self.ComicF3).grid(
            row=6, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.log = tk.Text(right_frame, state='disabled', height=30, width=40)
        self.log.grid(row=9, column=0, columnspan=2, sticky=tk.W)
        self.scrollY = tk.Scrollbar(right_frame, command=self.log.yview)
        self.scrollY.grid(row=9, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
        #self.scrollX = tk.Scrollbar(master, command=self.log.yview)
        #self.scrollX.grid(row=16, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

        self.info = tk.Button(left_frame, text="Tables", command=self.showTables, font=self.ComicF3)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(left_frame, text="Graphs", command=self.openURL_Video, font=self.ComicF3)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(left_frame, text="Images", command=self.hide, font=self.ComicF3)
        self.close_Frame.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(left_frame, text="Close", command=self.hide, font=self.ComicF3)
        self.close_Frame.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Project/worldMap.jpeg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.canvas.grid(row=0, column=1, rowspan=height, sticky=E)
        self.canvas.create_image(0, 1, anchor='nw', image=self.image)

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
        self.relationalDB = DBConnection(db_Info);
        self.writeToLog(self.relationalDB.getConnectionProgress())
        self.entryTable.config(state="normal")

    def VisualiseGender(self):
        # values, labels = self.relationalDB.visualiseClient()
        # print(values)
        self.relationalDB.visualiseClient()

    def show(self):
        self.update()  # Update the window
        self.deiconify()  # Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide()  # Hide the window

    def hide(self):
        self.withdraw()  # Removes the window from the screen, without destroying it.
        self.root.show()

    def showTables(self):
        self.Tables_Window.show()
        self.master.withdraw()

    def openURL_Video(self):
        url_video = "https://www.youtube.com/watch?v=RWJEfXOiebU"
        webbrowser.open_new_tab(url_video)

    def CloseApplication(self):
        print('closing')
        self.relationalDB.disposeConnection()
        self.master.destroy()
