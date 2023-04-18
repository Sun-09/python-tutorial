name = "Sonu"
friend = "Putai"
anotherFriend = "Rahul"

# Using Escape Character '\' to write double quotes in double quotes
apple = "He said, \"I want to eat apple\""

# Using ''' to print multiple lines in python '''

apple2  = '''He said,
Hi Sonu
hey I an good
"I want to eat apple"'''

print("Hello, " + name)
print(apple)
print('')
print(apple2)

print(name[0],name[1],name[2],name[3])

# print(name[4])  #this line will give you a error...... as there is nothing in name[4]


#printing all characters in a string by for loop....

for i in apple:
    print(i)