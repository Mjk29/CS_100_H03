"""
value = 1
if True and False:
 value += 1
elif not True or not False:
 value += 2
else:
 value += 4
if True or False:
 value += 8
elif True:
 value += 16
print(value)


aSeq = [-2, -1, 0, 1]
sum = aSeq[-2] + aSeq[0] + aSeq[1]
print(sum)



nested = [[''], '', 0]
print(nested[1:2])

 

aList = [-2, '-1', 0, 1, 2]
leading = aList[:2]
trailing = aList[-3:]
print(leading + trailing)



import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(7):
    if i%2 == 1:
        t.forward(100)
        t.right(90)



for i in range(7):
    if i%2 ==1:
        print(i)


def makePalindrome(aStr):
    idx = -1
    image = ""
    for i in aStr:
        image += aStr[idx]
        idx -= 1
    return aStr+image
palindrome = makePalindrome("aha")
print(palindrome)

"""

turnWest = False
turnEast = True
if turnWest:
    print('Jersey floods')
if turnEast:
    print('dodged a hurricane')
else:
    print('basements stay dry')











