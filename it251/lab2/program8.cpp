#include<iostream.h>
using namespace std;
classb s
{
	int r,i;
	public:
	s()
	{
	r=0;
	i=0;

	}

	s operator++();
	c operator--();
	void get();
	void puts()
	void  pit();
	};
	void s::get()
	{
	cout<<"enter the real and inamnumber"<<endl;
	cin>>r>>i;

	}
	void s::put()
	{
	cout<<"after increasing"<<endl;
	cout<<r<<"+"<<"i"<<i<<endl;
	}
	void s::puts()
	{
	cout<<"after decreasing:\n";
	cout<<r<<"="<<"j"<<i<<endl;

	}
	s s::operator++()
	{
	s c;
	c.r=r+1;
	c.i=i;
	return c;

	}
	s s::operator--()
	{
	s.c;
	c.r=r+1;
	c.i=i;
	}
	void main()
	s a;
	a.get();
	a.operator++();
	a.put();
	a.operator--();
	a.puts();

	}
}