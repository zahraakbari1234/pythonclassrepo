from tkinter import*
from tkinter import filedialog
import os
from tkinter import colorchooser

class gui:
    def __init__(self ):

        self.my_filetypes=[('all files','.*'),('png files','.txt')]
        self.string=""

        #root form
        self.root = Tk()
        self.root.config(bg="#D2DAFF")
        self.root.title("text reader")
      
        self.root.geometry( "600x600+100+100"  )


        self.txt=Text(self.root,height=30 , width = 64)
        self.txt.pack()
        self.txt.place(x=40 , y = 100 )
    
        #image vars
        
        self.icon_file = PhotoImage(file =
                               "icons8-document-48.png")
        self.icon_back_color = PhotoImage(file =
                                "icons8-paint-roller-30.png")
        self.icon_text_color = PhotoImage(file =
                                "icons8-color-palette-30.png")

        #action labels
 

        #action buttons
        self.b_file=Button(self.root,image=self.icon_file,borderwidth=0,
                                bg="#D2DAFF" , activebackground='#D2DAFF')
        self.b_file.pack()
        self.b_file.place(x=70 , y=32)
                  
        self.b_back_color=Button(self.root,image=self.icon_back_color,borderwidth=0,
                                bg="#D2DAFF" , activebackground='#D2DAFF',width=25
                              ,height = 30 )
        self.b_back_color.pack()
        self.b_back_color.place(x=400 , y=40)
                   
        self.b_text_color=Button(self.root,image=self.icon_text_color,borderwidth=0,
                                bg="#D2DAFF" , activebackground='#D2DAFF',width=25
                              ,height = 30 )
        self.b_text_color.pack()
        self.b_text_color.place(x=470 , y=40)


        #Entry
      

        #describing action

        
        self.b_back_color.bind("<Enter>" , self.mouse_on_bk_color)
        self.b_text_color.bind("<Enter>" , self.mouse_on_txt_color)
        self.b_file.bind("<Enter>" , self.mouse_on_file)

        self.b_back_color.config(command = self.bk_color_img)
        self.b_text_color.config(command = self.txt_color_img)
        self.b_file.config(command = self.open_choose_file)

 
    def mouse_on_bk_color(self,event = None):
        self.b_back_color.config(cursor="hand2")
    def mouse_on_txt_color(self,event = None):
        self.b_text_color.config(cursor="hand2")
    def mouse_on_file(self,event = None):
        self.b_file.config(cursor="hand2")

    def open_choose_file(self):
        self.answer = filedialog.askopenfilename(parent=self.root,
                                               initialdir=os.getcwd(),
                                               title="choose a file",
                                               filetypes= self.my_filetypes)

       
        file = open( self.answer,'r')
        self.string = file.read()
        file.close()

        self.txt.insert(END,self.string)
 
    def bk_color_img(self):
        self.x_color,self.back_color=colorchooser.askcolor(parent=self.root,
                                               initialcolor=(0,0,0))
        self.txt.config(bg = str(self.back_color))
                                          
    def txt_color_img(self):
        self.y_color,self.text_color=colorchooser.askcolor(parent=self.root,
                                               initialcolor=(0,0,0))
        self.txt.config(fg = str(self.text_color))

def main():
     x = gui()

if __name__ == "__main__":main()
