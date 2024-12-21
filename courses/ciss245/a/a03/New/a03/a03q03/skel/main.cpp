#include <iostream>
#include <limits>
#include "mystring.h"

const int MAX_BUF = 1024;


void test_str_cmp()
{
    // earlier test function
}


void test_str_cpy()
{
    // earlier test function
}


void test_str_chr()
{
    char x[MAX_BUF];
    char c;

    std::cin.getline(x, MAX_BUF);
    std::cin >> c;
    
    std::cout << str_chr(x, c) << std::endl;
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
        case 2:
            test_str_chr();
            break;
    }
    return 0;
}
