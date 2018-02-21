
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A']
rank = ['A','B','C','D','F']
frequency = []
x=len(grades)

for i in range(0, x):
    frequency.append(grades.count(rank[i]))
    i += i
"""the loop should be able to advance through the different ranks of a-f, but I cant figure out the correct syntax to do it. """
    
print(frequency)

