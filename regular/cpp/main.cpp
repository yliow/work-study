#include <iostream>
#include <unordered_set>
#include <set>

template < typename T >
class Set
{
public:
    void insert(const T & x) { xs.insert(x); ys.insert(x); }
    void erase(const T & x) { xs.erase(x); ys.erase(x); }
    bool has(const T & x) const { return ys.find(x) != ys.end(); }
    std::set< T > xs;
    std::unordered_set< T > ys;
};

int main()
{
    std::unordered_set< char > S;
    S.insert('a');
    S.insert('b');
    S.insert('c');
    S.insert('d');

    for (auto x: S)
    {
        std::cout << x << ' '; 
    }
    std::cout << '\n';

    std::set< char > S1;
    S1.insert('a');
    S1.insert('b');
    S1.insert('c');
    S1.insert('d');

    for (auto x: S1)
    {
        std::cout << x << ' '; 
    }
    std::cout << '\n';

    {
        Set< char > S;
        S.insert('a'); S.insert('b');
    }
    return 0;
}
