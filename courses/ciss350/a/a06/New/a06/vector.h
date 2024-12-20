// File: vector.h

template < typename T >
class vector
{
public:
    class iterator;
    class const_iterator;
    
    class iterator
    {
    public:
        iterator(T * const p)
        : p_(p)
        {}
                
        const iterator & operator++()
        {}
        
        const iterator operator++(int)
        {}

        const T & operator*() const
        {}
        
        T & operator*()
        {}

        // This is used by const_iterator(const iterator &)
        T * p() const
        {
            return p_;
        }
    private:
        T * p_;
    };
    
    class const_iterator
    {
    public:
        const_iterator(T * p)
        {}

        const_iterator(const iterator & p)
            : p_(p.p())
        {}
        
        const_iterator & operator++()
        {}
        
        void operator++(int)
        {}
        
        const T & operator*() const
        {}

    private:
        T * p_;    
    };
    
    vector(int size, int val)
        : capacity_(2 * size), size(size_), (p_(new T[size])
    {
        for (int i = 0; i < size; ++i)
        {
            p[i] = val;
        }
    }
    
    ~vector()
    {}

    // TODO: copy constructor
    // TODO: assignment operator
    
    iterator begin()
    {
        // TODO: return iterator object that points to p_[0];
    }
    
    const_iterator begin() const
    {
        // TODO: return const_iterator object that points to p_[0];
    }

    iterator end()
    {
        // TODO: return iterator object that points to p_[size_];
    }

    const_iterator end() const
    {
        // TODO: return const_iterator object that points to p_[size_];
    }

    const T & operator[](int i) const
    {
        return p_[i];
    }
    
    T & operator[](int i)
    {
        return p_[i];
    }
    
private:
    int capacity_;
    int size_;
    T * p_;
};
