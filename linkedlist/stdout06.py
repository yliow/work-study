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
    void set_next(SLNode * next0)
    {
        next_ = next0;
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

int main()
{
    SLNode n5(5, NULL);
    SLNode n4(4, NULL);
    SLNode n6(6, NULL);
    SLNode n2(2, NULL);

    n2.set_next(&n6);
    n6.set_next(&n4);
    n4.set_next(&n5);

    SLNode * phead = &n2;
    /*
    std::cout << n2 << '\n';
    std::cout << n6 << '\n';
    std::cout << n4 << '\n';
    std::cout << n5 << '\n';
    */

    SLNode * p = phead;
    while (p != NULL)
    {
        std::cout << (*p) << std::endl;
        p = p->next();
    }
    
    return 0;
}
'''
f = open('tmp12345678.cpp', 'w')
f.write(s)
f.close()

t = '''
SLNode * p = phead;
while (p != NULL)
{
    std::cout << (*p) << std::endl;
    p = p->next();
}
'''
print(console(t.strip()) + "\n" + "and the output is this:")
print(shell('g++ tmp12345678.cpp; ./a.out', fontsize=r'\footnotesize'))
