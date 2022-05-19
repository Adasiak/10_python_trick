from collections import Counter

names =['Ania', 'kasia','basia','mateusz ','karol','kacper','wiktor','Maja','Maja','wikor']

counter = Counter(names)
print(counter) 
print()
# conwersion to dicionary
# .most_common() sort dicionary from element present more to element which is sort
print(dict(counter.most_common()))
print()
# print the most frequent element in dicionary
print(dict(counter.most_common(1)))
print()
# 2 most frequent element
print(dict(counter.most_common(1)))
print()
# 
