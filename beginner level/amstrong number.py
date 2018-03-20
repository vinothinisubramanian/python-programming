a=int(input(" "))
b=len(str(a))
sum=0
temp=a
while(a>0):
	dig=a%10
	sum=sum+dig**b
	a=a//10
if(sum==temp):
	print("amstrong number")
else:
	print("not an amstrong number")
