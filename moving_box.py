from tkinter import*
import os
import time


#چرا سرعتش کم و زياد ميشه؟

class gui:
    def __init__(self ):

        self.root = Tk()
        self.root.config(bg="#000000")
        self.root.geometry("100x100+100+100")
        self.root.overrideredirect(True)


        self.move()

        self.root.mainloop()

    def move(self):
        for i in range( 100 , self.root.winfo_screenwidth()-2*100  , 1):
            self.root.geometry("100x100+%d+100" %(i))
            self.root.update()
           

        self.root.config(bg="#ff0000")
        self.root.update()


        for i in range( 100 , self.root.winfo_screenheight()-2*100  , 1):
            self.root.geometry("100x100+%d+%d" %(self.root.winfo_screenwidth() - 2*100,i))
            self.root.update()
           

        self.root.config(bg="#00ff00")
        self.root.update()


        for i in range( self.root.winfo_screenwidth()-2*100  , 100   , -1):
            self.root.geometry("100x100+%d+%d" %(i,self.root.winfo_screenheight() - 2*100  ))
            self.root.update()
           

        self.root.config(bg="#0000ff")
        self.root.update()


        for i in range(self.root.winfo_screenheight() - 2*100, 100  , -1):
            self.root.geometry("100x100+%d+%d" %(100,i))
            self.root.update()
         

        self.root.config(bg="#000000")
        self.root.update()

 
        self.root.after(10,self.move)
        

def main():
     x = gui()


if __name__ == "__main__":main()
