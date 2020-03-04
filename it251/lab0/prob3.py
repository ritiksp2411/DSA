def isprime(a):
	count=0
	for i in range(1,int(a/2)+1):
		if(a%i==0):
			count=count+1
	if(count>1):
		print('Not prime')
	else:
		print('Yes')

astr=input("Enter the number to find prime or not")
a=int(astr)
isprime(a)