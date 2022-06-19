
# coding: utf-8

# In[3]:


import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

def chatbot():
    root.destroy()
    os.system('python chatgui.py')
    #w.mainloop()
	
def train():
    root.destroy()
    os.system('python train_chatbot.py')
    #w.mainloop()
    

root = Tk()
root.geometry("1400x900")
# Create a photoimage object of the image in the path
image1 = Image.open("gogte.png")
#resized_image= image1.resize((800,705), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=150, y=100)

label = tkinter.Label(text="Gogte Institute of Technology", font=('arial' ,20 ,'bold'),bd=10)
label.place(x=550,y=30)

b1 = tkinter.Button(root, text="Chatbot", command=chatbot ,padx=10 ,pady=5 ,bd=5 ,fg="Black", font=('arial' ,10 ,'bold') ,bg="red")
b1.place(x=550,y=700)
b2 = tkinter.Button(root, text="Train Data", command=train ,padx=10 ,pady=5 ,bd=5 ,fg="Black", font=('arial' ,10 ,'bold') ,bg="red")
b2.place(x=900,y=700)


root.mainloop()

