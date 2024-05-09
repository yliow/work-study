#include <iostream>
#include "SinglyLinkedListNode.h"

std::ostream & operator<<(std::ostream & cout,
                          const SinglyLinkedListNode & node)
{
    cout << "<"
         << &node
         << ": "
         << node.get_data()
         << ", "
         << node.get_next()
         << ">";
    return cout;
}

