// File: SinglyLinkedlistNode.h

#ifndef SINGLYLINKEDLISTNODE_H
#define SINGLYLINKEDLISTNODE_H

#include <iostream>
class SinglyLinkedListNode;
std::ostream & operator<<(std::ostream &,
                          const SinglyLinkedListNode &);

class SinglyLinkedListNode
{
public:
    SinglyLinkedListNode(int data0=-99999, SinglyLinkedListNode * next0=0)
      : data(data0), next(next0)
    {}
    int & get_data()
    {
        return data;
    }
    int get_data() const
    {
        return data;
    }
    void set_data(int data0)
    {
        data = data0;
    }
    SinglyLinkedListNode * get_next() const
    {
        return next;
    }
    void set_next(SinglyLinkedListNode * next0)
    {
        next = next0;
    }
    
private:
    int data;
    SinglyLinkedListNode * next;
};

#endif

