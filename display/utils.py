from tkinter import Tk

def get_screen_dimensions():
    root = Tk()
    root.withdraw()

    return root.winfo_screenwidth(), root.winfo_screenheight()
