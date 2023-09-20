from tkinter import *
from GUI_Obj import AppGUI


def main():
    root = Tk()
    myGUI = AppGUI(root, "MASE Data Analysis & Visualisation")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
