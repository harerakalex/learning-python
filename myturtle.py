import turtle

# Turtle with loop
wn = turtle.Screen()
me = turtle.Turtle()
me.color('red')
me.shape('turtle')

distance = 50
angle = 90
me.up()
for _ in range(10): 
    me.stamp()
    me.forward(distance)
    me.right(angle)
    distance += 10