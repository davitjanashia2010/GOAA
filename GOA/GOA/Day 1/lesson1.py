from turtle import *
shape("turtle")

 #we want to paint a house

#step 1:  draw a square
speed(5)
width(5)
color("green")
forward(200)
left(90)
forward(200)
left(45)
forward(150)
left(90)
forward(150)
left(45)
forward(200)

left(90)

forward(75)
color("brown")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
penup()
goto(105,35)
pendown()
right(90)
forward(20)
penup()
goto(200,200)
pendown()

begin_fill()
color("blue")
forward(210)
left(90)
forward(70)
left(90)
forward(210)
left(90)
forward(70)
left(90)
forward(105)
left(90)
forward(70)
left(180)
forward(35)
left(90)
forward(105)
left(180)
forward(210)
end_fill()
penup()
goto(200,0)
color("green")
speed(20)
pendown()
begin_fill()
forward(500)
left(180)
forward(1200)
left(90)
forward(2000)
left(90)
forward(1900)
left(90)
forward(2000)
end_fill()
penup()
goto(400,400)
color ("yellow")
speed(5)
pendown()
begin_fill()
forward(2)
right(120)
forward(80)
left(90)
forward(60)
left(90)
forward(100)
penup()
goto(0,0)
pendown()
left(30)
color("green")
forward(200)
right(90)
color("brown")
forward(100)
color("green")
begin_fill()
circle(50)
right(180)
circle(50)
right(180)
forward(200)
circle(130)
right(180)
circle(130)
right(360)
forward(100)
circle(100)
right(180)
circle(100)








end_fill()
color("brown")
left(90)
forward(50)
right(180)
forward(100)
left(90)
forward(80)
left(90)
forward(100)
left(90)
forward(80)
width(2)
forward(200)
right(180)
forward(280)
begin_fill()
width(4)
right(45)
forward(75)
right(90)
forward(75)
end_fill()
left(180)
penup()
goto(0,0)
forward(200)
right(135)
color("green")
left(25)
pendown()
forward(20)
left(155)
forward(200)
left(90)
forward(35)



exitonclick()