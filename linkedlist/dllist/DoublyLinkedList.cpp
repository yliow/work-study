#include <iostream>
#include "DoublyLinkedListNode.h"
#include "DoublyLinkedList.h"

std::ostream & operator<<(std::ostream & cout, 
                          const DoublyLinkedList & list)
{
    cout << '[';
    DoublyLinkedListNode * p = list.get_head();
    while (p != list.get_tail_sentinel())
    {
        cout << p->get_data();
        if (p != list.get_tail()) 
        {
            cout << ", ";
        }
        p = p->get_next();
    }
    
    cout << ']';
    return cout;
}

