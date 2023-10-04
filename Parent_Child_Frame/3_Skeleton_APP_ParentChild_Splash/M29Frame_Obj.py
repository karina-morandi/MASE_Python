import webbrowser
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font


class M29Frame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)  # Initialize superclass
        """Constructor"""
        self.root = master
        # Title for window and do not kill the window
        self.title("PNe M2-9: Wings of a Butterfly Nebula")
        self.protocol('WM_DELETE_WINDOW, self.OverrideWindow', self.OverrideWindow)

        # Set up the fonts you want to use
        self.myFont1 = font.Font(family="Calibri", size=16, weight="normal")
        self.myFont2 = font.Font(family="Calibri", size=12, weight="normal")

        # Create two panels, one is for the buttons and the other is for the canvas (images)
        buttonPanel = tk.Frame(self, background="black")
        canvasPanel = tk.Frame(self, background="black")
        # Set the positioning of the panels
        buttonPanel.pack(side="left", fill="y")
        canvasPanel.pack(side="right", fill="both", expand=True)

        # ill in these two areas:
        self._layoutButtons(buttonPanel)
        self._layoutCanvas(canvasPanel)
        self.resizable(False, False)

    def _layoutButtons(self, parent):
        self.titleLabel = tk.Label(parent, text="Planetary Nebula\nM2-9", font=self.myFont1)
        self.titleLabel.grid(row=0, column=0, sticky=N + S + E + W)

        self.info = tk.Button(parent, text="NASA", command=self.openURL_NASA, font=self.myFont2)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(parent, text="Play Video", command=self.openURL_Video, font=self.myFont2)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(parent, text="Close", command=self.hide, font=self.myFont2)
        self.close_Frame.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

    def _layoutCanvas(self, parent):
        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Parent_Child_Frame/3_Skeleton_APP_ParentChild_Splash/images/M2-9.jpg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(parent, height=height, width=width)
        self.canvas.grid(row=3, column=0, sticky=N + S + E + W)
        self.canvas.create_image(0, 1, anchor='nw', image=self.image)

    def show(self):
        self.update()  # Update the window
        self.deiconify()  # Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide()  # Hide the window

    def hide(self):
        self.withdraw()  # Removes the window from the screen, without destroying it.
        self.root.show()

    def openURL_NASA(self):
        url_info = "https://science.nasa.gov/m2-9-wings-butterfly-nebula"
        webbrowser.open_new_tab(url_info)

    def openURL_Video(self):
        url_video = "https://www.youtube.com/watch?v=RWJEfXOiebU"
        webbrowser.open_new_tab(url_video)
