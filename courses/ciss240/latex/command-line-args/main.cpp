#include <iostream>
#include <fstream>

int main(int argc, char ** argv)
{
    char x[100];
    std::istream & f1 = std::cin;
    std::ifstream f("input.txt", std::ifstream::in);

    std::istream * f2 = &f;

    //f1 >> x;
    //std::cout << x << '\n';
    f2->getline(x, 100);
    std::cout << '[' << x << ']' << '\n';
    
    return 0;
}
