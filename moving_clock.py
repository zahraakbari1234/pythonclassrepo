from tkinter import *
import os
import time


class gui:

    time = 0

    def __init__(self):

        self.root = Tk()
        self.root.config(bg="#000000")
        self.root.geometry("300x100+-300+%d" %
                           (self.root.winfo_screenheight()-120))
        self.root.overrideredirect(True)

        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-alpha", 0.4)

        self.lab1 = Label(self.root, text=time.asctime()[11:19], bg="#000000",
                          fg="#ffffff", font=("Bnazanin", 50, "bold"))
        self.lab1.pack()
        self.lab1.place(x=10, y=10)

        self.move()

        self.root.mainloop()

    def move(self):
        for i in range(-300, self.root.winfo_screenwidth(), 1):
            self.root.geometry("300x100+%d+%d" %
                               (i, self.root.winfo_screenheight()-120))
            self.lab1.config(text=time.asctime()[11:19])
            self.root.update()

        self.root.after(10, self.move)


def main():
    x = gui()


if __name__ == "__main__":
    main()
