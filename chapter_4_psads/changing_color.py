import turtle

def tree(branchLen,t, pensize):
    if branchLen > 5:
        if branchLen <= 20:
            t.down()
            t.color("green")
            t.pensize(pensize-2)
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15,t,pensize-2)
            t.left(40)
            t.pensize(pensize)
            tree(branchLen-15,t,pensize-2)
            t.right(20)
            t.pensize(pensize-2)
            t.up()
            t.backward(branchLen)
        else:
            t.down()
            t.color("brown")
            t.pensize(pensize-2)
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15,t,pensize-2)
            t.left(40)
            t.pensize(pensize)
            tree(branchLen-15,t,pensize-2)
            t.right(20)
            t.pensize(pensize-2)
            t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.pensize(10)
    tree(75,t,10)
    myWin.exitonclick()

main()
