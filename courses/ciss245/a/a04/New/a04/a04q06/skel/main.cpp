#include <iostream>

int opendoors(int n)
{
    bool * open;   // open[i] is true when door i is open.
    int count = 0; // This will count the number of values in the
                   // array that open points to which are true.

    // Allocate an array of n values for open to point to.
    
    // Scan (left and right) and update the array that open points to
    // a certain number of times.
    
    // Update count.

    // Deallocate the memory used by the open pointer.

    return count;
}


int main()
{
    int n;
    std::cin >> n;
    std::cout << opendoors(n) << std::endl;
    return 0;
}
