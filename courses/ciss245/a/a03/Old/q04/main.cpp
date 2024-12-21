#include <iostream>
#include <limits>
#include "mystring.h"

const int MAX_BUF = 1024;


// earlier test functions


void test_str_str()
{
    char x[MAX_BUF];
    char y[MAX_BUF];

    std::cin.getline(x, MAX_BUF);
    std::cin.getline(y, MAX_BUF);
    
    std::cout << str_str(x, y) << std::endl;
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
        case 3:
            test_str_str();
            break;
    }
    return 0;
}
