#include <iostream>

class Hashable
{
public:
    virtual unsigned int hash(unsigned int s) = 0;
};


class Name
{
public:
    Name(const std::string & s)
        : _s(s)
    {}
private:
    std::string _s;
};

class HashableName: public Name, Hashable
{
public:
    HashableName(const std::string s)
        : Name(s) 
    {}
    
    unsigned int hash(unsigned int s)
    {
        unsigned int h = 0;
        //... compute h using _s...
        return h % s;
    }
};

class X
{
public:
};

class Row
{
public:
    int key;
    int value;
};
std::ostream & operator<<(std::ostream & cout, const Row & r)
{
    cout << "<Row key:" << r.key
         << ", value:" << r.value
         << ">";
    return cout;
}

class HT
{
public:
    HT()
    {
        for (int i = 0; i < 10; i++)
        {
            array[i].key = -1;
            array[i].value = -1;            
        }
    }
    int & operator[](int i)
    {
        array[i].key = i;
        return array[i].value;
    }
    Row array[10];
};

std::ostream & operator<<(std::ostream & cout, const HT & h)
{
    cout << "<HT\n";
    for (int i = 0; i < 10; i++)
    {
        cout << "    " << h.array[i] << '\n';
    }
    return cout;
}

int main()
{
    HashableName x("hello world");
    std::cout << x.hash(10) << '\n';

    HT h;
    std::cout << h << '\n';
    h[5] = 42;
    std::cout << h << '\n';
    std::cout << h[5] << '\n';
}
