import turtle
s=turtle.Screen()
s.bgcolor("Black")
s.register_shape("1.gif")
s5=turtle.Turtle(shape="1.gif")
s.register_shape("2.gif")
s4=turtle.Turtle(shape="2.gif")
s.register_shape("3.gif")
s3=turtle.Turtle(shape="3.gif")
s2=turtle.Turtle(shape="2.gif")
s1=turtle.Turtle(shape="1.gif")
s1.pu()
s2.pu()
s3.pu()
s4.pu()
s5.pu()
s1.sety(-74)
s2.sety(166)
s3.sety(406)
s4.sety(648)
s5.sety(889)
v=turtle.Turtle(shape="square")
v.ht()
v.shapesize(5,2)
v.pu()
v.goto(200,-82)
v.fillcolor("Blue")
v.st()
v1=v.clone()
v1.fillcolor("Cyan")
v1.goto(-300,-82)
t1=turtle.Turtle()
s.onscreenclick(t1.goto)
def h1():
    print(t1.pos())
s.onkey(h1,"h")
s.listen()
