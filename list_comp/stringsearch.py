#setting the variable txt to a string
txt = " Hello, welcome CIT 30900  "

x = txt.find("309")
print(x)

x = txt.find('405')
print(x)

x= txt.find("e", 5, 10)
print(x)

x=txt.replace('e', '')
print(x)
print(len(x))
