#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

std::ostream & operator<<(std::ostream & cout, 
                          const std::vector< int > & v)
{
    std::string sep = "";
    cout << '{';
    for (auto & x: v)
    {
        cout << sep << x;
        sep = ", ";
    }
    cout << '}';
    return cout;
}

int main()
{
    std::vector< int > v {5,3,0,1,2,6,7,4};
    std::cout << v << '\n';

    // Default is maxheap
    std::make_heap(v.begin(), v.end());
    std::cout << "maxheap: " << v << '\n';

    // Use std::greater to get a minheap
    std::make_heap(v.begin(), v.end(), std::greater< int >());
    std::cout << "minheap: " << v << '\n';

    // Make maxheap
    std::make_heap(v.begin(), v.end());
    std::cout << "maxheap: " << v << '\n';
    
    // Insert: push_back and push_heap
    std::cout << "insert 99\n";
    v.push_back(99);
    std::cout << "maxheap: " << v << '\n';
    std::push_heap(v.begin(), v.end());
    std::cout << "maxheap: " << v << '\n';

    // Extract root: pop_heap and pop_back
    std::cout << "extract-root\n";
    std::pop_heap(v.begin(), v.end());
    std::cout << "maxheap: " << v << '\n';
    v.pop_back();
    std::cout << "maxheap: " << v << '\n';

    // Heapsort
    std::sort_heap(v.begin(), v.end());
    std::cout << "heapsorted: " << v << '\n';
    
    return 0;
}