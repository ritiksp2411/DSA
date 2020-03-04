def fibbo1(a):
	fact1=0
	fact2=1
	print(fact1)
	print(fact2)
	for i in range(2,a):
		fact=fact1+fact2
		fact1=fact2
		fact2=fact
		print(fact)

def fibbo2(a):
	if(a==1):
		return 0
	elif(a==2):
		return 1
	else:
		return (fibbo2(a-2)+fibbo2(a-1))
	

astr=input("Enter the number to take fibbonacci series")
a=int(astr)
fibbo1(a)
print(fibbo2(a))