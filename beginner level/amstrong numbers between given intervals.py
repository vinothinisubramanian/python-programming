a=int(input(""))
b=int(input(""))
for num in range(a+1,b):
	c=len(str(num))
	sum=0
	temp=num
	while(temp>0):
		d=temp%10
		sum+=d**c
		temp//=10
	if(num==sum):
		print(num)
