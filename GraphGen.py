import random
import turtle

list_price = []
list_time = []

rand_mp = input("enter random multiplier: ")

# generates numbers for graph, and inserts the 0-100 time values
for x in range (100):
    rand_add = random.randint(1,int(rand_mp))
    list_time.append(x)
    list_price.append(x + rand_add)
print(list_price)
print(list_time)

#converts graph values to applicable coordinates
for x in range (len(list_price)):
    list_price[x] *= 6.7
    list_price[x] -= 335
    list_time[x] *= 5.5
    list_time[x] -= 275
print(list_price)
print(list_time)
print(len(list_time))
bn1 = 0
bn2 = 0

#finds highest price (currently useless)
for x in range(len(list_price)):
    if list_price[x] > bn1:
        bn1 = list_price[x]

#a test formula for working out the average graph
rm = list_price[len(list_price)-1]





#turtle instructions
turtle.penup()
turtle.goto(-335,-275)
turtle.pendown()
for x in range (len(list_price)):
    turtle.goto(list_time[x], list_price[x])
turtle.penup()
turtle.goto(-335,-275)
turtle.pendown()
turtle.color("red")
turtle.goto(list_time[len(list_time)-1],list_price[len(list_price)-1])
turtle.goto(-335,-275)
for x in range (len(list_price)):
    turtle.goto(list_time[x], (list_time[x]*rm))
print(len(list_time))

#just to keep the turtle tab open
input()
