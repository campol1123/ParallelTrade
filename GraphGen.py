import turtle
import random

list_price = []
list_time = []
n_list_p = []
n_list_t = []
d_list = []
ulc = []
llc = []
turtle.speed(0)

for x in range (101):
    list_price.append(x)
    list_time.append(x)

turtle.penup()
fc1 = (list_time[0] * 6) - 300
fc2 = (list_price[0]-100)
turtle.goto(fc1, fc2)
turtle.pendown()

for x in range(99):
    x = x+1
    c1 = (list_time[x]*6)-300
    c2 = (list_price[x]+random.randint(-20,150)-50)
    turtle.goto(c1,c2)
    n_list_t.append(c1)
    n_list_p.append(c2)

turtle.goto((list_time[len(list_time)-1]*6)-300,(list_price[len(list_price)-1])-50)
turtle.penup()

turtle.goto(fc1,fc2)
turtle.color("red")
turtle.pendown()
turtle.goto((list_time[len(list_time)-1]*6)-300,(list_price[len(list_price)-1])-50)

end_price = list_price[len(list_price)-1]
print(end_price)

end_price2 = list_price[len(list_price)-2]
print(end_price2)

pm = n_list_p[-1]/100
for x in range (99):
    n = n_list_p[x]-(pm*n_list_t[x])
    d_list.append(n)
bn = 0
sn = 0
for x in range(len(d_list)):
    if bn < d_list[x]:
        bn = d_list[x]
    if d_list[x] < sn:
        sn = d_list[x]
for x in range(len(d_list)):
    ulc.append((pm*n_list_t[x])+bn)
    llc.append((pm * n_list_t[x]) + sn)

turtle.penup()
turtle.goto(fc1, fc2)
turtle.pendown()

for x in range(len(d_list)):
    turtle.goto(n_list_t[x],ulc[x])
turtle.penup()
turtle.goto(fc1, fc2)
turtle.pendown()

for x in range(len(d_list)):
    turtle.goto(n_list_t[x],llc[x])


print(llc)
print(ulc)
print (sn)
print(bn)
print (d_list)






input()
