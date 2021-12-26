import random
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing speed game')

##############################################variables

words=['Mango','Apple','Blueberry','Peaches','Kiwi','Orange','Banana','Plum','Fig','Avocado','Durian','Dates',
'Apricot','Melon','Lemon','Pears','Pineapple','Papayas','Coconut','Grapefruit']
score=0
timeleft=60
count=0
sliderword=''
miss=0

#############################################functions

def labelslider():
    global count,sliderword
    text='Welcome to Typing Speed Game!!'
    if count>=len(text):
        count=0
        sliderword=''
    sliderword+=text[count]
    count+=1
    fontlabel.configure(text=sliderword)
    fontlabel.after(150,labelslider)

def timer():
    global timeleft,score,miss
    if timeleft>10:
        pass
    else:
        timelabelcount.configure(fg='red')
    if (timeleft>0):
        timeleft-=1
        timelabelcount.configure(text=timeleft)
        timelabelcount.after(1000,timer)
    else:
        gamedetail.configure(text='Hit={} | Miss={} | Total Score={}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notiffication','For play again Hit Enter')
        if rr==True:
            score=0
            timeleft=60
            miss=0
            timelabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)

def startgame(event):
    global score,miss
    if timeleft==60:
        timer()
    gamedetail.configure(text='')
    if wordentry.get()==wordlabel['text']:
        score+=1
        scorelabelcount.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)



##############################################creating the label

fontlabel=Label(root,text='',font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontlabel.place(x=10,y=10)
labelslider()

random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue',)
wordlabel.place(x=350,y=200)

scorelabel=Label(root,text='Your score is:',font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scorelabelcount.place(x=80,y=180)

timelabel=Label(root,text='Time Left:',font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timelabel.place(x=600,y=100)

timelabelcount=Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timelabelcount.place(x=680,y=180)

gamedetail=Label(root, text='Type word and Hit Enter Button',font=('airal',30,'italic bold'),bg='powder blue',fg='dark grey')
gamedetail.place(x=120,y=450)

################################################creating the entry label
wordentry = Entry(root, font=('airal',25,'italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=300)
wordentry.focus_set()

root.bind('<Return>',startgame)

root.mainloop()