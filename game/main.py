
##import turtle
##import random 

score=0
lives=10
###code for main window  
##main_window= turtle.Screen()
##main_window.title("falling apples game")
##main_window.bgcolor('pink')
##main_window.setup(width=600, height=600)
##main_window.tracer(0)

##direction= "stop"


##actor = turtle.Turtle()
##actor.shape("circle")
##actor.speed(0)
##actor.penup()
##actor.goto(0,-270)

##def move_left():
##    global direction
##    direction = " left "
##def move_right():
##    global direction
##    direction = " right "
##def stop_actor():
##    global direction
##    direction = " stop "

##main_window.listen()
##main_window.onkeypress(move_left,"Left")
##main_window.onkeypress(move_right,"Right")
##main_window.onkeypress(stop_actor,"Down")
##

        


#code for sub title 
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("yellow")
font = ("courier",26,"bold")
pen.goto(0,260)
pen.write("score: {} -- lives: {}".format(score,lives),align="center",font=font)
 

 
 
#code for box 
actor = turtle.Turtle()
actor.shape("circle")
actor.color("orange")
actor.speed(0)
actor.penup()
actor.goto(0,-270)



#code for a red apple
##red_apples=[]
##for i in range(6):
##    red_apple= turtle.Turtle()
##    red_apple.shape("circle")
##    red_apple.color("red")
##    red_apple.penup()
##    red_apple.speed(random.randint(1,4))
##    red_apple.goto(-50,270)
##    red_apples.append(red_apple)



#code for a green apple
green_apples=[]

for i in range(6):
    green_apple= turtle.Turtle()
    green_apple.shape("circle")
    green_apple.color((0,1,0))
    green_apple.penup()
    green_apple.speed(random.randint(1,4))
    green_apple.goto(50,270)
    green_apples.append(green_apple)
 
#code for faling green and red apple
while True:
 main_window.update()
 for red_apple in red_apples:   
     y=red_apple.ycor()
     y-=0.1*red_apple.speed()
     red_apple.sety(y)

     if y<-300:
         x=random.randint(-270,270)
         red_apple.goto(x,270)
     if red_apple.distance(actor) <40:
         x=random.randint(-270,270)
         red_apple.goto(x,270)
         score+=10
         pen.clear()
         pen.write("score: {} -- lives: {}".format(score,lives),align="center",font=font)
         


 for green_apple in green_apples:   
     y=green_apple.ycor()
     y-=0.1*green_apple.speed()
     green_apple.sety(y)

     if y<-300:
         x=random.randint(-270,270)
         green_apple.goto(x,270)
     if green_apple.distance(actor) <40:
         x=random.randint(-270,270)
         green_apple.goto(x,270)
         score-=10
         lives-=1
         pen.clear()
         pen.write("score: {} -- lives: {}".format(score,lives),align="center",font=font)
         if lives <0:
             main_window.bye()
             exit(0)
 
##while True:
##    main_window.update()
##    if direction == " left":
##        x = actor.xcor()
##        x -=0.05
##        actor.setx(x)
##    if direction == " right":
##        x = actor.xcor()
##        x +=0.05
##        actor.setx(x)  

main_window.mainloop()
