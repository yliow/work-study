#include <iostream>
#include <vector>

class node
{
    char f;
    node * c[26];
};

int main()
{
    std::cout << sizeof(node) << '\n';
    return 0;
}
