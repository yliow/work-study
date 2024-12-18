/*********************************************************************

File  : mystring.h
Author:
Date  :

The following describes how to use the mystring class.

mystring x;                    // x models the empty string ""
std::cout << x << std::endl;   // operator<< is overloaded to print
                               // mystring objects. In this case
                               // no character is printed because 
                               // x.length_ is 0

mystring y("abc");             // y is the string "abc", i.e., y.s_ is
                               // "abc"
std::cout << y << std::endl;   // abc appears in the output window

mystring z('a');               // z is the string "a", i.e., z.s_ is
                               // "a".

mystring w(10, ' ');           // w.s_ is the string "          ",
                               // i.e., a string of 10 ' '.

x += y;                        // concatenates y to x. x becomes "abc"
(x += y) += y;                 // x becomes "abcabcabc"
y += z;                        // y becomes "abca"
x = y + '?';                   // x becomes "abca?"
x = y + z;                     // x becomes "abcaa"

y[0] = 'A';                    // y becomes "Abca"

y[4] = 'z'                     // y is still "Abca" since the length_
                               // is still 4, i.e., y[4] is outside
                               // the boundary of the array.

y.resize(5);                   // y becomes "Abcaz".
y.resize(10, '$');             // y becomes "Abcaz$$$$$"
y.resize(3, '-');              // y becomes "Abc"

x = z;                         // x becomes "a".
y = "hello world";             // y becomes "hello world".

std::cout << (x == y) << std::endl;   // false, i.e., 0 is printed
std::cout << (x == "a") << std::endl; // true, i.e., 1 is printed
std::cout << (x == 'a') << std::endl; // true, i.e., 1 is printed

x = y.substr(6, 2);            // y.substr(6, 2) returns a substring
                               // of y (as a mystring object) at index
                               // 6 of length 2, i.e., x becomes
                               // "wo".
x = "hello world";
y = "world";
z = "columbia";
std::cout << x.find(y) << '\n';     // 6 is printed
std::cout << x.find(z) << '\n';     // -1 is printed
std::cout << x.find(' ') << '\n';   // 5 is printed
std::cout << x.find("ell") << '\n'; // 1 is printed

*********************************************************************/
#ifndef MYSTRING_H
#define MYSTRING_H

#include <iostream>


class mystring
{
public:
    mystring(const char x[])
        : capacity_(1024)  // NOTE: capacity is a const. You MUST initialize
                           // it with an initializer list
    {
        // Copy the relevant characters x[0], ... to s[0], ...
        // and set the length_ appropriately. For instance if x is "abc"
        // the length_ is set to 3.
    }

    mystring(char c)
    {
        // Copy c to s[0]. Set capacity_ and length_ accordingly.
    }

    mystring()  // The default constructor must initialize the object to
                // model an empty string, i.e., s_ is "".
                // 1. Do you need to set capacity to a value?
                // 2. What must you set length_ to?
    {}
    
    mystring(const mystring & x); // The copy constructor copies the
                                  // relevant characters in x.s_ to
                                  // the object being constructed.
                                  // The length_ of the object constructed
                                  // is set to the length_ of x.

    bool operator==(const mystring &); // Returns true iff the string
                                  // modeled by the object is the
                                  // same as the string modeled by
                                  // the parameter.
    bool operator!=(const mystring &);
    bool empty() const;           // Returns true iff the string modeled
                                  // is "".

    mystring & operator=(const mystring & x); // After assignment, the
                                  // (*this) == x is true.
    mystring & operator=(char c); // object becomes string of length_ 1
                                  // with the parameter as the character
                                  // at index 0.

    void clear();                 // After this, the object models "".

    char operator[](int) const;   // bracket operator to access the
    char & operator[](int);       // character of the string

    mystring & operator+=(const mystring &); // concatenation operators
    mystring & operator+=(char c);
    mystring operator+(const mystring &);
    mystring operator+(char);

    void resize(int i);           // Sets the length_ to i.
    void resize(int i, char c);   // Sets the length_ to i and if i is
                                  // greater than the original length,
                                  // then the new characters are set to c.

    int find(char c, int start = 0); // Returns the index of the first
                                  // occurrence of c in string s_. If c is
                                  // not found, -1 is returned.
                                  // Returns the index of the first
                                  // occurrence of the parameter.

    int find(const mystring & s, int start = 0); // Returns the index of the
                                  // first occurrence of s in string s_.
                                  // If s is not found, -1 is returned.
                                  // Returns the index of the first
                                  // occurrence of the parameter.

    mystring substr(int i, int len); // Return a mystring object
                                  // using the substring of s_ starting
                                  // at index i and length_ len.

private:
    const int capacity_;
    char s_[1024];
    int length_;
};

std::ostream & operator<<(std::ostream &, const mystring &);
std::istream & operator>>(std::istream &, mystring &);

bool operator== (const char[], const mystring &);

#endif
