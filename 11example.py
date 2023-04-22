import time

# curr = time.ctime(time.time())
# print(curr)

named_tuple = time.localtime()

if(named_tuple.tm_hour > 5 and named_tuple.tm_hour<=11):
    print("Good Morning")
elif(named_tuple.tm_hour > 11 and named_tuple.tm_hour<=16):
    print("Good Noon")
elif(named_tuple.tm_hour> 16 and named_tuple.tm_hour<=19):
    print("Good Afternoon")
elif(named_tuple.tm_hour>19 and named_tuple.tm_hour<=24):
    print("Good Evening")
else:
    print("Good Night")

