import math

a=3
b=4
c=5

print(a,b,c)

if a<b:
	print("ok")
else:
	print("not ok")
	pass

if c<b:
	print("ok")
else:
	print("not ok")
	pass

if a+b<c:
	print("ok")
else:
	print("not ok")
	pass	

if a**2 + b**2 == c**2:
	print("ok")
else:
	print("not ok")
	pass	

""""""

import turtle


t=turtle.Turtle()


t.color(input('what color? '))
t.pensize(input('what line width? '))
length=int(input('what line length? '))
shape=input('Line, triangle, or square? ')

print(t.width)

if shape == 'line':
   
    t.forward(length)
   
    

if shape =='triangle':
    for i in range(0,3):
        t.right(120)
        t.forward(length)
        
if shape == 'square':
    for i in range(0,4):
        t.right(90)
        t.forward(length)

s=turtle.Screen()
