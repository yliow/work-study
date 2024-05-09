#include <iostream>
#include <string>
#include <forward_list> 

void print(std::forward_list< int >::iterator p,
           std::forward_list< int >::iterator q)
{
    std::cout << '[';
    std::string delim = "";
    while (p != q)
    {
        std::cout << delim << (*p); delim = ", ";
        ++p;
    }
    std::cout << "]\n";
}


int main()
{
    std::forward_list< int >::iterator p;
    std::forward_list< int >::iterator q;
        
    std::cout << "1.\n";
    std::forward_list< int > list;
    std::cout << (list.empty() ? "true" : "false") << '\n';
    // forward_list does not have size
    std::cout << "size: " << std::distance(list.begin(), list.end())
              << '\n';

    // Operations at head/front.
    list.push_front(0);
    list.push_front(1);
    list.push_front(2);
    list.push_front(3);
    print(list.begin(), list.end()); // end() has runtime of O(n)
    list.clear();
    print(list.begin(), list.end());

    std::cout << "2.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    list.pop_front();
    print(list.begin(), list.end());

    std::cout << "3.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    list.front() = 42;
    std::cout << list.front() << '\n';
    print(list.begin(), list.end());

    // erase_after an iterator
    std::cout << "4.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.erase_after(p);
    print(list.begin(), list.end());
    
    // erase_after from one iterator to another
    std::cout << "5.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    q = list.end();
    list.erase_after(p, q);
    print(list.begin(), list.end());

    // insert_after an iterator
    std::cout << "6.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.insert_after(p, 99999);
    list.insert_after(p, 88888);
    list.insert_after(p, 77777);
    print(list.begin(), list.end());

    // insert_after 5 copies of -1 at iterator
    std::cout << "7.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.insert_after(p, 5, -1);
    print(list.begin(), list.end());

    // insert section of a list (specified by two iterators)
    // into another list at an iterator
    //
    // O---O---O---O---O---O---O---O---O---O
    //             |       |
    //             V       V
    //             ---------
    //                 V
    //     @---@---@---@---@---@
    //
    //  to get:
    // 
    //     @---@---@---@---O---O---O---@---@
    std::cout << "8.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    std::forward_list< int > list1 = {77, 88, 99};
    list.insert_after(p, ++list1.begin(), list1.end());
    print(list.begin(), list.end());

    return 0;
}
