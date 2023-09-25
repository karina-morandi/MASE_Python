import tkinter
import webbrowser
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import requests, os
from io import BytesIO


class WhirlpoolFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)  # Initialize superclass
        """Constructor"""
        self.root = master
        # Title for window and do not kill the window
        self.title("M51: Whirlpool Galaxy")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        # Set up the fonts you want to use
        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

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
        self.titleLabel = tk.Label(parent, text="M51\nWhirlpool Galaxy", font=self.ComicF1)
        self.titleLabel.grid(row=0, column=0, sticky=N + S + E + W)

        self.info = tk.Button(parent, text="Info", command=self.openURL_ESA, font=self.ComicF2)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(parent, text="Download\nHigh Res", command=self.openURL_Download, font=self.ComicF2)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(parent, text="Close", command=self.hide, font=self.ComicF2)
        self.close_Frame.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

    def _layoutCanvas(self, parent):
        img_Path = 'images/Whirlpool.jpg'
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

    def openURL_ESA(self):
        url_info = "https://www.esa.int/ESA_Multimedia/Images/2023/08/Webb_captures_a_cosmic_Whirlpool"
        webbrowser.open_new_tab(url_info)

    def openURL_Download(self):
        image_url = "https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2023/08/webb_captures_a_cosmic_whirlpool/25056954-1-eng-GB/Webb_captures_a_cosmic_Whirlpool.jpg"
        responce = requests.get(image_url)
        image = Image.open(BytesIO(responce.content))
        info = "Image Name: {0}\n" \
               "Image Size: {1}\n" \
               "Image Format: {2} \n" \
               "Image saved to the app folder \n" \
               "Click OK to display".format(os.path.basename(image_url), image.size, image.mode)
        tkinter.messagebox.showwarning("Success", info)
        print(info)
        image.show()
        image.save("URL _Image.jpg")
