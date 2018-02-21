# 1:	B
# 2:	A
# 3:	A
# 4:	D
# 5:	D
# 6:	E
# 7:	D
# 8:	C
# 9:	C
# 10:	D



# import turtle

# t = turtle.Turtle()

# def capT(turt,height):
# 	t.pd()
# 	t.fd(height)
# 	t.left(90)
# 	t.fd(height/2)
# 	t.bk(height)
# 	t.fd(height/2)
# 	t.right(90)
# 	t.bk(height)
# 	t.pu()

# # capT(t,100)

# def tRow(t,num,init,ratio):
# 	for i in range(num):
# 		capT(t,init)
# 		t.right(90)
# 		t.fd(init/2)
# 		init *= ratio
# 		t.fd(init/2)
# 		t.left(90)

# t.left(90)
# tRow(t,3,40,1.5)

# import string
# def fileStats(inFile,outFile):
# 	charNum =0
# 	wordNum =0
# 	lineNum =0
# 	digitNum =0
# 	punctNum =0

# 	inf = open(inFile)
# 	ouf = open(outFile,'w')

# 	for line in inf:
# 		lineNum +=1
# 		for char in line:
# 			charNum+=1
# 			if char in string.punctuation:
# 				punctNum+=1
# 			if char.isdigit():
# 				digitNum +=1
# 		words=line.split()
# 		for word in words:
# 			wordNum +=1

# 	ouf.write("characters"+str(charNum)+'\n')
# 	ouf.write("words"+str(wordNum)+'\n')
# 	ouf.write("lines"+str(lineNum)+'\n')
# 	ouf.write("digits"+str(digitNum)+'\n')
# 	ouf.write("punctuation"+str(punctNum)+'\n')


# 	inf.close()
# 	ouf.close()

# fileStats('fileStats.txt','out.txt')


# import string

# def symmetry(text):
# 	d = {}
# 	words = text.split()
# 	for word in words:
# 		word = word.lower()
# 		if word[0] == word[-1]:
# 			if word in d:
# 				d[word[0]] +=1
# 			else:
# 				d[word[0]]=1



# 	return d


# t = '''The sun did not shine it was too wet to play
# so we sat in the house all that cold cold wet day
# I sat there with Sally we sat there we two and I 
# said how I wish we had something to do'''

# print(symmetry(t))