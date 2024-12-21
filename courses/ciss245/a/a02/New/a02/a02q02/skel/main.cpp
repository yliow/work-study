// File  : main.cpp
// Author: smaug

#include <iostream>
#include "Fraction.h"

void test_Fraction_print()
{
    int xn = 0, xd = 0; // numerator and denominator of a fraction

    std::cin >> xn >> xd;
    Fraction_print(xn, xd);
    std::cout << std::endl;
}


void test_Fraction_add()
{
    int xn = 0, xd = 0; // Fraction xn/xd
    int yn = 0, yd = 0; // Fraction yn/yd
    int zn = 0, zd = 0; // Fraction zn/zd

    std::cin >> yn >> yd >> zn >> zd;
    Fraction_add(xn, xd, yn, yd, zn, zd);
    Fraction_print(xn, xd);
    std::cout << std::endl;
}


int main()
{
    int option;
    std::cin >> option:
    switch (option)
    {
        case 1:
            test_Fraction_print();
            break;
        case 2:
            test_Fraction_add();
            break;
    }
    
    return 0;
}
