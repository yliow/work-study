#include <iostream>
#include "DoublyLinkedListNode.h"
#include "DoublyLinkedList.h"

int main()
{
    DoublyLinkedListNode node(5);
    std::cout << node << std::endl;
    
    DoublyLinkedList xs;
    std::cout << xs << '\n';
    for (int i = 5; i < 8; ++i)
    {
        xs.insert_head(i);
        std::cout << xs << '\n';
    }

    int ret = xs.remove_head();
    std::cout << ret << std::endl;
    std::cout << xs << '\n';

    
    ret = xs.remove_head();
    std::cout << ret << std::endl;
    std::cout << xs << '\n';


    ret = xs.remove_head();
    std::cout << ret << std::endl;
    std::cout << xs << '\n';


    xs.insert_tail(1);
    std::cout << xs << '\n';
    xs.insert_tail(2);
    std::cout << xs << '\n';
    xs.insert_tail(3);
    std::cout << xs << '\n';
    xs.insert_tail(4);
    std::cout << xs << '\n';
    xs.insert_head(0);
    std::cout << xs << '\n';

    
    xs.clear();
    std::cout << xs << '\n';

    std::cout << "foo \n";

    xs.insert_tail(2);
    xs.insert_tail(3);
    xs.insert_tail(4);
    std::cout << xs << '\n';

    std::cout << xs << std::endl;
    DoublyLinkedList ys(xs);
    std::cout << "after copy constructor ..." << std::endl;
    std::cout << ys << std::endl;



    xs.insert_tail(100);
    std::cout << xs << std::endl;
    ys = xs;
    std::cout << xs << std::endl;
    std::cout << ys << std::endl;


    
    std::cout << (xs == ys) << std::endl;

    std::cout << xs << std::endl;
    DoublyLinkedListNode * p = xs.find(4);


    std::cout << p->get_data() << std::endl;

    
    p = xs.find(2);
    std::cout << p->get_data() << std::endl;

    p = xs.find(100);
    
    std::cout << p->get_data() << std::endl;

    int a = xs.remove(p);
    std::cout << a << std::endl;
    std::cout << xs << std::endl;


    p = xs.find(2);
    std::cout << p->get_data() << std::endl;


    a = xs.remove(p);
    std::cout << a << std::endl;
    std::cout << xs << std::endl;


    
    p = xs.find(4);
    std::cout << p->get_data() << std::endl;
    a = xs.remove(p);
    std::cout << a << std::endl;
    std::cout << xs << std::endl;


    
    p = xs.find(3);
    std::cout << p->get_data() << std::endl;
    a = xs.remove(p);
    std::cout << a << std::endl;
    std::cout << xs << std::endl;


    xs.clear();


    std::cout << xs << ' ' << xs.size() << '\n';
    xs.insert_tail(5);
    std::cout << xs << ' ' << xs.size() << '\n';
    xs.insert_tail(6);
    std::cout << xs << ' ' << xs.size() << '\n';
    xs.insert_tail(7);
    std::cout << xs << ' ' << xs.size() << '\n';


    //std::cout << xs[3] << std::endl;

    std::cout << xs << std::endl;
    xs[0] = 100;
    std::cout << xs << std::endl;
    xs[1] = 200;
    std::cout << xs << std::endl;
    xs[2] = 300;
    std::cout << xs << std::endl;


    
    std::cout << xs.remove_tail() << std::endl;
    std::cout << xs << std::endl;
    std::cout << xs.remove_tail() << std::endl;
    std::cout << xs << std::endl;
    std::cout << xs.remove_tail() << std::endl;
    std::cout << xs << std::endl;

    try
    {
        xs.remove_tail();
    }
    catch (ValueError & e)
    {
        std::cout << "exception\n";
    }

                                                    return 0;

    return 0;
}
