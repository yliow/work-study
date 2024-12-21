#include <iostream>
#include <limits>
#include "mystring.h"

const int MAX_BUF = 1024;


// earlier test functions


void test_str_tok()
{
    char x[MAX_BUF];
    char y[MAX_BUF];
    char delimiters[MAX_BUF] ~textred!= " ,."@;
    
    std::cin.getline(y, MAX_BUF);
    bool b = str_tok(x, y, delimiters);
    
    std::cout << b << ' ' << x << ' ' << y << std::endl;
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
        case 6:
            test_str_tok();
            break;
    }
    return 0;
}
