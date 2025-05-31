#include <iostream>
#include <vector>

std::ostream & operator<<(std::ostream & cout, const std::vector< int > & x)
{
    for (auto e: x)
    {
        cout << e << ' ';
    }
    return cout;
}

std::vector< int > swap(std::vector< int > x, int i, int j)
{
    int t = x[i];
    x[i] = x[j];
    x[j] = t;
    return x;
}
  
std::vector< int > bubblesort(std::vector< int > x, int last_index = -1)
{
    if (last_index == -1)
    {
        last_index = x.size() - 1;
    }

    if (last_index == 0)
    {
        return x;
    }
    else
    {
        // Do one pass:
        std::cout << "last index:" << last_index << '\n';
        for (int i = 0; i < last_index; ++i)
        {
            if (x[i] > x[i + 1])
            {
                x = swap(x, i, i + 1);
            }
            std::cout << i << " ... " << x << '\n';
        }
        // Recurse:
        x = bubblesort(x, last_index - 1);
        return x;
    }
}

int main()
{
    std::vector< int > x = {1, 2, 3};
    x = bubblesort(x);
    std::cout << x << '\n';
    return 0;
}
