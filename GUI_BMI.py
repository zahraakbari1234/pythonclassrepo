from tkinter import*
import os
import time

class gui:
    def __init__(self ):

        self.state = 0 #تعريف متغيير
        self.BMI = ""
        self.result =""

        self.root = Tk()
        self.root.config(bg="#98E4FF")
        self.root.geometry("400x300+200+100")
        self.root.title("BMI CALCULATOR")
        self.root.resizable(False,False)

        self.weighttxt = Label(self.root , text="وزن:" ,font =("B_nazanin", 20 ,"bold"),
                               bg="#98E4FF")
        self.weighttxt.pack()
        self.weighttxt.place( x =10 , y =20 )

        self.heighttxt = Label(self.root , text="قد:" ,font =("B_nazanin", 20 ,"bold"),
                               bg="#98E4FF")
        self.heighttxt.pack()
        self.heighttxt.place( x =30 , y =80 )

        self.weightentry = Entry(self.root , width = 20 , font =("arial",20),
                                 bg = "#B6FFFA")
        self.weightentry.pack()
        self.weightentry.place( x =80 , y =20 )

        self.heightentry = Entry(self.root , width = 20 , font =("arial",20),
                                 bg = "#B6FFFA")
        self.heightentry.pack()
        self.heightentry.place( x =80 , y =80 )

        self.but1 = Button(self.root,text="محاسبه",
                           bg='#98E4FF',font =("B_nazanin", 20 ,"bold"),
                           activebackground='#B6FFFA',cursor='hand2')
        self.but1.pack()
        self.but1.place(x=20, y=140)
        self.but1.config(command=self.click)

        self.resulttxt = Label(self.root , text="نتيجه:" ,font =("B_nazanin", 20 ,"bold"),
                               bg="#98E4FF")
        self.resulttxt.pack()
        self.resulttxt.place( x =170 , y =150 )

        
        self.bmi = Label(self.root , text= self.BMI ,font =("arial",20),
                               bg="#98E4FF")
        self.bmi.pack()
        self.bmi.place( x =240 , y =150 )

        self.text = Label(self.root , text= "نمايش تفسير نتيجه محاسبات" ,font =("B_nazanin", 20 ),
                               bg="#98E4FF")
        self.text.pack()
        self.text.place( x =20 , y =220 )
   
        
        self.root.mainloop()

    def click(self):

        try:
            self.weight = int(self.weightentry.get())
            self.height = float(self.heightentry.get())
            self.BMI = self.weight / ( self.height **2 )

            self.text.config(fg = "#000000")

            
            if( self.BMI < 18.5 ):
                self.result = "شما خيلي لاغر هستيد"
 
            elif( self.BMI < 24.9 ):
                self.result = "شما وزن ايده آل داريد"

            elif( self.BMI < 29.9 ):
                self.result = "شما کمي اضافه وزن داريد"

            else:
                self.result = "نياز فورررري به ورزش و رژيم"

            self.text.config(text = self.result )

                
            self.BMI= ("%0.2f" %self.BMI)
            self.bmi.config( text = self.BMI )

            

        except:
            self.result = "لطفا مقدار درست وارد نماييد"
            self.text.config(text = self.result , fg = "#ff0000")
            






       

    def mouse_on(self,event = None):

        self.lab1.config(cursor = "hand2" )
        self.lab1.config(image = self.image2)
        self.lab1.place(x = 102 , y = 102 )

    def mouse_left(self,event = None):

        self.lab1.config(image = self.image1)
        self.lab1.place(x = 100 , y = 100 )

    def click_button(self):
        if( self.state == 0 ):
            self.b1.config(text = "Green")
            self.lab1.config(image = self.image2)
            self.state = 1 

        else:
            self.b1.config(text = "Red")
            self.lab1.config(image = self.image1)
            self.state = 0

        #text = self.e1.get()
        #print(text)

        num  = int(self.e1.get() )
        print(num * "@" )
            
        
def main():
     x = gui()

if __name__ == "__main__":main()
