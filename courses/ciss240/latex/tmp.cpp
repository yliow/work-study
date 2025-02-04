
#include <iostream>

class C
{
public:
    int m(int x)
    {
        return x * x;
    }
    static int * fptr(int);
};

int C::*fptr = &C::m;
int g(int f(int))
{
    return f(3);
}

int main()
{
    C obj;
    std::cout << g(obj.m) << '\n';
    return 0;
}
