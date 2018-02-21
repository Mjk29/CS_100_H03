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

