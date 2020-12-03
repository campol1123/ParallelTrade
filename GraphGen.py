import turtle
import random

ulc = []
llc = []
n_list_p = []
n_list_t = []
d_list = []
turtle.speed(0)
ft = 1

for x in range (120):
    if ft == 1:
        turtle.penup()
    else:
        turtle.pendown()
    x += 1
    ft = 0
    n_list_t.append((x*3)-300)
    n_list_p.append(((x*4)+(random.randint(9,12)*6))-300)
    turtle.goto(n_list_t[x-1],n_list_p[x-1])
turtle.penup()
turtle.goto(n_list_t[0],n_list_p[0])
turtle.color("red")
turtle.pendown()
turtle.goto(n_list_t[-1],n_list_p[-1])

gl = n_list_p[-1]-n_list_p[0]
lm = gl/len(n_list_t)
turtle.penup()
turtle.goto(n_list_t[0],n_list_p[0])
turtle.pendown()

for x in range (120):
    turtle.goto(n_list_t[x],n_list_t[x]*lm)

input()
