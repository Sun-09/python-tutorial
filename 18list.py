# PYTHON LISTS


l = [1, 7, 9]
print(l, type(l), l[0], l[1], l[2])

l.append("sonu")   #To enter a new element in a list in last position

print(l, type(l), l[1], l[2], l[3])

print(len(l), l[-1])  # To print the length of list


if "sonu" in l:
    print("yes")

# For printing all elements in List

for i in l:
    print(i,end=':')

l.append(True)
l.append(False)
print('')
print(l[1:5:2])

lst = [i*i for i in range(7)]
print(lst)