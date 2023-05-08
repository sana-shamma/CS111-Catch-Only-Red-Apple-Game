import turtle
import random

score=0
lives=5

#code for design main window

main_window= turtle.Screen()
main_window.title("Catch only Red Apple")
main_window.bgpic('back.gif')
main_window.setup(width=600, height=600)
main_window.tracer(0)
main_window.register_shape("red.gif")
main_window.register_shape("green.gif")
main_window.register_shape("right.gif")
main_window.register_shape("left.gif")

#code for score and lives
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("red")
font=("Courier",26,"bold")
pen.goto(0,260)
pen.write("score:{} -- Lives:{}".format(score,lives),align="center",font=font)




#code for the horse
actor = turtle.Turtle()
actor.shape("right.gif")
actor.speed(0)
actor.penup()
actor.goto(0,-250)

#code for red apples
red_apples=[]
for i in range(6):
    red_apple=turtle.Turtle()
    red_apple.shape("red.gif")
    red_apple.penup()
    red_apple.speed(random.randint(1,4))
    red_apple.goto(-50,270)
    red_apples.append(red_apple)

#code for green apple
green_apples=[]
for i in range(6):
        green_apple=turtle.Turtle()
        green_apple.shape("green.gif")
        green_apple.penup()
        green_apple.speed(random.randint(1,4))
        green_apple.goto(50,270)
        green_apples.append(green_apple)
        
#code for moving the horse
direction= "Stop"

def move_left():
        global direction
        direction = "Left"

def move_right():
        global direction
        direction = "right"

def stop_actor():
        global direction
        direction = "Stop "



main_window.listen()
main_window.onkeypress(move_left,"Left")
main_window.onkeypress(move_right,"Right")
main_window.onkeypress(stop_actor,"Down")

 
while True:
    main_window.update()
    if direction == "Left":
        actor.shape("left.gif")
        x = actor.xcor()
        x -=0.3
        if x< -270:
              x=-270
        actor.setx(x)
    if direction == "right":
        actor.shape("right.gif")
        x = actor.xcor()
        x +=0.3
        if x>270:
            x=270
        actor.setx(x)
        
#code for droping the red apples        
    for red_apple in  red_apples:  
        y=red_apple.ycor() #ycor show the postion of red apple
        y-=0.1*red_apple.speed()
        red_apple.sety(y)# sety show the postion of red apple after changes in its postion

        if y <-300:
            x= random.randint(-270,270)
            red_apple.goto(x,270)
        #code when red apples colucte whith horse to change the score       
        if red_apple.distance(actor)<40:
            x= random.randint(-270,270)
            red_apple.goto(x,270)
            score+=10
            pen.clear()
            pen.write("score:{} -- Lives:{}".format(score,lives),align="center",font=font)
            
#code for droping the green apples                    
    for green_apple in green_apples:  
        y=green_apple.ycor()#ycor show the postion of green apple
        y-=0.1*green_apple.speed()
        green_apple.sety(y)# sety show the postion of green apple after changes in its postion

        if y <-300:
            x= random.randint(-270,270)
            green_apple.goto(x,270)
        #code when green apples colucte whith horse to change the lives       
        if green_apple.distance(actor)<40:
            x= random.randint(-270,270)
            green_apple.goto(x,270)
            score-=10
            lives-=1
            if lives <0:
                main_window.bye()
                exit(0)
            pen.clear()
            pen.write("score:{} -- Lives:{}".format(score,lives),align="center",font=font)
            
                

      

main_window.mainloop()


