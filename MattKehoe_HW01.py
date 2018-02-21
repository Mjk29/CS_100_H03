flowers= ['rose', 'bougainvillea','yucca', 'marigold', 'daylilly',  'lilly of the valley']

print ('potato' in flowers)

thorny = flowers[:3]

poisonous = flowers[-1]

dangerous = thorny + poisonous

print (dangerous)

print (poisonous)

print ( thorny)

print ( flowers)



xpoint = [0,10,6,7]
ypoint = [0,10,6,8]
radius = 10


for i in range(0, 4):
    print (xpoint[i], ',', ypoint[i])
    print (((xpoint[i]**2)+ (ypoint[i]**2)) < radius**2)

    print (radius**2)
    i += i




string1='phone'

print (string1)

x = len(string1)


for i in range(0, x):
    string2.append = string1[i]

    print(string2)

    
    i += i




print(string1.split())

string2.reverse()

print(string2)



grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A']
rank = ['A','B','C','D','F']
frequency = []
x=len(grades)

for i in range(0, x):
    frequency.append(grades.count(rank[i]))
    i += i
"""the loop should be able to advance through the different ranks of a-f, but I cant figure out the correct syntax to do it. """
    
print(frequency)

