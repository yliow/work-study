#include <iostream>

void filter(int x[], int n)
{
    int * p;
    // Allocate an integer array of size n for p to point to.

    // Compute the weighted average values of x and store in the array
    // that p points to.

    // Copy the values in the array that p points to into
    // the values of array x.

    // Deallocate the memory used by p.
    
    return; 
}


int main()
{
    int x[1024];
    
    int n = 0;
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> x[i];
    }
    filter(x, n);
    for (int i = 0; i < n; ++i)
    {
        std::cout << x[i] << ' ';
    }
    std::cout << '\n';
    
    return 0;
}


