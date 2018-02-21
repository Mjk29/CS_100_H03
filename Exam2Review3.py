# 1: D
# 2: C
# 3: B
# 4: C
# 5: A
# 6: E
# 7: E
# 8: C
# 9: C
# 10: E


# ////////////////////////////////////////////
# //////////////		11A		//////////////
# ///////////////////////////////////////////

# import turtle

# t = turtle.Turtle()

# def capitalL(t,width):
# 	s = t.pos()
# 	h = t.heading()
# 	t.pd()
# 	t.fd(width)
# 	t.pu()
# 	t.goto(s)
# 	t.left(90)
# 	t.pd()
# 	t.fd(2*width)
# 	t.pu()
# 	t.goto(s)
# 	t.setheading(h)

# capitalL(t,100)



# ////////////////////////////////////////////
# //////////////		11B		//////////////
# ///////////////////////////////////////////


# def Ls(t,initWidth,multiplier,reps,angle):
# 	for i in range(reps):
# 		capitalL(t,initWidth)
# 		initWidth *= multiplier
# 		t.right(angle)


# t.left(60)
# Ls(t,20,1.5,3,20)

# ////////////////////////////////////////////
# //////////////		12		//////////////
# ///////////////////////////////////////////


# def initialDict(text):
# 	dict={}
# 	sT = text.split()
# 	for i in range(len(sT)):
# 		x = str.lower(sT[i])
# 		if x[0] in dict:
# 			dict[x[0]].append(sT[i])
# 		if x[0] not in dict:
# 			dict[x[0]] = [sT[i]]
# 	return dict

# print(initialDict('The Call of the Wild'))


# ////////////////////////////////////////////
# //////////////		13		//////////////
# ///////////////////////////////////////////



def lineStats(infile, outfile):
	inf = open(infile)
	otf = open(outfile,'w')

	for line in inf:
		words = line.split()
		c=0
		for word in line:
			if word == '\n':
				continue
			c += len(word)

		otf.write(str(len(words)))
		otf.write(' ')
		otf.write(str(c))
		otf.write('\n')

	inf.close()
	otf.close()

lineStats("file.txt", "out.txt")	