#include <iostream>
#include <cmath>
#include "LongInt.h"

typedef LongInt Z; // see note on typedef

int main()
{
    {
        Z z;
        std::cout << "Testing constructor: You should see 0\n" << z << '\n';
    }
    {
        std::cout << "Testing constructor: You should see -20 -19 ... 19 20\n"; 
        for (int i = -20; i <= 20; i++)
        {
            Z z(i);
            std::cout << z << ' ';
        }
        std::cout << '\n';
    }
    {
        std::cout << "Testing LongInt(char []) ...\n";
        if (Z("0") != Z(0)) std::cout << "fail for \"0\"\n";
        if (Z("1") != Z(1)) std::cout << "fail for \"1\"\n";
        if (Z("-1") != Z(-1)) std::cout << "fail for \"-1\"\n";
        if (Z("54321") != Z(54321)) std::cout << "fail for \"54321\"\n";
        if (Z("-54321") != Z(-54321)) std::cout << "fail for \"-54321\"\n";        
    }
    {
        std::cout << "Testing == and != ... " << std::endl;
        for (int i = -1000; i < 1000; i++)
        {
            for (int j = -1000; j < 1000; j++)
            {
                LongInt I(i), J(j);
                if ((i == j) != (I == J))
                {
                    std::cout << "== error for i:"
                              << i << ", " << "j:" << j << std::endl;
                }
                if ((i != j) != (I != J))
                {
                    std::cout << "!= error for i:"
                              << i << ", " << "j:" << j << std::endl;
                }
            }
        }
    }

    {
        std::cout << "Testing < ...\n";
        for (int i = -1000; i < 1000; i++)
        {
            for (int j = -1000; j < 1000; j++)
            {
                if (
                    ((i < j) != (Z(i) < Z(j))) &&
                    ((i < j) != (Z(i) < j)) &&
                    ((i < j) != (i < Z(j)))
                    )
                {
                    std::cout << "< error for " << i << ' ' << j << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing += and + ...\n";
        for (int i = -1000; i < 1000; i++)
        {
            for (int j = -1000; j < 1000; j++)
            {
                LongInt I(i), J(j);
                LongInt a = (I += J);
                LongInt b = LongInt(i) + LongInt(j);
                if ((i + j) != a || I != (i + j))
                {
                    std::cout << "+= error for ";
                    std::cout << i << ' ' << j << '\n';
                }
                if ((i + j) != b)
                {
                    std::cout << "+ error for ";
                    std::cout << i << ' ' << j << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing -= and - ...\n";
        for (int i = -1000; i < 1000; i++)
        {
            for (int j = -1000; j < 1000; j++)
            {
                LongInt I(i), J(j);
                LongInt a = (I -= J);
                LongInt b = LongInt(i) - LongInt(j);
                if ((i - j) != a || (i - j) != I)
                {
                    std::cout << "-= error for " << i << ' ' << j << '\n';
                }
                if ((i - j) != b)
                {
                    std::cout << "- error for " << i << ' ' << j << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing multeq_tenpower ...\n";
        for (int i = -1000; i < 1000; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                LongInt a(i);
                a.multeq_tenpower(j);
                if (i * int(pow(10, j)) != a)
                {
                    std::cout << i << ' ' << j << ' ' << a << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing multeq_digit ...\n"; 
        for (int i = -10000; i < 10000; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                LongInt a(i);
                a.multeq_digit(j);
                if (i * j != a)
                {
                    std::cout << "error for " << i << ' ' << j << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing *= and * ...\n";
        for (int i = -10000; i < 10000; i++)
        {
            for (int j = -10000; j < 10000; j++)
            {
                LongInt a(i);
                LongInt b(j);
                LongInt c = a * b;
                a *= b;
                if (i * j != a)
                {
                    std::cout << "error for *= for " << i << ' ' << j << '\n';
                }
                if (i * j != c)
                {
                    std::cout << "error for * for " << i << ' ' << j << '\n';
                }
            }
        }
    }

    {
        std::cout << "Testing pre ++ ...\n";
        for (int i = -1000000; i < 1000000; i++)
        {
            LongInt a(i);
            if (i + 1 != (++a))
            {
                std::cout << "error for " << i << '\n';
            }
        }
    }

    {
        std::cout << "Testing post ++ ...\n";
        for (int i = -1000000; i < 1000000; i++)
        {
            LongInt I(i);
            LongInt c = (I++);
            if (i != c || i + 1 != I)
            {
                std::cout << "error for " << i << '\n';
            }
        }
    }


    {
        std::cout << "Testing / and % ...\n";
        int i,j;
        for (j = 1; j < 1000000; j++)
        {
            for (i = 1; i < 1000000; i++)
            {
                if (i % 1000 == 0)
                    std::cout << "i:" << i << "  j:" << j << std::endl;
                LongInt a(i), b(j);
                LongInt q = a / b, r = a % b;
                if (i / j != q)
                {
                    std::cout << "/ error for "
                              << i << ' ' << j << std::endl;
                    return 0;
                }
                if (i % j != r)
                {
                    std::cout << "% error in "
                              << i << ' ' << j << std::endl;
                    return 0;

                }
            }
        }
    }
    
    return 0;
}
