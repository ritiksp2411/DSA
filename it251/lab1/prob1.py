class Fraction:
	def __init__(self,num,den):
		self.num=num
		self.den=den
	def __str__(self):
		return str(self.num/self.den)
	def inverse(self):
		return self.den,self.num
	def add(self,other):
		if (self.den==other.den):
			return (self.num+other.num)/self.den
		else:
			return (self.num*other.den+self.den+other.num)/self.den*other.den
	def multiply(self,other):
		return self.num*other.num/self.den*other.den
	def equal(self,other):
		a=self.num/self.den
		b=other.num/other.den
		if (a==b):
			print('True')
		else:
			print('False')

def main():
	f1=Fraction(3,5)
	f2=Fraction(3,5)
	f1.equal(f2)
	print(f1.inverse())
	print(str(f1))


if __name__=="__main__":
	main()

