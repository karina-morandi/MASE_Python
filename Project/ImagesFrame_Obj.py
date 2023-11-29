import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import font


class ImagesFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("World Images")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="left", fill="y")

        self._layoutButtons(buttonPanel)
        self.resizable(False, False)

    def _layoutButtons(self, parent):
        self.titleLabel = tk.Label(parent, text="Images Window", font=self.ComicF1)
        self.titleLabel.grid(row=0, column=0, sticky=N + S + E + W)

        self.asiaButton = tk.Button(parent, text="Asia", command=self.asiaImages, font=self.ComicF2)
        self.asiaButton.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.africaButton = tk.Button(parent, text="Africa", command=self.africaImages, font=self.ComicF2)
        self.africaButton.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.nAmericaButton = tk.Button(parent, text="North America", command=self.nAmImages, font=self.ComicF2)
        self.nAmericaButton.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.sAmericaButton = tk.Button(parent, text="South America", command=self.sAmImages, font=self.ComicF2)
        self.sAmericaButton.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.europeButton = tk.Button(parent, text="Europe", command=self.europeImages, font=self.ComicF2)
        self.europeButton.grid(row=5, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.antButton = tk.Button(parent, text="Antarctica", command=self.antarImages, font=self.ComicF2)
        self.antButton.grid(row=6, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.oceButton = tk.Button(parent, text="Oceania", command=self.oceImages, font=self.ComicF2)
        self.oceButton.grid(row=7, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(parent, text="Close", command=self.hide, font=self.ComicF2)
        self.close_Frame.grid(row=8, column=0, sticky=N + S + E + W, padx=5, pady=5)

    def show(self):
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
        self.master.show_main_window()

    def asiaImages(self):
        url_info = "https://www.wwftc.com/maps/asia/"
        webbrowser.open_new_tab(url_info)

    def africaImages(self):
        url_info = "https://www.wwftc.com/maps/africa/"
        webbrowser.open_new_tab(url_info)

    def nAmImages(self):
        url_info = "https://www.wwftc.com/maps/north-america/"
        webbrowser.open_new_tab(url_info)

    def sAmImages(self):
        url_info = "https://www.wwftc.com/maps/south-america/"
        webbrowser.open_new_tab(url_info)

    def europeImages(self):
        url_info = "https://www.wwftc.com/maps/europe/"
        webbrowser.open_new_tab(url_info)

    def antarImages(self):
        url_info = "https://www.wwftc.com/maps/antarctica/"
        webbrowser.open_new_tab(url_info)

    def oceImages(self):
        url_info = "https://www.wwftc.com/maps/australia-and-oceania/"
        webbrowser.open_new_tab(url_info)
