// File: main.cpp

#include <iostream>
#include "Rational.h"


void test_input()
{
    Rational r;
    std::cin >> r;
    std::cout << r.get_n() << ' ' << r.get_d() << std::endl;
}


void test_output()
{
    int n = 0, d = 0;
    std::cin >> n >> d;
    std::cout << Rational(n, d) << std::endl;
}


void test_reduce_method()
{
    Rational r;
    std::cin >> r;
    r.reduce();
    std::cout << r << std::endl;
}


void test_reduce_function()
{
    Rational r;
    std::cin >> r;
    reduce(r); 
    std::cout << r << std::endl;
}


void test_abs_method()
{
    Rational r;
    std::cin >> r;
    std::cout << r.abs() << std::endl;
}


void test_abs_function()
{
    Rational r;
    std::cin >> r;
    std::cout << abs(r) << std::endl;
}


void test_eq()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 == r2) << std::endl;
}


void test_ne()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 != r2) << std::endl;
}


void test_gt()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 > r2) << std::endl;
}


void test_ge()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 >= r2) << std::endl;
}


void test_lt()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 < r2) << std::endl;
}


void test_le()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 <= r2) << std::endl;
}


void test_pluseq()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 += r2);
    std::cout << ' ' << r1 << std::endl;
}


void test_minuseq()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 -= r2);
    std::cout << ' ' << r1 << std::endl;
}


void test_multeq()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 *= r2);
    std::cout << ' ' << r1 << std::endl;
}


void test_diveq()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 /= r2);
    std::cout << ' ' << r1 << std::endl;
}


void test_positive()
{
    Rational r1;
    std::cin >> r1;
    std::cout << (+r1) << std::endl;
}


void test_negative()
{
    Rational r1;
    std::cin >> r1;
    std::cout << (-r1) << std::endl;
}


void test_plus()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 + r2) << std::endl;
}


void test_minus()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 - r2) << std::endl;
}


void test_mult()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 * r2) << std::endl;
}


void test_div()
{
    Rational r1, r2;
    std::cin >> r1 >> r2;
    std::cout << (r1 / r2) << std::endl;
}


void test_int()
{
    Rational r;
    std::cin >> r;
    std::cout << r.get_int() << std::endl;
}


void test_double()
{
    Rational r;
    std::cin >> r;
    std::cout << r.get_double() << std::endl;
}


void test_int_eq()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i == r) << std::endl;
}


void test_int_ne()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i != r) << std::endl;
}


void test_int_ne()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i != r) << std::endl;
}


void test_int_gt()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i > r) << std::endl;
}


void test_int_ge()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i >= r) << std::endl;
}


void test_int_lt()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i < r) << std::endl;
}


void test_int_le()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i <= r) << std::endl;
}


void test_int_pluseq()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i += r);
    std::cout << ' ' << i << std::endl;
}


void test_int_minuseq()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i -= r);
    std::cout << ' ' << i << std::endl;
}


void test_int_multeq()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i *= r);
    std::cout << ' ' << i << std::endl;
}


void test_int_diveq()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i /= r);
    std::cout << ' ' << i << std::endl;
}


void test_int_plus()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i + r) << std::endl;
}


void test_int_minus()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i - r) << std::endl;
}


void test_int_mult()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i * r) << std::endl;
}


void test_int_div()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << (i / r) << std::endl;
}


void test_pow_function()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << pow(r, i) << std::endl;
}


void test_pow_method()
{
    int i;
    Rational r;
    std::cin >> i >> r;
    std::cout << r.pow(i) << std::endl;
}


int main()
{
    int option = 0;
    std::cin >> option;

    switch (option)
    {
        case 1:
            test_input();
            break;
        case 2:
            test_output();
            break;
        case 3:
            test_reduce_method();
            break;
        case 4:
            test_reduce_function();
            break;
        case 5:
            test_abs_method();
            break;
        case 6:
            test_abs_function();
            break;
        case 7:
            test_eq();
            break;
        case 8:
            test_ne();
            break;
        case 9:
            test_gt();
            break;
        case 10:
            test_ge();
            break;
        case 11:
            test_lt();
            break;
        case 12:
            test_le();
            break;
        case 13:
            test_pluseq();
            break;
        case 14:
            test_minuseq();
            break;
        case 15:
            test_multeq();
            break;
        case 16:
            test_diveq();
            break;
        case 17:
            test_positive();
            break;
        case 18:
            test_negative();
            break;
        case 19:
            test_plus();
            break;
        case 20:
            test_minus();
            break;
        case 21:
            test_mult();
            break;
        case 22:
            test_div();
            break;
        case 23:
            test_int();
            break;
        case 24:
            test_double();
            break;
        case 25:
            test_int_eq();
            break;
        case 26:
            test_int_ne();
            break;
        case 27:
            test_int_gt();
            break;
        case 28:
            test_int_ge();
            break;
        case 29:
            test_int_lt();
            break;
        case 30:
            test_int_le();
            break;
        case 31:
            test_int_pluseq();
            break;
        case 32:
            test_int_minuseq();
            break;
        case 33:
            test_int_multeq();
            break;
        case 34:
            test_int_diveq();
            break;
        case 35:
            test_int_plus();
            break;
        case 36:
            test_int_minus();
            break;
        case 37:
            test_int_mult();
            break;
        case 38:
            test_int_div();
            break;
        case 39:
            test_pow_function();
            break;
        case 40:
            test_pow_method();
            break;
    }

    return 0;
}
