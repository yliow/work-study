#include <iostream>


// Swaps the values *p, *q
void swap(int * p, int * q)
{
    int t;
}


// Performs bubblesort from *begin to one int before *end.
// For swapping, you should use the above swap function.
void bubblesort(int * begin, int * end)
{
    int * p;
    int * q;
}


// Prints array from *begin to one int before *end. The print format is
// {1, 4, -2, 42}.
void println(int * begin, int * end)
{
    int * p;
    // TO BE COMPLETED
    std::cout << '\n';
}


int main()
{
    int x[1024];
    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> x[i];
    }
    println(&x[0], &x[n]);
    
    bubblesort(&x[0], &x[n]);
    println(&x[0], &x[n]);
    
    return 0;
}
