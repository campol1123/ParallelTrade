import random
import turtle

list_price = []
list_time = []

rand_mp = input("enter random multiplier: ")

for x in range (100):
    rand_add = random.randint(1,int(rand_mp))
    list_time.append(x)
    list_price.append(x + rand_add)
print(list_price)
print(list_time)

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

    






turtle.penup()
turtle.goto(-335,-275)
turtle.pendown()
for x in range (len(list_price)):
    turtle.goto(list_time[x], list_price[x])
turtle.penup()
turtle.goto(-335,-275)

input()
