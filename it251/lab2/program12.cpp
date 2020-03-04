#include <iostream>
using namespace std;
class student
{
        string name,gender,branch;
        int reg_no,sem,age;
        public:
        void get();
        void put();
};
class result:public student
{
        int total_marks,m,p,c;
        float per;
        string grade;
        public:
        void res();
        void res1();
};
void student::get()
{
        cout<<"Enter the student name:\n";
        cin>>name;
        cout<<"Gender of the student:\n";
        cin>>gender;
        cout<<"Enter age of a student:\n";
        cin>>age;
        cout<<"Enter the branch of a student:\n";
        cin>>branch;
        cout<<"Enter register number of a student:\n";
        cin>>reg_no;
        cout<<"Enter the semester(in number) in which student is studying:\n";
        cin>>sem;
};
void student::put()
{
        cout<<"Entered details are:\n";
        cout<<"NAME:"<<name<<endl<<"GENDER:"<<gender<<endl<<"AGE:"<<age<<endl<<"REGISTER NUMBER:"<<reg_no<<endl<<"SEMESTER:"<<sem<<endl;
        cout<<"BRANCH:"<<branch<<endl;
}
void result::res()
{
        cout<<"Enter the marks in physics, psc and maths:\n";
        cin>>p>>c>>m;
}
void result::res1()
{
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
int main()
{
        result r;
        r.get();
        r.res();
        r.put();
        r.res1();
        return 0;
}

