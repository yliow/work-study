#include <iostream>
#include <sys/time.h>
#include <sys/resource.h>


int main()
{    
    rusage start, end;
    
    getrusage(RUSAGE_SELF, &start);

    for (unsigned long int i = 0; i < 1000000000; i++)
    {
        double t = 3.14;
        t * t * t;
    }

    getrusage(RUSAGE_SELF, &end);

    double endtime = end.ru_utime.tv_sec
                     + end.ru_utime.tv_usec * 1e-6;
    double starttime = start.ru_utime.tv_sec
                       + start.ru_utime.tv_usec * 1e-6;
    double diff = endtime - starttime; 
    std::cout << diff << "secs \n";

    return 0;
}
