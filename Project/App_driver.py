from tkinter import *
from GUI_Obj import AppGUI
from SplashScreen import Splash

def main():
    root = Tk()
    image_file = "splash.png"
    s = Splash(root, timeout=3000, image=image_file)
    myGUI = AppGUI(root, "MASE Data Analysis & Visualisation")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
