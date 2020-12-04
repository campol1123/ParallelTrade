import turtle
import random

ulc = []
llc = []
n_list_p = []
n_list_dp = []
n_list_t = []
d_list = []
turtle.speed(0)
ft = 1

for x in range (50):
    if ft == 1:
        turtle.penup()
    else:
        turtle.pendown()
    x += 1
    ft = 0
    n_list_t.append((x*3)-300)
    n_list_p.append(((x * 5) - 300) + (random.randint(-20, 120)))
    n_list_dp.append(((x * 5) - 300))
    turtle.goto(n_list_t[x-1],n_list_p[x-1])

ft = 1
turtle.color("red")
for x in range (50):
    if ft == 1:
        turtle.penup()
    else:
        turtle.pendown()
    x += 1
    ft = 0
    turtle.goto(n_list_t[x-1],n_list_dp[x-1])
    d_list.append(n_list_p[x-1]-n_list_dp[x-1])

bd = 0
sd = 0

for x in range (50):
    if bd < d_list[x]:
        bd = d_list[x]
    if sd > d_list[x]:
        sd = d_list[x]
for x in range (50):
    ulc.append(n_list_dp[x] + bd)
    llc.append(n_list_dp[x] + sd)

ft = 1
for x in range (50):
    if ft == 1:
        turtle.penup()
    else:
        turtle.pendown()
    x += 1
    ft = 0
    turtle.goto(n_list_t[x-1],ulc[x-1])
ft = 1
for x in range (50):
    if ft == 1:
        turtle.penup()
    else:
        turtle.pendown()
    x += 1
    ft = 0
    turtle.goto(n_list_t[x-1],llc[x-1])


input()
