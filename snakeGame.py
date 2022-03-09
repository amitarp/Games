"""Importing the required libraries............................................................................."""
from cProfile import label
from tkinter import *
import random
from tkinter import font

from matplotlib.pyplot import fill, text

"""Constants....................................................................................................."""
GAME_WIDTH=500
GAME_HEIGHT=500
SPEED=150
SPACE_sIZE=50
BODY_PARTS=3
SNAKE_COLOR='green'
FOOD_COLOR='red'
BACKGROUND_COLOR='#000000'

"""Snake Class......................................................................................................"""
class Snake:
    def __init__(self) -> None:
        self.bodySize=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_sIZE,y+SPACE_sIZE,fill=SNAKE_COLOR,tag='snake')
            self.squares.append(square)
        

"""Food class..........................................................................................................."""
class Food:
    def __init__(self) -> None:
        x=random.randint(0,(GAME_WIDTH/SPACE_sIZE)-1)*SPACE_sIZE
        y=random.randint(0,(GAME_HEIGHT/SPACE_sIZE)-1)*SPACE_sIZE

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+SPACE_sIZE,y+SPACE_sIZE,fill=FOOD_COLOR,tag='food')


"""Necessary functions................................................................................................"""
def nextTurn(snake,food):
    
    x,y=snake.coordinates[0]
    
    if direction=='up':
        y-=SPACE_sIZE

    elif direction=='down':
        y+=SPACE_sIZE

    elif direction=='left':
        x-=SPACE_sIZE

    elif direction=='right':
        x+=SPACE_sIZE

    snake.coordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+SPACE_sIZE,y+SPACE_sIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        scoreLabel.config(text='Score:{}'.format(score))
        canvas.delete('food')
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkCollision(snake):
        gameOver()
    else:
        window.after(SPEED,nextTurn,snake,food)

"""For changing the directions................................................................................................"""
def changeDirection(newDirection):
    global direction

    if newDirection=='left':
        if direction!='right':
            direction=newDirection
    elif newDirection=='right':
        if direction!='left':
            direction=newDirection
    elif newDirection=='up':
        if direction!='down':
            direction=newDirection
    elif newDirection=='down':
        if direction!='up':
            direction=newDirection

"""For checking the collisions............................................................................................."""
def checkCollision(snake):
    x,y=snake.coordinates[0]   
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    for bodyParts in snake.coordinates[1:]:
        if x==bodyParts[0] and y==bodyParts[1]:
            return True
    return False

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas,100'),text="GAME OVER",fill='red',tag='gameover')

'''Main Program.............................................................................................................'''

window=Tk()
window.title('Snake Game')
window.resizable(False,False)

score=0
direction='down'
scoreLabel=Label(window,text='Score:{}'.format(score),font=('consolas',40))
scoreLabel.pack()

canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

'''For setting the window in the middle.......................................................................................'''
window.update()
windowWidth=window.winfo_width()
windowHeight=window.winfo_height()
screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_screenheight()

y=int((screenHeight/2)-(windowHeight/2))
x=int((screenWidth/2)-(windowWidth/2))

window.geometry(f'{windowWidth}x{windowHeight}+{x}+{y}')

window.bind('<Left>',lambda event:changeDirection('left'))
window.bind('<Right>',lambda event:changeDirection('right'))
window.bind('<Up>',lambda event:changeDirection('up'))
window.bind('<Down>',lambda event:changeDirection('down'))

'''Creating objects..................................................................................................'''
snake=Snake()
food=Food()

nextTurn(snake,food)

window.mainloop()