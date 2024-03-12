s = r'''
#include <iostream>
#include <string>
#include <unordered_map>
#include "Height.h"

class Hash // or use a struct
{
public:
    unsigned int operator()(const std::string & s) const
    {
        return 3; // a very bad hash function
    }
};

typedef std::unordered_map<std::string, double, Hash> Height;

int main()
{
    Height h;
    h.insert({"John", 5.7});
    h.insert({"Tom", 5.8});
    h["Mary"] = 5.9;
    h["Sue"] = 6.0;

    print(h);
    print_buckets(h);
    print_stats(h);
              
    return 0;
}
'''.strip()
f = open('main.cpp', 'w')
f.write(s)
f.close()
from latextool_basic import *
import os
os.system('rm a.out; rm out.txt; g++ main.cpp -std=c++11; ./a.out > out.txt')
