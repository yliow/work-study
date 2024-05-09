from latextool_basic import *

s = r'''#include <iostream>
#include <cstddef>

class SLNode
{
public:
    SLNode(int key, SLNode * next = NULL)
      : key_(key), next_(next)
    {}
    int key() const
    {
        return key_;
    }
    SLNode * next() const
    {
        return next_;
    }
    void set_next(SLNode * next)
    {
        next_ = next;
    }
    
private:
    int key_;
    SLNode * next_;
};


std::ostream & operator<<(std::ostream & cout,
                          const SLNode & node)
{
    cout << "<SLNode " << &node
         << " key:" << node.key()
         << ", next:" << node.next()
         << '>';
    return cout;
}

void print(SLNode * p)
{
    if (p != NULL)
    {
        std::cout << (*p) << std::endl;
        print(p->next());
    }
}

void insert_head(SLNode ** phead, int i)
{
    *phead = new SLNode(i, *phead);
}

int main()
{
    SLNode * phead = NULL;
    insert_head(&phead, 5);
    insert_head(&phead, 4);
    insert_head(&phead, 6);
    insert_head(&phead, 2);
    print(phead);
    return 0;
}
'''
f = open('tmp12345678.cpp', 'w')
f.write(s)
f.close()
import os
t = r'''
...
int main()
{
    SLNode * phead = NULL;
    insert_head(&phead, 5);
    insert_head(&phead, 4);
    insert_head(&phead, 6);
    insert_head(&phead, 2);
    print(phead);
    
    return 0;
}
''' 
print(console(t.strip()))
print("The output is this:")
print(shell('g++ tmp12345678.cpp; ./a.out'))
