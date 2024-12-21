#include <iostream>
#include <limits>
#include "mystring.h"

const int MAX_BUF = 1024;


// earlier test functions


void test_str_lower()
{
    char x[MAX_BUF];
    char y[MAX_BUF];

    std::cin.getline(y, MAX_BUF);
    str_lower(x, y);
    
    std::cout << x << std::endl;
    return;
}


int main()
{
    int i = 0;
    std::cin >> i;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    switch (i)
    {
        // earlier cases
        case 5:
            test_str_lower();
            break;
    }
    return 0;
}
