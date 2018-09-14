a= input("enter the number=")
con_str = str(a)
n=len(con_str)
single = [int(x) for x in con_str]
print(single)
result = 0
for i in range(len(single)):
 	result1= result + single[i]**n
 	result= result1
print("power of the number = "+ str(result1))
if(a == str(result1)):
 	print("it is an armstrong number")
else:
 	print("it is not an armstrong number")