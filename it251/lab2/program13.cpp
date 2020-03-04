

#include<iostream>
using namespace std;

int main() {

    int x, y, res;
    int ch;

    cout << "Enter 1 For Addition :";
    cout << "\nEnter 2 For Subtraction :";
    cout << "\nEnter 3 For Multiplication :";
    cout << "\nEnter 4 For Division :";
    cout << "\nEnter 5 For Modulus :";
    cin >> ch;

    switch (ch) {
        case 1:
        {
            cout << "\nEnter Two Numbers :";
            cin >> x >> y;

            res = x + y;

            cout << "\nResult is :" << res;
            break;
        }
        case 2:
        {
            cout << "\nEnter Two Numbers :";
            cin >> x >> y;

            res = x - y;

            cout << "\nResult is :" << res;
            break;
        }
        case 3:
        {
            cout << "\nEnter Two Numbers :";
            cin >> x >> y;

            res = x * y;

            cout << "\nResult is :" << res;
            break;
        }
        case 4:
        {
            cout << "\nEnter Two Numbers :";
            cin >> x >> y;

            res = x / y;

            cout << "\nResult is :" << res;
            break;
        }
    
    }

    return 0;
cout<<"enter the y for yes for asking further calculationfor no calculation press no"<<endl;
cin>>chr;
if(chr=='y')
{
    goto main();
}
}

