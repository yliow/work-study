#include <iostream>
#include "DoublyLinkedListNode.h"

std::ostream & operator<<(std::ostream & cout,
                          const DoublyLinkedListNode & node)
{
    cout << "<"
         << &node
         << ": "
         << node.get_data()
         << ", "
         << node.get_prev()
         << ", "
         << node.get_next()
         << ">";
    return cout;
}

