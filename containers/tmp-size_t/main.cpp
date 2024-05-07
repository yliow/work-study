#include <iostream>

int main()
{
    std::cout << sizeof(size_t) << '\n';
    size_t x = -1;
    std::cout << x << '\n';

    size_t s = 10;
    int y[18446744073709551616];
    return 0;
}
