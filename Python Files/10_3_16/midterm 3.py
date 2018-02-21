# 1: E
# 2: B
# 3: C
# 4: B
# 5: C
# 6: A
# 7: C
# 8: A
# 9: B
# 10: B

import turtle
def drawSquare(tur,len):
	for i in range(4):
		tur.pd()
		tur.forward(len)
		tur.right(90)
		t.pu()
s=turtle.Screen()
t=turtle.Turtle()
# drawSquare(t, 100)

def drawSquares(tur, size, num, angle):
	for i in range(num):
		t.pd()
		drawSquare(tur, size)
		tur.right(angle)

# drawSquares(t, 100, 4, 20)

def bigCount(numList, threshold):
	count = 0
	for x in numList:
		if threshold > x:
			count+= 1
	return count
someNums = [-5, 6, 3, 0, 7]
# print(bigCount(someNums, 2))

def getDate(message):
	
	month = input("whats the month")
	day= input("whats the day")

	print(month, day, message)
	retSt=month+day
	return retSt

today = getDate("great day")
print(today)
