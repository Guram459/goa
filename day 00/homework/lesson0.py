from turtle import *

#we want paint house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

left(30)
color("purple")
forward(120)
color("brown")
begin_fill()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
end_fill()

color("purple")
left(90)
forward(130)

left(90)
forward(200)

left(90)
forward(120)

color("brown")
begin_fill()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

end_fill()

#draw Grass

color("purple")
right(90)
forward(75)
left(90)

color("green")
begin_fill()
forward(175)
right(90)
forward(310)

right(90)
forward(760)

right(90)
forward(310)

right(90)
forward(700)
end_fill()




exitonclick()