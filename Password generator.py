from tkinter import *
import string
import random
import pyperclip



def generator():
    small_alphabets=string.ascii_lowercase 
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    
    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())
    # password=random.sample(all,password_length)
    # passwordfield.insert(0,password)
    
    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))
    
    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets+numbers+special_characters,password_length))
    
def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)

#Background colour
root=Tk()
root.config(bg='Pink')
choice=IntVar()
font=('arial',15,'bold')
passwordlabel=Label(root,text='Password Generator',font=(' Farray',20,'italic'),bg='lightpink')
passwordlabel.grid(pady=10)

#Button
weakradioButton=Radiobutton(root,text='WEAK',value=1,variable=choice)
weakradioButton.grid(pady=10)
 
StrongradioButton=Radiobutton(root,text='Strong',value=2,variable=choice)
StrongradioButton.grid(pady=10)

lengthlabel=Label(root,text='Password Length',font=('times new roman',20,'bold'),bg='white')
lengthlabel.grid(pady=10)
length_box=Spinbox(root,from_=3,to_=1000,width=6,font=font)
length_box.grid(pady=10)


 

generateButton=Button(root,text='Generate',font=font,command=generator)
generateButton.grid(pady=10)

passwordfield=Entry(root,width=25,bd=2,font=font)
passwordfield.grid(pady=10)

copyButton=Button(root,text='Copy',font=font,command=copy)
copyButton.grid(pady=10)
 


root.mainloop()


