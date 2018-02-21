1: a
2: c
3: c
4: c
5: b
6: c
7: a
8: c
9: a
10: e


import turtle

def equalSign(tur,len):
	s=turtle.Screen()
	start=tur.pos()
	tur.forward(len)
	tur.pu()
	tur.goto(start)
	tur.sety(len/2)
	tur.pd()
	tur.forward(len)
	tur.pu()
	tur.goto(start)


def equalSigns(tur, siz, spc, numb):
	for W in range(numb):
		tur.speed(10)
		start=tur.pos()
		equalSign(tur, siz)
		tur.pu()
		tur.fd(spc)
		tur.pd()
		

x=turtle.Turtle()
equalSigns(x, 10, 20, 6)






def vowelCount(string):
	ret=''
	vowel = 'aeiou'
	st=string.lower()
	for letter in (st):
		if letter in vowel:
			ret += letter
	return len(ret)

string = 'I am the walrus'
print(vowelCount(string))





def getInitials(response):
	first=input("whats your first name?",)
	last= input("whats your last name?",)
	print(response, first, last)
	return first[0]+last[0]

init =getInitials("Thank you")
print(init)