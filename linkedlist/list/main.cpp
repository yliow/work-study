#include <iostream>
#include <list>         // doubly-linked list

void print(std::list< int >::iterator p,
           std::list< int >::iterator q)
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
    std::list< int >::iterator p;
    std::list< int >::iterator q;

    std::cout << "1.\n";
    std::list< int > list;
    std::cout << (list.empty() ? "true" : "false") << '\n';
    std::cout << "size: " << list.size() << '\n';

    // Operations at head/front.
    list.push_front(0);
    list.push_front(1);
    list.push_back(111);
    list.push_back(222);
    print(list.begin(), list.end());

    std::cout << "2.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    list.pop_front();
    list.pop_back();
    print(list.begin(), list.end());
    
    std::cout << "3.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());        
    list.front() = 111;
    list.back() = 999;
    print(list.begin(), list.end());
    
    // erase at an iterator
    std::cout << "4.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.erase(p);
    print(list.begin(), list.end());
    p = list.end(); --p;
    print(list.begin(), list.end());
        
    // erase from one iterator to another
    std::cout << "5.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    q = list.end(); --q;
    list.erase(p, q);
    print(list.begin(), list.end());

    // insert at an iterator (i.e., just before)
    std::cout << "6.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.insert(p, 99999);
    list.insert(p, 88888);
    list.insert(p, 77777);
    print(list.begin(), list.end());

    // insert 5 copies of -1 at iterator
    std::cout << "7.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    list.insert(p, 5, -1);
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
    //  get:
    // 
    //     @---@---@---@---O---O---O---@---@  
    
    std::cout << "8.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    p = list.begin(); ++p;
    std::list< int > list1 = {77, 88, 99};
    list.insert(p, ++list1.begin(), list1.end());
    print(list.begin(), list.end());
        
    // reverse iterator
    std::cout << "9.\n";
    list = {1, 2, 3, 4};
    print(list.begin(), list.end());
    for (std::list< int >::reverse_iterator p = list.rbegin();
         p != list.rend(); ++p)
    {
        std::cout << (*p) << ' ';
    }
    std::cout << std::endl;

    return 0;
}
