#include <iostream>
#include "Fib1.h"
#include "Fib2.h"
#include "Fib3.h"

int main()
{
    int correct[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    ... test code for Fib1 ...
    ... test code for Fib2 ...
    
    std::cout << "Testing Fib3:" << std::endl;
    Fib3 fib3;
    std::cout << "Test 1 " << (Fib3::lookup(2) == -1 ? "pass" : "FAIL")
              << std::endl;

    for (int i = 0; i < 10; ++i)
    {
        std::cout << "Test " << i + 2 << ' '
                  << (fib3(i) == correct[i] ? "pass" : "FAIL")
                  << std::endl;
    }
      
    std::cout << "Test 12 "
              << (Fib3::lookup(2) == 2 ? "pass" : "FAIL") << std::endl;
    
    return 0;
}
