#here we will learn about string functions such as len(),str(),.lower(),.upper()
#len() is used to get the length of a string
l1="Alligator"
l2=len(l1)
print(l2)
print(len("United kingdom"))#we can directly get the lenght of any string


#str() is used to convert any numeric value to string
num1=12345
num2=str(num1)
print("its a numeric value ",num2,"\n") #printing the string value
print("heyy its a String slicing",num2[2],"\n")#doing the slicing operation which only can be held on string

#.upper() used to convert the any case to upper case

up="i am not happy"
print(up.upper(),"\n")
#we can directly change the string to upper case without any varriable

print("just cs things".upper(),"\n")

#.lower() is used to convert any case to lower case
lo="I AM NOT HAPPY"
print(lo.lower(),"\n")
# alternative way
print("JUST CS THINGS".lower())