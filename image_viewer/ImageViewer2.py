from tkinter import*
from tkinter import filedialog
import os
import sys

class gui:
    def __init__(self ):

        self.my_filetypes=[('all files','.*'),('png files','.png')]
        self.img_index = 0
        self.fullscreen_var = False
        self.answer=""
       

        #root form
        self.root = Tk()
        self.root.config(bg="#282828")
        self.root.geometry("500x500+100+100")
        self.root.overrideredirect(True)

        #image vars
        self.icon_close_white = PhotoImage(file =
                               "icons8-close-28_white.png")
        self.icon_fullscreen_white = PhotoImage(file =
                               "icons8-restore-down-15_white.png")
        self.icon_minimize_white = PhotoImage(file =
                               "icons8-minimize-28_white.png")

        self.icon_close_pink = PhotoImage(file =
                               "icons8-close-28_pink.png")
        self.icon_fullscreen_pink = PhotoImage(file =
                               "icons8-restore-down-15_pink.png")
        self.icon_minimize_pink = PhotoImage(file =
                               "icons8-minimize-28_pink.png")
        
        self.icon = PhotoImage(file =
                               "icons8-pink-cute-folder-48.png")
        self.next_arrow = PhotoImage(file =
                                "icons8-chevron-right-48.png")
        self.prev_arrow = PhotoImage(file =
                                "icons8-chevron-left-48.png")

        #action labels
        self.label_close = Label(self.root, bg="#282828" , width = 4
                                , height = 1)
        self.label_close.pack()
        self.label_close.place(x=455 , y = 10 )

        self.label_minimize = Label(self.root, bg="#282828" , width = 4
                                , height = 1)
        self.label_minimize.pack()
        self.label_minimize.place(x=385 , y = 10 )

        self.label_fullscreen = Label(self.root, bg="#282828" , width = 4
                                , height = 1)
        self.label_fullscreen.pack()
        self.label_fullscreen.place(x=420 , y = 10 )

        #action buttons
        self.close_button=Button(self.label_close,image=self.icon_close_white,borderwidth=0,
                                bg="#282828" , activebackground='#3c3c3c',
                                 width = 10 , height = 10 )
        self.close_button.pack()
        self.close_button.place(x=8 , y=1.5)

        self.fullscreen_button=Button(self.label_fullscreen,image=self.icon_fullscreen_white,borderwidth=0,
                                bg="#282828" , activebackground='#282828',
                                 width = 20 , height = 20 )
        self.fullscreen_button.pack()
        self.fullscreen_button.place(x=8 , y=-2)


        self.minimize_button=Button(self.label_minimize,image=self.icon_minimize_white,borderwidth=0,
                                bg="#282828" , activebackground='#282828',
                                 width = 20 , height = 20 )
        self.minimize_button.pack()
        self.minimize_button.place(x=8 , y=-3)

        self.icon_folder=Button(self.root,image=self.icon,borderwidth=0,
                                bg="#282828" , activebackground='#282828')
        self.icon_folder.pack()
        self.icon_folder.place(x=220 , y=430)
                  
        self.icon_next=Button(self.root,image=self.next_arrow,borderwidth=0,
                                bg="#282828" , activebackground='#282828',width=25
                              ,height = 30 )
        self.icon_next.pack()
        self.icon_next.place(x=320 , y=440)
                   
        self.icon_prev=Button(self.root,image=self.prev_arrow,borderwidth=0,
                                bg="#282828" , activebackground='#282828',width=25
                              ,height = 30 )
        self.icon_prev.pack()
        self.icon_prev.place(x=140 , y=440)


        #background label
     
        self.imgback=Label(self.root ,
                           width = 500  , height = 25,
                           bg="#3c3c3c" )
        self.imgback.pack()
        self.imgback.place(x=0 , y = 40 )

        #describing action
        self.label_close.bind("<Enter>" , self.mouse_on_close )
        self.label_fullscreen.bind("<Enter>" , self.mouse_on_fullscreen )
        self.label_minimize.bind("<Enter>" , self.mouse_on_minimize )

        self.label_close.bind("<Leave>" , self.mouse_leave_close )
        self.label_fullscreen.bind("<Leave>" , self.mouse_leave_fullscreen )
        self.label_minimize.bind("<Leave>" , self.mouse_leave_minimize )

        self.close_button.config(command = self.close)
        self.fullscreen_button.config(command = self.fullscreen)
        self.minimize_button.config(command = self.minimize)
        
        self.icon_next.bind("<Enter>" , self.mouse_on_next)
        self.icon_prev.bind("<Enter>" , self.mouse_on_prev)
        self.icon_folder.bind("<Enter>" , self.mouse_on_folder)

        self.icon_next.config(command = self.next_img)
        self.icon_prev.config(command = self.prev_img)
        self.icon_folder.config(command = self.open_choose_img)


    def mouse_on_close(self,event = None):
        self.close_button.config(cursor="hand2")
        self.close_button.config(image = self.icon_close_pink)
  
    def mouse_on_fullscreen(self,event = None):
        self.fullscreen_button.config(cursor="hand2")
        self.fullscreen_button.config(image = self.icon_fullscreen_pink)
        
    def mouse_on_minimize(self,event = None):
        self.minimize_button.config(cursor="hand2")
        self.minimize_button.config(image = self.icon_minimize_pink)

    def mouse_leave_close(self,event = None):
        self.close_button.config(cursor="hand2")
        self.close_button.config(image = self.icon_close_white)
  
    def mouse_leave_fullscreen(self,event = None):
        self.fullscreen_button.config(cursor="hand2")
        self.fullscreen_button.config(image = self.icon_fullscreen_white)
        
    def mouse_leave_minimize(self,event = None):
        self.minimize_button.config(cursor="hand2")
        self.minimize_button.config(image = self.icon_minimize_white)
 
    def mouse_on_next(self,event = None):
        self.icon_next.config(cursor="hand2")
    def mouse_on_prev(self,event = None):
        self.icon_prev.config(cursor="hand2")
    def mouse_on_folder(self,event = None):
        self.icon_folder.config(cursor="hand2")

    def close(self):
        os._exit(1)
    def fullscreen(self):

        if ( self.fullscreen_var == False ):
            self.root.overrideredirect(False)#error after minimize ===> made it false
            self.root.attributes("-fullscreen", True)
            self.imgback.config( width = self.root.winfo_screenwidth() ) 
            if(self.answer != ""): self.imgback.config(height = 640)
            else: self.imgback.config(height = 43)
            
            self.label_close.place(x=self.root.winfo_screenwidth()-30 , y = 10 )
            self.label_minimize.place(x=self.root.winfo_screenwidth()-110 , y = 10 )
            self.label_fullscreen.place(x=self.root.winfo_screenwidth()-70 , y = 10 )

            self.icon_folder.place(x=self.root.winfo_screenwidth()/2 -20
                                   , y=self.root.winfo_screenheight()-70)

            self.icon_next.place(x=self.root.winfo_screenwidth()/2 -20 +100
                                   , y=self.root.winfo_screenheight()-60)

            self.icon_prev.place(x=self.root.winfo_screenwidth()/2 -20 -80
                                   , y=self.root.winfo_screenheight()-60)
            
            
            self.fullscreen_var = True

        else:
            self.root.overrideredirect(True)#error after minimize ===> made it false
            self.root.attributes("-fullscreen", False)
            self.imgback.config( width = 500)
            if(self.answer != ""): self.imgback.config(height = 380)
            else:self.imgback.config(height = 25)

            self.label_close.place(x=455 , y = 10 )
            self.label_minimize.place(x=385, y = 10 )
            self.label_fullscreen.place(x=420 , y = 10 )

            self.icon_folder.place(x=220 , y=430)    
            self.icon_next.place(x=320 , y=440)    
            self.icon_prev.place(x=140 , y=440)
        
            
            self.fullscreen_var = False
            
    def minimize(self):
        self.root.overrideredirect(False)#error after minimize ===> made it false
        self.root.iconify()
    def open_choose_img(self):
        self.answer=filedialog.askopenfilenames(parent=self.imgback,initialdir=os.getcwd(),
                                     title="choose files",filetypes=self.my_filetypes)
        self.image_index= 0 

        self.showing_imag = PhotoImage( file = self.answer[self.image_index] )
 
        if self.fullscreen_var:
            
            self.imgback.config(image= self.showing_imag ,height = 640)
        else:
            self.imgback.config(image= self.showing_imag ,height = 380)

    def next_img(self):

        try:
            self.image_index +=1
            self.showing_imag = PhotoImage( file = self.answer[self.image_index] )
        except:
            self.image_index = 0
            self.showing_imag = PhotoImage( file = self.answer[self.image_index] )
        if self.fullscreen_var:
            
            self.imgback.config(image= self.showing_imag ,height = 640)
        else:
            self.imgback.config(image= self.showing_imag ,height = 380)
        
    def prev_img(self):
        try:
            self.image_index-=1
            self.showing_imag = PhotoImage( file = self.answer[self.image_index] )
        except:
            self.image_index = 0
            self.showing_imag = PhotoImage( file = self.answer[self.image_index] )

        if self.fullscreen_var:
            
            self.imgback.config(image= self.showing_imag ,height = 640)
        else:
            self.imgback.config(image= self.showing_imag ,height = 380)

def main():
     x = gui()

if __name__ == "__main__":main()
