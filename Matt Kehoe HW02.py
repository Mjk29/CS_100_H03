

""""CS.2"""

import turtle
import time

s = turtle.Screen()

t=turtle.Turtle()

for x in range(0,4):
	t.forward(100)
	t.left(90)


"""CS.3"""

for x in range(0,2):
	
	t.left(120)
	t.forward(100)

t.left(60)
t.forward(100)

t.left(120)
t.forward(100)

"""CS.4"""

for x in range(0,5):
	
	t.left(72)
	t.forward(100)

	
"""CS.6"""

t.circle(100)

t.pu()
t.setpos(50,100)
t.pd()

t.circle(-100)

t.pu()
t.setpos(-50,100)
t.pd()

t.circle(-100)

t.pu()
t.setpos(0,0)
t.pd()

t.circle(-100)