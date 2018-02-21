#########################################################################
#############					Problem 1					#############
#########################################################################

def twoWords(length, firstLetter):
	
	Lenword = ""
	while  True:
		print("Enter a %s letter word" %length)
		Lenword = input()
		if len(Lenword) == length:
			break

	Chword = " "	
	while True :
		print("Enter a word that begins with %s" %firstLetter)
		Chword = input()
		if(Chword[0] == firstLetter):
			break


	return Lenword, Chword
	
print(twoWords(4, 'b'))

# #########################################################################
# #############					Problem 2					#############
# #########################################################################


def twoWords2(length, firstLetter):
	
	Lenword = ""
	while len(Lenword) != length:
		print("Enter a %s letter word" %length)
		Lenword = input()

	Chword = " "	
	while Chword[0] != firstLetter:
		print("Enter a word that begins with %s" %firstLetter)
		Chword = input()

	return Lenword, Chword
	
print(twoWords2(4, 'b'))


# #########################################################################
# ############# 				Problem 5.29					#############
# #########################################################################

Namelist = ['Gerber, Len', 'Fox, Kate', 'Dunn, Bob'] 

def lastfirst(nList):
	SpList = [i.split(', ') for i in nList]
	firstN = []
	lastN = []

	for i in SpList:
		firstN.append(i[0])
		lastN.append(i[1])

	print(lastN, firstN)


lastfirst(Namelist)

# #########################################################################
# ############# 				Problem 5.33					#############
# #########################################################################
import math

def mystery(num):
	count = 0
	while math.trunc(num) != 1:
		num = num/2
		count += 1
	print(count)

mystery(25)

#########################################################################
############# 				Problem 5						#############
#########################################################################

def enterNewPassword():
	password=[]
	while True:
		password = input("enter a password ")
		
		if len(password) < 8:
			print("Password is too short")
		
		if len(password) > 15:
			print("Password is too long")
			
		if any(char.isdigit() for char in password) is False:
			print("Password must have a digit")
		
		else:
			return password

enterNewPassword()







































# i = 0
# for x in SpList:
# 	if (i%2 == 0):
# 		firstN + x[i]
# 	# if (i%2 == 1)
# 		# lastN + x
# 	i=+1
		
# print(SpList)




# newL = [i.split(', ') for i in list]

# for i in newL:
# 	# print(i[1])
# 	i[0],i[1] = i[1],i[0]
# print(newL)


# sList = [i.split(',', 0)[0] for i in list]
# s2List = [i.split(',', 2)[0] for i in list]

# list[0].split( )
# print(sList)
# print(s2List)



	# newL[x][0], newL[x][1] = newL[x][1], newL[x][0] 
	# x=+1


# for x in list:
# 	print(x)

# print(newL)
# def lastfirst(list):
# 	list[0]