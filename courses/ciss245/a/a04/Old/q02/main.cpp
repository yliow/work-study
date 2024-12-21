
#include <iostream>

// version of vec2d_add that uses references
void vec2d_add(int & x0, int & y0, 
               int x1, int y1,
               int x2, int y2)
{
    x0 = x1 + x2;
    y0 = y1 + y2;
}


// version of vec2d_add that uses pointers
void vec2d_add(int * x0, int * y0, 
               int x1, int y1,
               int x2, int y2)
{
    // TO BE COMPLETED.
}


void vec2d_println(int x, int y)
{
    std::cout << '<' << x << ", " << y << ">\n";
}


int main()
{
    int x0 = 0, y0 = 0, x1, y1, x2, y2;
    std::cin >> x1 >> y1 >> x2 >> y2;

    int old_x0 = x0, old_y0 = y0;

    vec2d_add(x0, y0, x1, y1, x2, y2);
    vec2d_println(x0, y0);

    x0 = old_x0;
    y0 = old_y0;

    vec2d_add(&x0, &y0, x1, y1, x2, y2);
    vec2d_println(x0, y0);

    return 0;
}

