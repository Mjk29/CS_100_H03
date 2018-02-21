def vowelCount(string):
	ret=''
	vowel = 'aeiou'
	st=string.lower()
	for letter in (st):
		if letter in vowel:
			ret += letter
	return len(ret)

string = 'I am the walrus'
print(vowelCount(string))