from turtle import *
root=Screen() #obeject of screen class
root.title("snake game:  developer usama")
root.setup(width=600,height=600)
root.bgcolor('black')
root.bgpic('bodder.gif')
root.addshape('snakeup.png.gif')
root.addshape('food.gif')
root.addshape('snakedown.gif')
root.addshape('sankeright.gif')
root.addshape('snakeleft.gif')
root.addshape('body.gif')
root.tracer(False)
delay=0.1
score=0
hiigh_score=0
head=Turtle()#this is use for makinh snake head by default
head.shape('snakeup.png.gif')
head.penup()
head.goto(0,0)
head.direction='stop'
food=Turtle()#make food by default
food.shape('food.gif')
food.penup()
food.goto(0,180)

pen=Turtle()
pen.penup()
pen.goto(0,270)
pen.hideturtle()
pen.color('white')
pen.write("Score=0 High_score=0",align="center",font="monaco 19 bold")

end=Turtle()
end.penup()
end.hideturtle()

def moving():
    if(head.direction=='up'):
        y=head.ycor()
        y=y+20
        y=head.sety(y)
    if (head.direction == 'down'):
        y = head.ycor()
        y = y - 20
        y = head.sety(y)
    if(head.direction=='left'):
        x=head.xcor()
        x=x-20
        x=head.setx(x)
    if (head.direction =='right'):
            x = head.xcor()
            x=x+20
            x=head.setx(x)

def top():
    if(head.direction!='down'):
        head.direction='up'
        head.shape('snakeup.png.gif')
def bottom():
    if (head.direction !='up'):
        head.direction='down'
        head.shape('snakedown.gif')
def rigt():
    if (head.direction != 'left'):
        head.direction='right'
        head.shape('sankeright.gif')
def lft():
    if (head.direction != 'right'):
        head.direction='left'
        head.shape('snakeleft.gif')
def sound():
    import pygame as pg
    from pygame import mixer
    pg.init()
    # mixer.music.load('sound snake.mp3')
    # mixer.music.play(-1)

root.listen()
sound()
root.onkeypress(top,'Up')
root.onkeypress(bottom,'Down')
root.onkeypress(rigt,'Right')
root.onkeypress(lft,'Left')
segments=[]
while(True):
    import time
    import random
    root.update()
    if head.xcor()>259 or head.xcor()<-259 or head.ycor()>259 or head.ycor()<-259:
        end.color('white')
        end.write('Game lost...!!!\nDevelop By Usama',align="center",font="monaco 25 bold")
        time.sleep(2)
        end.clear()
        head.goto(0,0)
        head.direction='stop'
        for body in segments:
            body.goto(1000,1000)

        segments.clear()

        score=0
        hiigh_score=0
        delay=0.1
        with open("highscore.txt", "r") as f:
            hiigh_score = f.read()
        pen.clear()
        pen.write(f'Score:{score}' f' High Score:{hiigh_score}', font="monaco 19 bold", align='center')

    if(head.distance(food)<20):
        x=random.randint(-255,255)
        y=random.randint(-255,255)
        food.goto(x,y)
        delay=delay-0.003


        body=Turtle()
        body.penup()
        body.shape('body.gif')
        segments.append(body)

        score = score + 5

        # if score > hiigh_score:
        with open("highscore.txt", "w") as f:
            hiigh_score = score
            f.write(str(hiigh_score))
        pen.clear()
        with open("highscore.txt", "r") as f:
            hiigh_score=f.read()
        pen.write(f'Score:{score}' f' High Score:{hiigh_score}',font="monaco 19 bold", align='center')

    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if(len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    moving()

    for body in segments:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for body in segments:
                body.goto(1000,1000)
            segments.clear()
            score=0
            hiigh_score=0
            delay=0.1
            end.color('white')
            end.write('Game lost...!!!\nDevelop By Usama',align="center", font="monaco 25 bold")
            time.sleep(2)
            end.clear()

            pen.clear()
            with open("highscore.txt", "r") as f:
                hiigh_score = f.read()
            pen.write(f'Score:{score}'f' High Score:{hiigh_score}', font="monaco 19 bold", align='center')

    time.sleep(delay)

