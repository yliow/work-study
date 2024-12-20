/*********************************************************************

File  : mystring.cpp
Author:
Date  :

*********************************************************************/

#include <iostream>
#include "mystring.h"

std::ostream & operator<<(std::ostream & cout, const mystring & x)
{
       // Get the length of x, say you store it in local variable len.
       // Print the string in x, i.e., x.s[0], ..., x.s[len - 1].
       // Finally, return the reference cout.
}

std::istream & operator>>(std::istream & cin, mystring & x)
{
       // Get a string from the user, say you store it in local character
       // array t of size 1024. (use cin and t.)
       // Copy t[i], ... to x.s[i] starting with i = 0;. Stop when t[i] is 
       // '\0'. Set the length of x accordingly.
       // Finally, return the reference cin.
       //
       // To minimize code duplication, it's easier to do the following:
       // 1. Clear x (see the method mystring::clear())
       // 2. Perform += to add the string in t to x (i.e., to x.s).
}
