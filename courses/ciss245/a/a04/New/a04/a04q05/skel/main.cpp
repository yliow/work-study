
#include <iostream>

int pi(double x)
{
    int * numprimes;
    // Declare pointers and allocate memory for all of them

    // Compute number of primes <= x and store at integer that
    // numprimes points to.

    int ret = numprimes;
    // Deallocate memory for all pointers declared

    return ret;
}

int main()
{
    double x;
    std::cin >> x;
    std::cout << pi(x) << '\n';
}
