import itertools

skils = [
    ["Python","Java"],
    ["C++","JavaScript"],
    ["C","Docker"]
]
# print list with [] 
print(skils)
print()
# there we have adres to sklis 
print(itertools.chain.from_iterable(skils))
print()
# thats give us a list in clear form
print(list(itertools.chain.from_iterable(skils)))
print()

from itertools import chain
# thats give us a list in clear form but we deont use iterators but only chain
print(list( chain.from_iterable(skils)))
print()


