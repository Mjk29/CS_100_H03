def getInitials(response):
	first=input("whats your first name?",)
	last= input("whats your last name?",)
	print(response, first, last)
	return first[0]+last[0]

init =getInitials("Thank you")
print(init)