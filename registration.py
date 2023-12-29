from tkinter import *
import os
import sys
from csv import writer

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Registration form", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=230)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)

main_lst=[]
def Add():
   lst=[entry_1.get(),entry_3.get(),var.get()]
   main_lst.append(lst)
   with open('data.csv', 'a') as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(main_lst)
  
    #Close the file object
    f_object.close()


def run_program():
    os.system('food_delivery.py')

Button(root,text="Add",width=20,bg="black",fg='white',command=Add).place(x=180,y=350)

#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="black",fg='white',command=run_program).place(x=180,y=380)


#this will run the mainloop.
root.mainloop()
