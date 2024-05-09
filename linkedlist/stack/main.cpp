#include <iostream>
#include <list>
#include <stack>

int main()
{
    // stack using std::deque< int >
    std::stack< int > s1;

    // stack using std::list< int >
    std::stack< int, std::list< int > > s2; 

    s1.push(5); s1.push(42);
    s2.push(5); s2.push(42);

    std::cout << s1.top() << ' ' << s2.top() << '\n';
    std::cout << s1.size() << ' ' << s2.size() << '\n';
    std::cout << s1.empty() << ' ' << s2.empty() << '\n';

    s1.pop();
    s2.pop();
    
    std::cout << s1.top() << ' ' << s2.top() << '\n';
    std::cout << s1.size() << ' ' << s2.size() << '\n';
    std::cout << s1.empty() << ' ' << s2.empty() << '\n';

    return 0;
}
