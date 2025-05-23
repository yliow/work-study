#include <iostream>
#include <queue>

int main()
{
    std::queue< int > q;
    std::cout << q.empty() << ' ' << q.size() << '\n';

    std::cout << "Putting 42, 23, 6 into the queue ... \n";
    q.push(42);
    std::cout << q.empty() << ' ' << q.size() << ' '
              << q.front() << ' ' << q.back() << '\n';
    q.push(23);
    std::cout << q.empty() << ' ' << q.size() << ' '
              << q.front() << ' ' << q.back() << '\n';
    q.push(6);
    std::cout << q.empty() << ' ' << q.size() << ' '
              << q.front() << ' ' << q.back() << '\n';

    std::cout << "changing front to 1000 ...\n";
    q.front() = 1000;
    std::cout << q.empty() << ' ' << q.size() << ' '
              << q.front() << ' ' << q.back() << '\n';
    
    std::cout << "changing back to -1000 ...\n";
    q.back() = -1000;
    std::cout << q.empty() << ' ' << q.size() << ' '
              << q.front() << ' ' << q.back() << '\n';

    std::cout << "dequeue until empty ...\n";
    while (!q.empty())
    {
        std::cout << q.empty() << ' ' << q.size() << ' '
                  << q.front() << ' ' << q.back() << '\n';
        q.pop();
    }

    std::cout << "copy constructor, operator=, operator== ...\n";
    q.push(5); q.push(3); q.push(7);
    std::queue< int > r = q;
    std::cout << (r == q) << '\n';

    while (!r.empty()) r.pop();
    r = q;
    std::cout << (r == q) << '\n';
    return 0;
}
