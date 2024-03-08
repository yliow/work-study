#include <iostream>
#include <string>
#include <unordered_map>
#include "Height.h"

typedef std::unordered_map<std::string, double> Height;

int main()
{
    Height h;
    h.insert({"John", 5.7});
    h.insert({"Tom", 5.8});
    h["Mary"] = 5.9;
    h["Sue"] = 6.0;

    print_buckets(h);
    print_stats(h);

    std::cout << "rehash with suggested bucket size 5\n";
    h.rehash(5);
    print_buckets(h);
    print_stats(h);

    return 0;
}