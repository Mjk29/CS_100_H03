# 1: A
# 2: D
# 3: E
# 4: D
# 5: B
# 6: D
# 7: A
# 8: B
# 9: B
# 10:C



# import turtle
# t = turtle.Turtle()

# def midline(t,length):
# 	t.pd()
# 	t.back(length/2)
# 	t.fd(length)
# 	t.bk(length/2)

# # midline(t,100)

# def starburst(t,num,init, delta, angle):
# 	for i in range(num):
# 		midline(t,init)
# 		t.left(angle)
# 		init *= delta

# t.left(45)
# starburst(t,7,50,1.2,20)





# def mostFrequent(inFile, outFile):
# 	inf = open(inFile)
# 	ouf = open(outFile, 'w')
# 	for line in inf:
# 		letter = ''
# 		num = 0
# 		for char in line:
# 			if char == ' ':
# 				continue
# 			if line.count(char) > num:
# 				letter = char
# 				num = line.count(char)
# 			if line.count(char) == num:
# 				if char in letter:
# 					continue
# 				letter += char
# 		ouf.write(str(letter+'\n'))
# 	inf.close()
# 	ouf.close()


# mostFrequent('moreYouKnow.txt', 'out.txt')



# def longEnough(s, threshold):
# 	if len(s)>= threshold:
# 		return True
# 	else:
# 		return False


# # print(longEnough('ass',4))


# def longWords(t, i):
# 	dict = {}
# 	words = t.split()
# 	for word in words:
# 		if longEnough(word,i):
# 			if word in dict:
# 				dict[word] +=1
# 			if word not in dict:
# 				dict[word] = 1
# 	return dict


# text = 'one fish two fish red fish blue fish'
# print(longWords(text, 4))
# # {'blue': 1, 'fish': 4}