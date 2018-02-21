# 1:	A
# 2:	
# 3:	
# 4:	
# 5:	
# 6:	
# 7:	
# 8:	
# 9:	
# 10:	



def testString(aString):
	aDict = {}
	for letter in aString:
		num = aString.count(letter)
		if num not in aDict:
			aDict[num] = letter
		else:
			return num
	return -1
text = 'eager'
print(testString(text))
