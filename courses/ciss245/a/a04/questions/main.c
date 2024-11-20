#include <cstdio>
#include <iostream>

int main()
{
    char c = ' ';
    int i = 0;
    double d = 0;
    
    scanf("%c", &c);  // char input for c
    scanf("%d", &i);  // int input for n
    scanf("%lf", &d); // double input for d
//    std::cout << c << ' ' << i << ' ' << d << '\n';

    printf("%c %d %lf\n", c, i, d);
    
    return 0;
}
