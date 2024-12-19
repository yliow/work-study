#include <iostream>
#include "Fib1.h"
#include "Fib2.h"
#include "Fib3.h"
#include "Fib4.h"

int main()
{
    int correct[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    ... test code for Fib1 ...
    ... test code for Fib2 ...
    ... test code for Fib3 ...

    std::cout << "Testing Fib4:" << std::endl;
    Fib4 fib4;
    std::cout << "Test 1 " << (Fib4::lookup(2) == -1 ? "pass" : "FAIL")
              << std::endl;

    for (int i = 0; i < 10; ++i)
    {
        std::cout << "Test " << i + 2 << ' '
                  << (fib4(i) == correct[i] ? "pass" : "FAIL")
                  << std::endl;
    }
    std::cout << "Test 12 "
              << (Fib4::lookup(2) == 2 ? "pass" : "FAIL") << std::endl;

    Fib4 fib4b(30);
    std::cout << "Test 13 "
              << (Fib4::lookup(2) == 2 ? "pass" : "FAIL") << std::endl;
    std::cout << "Test 14 "
              << (Fib4::lookup(25) == -1 ? "pass" : "FAIL") << std::endl;

    return 0;
}
