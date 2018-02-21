# 1: C
# 2: C
# 3: A
# 4: D
# 5: D
# 6: C
# 7: D
# 8: C
# 9: E
# 10: B


# ///////////////////////////////////
#//////////////// 11 ////////////////
# //////////////////////////////////

# import turtle 
# def halfSquare(t, length):
# 	t.pd()
# 	t.fd(length)
# 	t.left(90)
# 	t.fd(length)
# 	t.left(90)

# t = turtle.Turtle()
# # halfSquare(t,100)

# def halfSquares(t, initial, increment, reps):
# 	for i in range(reps):
# 		print(i)
# 		halfSquare(t, initial)
# 		initial += increment

# halfSquares(t,20,20,10)

# ///////////////////////////////////
#//////////////// 12 ////////////////
# //////////////////////////////////



# def wordCount(infile, outfile):
# 	i = open(infile)
# 	o = open(outfile, 'w')
# 	lCount = 0
# 	tCount = 0	
# 	for line in i:
# 		text = line.split()
# 		for word in text:
# 			lCount+= 1
# 		o.write(str(lCount) + '\n')
# 		tCount += lCount
# 		lCount = 0
# 	i.close()
# 	o.close()	

# wordCount("seuss.txt", "outfile.txt"),'\n'


# ///////////////////////////////////
#//////////////// 13 ////////////////
# //////////////////////////////////




# def initialVowels(inFile):
# 	vowel = ['a','e','i','o','u']
# 	vowels = "aeiou"
# 	V = {'a':'','e':'','i':'','o':'','u':''}
# 	# V = {'a':None,'e':None,'i':None,'o':None,'u':None}

# 	i = open(inFile)
# 	for line in i:
# 		tokens = line.lower().split()
# 		for word in tokens:
# 			if word[0] in V:
# 				V[word[0]] +=word +' '	
# 	return V

# V = initialVowels("seuss.txt")
# for c in V.keys():
# 		if len(V[c]) != 0:
# 			print('{',c,'[', V[c],']','}')