import turtle          
win = turtle.Screen()  
donatelo = turtle.Turtle()

# add some display options
donatelo.pensize(4)            # increase pensize (takes integer)
donatelo.pencolor("red")     # set pencolor (takes string)
donatelo.shape("turtle")       #icon on screen

#create square
for item in range(4):
    donatelo.forward(100)
    donatelo.right (90)

#shift position
donatelo.pensize(0)
donatelo.pencolor("white")
donatelo.left(90)
donatelo.forward(250)
donatelo.pensize(4)
donatelo.pencolor("red")

#create triangle
for item in range(3):
    donatelo.right(120)
    donatelo.forward(100)




win.mainloop()

