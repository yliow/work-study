s = r'''
#include <iostream>
#include <string>
#include <unordered_map>

// Height is hashtable with key = std::string, value = double
typedef std::unordered_map<std::string, double> Height;

template < typename T >
void print(const T & h)
{
    std::cout << "(key, value) pairs in h ...\n"; // iterating
                                     // over all entries
    for (typename T::const_iterator p = h.begin();
         p != h.end(); ++p)
    {
        std::cout << p->first << ": " << p->second
                  << " ... "
                  << '\n';
    }
}

template < typename T >
void print_buckets(const T & h)
{
    std::cout << "(key, value) pairs in buckets of h ..."; 
    for (unsigned int i = 0; i < h.bucket_count(); ++i)
                                     // iterating over all
                                     // buckets
    {
        std::cout << "bucket " << i << ": ";
        for (typename T::const_local_iterator p = h.begin(i);
             p != h.end(i); ++p)
        {
            std::cout << '['
                      << p->first << ": " << p->second
                      << "] ";
        }
        std::cout << '\n';
    }
}
  
void print_stats(Height & h)
{
    std::cout << "size/buckets/load factor/max load factor:"
              << h.size() << '/'
              << h.bucket_count() << '/'
              << h.load_factor() << '/'
              << h.max_load_factor() << '\n';
}

int main()
{
    Height h;
    h.insert({"John", 5.7});         // insert operation
    h.insert({"Tom", 5.8});
    h["Mary"] = 5.9;
    h["Sue"] = 6.0;
    h["Jane"] = 6.1;
    h["Priscilla"] = 6.1;
    h["Sheila"] = 6.1;
    h["Ashley"] = 6.1;
    
    h.erase("Tom");                  // delete operation
    
    std::cout << h["John"] << '\n';  // find key and get value
    h["John"] = 6.2;                 // update by key with new
                                     // value
    std::cout << h["John"] << '\n';
    
    Height::iterator p = h.find("Mary"); // find by key and
                                     // get iterator
    std::cout << (p != h.end() ? "found" : "not found")
              << '\n';
    print(h);
    print_buckets(h);
    print_stats(h);

    std::cout << "increase size to 641 ...\n"; // changing the
                                     // size
    h.reserve(641);
    print_stats(h);

    std::cout << "clear ...\n";           
    h.clear();                       // clear the map
    print_stats(h);

    std::cout << "constructor with size 1000...\n";
    Height h1(1000);                 // reserve size of
                                     // approx 1000
    print_stats(h);
    
    return 0;
}
'''.strip()
f = open('main23.cpp', 'w')
f.write(s)
f.close()
from latextool_basic import *
os.system('g++ main23.cpp -std=c++11')
os.system('./a.out > out23.txt')
