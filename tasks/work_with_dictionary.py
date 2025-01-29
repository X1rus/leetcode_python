import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

for x in d.values():
    print(x)

#sort by value increase
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)

#sort by value decrease
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)