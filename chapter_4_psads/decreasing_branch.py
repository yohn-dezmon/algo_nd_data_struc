# my modifications to the code allow each branch to be smaller than the previous
# branch


import turtle

def tree(branchLen,t, pensize):
    if branchLen > 5:
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
    t.color("green")
    t.pensize(10)
    tree(75,t,10)
    myWin.exitonclick()

main()


# brancLength = 50
# if >> YES so... pensize >> 8, forward 50, turn right 20 degrees
# tree(35,t,8)
# if >> YES so... pensize >> 6, forward 35, turn right 20 degrees
# tree(20,t,6)
#  if >> YES so ...  pensize >> 4, forward 20, turn right 20
# tree(5,t,4)
# if >> FALSE, so ... t(20,t,6) turn left 40
