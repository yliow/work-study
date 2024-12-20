class < typename T >
class Set
{
public:

    // Adds x to d is x is not in d.
    void insert(const T & x)
    {}

    // Removes x from d if x is in d. Otherwise KeyError is thrown.
    void remove(const T & x)
    {}

    // Returns true if x is in d
    bool has_element(const T & x) const
    {}

    // Returns true if each value in d is also in set.d
    bool issubset(const Set< T > & set) const
    {}

    // Same as issubset
    bool operator<=(const Set< T > & set) const
    {}

    // Returns true if each value in set.d is also in d
    bool issuperset(const Set< T > & set) const
    {}

    // Same as issuperset
    bool operator>=(const Set< T > & set) const
    {}

    // Returns true if *this and set contains the same values
    bool operator==(const Set< T > & set) const
    {}

private:
    HT< T, char > d;
};

// If set contains "a", "b", print as {a, b}
template < typename T >
std::ostream & operator<<(std::stream & cout, const Set< T > set)
{}
