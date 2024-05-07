#include <iostream>
#include <vector>

typedef std::pair< double, double > twodouble;
typedef std::vector< twodouble > twodoubles;

std::ostream & operator<<(std::ostream & cout, const twodouble & x)
{
    cout << '(' << x.first << ", " << x.second << ')';
    return cout;
}

std::ostream & operator<<(std::ostream & cout, const twodoubles & v)
{
    cout << '{';
    std::string delim = "";
    for (auto & x: v)
    {
        cout << delim << x;
        delim = ", ";
    }
    cout << '}';
    return cout;
}

int main()
{
    twodoubles v = {{0.0, 0.1}, {0.2, 0.3}, {0.4, 0.5}};
    std::cout << v << '\n';

    v = {{1.1, 2.2}};
    std::cout << v << '\n';

    std::cout << (twodoubles {{0.0, 0.1}, {0.2, 0.3}, {0.4, 0.5}}) << '\n';

    return 0;
}