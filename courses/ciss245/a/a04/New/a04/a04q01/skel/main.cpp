
#include <iostream>

void scanf(int *);
void scanf(char *);
void scanf(double *);

int main()
{
    char c = 0;
    int i = 0;
    double d = 0;
    scanf(&c);     // same effect as std::cin >> c
    scanf(&i);     // same effect as std::cin >> i 
    scanf(&d);     // same effect as std::cin >> d
    std::cout << c << std::endl;
    std::cout << i << std::endl;
    std::cout << d << std::endl;
    
    return 0;
}

// Implement the functions here

