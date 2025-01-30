#include <iostream>

int f(int x)
{
    return x * x;
}

int g(int f(int))
{
    return f(3);
}

int main()
{
    std::cout << g(f) << '\n';
    return 0;
}
