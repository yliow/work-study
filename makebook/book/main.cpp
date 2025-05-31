#include <iostream>
#include <cstdlib>
#include <sys/time.h>
#include <sys/resource.h>

int doors(int n)
{
    bool * open = new bool[n];
    for (int i = 1; i < n; ++i)
    {
        if (i % 2 == 1) // open, left-to-right
        {
            //std::cout << "open ";
            for (int j = 0; j < n; j += i)
            {
                open[j] = true;
                //std::cout << j << ' ';
            }
            //std::cout << '\n';
        }
        else // close, right-to-left
        {
            //std::cout << "close ";
            for (int j = n - 1; j >= 0; j -= i)
            {
                open[j] = false;
                //std::cout << j << ' ';
            }
            //std::cout << '\n';
        }
    }
    int s = 0;
    for (int i = 0; i < n; ++i)
    {
        if (open[i]) ++s;
    }
    delete [] open;
    return s;
}

int doors2(int n)
{
    if (n % 2 == 0)
    {
        return 2 + (n - 2)/2 + (n - 1)/2 - n/4;
    }
    else
    {
        int s = (n - 1)/2;
        // std::cout << "    s:" << s << '\n';
        for (int k = 2 * (n - 1)/3; k <= n - 2; ++k)
        {
            int k0 = k;
            if (k0 % 2 == 0)
            {
                // std::cout << "    0 k:" << k << " k0:" << k0 << '\n';
                k0 /= 2;
                // std::cout << "    1 k:" << k << " k0:" << k0 << '\n';
                while (k0 % 2 == 0)
                {
                    k0 /= 2;
                    // std::cout << "    2 k:" << k << " k0:" << k0 << '\n';
                }
                // std::cout << "    3 k:" << k << " k0:" << k0 << '\n';
                if (k0 > n - 1 - k)
                {
                    // std::cout << "    4 k:" << k << " k0:" << k0 << '\n';
                    ++s;
                }
                else
                {
                    // std::cout << "    5 k:" << k << " k0:" << k0 << '\n';
                }
            }
        }
        return s;
    }
}

void test()
{
    std::cout << "test" << std::endl;
    for (int n = 1000000; n <= 10000000; ++n)
    {
        std::cout << n << ". " << std::flush;
        int a = doors(n);
        std::cout << a << ' ' << std::flush;
        int b = doors2(n);
        std::cout << b << ' '
                  << (a != b ? "FAIL" : "pass")
                  << ' '
                  << double(a) / n * 100 << '%'
                  << std::endl;
        if (a != b) throw 1;
    }
}

void time(int argc, char ** argv)
{
    int start = atoi(argv[1]);
    int end = atoi(argv[2]);
    int step = atoi(argv[3]);
    int numtimes = atoi(argv[4]);
    
    for (int n = start; n <= end; n += step)
    {
        rusage start, end;
        getrusage(RUSAGE_SELF, &start);
        for (int i = 0; i < numtimes; ++i)
        {
            doors(n);
        }
        getrusage(RUSAGE_SELF, &end);
        double endtime = end.ru_utime.tv_sec + end.ru_utime.tv_usec * 1e-6;
        double starttime = start.ru_utime.tv_sec + start.ru_utime.tv_usec * 1e-6;
        double diff = (endtime - starttime) / numtimes;
        std::cout << '(' << n << ',' << diff << ")," << std::endl;
    }

}

int main(int argc, char ** argv)
{
    test();
    //time(argc, argv);
    return 0;
}
