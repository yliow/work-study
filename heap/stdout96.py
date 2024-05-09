s = r'''
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

void println(int v[], int size)
{
    std::string delim = "";
    std::cout << '{';
    for (int i = 0; i < size; ++i)
    {
        std::cout << delim << v[i];
        delim = ", ";
    }
    std::cout << "}\n";
}

int main()
{
    int x[] = {5,3,0,1,2,6,7,4};
    println(x, 8);
    std::make_heap(x, x + 8);
    println(x, 8);
    return 0;
}
'''.strip()

print(r'''
\begin{Verbatim}[frame=single, fontsize=\small]
%s
\end{Verbatim}
''' % s)

from latextool_basic import *
f = open("heapsort2.cpp", "w")
f.write(s)
f.close()
print(shell(['g++ heapsort2.cpp -std=c++11', './a.out']))
#print(shell('./a.out'))
