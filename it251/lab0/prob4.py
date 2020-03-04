a=int(input("Enter the numer of elements"))
print("Enter the elemnts")
list=[]
for i in range(0,a):
	x=int(input())
	list.append(x)

for j in range(0,a):
	for k in range(0,a-j-1):
		if(list[k]>list[k+1]):
			temp=list[k]
			list[k]=list[k+1]
			list[k+1]=temp

print(list)