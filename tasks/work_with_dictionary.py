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


## add two dict in one
a = {1: 3, 3: 5, 4: 6, 2: 8, 0: 7}
b = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

c = {**a, **b}  # Об'єднання словників

print(c)

'''
Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
'''

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
res=sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True)[:3]
print(res)
