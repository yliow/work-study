#include <iostream>
#include <functional>

int main()
{
    std::hash< int > h0;
    std::cout << h0(42) << '\n';
    // or
    std::cout << std::hash< int >()(42) << '\n';
    
    std::hash< double > h1;
    std::cout << h1(3.14) << '\n';
    // or
    std::cout << std::hash< double >()(3.14) << '\n';
    
    std::hash< char > h2;
    std::cout << h2('a') << '\n';
    
    std::hash< std::string > h3;
    std::cout << h3("hello world") << '\n';

    std::hash< bool > h4;
    std::cout << h4(true) << '\n';
    
    return 0;
}
