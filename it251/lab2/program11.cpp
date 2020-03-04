#include <iostream>
using namespace std;
class stu
{
	protected:
	string name,gender;
	int age;
	public:
	void get();
};
class stu1
{
	protected:
		int reg_no,sem;
		string branch;
	public:
		void get1();
};
class result:public stu,public stu1
{
	int total_marks,m,p,c;
	float per;
	string grade;
	public:
	void get2();
	void put();
};
void result::get2()
{
	cout<<"Enter the marks of a student in physics psc and maths:\n";
        cin>>p>>m>>c;
}	
void result::put()
{
	 cout<<"NAME:"<<name<<endl<<"GENDER:"<<gender<<endl<<"AGE:"<<age<<endl<<"REGISTER NUMBER:"<<reg_no<<endl<<"SEMESTER:"<<sem<<endl;
        cout<<"BRANCH:"<<branch<<endl;


	total_marks=m+p+c;
        per=float(total_marks/3.0);
        if(per>=90 && per<=100)
        {
                grade="AA\n";
        }
        else
        {
                if(per<90 && per>=80)
                {
                        grade="AB";
                }
                else
                {
                        if(per<80 && per>=70)
                        {
                                grade="BB";
                        }
                        else
                        {
                                if(per<70 && per>=60)
                                {
                                        grade="BC";
                                }
                                else
                                {
                                        if(per<60 && per>=50)
                                        {
                                                grade="CC";
                                        }
                                        else
                                        {
                                                if(per<50 && per>=40)
                                                {
                                                        grade="CD";
                                                }
                                                else
                                                {
                                                        grade="FF";
                                                }

                                        }
                                }
                        }
                }
        }
        cout<<"TOTAL MARKS:"<<total_marks<<endl<<"PERCENTAGE:"<<per<<endl<<"GRADE:"<<grade<<"\n";
}
void stu::get()
{
          cout<<"Enter the name of a student:\n";
          cin>>name;
          cout<<"Enter the gender of a student:\n";
          cin>>gender;
          cout<<"Enter the age of a student:\n";
          cin>>age;
}
void stu1::get1()
{
	cout<<"Enter the register number of a student:\n";
	cin>>reg_no;
	cout<<"Enter the branch of a student:\n";
	cin>>branch;
	cout<<"Enter the semester(in number) of a student:\n";
	cin>>sem;
}
int main()
{
	result r;
	r.get();
	r.get1();
	r.get2();
	r.put();
	return 0;
}
