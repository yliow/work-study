#include <iostream>
#include "Fib1.h"
#include "Fib2.h"
#include "Fib3.h"
#include "Fib4.h"
#include "Fib5.h"
#include "Math.h"

int main()
{
    int correct[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    ... test code for Fib1 ...
    ... test code for Fib2 ...
    ... test code for Fib3 ...
    ... test code for Fib4 ...
    ... test code for Fib5 ...

    std::cout << "Testing fib:" << std::endl;
    for (int i = 0; i < 10; ++i)
    {
        std::cout << "Test " << i + 1 << ' '
                  << (fib(i) == correct[i] ? "pass" : "FAIL")
                  << std::endl;
    }

    return 0;
}
