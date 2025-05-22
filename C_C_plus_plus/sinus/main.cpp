#include<iostream>
using namespace std;

double s(double);
double c(double);

double s(double x)
{
    if (x<0.001) return x;
    else return 2*s(x/2)*c(x/2);
}
double c(double x)
{
    if (x<0.001) return 1;
    else return c(x/2)*c(x/2)-s(x/2)*s(x/2);
}
int main()
{ double x;
cout << "Podaj liczbe rzeczywista: ";
cin >> x;
cout << "s(" << x << ")=" << s(x) << endl;
cout << "c(" << x << ")=" << c(x) << endl;
return 0;
}
