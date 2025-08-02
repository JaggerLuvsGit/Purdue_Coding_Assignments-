import re 
text = ' Welcome, to CIT 30900'

# remove all non numbers 
shownumbers= re.sub(r'\D', '', text)
print(shownumbers)

# remove all numbers 
showletters = re.sub(r'\d', '', text)
print(showletters)


#remove all non numbers and alpha 
showletters = re.sub(r'\W', '', text)
print(showletters)

#REMOVE ALL NUMBERS IN ALPHA
showletters = re.sub(r'\w', '', text)
print(showletters)
