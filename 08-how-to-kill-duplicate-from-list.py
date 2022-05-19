skils = ["Python","Java","C++","JavaScript","C","Docker","C","Python"]
# that's deleted element from list which are more than once
# but it's not sort and every time we get in random oreder
print(list(set(skils)))
# that's give the same but with the same order 
from collections import OrderedDict
print(list(OrderedDict.fromkeys(skils).keys())) 
  

