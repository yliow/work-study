#include <iostream>
#include <deque>

int main()
{
    std::deque< int > dq;

    dq.push_front(1);
    dq.push_front(2);
    std::cout << dq.front() << ' ' << dq.back() << '\n';

    dq.push_back(100);
    dq.push_back(101);    
    std::cout << dq.front() << ' ' << dq.back() << '\n';

    dq.pop_front(); dq.pop_back();
    std::cout << dq.front() << ' ' << dq.back() << '\n';
    
    std::cout << dq.size() << ' ' << dq.empty() << '\n';
    
    return 0;
}
