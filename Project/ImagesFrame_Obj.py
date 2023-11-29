import os
import sys
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk


class ImagesFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("World Images")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(main_frame, background="black")
        self.left_frame.grid(row=1, column=1, sticky="nsew")

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="left", fill="y")

        self._layoutButtons(buttonPanel)
        self.resizable(False, False)

    def _layoutButtons(self, parent):
        image_frame = tk.Frame(parent, background="black")
        image_frame.grid(row=0, column=0, sticky=N + S + E + W)

        self.titleLabel = tk.Label(image_frame, text="Images Window", font=self.ComicF1)
        self.titleLabel.grid(row=0, column=0, columnspan=2, sticky=N + S + E + W)

        # Load the image using PIL
        img_Path = self.resource_path('continents.jpeg')
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(image_frame, height=height, width=width)
        self.canvas.grid(row=1, column=0, rowspan=height, sticky=E)
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)

        button_frame = tk.Frame(image_frame, background="black")
        button_frame.grid(row=1, column=1, padx=10)

        self.asiaButton = tk.Button(button_frame, text="Asia", command=self.asiaImages, font=self.ComicF2)
        self.asiaButton.grid(row=1, sticky=N + S + E + W, padx=5, pady=5)

        self.africaButton = tk.Button(button_frame, text="Africa", command=self.africaImages, font=self.ComicF2)
        self.africaButton.grid(row=2, sticky=N + S + E + W, padx=5, pady=5)

        self.nAmericaButton = tk.Button(button_frame, text="North America", command=self.nAmImages, font=self.ComicF2)
        self.nAmericaButton.grid(row=3, sticky=N + S + E + W, padx=5, pady=5)

        self.sAmericaButton = tk.Button(button_frame, text="South America", command=self.sAmImages, font=self.ComicF2)
        self.sAmericaButton.grid(row=4, sticky=N + S + E + W, padx=5, pady=5)

        self.europeButton = tk.Button(button_frame, text="Europe", command=self.europeImages, font=self.ComicF2)
        self.europeButton.grid(row=5, sticky=N + S + E + W, padx=5, pady=5)

        self.antButton = tk.Button(button_frame, text="Antarctica", command=self.antarImages, font=self.ComicF2)
        self.antButton.grid(row=6, sticky=N + S + E + W, padx=5, pady=5)

        self.oceButton = tk.Button(button_frame, text="Oceania", command=self.oceImages, font=self.ComicF2)
        self.oceButton.grid(row=7, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(button_frame, text="Close", command=self.hide, font=self.ComicF2)
        self.close_Frame.grid(row=8, sticky=N + S + E + W, padx=5, pady=5)

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

    def resource_path(self, relative_path):
        # Get absolute path to images, as PyInstaller changes the directories when packaged
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
