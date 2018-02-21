1: d
2: a 
3: d
4: e
5: c
6: a
7: e
8: d
9: b
10: d






import turtle 
s=turtle.Screen()
t=turtle.Turtle()

def drawTick(tur, tickLen):
	start=tur.position()
	tur.pd
	tur.right(90)
	tur.forward(tickLen)
	tur.pu
	tur.seth(0)
	tur.goto(start)


def drawTicks(tur, tickLen, numTicks, distance):
	for i in range(numTicks):
		drawTick(tur,tickLen)
		tur.pu()
		tur.setx(tur.xcor()+distance)
		tur.pd()
		
drawTicks(t,5,10,15)






def beginsWith(letter, strList):
	i=0
	for word in strList:
		if word[0] == letter:
			i+=1
	return i

eliza = ['the','rain','in','spain','falls','mainly','on','the','plain']
firstLetter = 't'

print(beginsWith(firstLetter, eliza))





def greeting(greetStr):
	name=input("Whats your name \n",)
	day=input("Whats the day \n",)
	print(greetStr,day, name)
	if len(name) > len(day):
		print("name has more")
	if len(name) == len(day):
		print("name has same")
	if len(name) < len(day):
		print("name has less")

greeting("hello")