import turtle

# window
win = turtle.Screen()
win.bgcolor("White")
win.title("Turtle Logo Tel-U")
win.setup(width=666, height=666)

# turtle
t = turtle.Turtle()

# buku kiri
t.color("white")
t.goto(-113,193)
t.color('#ed3237')
t.begin_fill()
t.forward(50)
t.circle(-150,25)
t.right(65)
t.forward(60)
t.goto(-113,193)
t.forward(60)
t.left(90)
t.forward(50)
t.circle(-150,25)
t.right(65)
t.end_fill()

# buku kanan
t.color('#b22d30')
t.begin_fill()
t.goto(113,193)
t.right(90)
t.forward(50)
t.circle(150,25)
t.left(65)
t.forward(60)
t.goto(113,193)
t.forward(60)
t.right(90)
t.forward(50)
t.circle(150,25)
t.end_fill()

# perisai
t.color("white")
t.goto(-113,83)
t.left(155)
t.color('#848688')
t.begin_fill()
t.forward(48)
t.circle(-25,90)
t.forward(50)
t.circle(40,180)
t.forward(50)
t.circle(-25,90)
t.forward(48)
t.right(90)
t.forward(66)
t.circle(-113,180)
t.forward(66)
t.end_fill()

# tengah perisai
t.right(90)
t.forward(48)
t.circle(-25,90)
t.forward(55)
t.color("#606062")
t.forward(91)
t.begin_fill()
t.backward(96)
t.circle(40,180)
t.backward(96)
t.left(90)
for i in range(7):
    t.forward(5)
    t.left(90)
    t.forward(1)
    t.right(90)
t.forward(1)
for i in range(7):
    t.forward(6)
    t.right(90)
    t.forward(1)
    t.left(90)
t.left(45)
t.end_fill()
t.forward(1)

# Tulisan Tel-U
t.color("white")
t.goto(-110, -180)
t.color('#373435')
t.write('Telkom', font=("courier", 48, "bold"))
t.color("white")
t.goto(-125, -215)
t.color('#373435')
t.write('University', font=("courier", 32, "bold"))
t.color("white")

# Exit jika di klik
win.exitonclick()