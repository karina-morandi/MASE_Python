from tkinter import *
from MainWindow import MainWindow
from SplashScreen import Splash
import tkinter as tk

def main():
    root = Tk()
    image_file = "splash.png"
    s = Splash(root, timeout=3000, image=image_file)
    myGUI = MainWindow(root)
    root.title = "Karol"
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()
