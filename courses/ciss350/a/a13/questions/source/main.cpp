#include <iostream>
#include <vector>
#include <list>

//=============================================================================
// hash(std::string) -> unsigned int is a simple hash function for std::string
// objects.
//
// WARNING: Remmeber to mod by the size of your table!
//=============================================================================
unsigned int hash(const std::string & s)
{
    unsigned int h = 0;
    unsigned int power = 1;
    for (unsigned int i = 0; i < s.length(); i++)
    {
        h += int(s[i]) * power;
        power *= 10;
    }
    return h;
}


//=============================================================================
// Each record in the hash table is a (key, value) pair of type (std::string,
// double).
//=============================================================================
class HTRow
{
public:
    // TODO
private:
    std::string key_;
    double value_;
};


//=============================================================================
// This exception class is used to throw an exception in the event that a key
// is not found in the hash table during a search or a remove.
//=============================================================================
class KeyError
{};


//=============================================================================
// Hashtable of (key, value) of type (std::string, double).
// 
// When the percentage of get collisions is > threshold, the hashtable
// resizes by doubling its size. See num_gets_, num_gets_collisions_,
// and threshood_.
//
// The number of get() invocation is stored in _num_gets and the number
// of get collisions is stored in _num_get_collisions. The threshold for
// resize is stored in _threshold. A get collision is accessing a (key,
// value) pair that is not what you want. Therefore if you hash to a linked
// linked of three nodes and the node you really want is the last, then
// there are two collisions.
//=============================================================================
class HT
{
public:
    
    // The instance variable table is initialized to a vector of linked list
    // of HTRows objects. The size of the table is the given size.
    // When the percentage collision for get() operations is greater than
    // threshold, the table doubles its size.
    // 
    // num_gets_ and num_get_collisions_ must be initialized to 0.
    // The default threshold is 0.75.
    HT(int size=10, double threshold=0.75)
    {}

    // 1. Search for record with key_ matching key
    // 2. If the record is found, modify value_ to value
    // 3. If the record is not found, insert a new record
    void set(std::string key, double value)
    {
    }

    // 1. Search for record with key_ matching key
    // 2. If the record is found, return the value
    // 3. If the record is not found, KeyError is thrown
    double get(const std::string & key)
    {
    }

    // 1. Removes record with key_ matching key
    // 2. If record is not found, KeyError is thrown
    void remove(const std::string & key)
    {
    }

    // Clear all entries in all linked lists.
    void clear()
    {
    }

    // Returns a std::vector<std::string> of keys
    std::vector<std::string> keys()
    {}
    
    // Resizes the hashtable
    void resize(int size)
    {
        // Resize the table (you need to recreate the hashtable structure.
        // Remember to reset num_gets_ and num_get_collisions_ to 0.
    }

private:
    std::vector< std::list< HTRow > > table_;

    int num_get_collisions_; // Records number of collisions in get()
    int num_gets_;           // Records number of get()
    double threshold_;       // If num_get_collisions_/num_gets_ > threshold
                             // (when num_gets_ > 0) the table must resize
};


std::ostream & operator<<(std::ostream & cout, const HT & d)
{
    // TODO
    return cout;
}

int main()
{
    HT d0;     // 10 linked lists (i.e. 10 buckets)
    HT d1(20); // 20 linked lists (i.e. 20 buckets)

    d0.set("John", 5.2); 
    std::cout << d0 << std::endl; // prints {John:5.2} 

    // Add more test cases to test your class.
    
    return 0;
}
