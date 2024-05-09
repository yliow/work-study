#include <iostream>
#include <list>
#include <queue>

int main()
{
    // queue using std::deque< int >
    std::queue< int > q1;

    // stack using std::list< int >
    std::queue< int, std::list< int > > q2; 

    q1.push(5); q1.push(42);
    q2.push(5); q2.push(42);

    std::cout << q1.front() << ' ' << q2.front() << '\n';
    std::cout << q1.back() << ' ' << q2.back() << '\n';
    std::cout << q1.size() << ' ' << q2.size() << '\n';
    std::cout << q1.empty() << ' ' << q2.empty() << '\n';

    q1.pop();
    q2.pop();
    
    std::cout << q1.front() << ' ' << q2.front() << '\n';
    std::cout << q1.back() << ' ' << q2.back() << '\n';
    std::cout << q1.size() << ' ' << q2.size() << '\n';
    std::cout << q1.empty() << ' ' << q2.empty() << '\n';
    
    return 0;
}
