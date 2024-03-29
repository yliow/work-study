s = r'''
#include <iostream>
#include <queue> // for std::priority_queue
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
    std::priority_queue< int > pq {5,3,0,1,2,6,7,4};
    std::cout << pq << '\n';

    // Default is maxheap
    std::cout << "pq: " << pq << '\n';
    std::cout << "size: " << pq.size() << '\n';
    pq.push(99);
    std::cout << "after push(99): " << pq << '\n';
    std::cout << "top: " << pq.top() << '\n';
    pq.pop();
    std::cout << "after pop: " << pq << '\n';
    
    return 0;
}
'''.strip()
print(r'''
\begin{Verbatim}[frame=single, fontsize=\small]
%s
\end{Verbatim}
''' % s)
from latextool_basic import *
f = open("priqueue.cpp", "w")
f.write(s)
f.close()
print(r'{\footnotesize %s}' % shell('g++ priqueue.cpp; ./a.out'))
