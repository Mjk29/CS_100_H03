# 1:	A
# 2:	E
# 3:	E
# 4:	D
# 5:	C
# 6:	A
# 7:	B
# 8:	E
# 9:	A
# 10:	E



# import turtle 

# def tri(t, sideLen):
# 	for i in range(3):
# 		t.fd(sideLen)
# 		t.left(120)

# def tris(t, init, incr, num, angle):
# 	for i in range(num):
# 		tri(t,init)
# 		t.left(angle)
# 		init += incr

# t = turtle.Turtle()
# # tri(t,50)
# tris(t,20,50,5,60)



# def wordsByLine(inFile, outFile):
# 	filein = open(inFile, 'r')
# 	fileout = open(outFile, 'w')
# 	for line in filein:
# 		dict = {}
# 		words = line.split()
# 		for word in words:
# 			if word not in dict:
# 				dict[word]=1
# 				continue
# 			if word in dict:
# 				dict[word]+=1
# 		print(dict)
# 	filein.close()
# 	fileout.close()


# wordsByLine('fish.txt', 'fishwords.txt')


# from collections import defaultdict

# def lineIndex(fName):
# 	linenum = 0
# 	d ={}
# 	fin = open(fName, 'r')

# 	for line in fin:
# 		words = line.split()
# 		for word in words:
# 			if word not in d:
# 				d[word]=[linenum]
# 			if linenum not in d[word]:
# 				d[word].append(linenum)
# 		linenum+=1
# 	return d

# print(lineIndex('rain.txt'))