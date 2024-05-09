#include <iostream>
#include "SinglyLinkedListNode.h"
#include "SinglyLinkedList.h"

std::ostream & operator<<(std::ostream & cout, 
                          const SinglyLinkedList & list)
{
    cout << '[';
    SinglyLinkedListNode * p = list.get_head();
    while (p != NULL)
    {
        cout << p->get_data();
        SinglyLinkedListNode * next = p->get_next();
        if (next != NULL)
        {
            cout << ", ";
        }
        p = next;
    }
    cout << ']';
    return cout;
}

