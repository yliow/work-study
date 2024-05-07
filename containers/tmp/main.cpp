#include <vector>
#include <iostream>
#include <tuple>

int main()
{
    std::vector< int > v {1, 3, 5, 7, 9};
    auto p = v.begin();
    auto q = v.end();
    auto r = p + std::distance(p, q) / 2;
    std::cout << (*p) << ' ' << (*r) << ' ' << (*(q-1)) << '\n';

    std::pair< int , int > u = {1, 2};
    std::pair< std::pair< double, double >, double > w = {{1.1, 2.2}, 3.3};
    std::tuple< int, double, char > t = {1, 2.2, 'a'};
    return 0;
}
