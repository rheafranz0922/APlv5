import turtle

# Function from a drawline
def draw_line(x1, y1, x2, y2, linestyle='-'):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Draw a line from (1, 2) to (6, 8)
draw_line(1, 2, 6, 8)

# Draw a line2 from (1, 3) to (2, 8) to (6, 1) to (8, 10)
turtle.penup()
turtle.goto(1, 3)
turtle.pendown()
turtle.dot()
draw_line(2, 8, 6, 1, linestyle=':')
draw_line(6, 1, 8, 10)

#Result
turtle.exitonclick()