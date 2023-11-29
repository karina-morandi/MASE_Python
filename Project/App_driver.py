from tkinter import *
from GUI_Obj import AppGUI
from SplashScreen import Splash
import os
import sys


def resource_path(relative_path):
    # Get absolute path to images, as PyInstaller changes the directories when packaged
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    root = Tk()
    # image_file = "splash.png"
    image_file = resource_path("splash.png")
    s = Splash(root, timeout=3000, image=image_file)
    myGUI = AppGUI(root, "MASE Data Analysis & Visualisation")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
