#include <iostream>

int main()
{
    int x[8] = {2, 3, 5, 7, 11, 13, 17, 19};
    int * left = &x[0];
    int * right = &x[8];
    int * mid = left + (right - left) / 2; // you cannot do (left + right)/2 !!!
    std::ptrdiff_t diff = right - left;
    std::cout << left << ' ' << mid << ' ' << right << '\n';
    std::cout << (unsigned long long) left << ' '
              << (unsigned long long) mid << ' '
              << (unsigned long long) right << '\n'; 
    std::cout << *left << ' ' << *mid << ' ' << *right << '\n';
    return 0;
}
