# STRINGS ARE IMMUTABLE

a = "SonuBera"

print(a.upper())  # to uppercase
print(a.lower())  # to lowercase

#stripping special character

b = "!!HelloUser!!!!!!!"
print(b.rstrip("!"))  #strips '!' at end

print(b.replace("Hello", "Welcome"))


c = "Hello Bhai Let's eat apple"
print(c.split(" "))

# Capitalizing first letter in python 

d = "introduction tO pythoN"
print(d.capitalize())

d = d.capitalize()

print(d.count('n'))  #count's the number of n

print(d.endswith("i", 4, 10))

print(d.find('o')) #gives index of 'o'
print(d.find('k')) #gives -1 if there is no k


str1 = "Welcometotheconsole590"
print(str1.isalnum())   #Checks if the string is alphanumerical or not
print(str1.isalpha())   #Checks if the string is alphabetic or not


str1 = "            "
print(str1.isspace())   #check's if there is any such space
str1 = ""
print(str1.isspace())

str1 ="World Health Organization"  #check if the string is title or not?
print(str1.istitle())

str1 ="To kill the evil"  
print(str1.istitle())

str1 = "Python is a Interpretated Language"
print(str1.swapcase())  #Swap's the cases of string


str1 = "the titanic"
print(str1.title())  #Makes the string as a title


