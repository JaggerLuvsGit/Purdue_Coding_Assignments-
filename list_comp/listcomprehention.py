numbers = [1,2,3,4,5]
newlist = []
# for any number in the ' numbers' square it and put it in new list. 
for x in numbers:
    newlist.append(x**2)
print(newlist)

# the list above and below are the same  function with = output 

newlist = [x**2 for x in numbers]
print(newlist)
# must use this this for ^ type of function for assignment two for list comprehention! 
newlist2 = [x for x in numbers if x%2 ==0]
print(newlist2)

# video for this within course brightspace 