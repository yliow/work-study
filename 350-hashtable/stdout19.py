s = r'''#ifndef HEIGHT_H
#define HEIGHT_H

#include <iostream>
#include <string>
#include <unordered_map>

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
void print_buckets(T & h)
{
    std::cout << "(key, value) pairs in buckets of h ...\n"; 
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

template < typename T >
void print_stats(const T & h)
{
    std::cout << "size/buckets/load factor/max load factor:"
              << h.size() << '/'
              << h.bucket_count() << '/'
              << h.load_factor() << '/'
              << h.max_load_factor() << '\n';
}

#endif

'''
f = open('Height.h', 'w')
f.write(s)
f.close()
