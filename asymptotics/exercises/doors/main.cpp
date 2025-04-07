#include <iostream>
#include <string>
#include <sys/time.h>
#include <sys/resource.h>

int main(int argc, char ** argv)
{
    int n = atoi(argv[1]);
    std::cout << n << ' ' << n + 1 << '\n';
    
    return 0;
}
