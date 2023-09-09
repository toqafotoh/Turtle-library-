#Hello, this is a program for drawing a cute dog 🐕😊

#importing turtle library 🐢 for drawing shapes
import turtle as t
#function to draw any rectangle 
def rectangle(horizontal, vertical, color):
  #put the pen down on our paper to start drawing 🖊️
    t.pendown()
    t.pensize(1)
    t.color(color)
  #start filling the shape color 
    t.begin_fill()
  #for loop that draw the rectangle by repeating two sides
    for _ in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
  #after finishing the drawing we rasie the pen
    t.penup()

#Define dimensions and color for body, tail, legs, and feet
body = [285, 90, "green"] # 🟢 
tail = [30, 105, "orange"] # 🟠 
legs = [30, 105, "blue"] # 🔵
feet = [60, 30, "brown"] # 🟤

# Start of the main drawing program
t.penup()
t.speed('normal')
t.shape('turtle')
t.setheading(0)

#Draw body
'''
body dimensions and color are defined as a list.
and our function receives separate parameters,
In this case, we use the asterisk symbol *️⃣ to extract the elements from the list.
'''
t.goto(-120, 90)
rectangle(*body)

#Draw tail
t.goto(165, 170)
rectangle(*tail)

#Draw legs
'''
We have four legs, two on the left and two on the right.
The inner loop is responsible for drawing the legs
and adjusting the spacing between each pair of legs. 
The outer loop is responsible for adjusting the spacing in the middle.
'''
t.goto(-120,0)
for j in range(1,3):
    for i in range(1,3):
        rectangle(*legs)
        t.penup()
        t.forward(65)
    t.forward(60)


#Draw feet
#As we have four typical feet 🐾 we will use a for loop in range 4 to draw them
t.goto(-150, -105)
for i in range(4):
    rectangle(*feet)
    t.forward(95)

#Function to draw the head of the dog 🐶
def draw_head():

  #Define the paramters for the two parts of the head
    head_1 = [
        (60, 30, "red"),
        (90, 30, "red"),
    ]
    head_2 = [
        (90, 25, "red"),
        (30, 25, "red"),
        (60, 25, "red")
    ]   


    x = -60
    #Adjusting the starting point for drawing the head
    t.goto(-100,190)
    for i in (head_1):
        rectangle(*i)
        t.penup()
        t.right(90)
        t.forward(30)
        t.left(90)
        #Move the turtle forward by 'x' units - and changing value of 'x' each time-
        t.forward(x)
        x = x + 10

    #Drawing the middle part of the head 
    rectangle(140,20,"red")
    t.penup()
    t.right(90)
    t.pendown()
    t.forward(40)
    t.left(90)

    #Adjusting the distance we move forward ➡️
    #and the angle at wich we will turn right .↩️
    dist,angle=85,180
    for i in (head_2):
        rectangle(*i)
        t.forward(dist)
        t.right(angle)
        dist = dist -140
        angle = angle -180
        t.penup()

    #Draw the eyes 👀
    t.goto(-140,145)
    rectangle(25,25,"yellow")
    t.right(90)
    t.forward(7)
    t.left(90)
    t.forward(7)
    rectangle(10,10,"black")

#call the fuction that we wrote to draw the head
draw_head()
#Hide the turtle to see our cute dog clearly 🐕🥰
t.hideturtle()
