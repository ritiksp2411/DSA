def fact1(a):
	fact=1
	for i in range(1,a+1):
		fact=fact*i
	return fact

def fact2(a):
	if(a==1):
		return 1
	else:
		return (a*fact2(a-1))
	

astr=input("Enter the number to take factorial")
a=int(astr)
print(fact1(a))
print(fact2(a))