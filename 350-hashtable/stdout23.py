s = r'''
#include <iostream>
#include <functional> // for std::hash
#include <unordered_map>
#include "vec2d.h"

template <>
struct std::hash< vec2d >
{
    size_t operator()(const vec2d & v) const
    {
        return std::hash< double >{}(v.x() + v.y()) ; // bad hash!
    };
};

typedef std::unordered_map< vec2d, double > temperature;

int main()
{
    temperature h;
    h[vec2d(1.1, 2.2)] = 5.9;
    return 0;
}
'''.strip()
f = open('main.cpp', 'w')
f.write(s)
f.close()
from latextool_basic import *
