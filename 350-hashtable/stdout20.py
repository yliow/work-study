s = r'''
#include <iostream>
#include <string>
#include <functional> // for std::hash

int main()
{
    std::hash< int > h0;
    std::cout << "hash of\n";
    std::cout << "42: " << h0(42) << '\n';
    // or
    std::cout << "42: " << std::hash< int >()(42) << '\n';

    std::cout << "-1: " << std::hash< int >()(-1) << '\n'
              << "3.14: " << std::hash< double >()(3.14) << '\n'
              << "0.0: " << std::hash< double >()(2.0) << '\n'   
              << "'a': " << std::hash< char >()('a') << '\n'
              << "true: " << std::hash< bool >()(true) << '\n'
              << "\"hello world\": "
              << std::hash< std::string >()("hello world") << '\n';
    return 0;
}
'''.strip()
f = open('main.cpp', 'w'); f.write(s); f.close()
#import os
#os.system('rm stdout.txt; g++ main.cpp; ./a.out > stdout.txt')
