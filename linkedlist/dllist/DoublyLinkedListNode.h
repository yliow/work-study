// File: DoublyLinkedlistNode.h

#ifndef DOUBLYLINKEDLISTNODE_H
#define DOUBLYLINKEDLISTNODE_H

#include <iostream>
class DoublyLinkedListNode;
std::ostream & operator<<(std::ostream &,
                          const DoublyLinkedListNode &);

class DoublyLinkedListNode
{
public:
    DoublyLinkedListNode(int data0=-99999,
                         DoublyLinkedListNode * next0=0,
                         DoublyLinkedListNode * prev0=0)
        : data(data0), next(next0), prev(prev0)
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
    DoublyLinkedListNode * get_next() const
    {
        return next;
    }
    void set_next(DoublyLinkedListNode * next0)
    {
        next = next0;
    }
    DoublyLinkedListNode * get_prev() const
    {
        return prev;
    }
    void set_prev(DoublyLinkedListNode * prev0)
    {
        prev = prev0;
    }
    
private:
    int data;
    DoublyLinkedListNode * prev;
    DoublyLinkedListNode * next;
};

#endif
