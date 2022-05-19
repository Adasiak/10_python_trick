from email.policy import strict


numbers = [1,2,3,4]
letters = ['a','b','c','d','e']

# zip function combine list numerators and letters and print them together, 
# is conntinue to end valuee od one of this list

for number,letter in zip(numbers,letters, strict==True):
    print(number,letter)
     
print()
# zip_longest function combine list numerators and letters and print them together,
# is conntinue over one of the list was end. if thats 
# happend zip_longest get none to them

from itertools import zip_longest

numbers = [1,2,3,4]
letters = ['a','b','c','d','e']

for number,letter in zip_longest(numbers,letters):
    print(number,letter)
# python show we error because list not have the same long 
for number,letter in zip(numbers,letters, strict==True):
    print(number,letter)
     