#include <string>

class Hashable
{
public:
    virtual unsigned int hash() = 0;
};


class HashableString: public std::string, Hashable
{
public:
    HashableString(const std::string & s)
        : std::string(s)
    {}
    
    unsigned int hash()
    {
        unsigned int h = 0;
        unsigned int power = 1;
        for (unsigned int i = 0; i < length(); i++)
        {
            h += operator[](i) * power; power *= 10;
        }
        return h;
    }
};
