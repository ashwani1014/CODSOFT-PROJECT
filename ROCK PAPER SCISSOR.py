from tkinter import*
from PIL import Image,ImageTk
from random import randint
#main window  
root=Tk()
root.title('Rock Papaer Scissor')
root.configure(background='purple' )

#Picture

rock_img=ImageTk.PhotoImage(Image.open('rock.jpg'))
paper_img=ImageTk.PhotoImage(Image.open('paper.jpg'))
scissor_img=ImageTk.PhotoImage(Image.open('scissor.jpg'))
rock_img_comp=ImageTk.PhotoImage(Image.open('rock.jpg'))
paper_img_comp=ImageTk.PhotoImage(Image.open('paper.jpg'))
scissor_img_comp=ImageTk.PhotoImage(Image.open('scissor.jpg'))

#insert picture
user_label=Label(root,image=scissor_img,background='purple')
comp_label=Label(root,image=scissor_img_comp,background='purple')
comp_label.grid(row=1,column=6)
user_label.grid(row=2,column=3)

#Scores
playerscore=Label(root,text=0,font=100,background='purple',fg='white')
computerscore=Label(root,text=0,font=200,background='purple',fg='white')
computerscore.grid(row=1,column=0)
playerscore.grid(row=2,column=0)

#Indicators

user_indicator=Label(root,font=100,text='USER',background='orange',fg= 'Purple')
comp_indicator=Label(root, font=100,text='COMPUTER',background='orange',fg='purple')
comp_indicator.grid(row=1,column=3)
user_indicator.grid(row=2,column=1)

#Message
msg=Label(root,font=50,bg='purple',fg='white')
msg.grid(row=1,column=1)

#update message
def updateMessage(x):
    msg['text']=x
    
#update user score 
def updateUserscore():
    score=int(playerscore['text'])
    score+=1
    playerscore['text']=str(score)
    
    
#computerscore
def updatecomputerscore():
    score=int(computerscore['text'])
    score+=1
    computerscore['text']=str(score)
#check winner 
def checkwim(player,computer):
    if player==computer:
        updateMessage('Its tie !')    
        
    elif player=='rock':
        if computer=='paper':
            updateMessage("You loose")
            updatecomputerscore()
            
        else: 
        
            updateMessage("You Win")
            updateUserscore()
            
    elif player=='scissor':
        if computer=='rock':
           updateMessage('You loose',)
           updatecomputerscore   
        else:
            updateMessage("You win")
            updateUserscore
    else:
        pass        
    

#choices
choices=('rock','paper','scissor')
def updatedchoice(x):
    
 #for computer   
    compChoice=choices[randint(0,2)]
    if compChoice=='rock':
        comp_label.configure(image=rock_img)
    elif compChoice==('paper'):
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)
    
    
 #for user   
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x==('paper'):
        user_label.configure(image=paper_img)
    elif x==('scissor'):
        user_label.configure(image=scissor_img)
    
    checkwim(x,compChoice)




#buttons
rock=Button(root,width=20,height=2,text='ROCK',background='lightblue',fg='black',command=lambda:updatedchoice('rock')).grid(row=0,column=2)
paper=Button(root,width=20,height=2,text='PAPER',background='pink',fg='black',command=lambda:updatedchoice('paper')).grid(row=0,column=1)
scissor=Button(root,width=20,height=2,text='SCISSOR',background='silver',fg='black',command=lambda:updatedchoice('scissor')).grid(row=0)


root.mainloop()