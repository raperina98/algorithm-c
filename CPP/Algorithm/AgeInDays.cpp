/*
    Read an integer value corresponding to a person's age (in days) and print it in years, months and days, 
    followed by its respective message "ano(s)", "mes(es)", "dia(s)"
*/

#include <iostream>
 
using namespace std;
 
int main() {
  
    int days, year, month;
    
    cin >> days;
    
    year = days/365;
    
    month = (days % 365) / 30;
    
    days = (days % 365) % 30;
    
    cout << year << " ano(s)" << endl;
    cout << month << " mes(es)"<< endl;
    cout << days << " dia(s)"<< endl;
 
    return 0;
}
