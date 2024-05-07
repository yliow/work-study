#ifndef ARRAY_H
#define ARRAY_H

template < typename T >
class Array
{
public:
    void delete()
    {
    }
private:
    static const int N = 1000;
    T x[N];
    int n;
};

#endif
