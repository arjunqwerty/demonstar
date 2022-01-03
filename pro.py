#background and setup
import turtle
import time
s=turtle.Screen()
s.bgcolor("Black")
s.register_shape("B.gif")
bg=turtle.Turtle(shape="B.gif")
g1=turtle.Turtle()
g1.ht()
g1.fillcolor("White")
g1.shapesize(1.5,1.5)
g1.pu()
g1.goto(-75,-175)
g1.st()
w=ww=0
k=-175
q=0
hv=True
def h1():
    global hv
    hv=False
def q1():
    global k
    if k==-175:
        g1.sety(-175-60)
    else:
        g1.sety(-175)
    k=g1.ycor()
def q2():
    global k
    if k==-175:
        g1.sety(-175-60)
    else:
        g1.sety(-175)
    k=g1.ycor()
def q3():
    global hv
    global k
    global q
    s.bgcolor("Black")
    s.register_shape("1.gif")
    s.register_shape("4.gif")
    s5=turtle.Turtle(shape="4.gif")
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
    s4.sety(646)
    s5.sety(886)
    #hero
    h=turtle.Turtle(shape="square")
    h.ht()
    h.shapesize(5,2)
    h.fillcolor("Yellow")
    h.pu()
    h.goto(-250,-200)
    h.st()
    #gun
    t=turtle.Turtle()
    t.ht()
    t.pu()
    t.begin_poly()
    t.fd(130)
    t.bk(30)
    t.rt(120)
    t.fd(20)
    t.rt(60)
    t.fd(80)
    t.lt(60)
    t.fd(40)
    t.rt(60)
    t.fd(20)
    t.end_poly()
    p=t.get_poly()
    s.register_shape("Gun",p)
    m=turtle.Turtle(shape="Gun")
    m.ht()
    m.pu()
    m.shapesize(0.5,0.5)
    m.lt(90)
    m.goto(-250,-200)
    m.fillcolor("red")
    m.st()
    #second gun
    t.clear()
    t.goto(0,0)
    t.begin_poly()
    t.backward(130)
    t.fd(30)
    t.lt(120)
    t.backward(20)
    t.lt(60)
    t.backward(80)
    t.rt(60)
    t.backward(40)
    t.lt(60)
    t.backward(20)
    t.end_poly()
    p3=t.get_poly()
    s.register_shape("SecondGun",p3)
    m1=turtle.Turtle(shape="SecondGun")
    m1.ht()
    m1.rt(90)
    m1.pu()
    m1.shapesize(0.5,0.5)
    m1.goto(200,-200)
    m1.fillcolor("Red")
    t.clear()
    #text turtles initialization
    a=turtle.Turtle()
    a.ht()
    a2=turtle.Turtle()
    a2.ht()
    bh=turtle.Turtle(shape="circle")
    bh.ht()
    bh.pu()
    bh.shapesize(1,10)
    bh.goto(-250,0)
    if g1.ycor()==-175:
        #eyes
        e1=turtle.Turtle(shape="circle")
        e1.ht()
        e2=turtle.Turtle(shape="circle")
        e2.ht()
        e1.shapesize(0.5,0.5)
        e2.shapesize(0.5,0.5)
        e1.pu()
        e2.pu()
        e2.goto(-257,-165)
        e1.goto(-243,-165)
        e1.st()
        e2.st()
        #hey here i am!
        a1=turtle.Turtle()
        a1.ht()
        a1.pu()
        a.pu()
        a.goto(-255,-150+14.14)
        a1.goto(-250,-150)
        a1.pencolor("Black")
        a1.pd()
        a1.lt(45)
        a1.fd(20)
        a.pencolor("Black")
        a.write("Hey! Here I am!",font=("Calibri",15))
        #since when did i own a gun?
        time.sleep(3)
        e1.rt(45)
        e2.rt(45)
        e1.fd(5)
        e2.fd(5)
        e1.shapesize(0.75,0.75)
        e2.shapesize(0.75,0.75)
        time.sleep(3)
        a.clear()
        a.write("since when did i own a gun?",font=("Calibri",15))
        e1.bk(5)
        e2.bk(5)
        e1.shapesize(0.5,0.5)
        e2.shapesize(0.5,0.5)
        #villian
        v=turtle.Turtle(shape="square")
        v.ht()
        v.shapesize(5,2)
        v.pu()
        v.goto(170,-82)
        v.fillcolor("Blue")
        v.st()
        #dialogues
        a3=turtle.Turtle()
        a3.ht()
        a3.pencolor("Red")
        a3.pu()
        a3.goto(189,-30)
        a3.pd()
        a3.lt(135)
        a3.fd(20)
        a2.pu()
        a2.goto(100,-15)
        a2.pencolor("Red")
        time.sleep(2)
        a.clear()
        e1.lt(90)
        e2.lt(90)
        e1.fd(5)
        e2.fd(5)
        a.clear()
        time.sleep(3)
        a.write("Hey There... Blind Man!",font=("Calibri",15))
        time.sleep(3)
        a2.write("You've got fancy eyes...",font=("Calibri",15))
        time.sleep(3)
        a.clear()
        a.write("OHH! How could you see???",font=("Calibri",15))
        time.sleep(3)
        a2.clear()
        a2.write("Doesn't matter...",font=("Calibri",15))
        time.sleep(3)
        a2.clear()
        a.clear()
        a2.write("What matters is... ",font=("Calibri",15))
        time.sleep(3)
        a2.clear()
        a2.write("U DONT DESERVE THEM!",font=("Calibri",15))
        time.sleep(3)
        bh.st()
        e1.sety(0)
        e2.sety(0)
        e1.ht()
        e2.ht()
        time.sleep(1)
        bh.ht()
        time.sleep(2)
        a.write("AAAAAHHHHHHH! MY EYES",font=("Calibri",15))
        time.sleep(3)
        a2.clear()
        time.sleep(0.5)
        a.clear()
        a.write("I will NOT spare you for this!",font=("Calibri",15))
        time.sleep(3)
        a2.write("Haha!! We'll see",font=("Calibri",15))
        a.clear()
        time.sleep(3)
        a3.clear()
        a2.clear()
        time.sleep(3)
        a.write("Help me kill him",font=("Calibri",15))
        time.sleep(3)
        a.clear()
        a1.clear()
        g1.ht()
    elif g1.ycor()==-175-60:
        #villian
        v=turtle.Turtle(shape="square")
        v.ht()
        v.shapesize(5,2)
        v.pu()
        v.goto(175,-82)
        v.fillcolor("Blue")
        v.st()
    v1=v.clone()
    v1.ht()
    v1.fillcolor("Cyan")
    v1.goto(-200,-82)
    #bullet
    b=turtle.Turtle(shape="circle")
    b.ht()
    b.shapesize(0.5,0.5)
    b.fillcolor("White")
    b.pu()
    b.goto(-250,-200)
    b.speed(5)
    bg.ht()
    #game starts
    while q<4:
        v.st()
        b.ht()
        b.goto(-250,-200)
        hv=True
        m.seth(90)
        m1.seth(-90)
        #gun physics
        while hv==True:
            for i in range(90):
                m.lt(1)
                if hv==False:
                    k=m.heading()-90
                    break
            if hv==True:
                for j in range(90):
                    m.rt(1)
                    if hv==False:
                        k=m.heading()-90
                        break
        b.st()
        b.seth(k)
        if b.heading()<10.3:
            b.fd(300)
        #gun physics closed
        elif b.heading()>23:
            b.fd(300)
            b.fd(1200)
        else:
            b.fd(300)
            v.ht()
            b.fd(1200)
        if b.heading()<10.3 or b.heading()>23:
            if q==3:
                a2.pencolor("White")
            a2.write("TRYING TO KILL ME?",font=("Calibri",15))
            time.sleep(3)
            a2.clear()
            a2.write("HOW DARE YOU!!",font=("Calibri",15))
            bh.st()
            m.sety(0)
            m.ht()
            h.sety(0)
            h.ht()
            break
        if g1.ycor()==-175 and q==0:
            time.sleep(1)
            a.write("WOAH! Where did he go?",font=("Calibri",15))
            time.sleep(3)
            a.clear()
        m.seth(0)
        time.sleep(0.5)
        m.ht()
        h.fd(250)
        for i in range(3):
            h.sety(h.ycor()+40)
            h.fd(50)
        h.fd(50)
        for i in range(10*3):
            h.sety(h.ycor()-4)
            s1.sety(s1.ycor()-4)
            s2.sety(s2.ycor()-4)
            s3.sety(s3.ycor()-4)
            s4.sety(s4.ycor()-4)
            s5.sety(s5.ycor()-4)
        if g1.ycor()==-175 and q==0:
            a.setx(100)
            a.write("What just happened?",font=("Calibri",15))
            time.sleep(3)
            a.clear()
        v1.st()
        m1.st()
        time.sleep(0.5)
        #gun physics
        b.ht()
        b.goto(200,-200)
        hv=True
        while hv==True:
            for i in range(90):
                m1.rt(1)
                if hv==False:
                    k=m1.heading()-90
                    break
            if hv==True:
                for j in range(90):
                    m1.lt(1)
                    if hv==False:
                        k=m1.heading()-90
                        break
        b.st()
        b.seth(k)
        b.fd(250)
        if 180-b.heading()<12:
            b.ht()
        elif 180-b.heading()>24:
            b.fd(1250)
        else:
            v1.ht()
            b.fd(1250)
        #gun physics closed
        if 180-b.heading()<12 or 180-b.heading()>24:
            los=turtle.Turtle()
            los.ht()
            los.pu()
            los.goto(-200,-15)
            los.write("TRYING TO KILL ME?",font=("Calibri",15))
            time.sleep(3)
            los.clear()
            los.write("U DON'T DESERVE TO LIVE!!",font=("Calibri",15))
            bh1=turtle.Turtle(shape="circle")
            bh1.ht()
            bh1.shapesize(1,10)
            bh1.pu()
            bh1.setx(200)
            bh1.st()
            m1.sety(0)
            m1.ht()
            h.sety(0)
            h.ht()
            break
        m1.seth(0)
        time.sleep(0.2)
        m1.ht()
        v1.ht()
        h.bk(250)
        for i in range(3):
            h.sety(h.ycor()+40)
            h.bk(50)
        h.bk(50)
        for i in range(10*3):
            h.sety(h.ycor()-4)
            s1.sety(s1.ycor()-4)
            s2.sety(s2.ycor()-4)
            s3.sety(s3.ycor()-4)
            s4.sety(s4.ycor()-4)
            s5.sety(s5.ycor()-4)
        if i<3:
            v.st()
        m.st()
        q+=1
    s1.ht()
    s2.ht()
    s3.ht()
    s4.ht()
    s5.ht()
    if q==4 and g1.ycor()==-175:
        v.st()
        win=turtle.Turtle()
        win.ht()
        win.pu()
        win.pencolor("White")
        win.goto(-100,-30)
        win.write("All right! All right! You Win!",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        win.write("You can have your eyes back",font=("Calibri",15))
        time.sleep(3)
        e2.goto(-257,-165)
        e1.goto(-243,-165)
        e1.st()
        e2.st()
        time.sleep(3)
        win.clear()
        a.pencolor("White")
        e1.fd(5)
        e2.fd(5)
        a.write("But why did you do this to me?",font=("Calibri",15))
        time.sleep(3)
        a.clear()
        win.write("I am a magician with no eyes",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        win.write("I was jealous of your beautiful eyes...",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        win.write("So I wanted it to be mine",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        win.write("I am sorry for what I did...",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        win.write("I don't deserve to live...",font=("Calibri",15))
        time.sleep(3)
        win.clear()
        bh.st()
        bh.setx(170)
        bh.fillcolor("White")
        v.sety(0)
        v.ht()
        time.sleep(1)
        bh.ht()
        time.sleep(5)
        s.register_shape("C.gif")
        cre=turtle.Turtle("C.gif")
    if q!=4:
        time.sleep(5)
        s.register_shape("L.gif")
        cre=turtle.Turtle("L.gif")
s.onkey(q1,"Up")
s.onkey(q2,"Down")
s.onkey(q3,"Return")
s.onkey(h1,"space")
s.listen()
