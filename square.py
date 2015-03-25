import turtle
turtle.fillcolor("pink")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
inp = input("quit?")
while(inp != 'q' and inp !='Q'):
    inp = input("quit?")
