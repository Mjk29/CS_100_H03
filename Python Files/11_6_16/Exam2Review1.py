# 1: A
# 2: B
# 3: B
# 4: D
# 5: D
# 6: C
# 7: D
# 8: E
# 9: B
# 10: E


# ////////////////////////////////////////////
# //////////////		11A		//////////////
# ///////////////////////////////////////////


# import turtle

# def cup(t, sidelength):
# 	s = t.pos()
# 	h = t.heading()
# 	t.pd()

# 	for i in range(3):
# 		t.fd(sidelength)
# 		t.left(90)

# 	t.pu()
# 	t.setpos(s)
# 	t.setheading(h)

# t = turtle.Turtle()	
# # cup(t,100)



# ////////////////////////////////////////////
# //////////////		11B		//////////////
# ///////////////////////////////////////////


# def cups(t,init,incr,reps):
# 	for i in range(reps):
# 		cup(t,init)
# 		init += incr
# 		t.right(90)
# 		t.fd(incr/2)
# 		t.left(90)

# cups(t,50,30,4)


# ////////////////////////////////////////////
# //////////////		12		//////////////
# ///////////////////////////////////////////


# def uniqueWords(infile,outfile):
# 	inf = open(infile)
# 	ouf = open(outfile,'w')
# 	uqL=[]

# 	for line in inf:
# 		words = line.split()
# 		for word in words:
# 			if word not in uqL:
# 				uqL.append(word)
# 			else: 
# 				continue

# 		ouf.write(str(len(uqL)))
# 		ouf.write('\n')
# 		uqL.clear()
		
# uniqueWords("turn.txt", "Qout.txt")


# ////////////////////////////////////////////
# //////////////		12		//////////////
# ///////////////////////////////////////////



# def importantWords(s, threshold):
# 	words = s.split()
# 	impWord={}
# 	for word in words:
# 		if len(word) >= threshold:
# 			if word in impWord:
# 				impWord[word] +=1
# 			else:
# 				impWord[word]=1
# 	print(impWord)




# lyric = '''a time to build up a time to break down
# a time to dance a time to mourn'''

# print(importantWords(lyric, 4))
