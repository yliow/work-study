// File: SinglyLinkedList.h

#ifndef SINGLYLINKEDLIST_H
#define SINGLYLINKEDLIST_H

#include <iostream>
#include "SinglyLinkedListNode.h"


class ValueError;
class SinglyLinkedList;
std::ostream & operator<<(std::ostream &, 
                          const SinglyLinkedList &);

class ValueError
{};

class SinglyLinkedList
{
public:
    SinglyLinkedList()
        : head(NULL)
    {}
    
    SinglyLinkedList(const SinglyLinkedList & list)
        : head(NULL)
    {
        *this = list;
    }
    
    ~SinglyLinkedList()
    {
        clear();
    }

    void clear()
    {
        while (!is_empty())
        {
            remove_head();
        }
    }

    SinglyLinkedList & operator=(const SinglyLinkedList & list)
    {
        if (this == &list) return (*this);
        
        clear();
        SinglyLinkedListNode * p = list.get_head();
        while (p != NULL)
        {
            insert_tail(p->get_data());
            p = p->get_next();
        }
        return *this;
    }

    bool operator==(const SinglyLinkedList & list) const
    {
        SinglyLinkedListNode * p = head;
        SinglyLinkedListNode * q = list.get_head();
        while (1)
        {
            if (p == NULL && q == NULL)
            {
                return true;
            }
            if ((p == NULL && q != NULL) || (p != NULL && q == NULL))
            {
                return false;
            }
            if (p->get_data() != q->get_data())
            {
                return false;
            }
            p = p->get_next();
            q = q->get_next();
        }
    }

    bool operator!=(const SinglyLinkedList & list) const
    {
        return !(*this == list);
    }

    bool is_empty() const
    {
        return (head == NULL);
    }
    
    //-------------------------------------------------------------------------
    // Operations at head
    //-------------------------------------------------------------------------
    SinglyLinkedListNode * get_head() const
    {
        return head;
    }

    void insert_head(int x) 
    {
        SinglyLinkedListNode * node = new SinglyLinkedListNode(x, head);
        head = node;
    }

    int remove_head()
    {
        if (head == NULL) throw ValueError();

        int ret = head->get_data();
        SinglyLinkedListNode * newhead = head->get_next();
        delete head;
        head = newhead;
        return ret;
    }

    //-------------------------------------------------------------------------
    // Operations at tail
    //-------------------------------------------------------------------------
    SinglyLinkedListNode * get_tail() const
    {
        if (head == NULL) return NULL;
        
        SinglyLinkedListNode * tail = head;
        while (tail->get_next() != NULL)
        {
            tail = tail->get_next();
        }
        return tail;
    }

    int remove_tail()
    {
        if (head == NULL) throw ValueError();
        
        SinglyLinkedListNode * tail = get_tail();
        return remove(tail);
    }
    
    void insert_tail(int x)
    {
        SinglyLinkedListNode * node = new SinglyLinkedListNode(x);

        if (is_empty())
        {
            // CASE: No tail node (i.e. list is empty)
            head = node;
        }
        else
        {
            // CASE: Tail node exists
            SinglyLinkedListNode * tail = get_tail();
            tail->set_next(node);
        }
    }

    //-------------------------------------------------------------------------
    // Global operations
    //-------------------------------------------------------------------------
    SinglyLinkedListNode * find(int x)
    {
        SinglyLinkedListNode * p = head;
        while (p != NULL)
        {
            if (p->get_data() == x)
            {
                return p;
            }
            p = p->get_next();
        }
        return p;
    }

    SinglyLinkedListNode * prev(const SinglyLinkedListNode * p) const
    {
        // Returns pointer to the previous node.
        // If previous is not found, then NULL is returned.
        // This happens if either the pointer argument does not point
        // to any node in the list or when the list is empty.

        if (head == NULL)
        {
            return NULL;
        }
        else if (p == head)
        {
            return NULL;
        }
        else
        {
            SinglyLinkedListNode * previous = head;
            SinglyLinkedListNode * next = previous->get_next();
            
            while (next != p)
            {
                if (next == NULL) return NULL;
                
                previous = next;
                next = previous->get_next();
            }
            return previous;
        }
    }

    int remove(SinglyLinkedListNode * p)
    {
        if (p == NULL) throw ValueError();

        if (p == head)
        {
            return remove_head();
        }
        else
        {
            SinglyLinkedListNode * previous = prev(p);
            int ret = p->get_data();
            previous->set_next(p->get_next());
            delete p;
            return ret;
        }
    }

    int remove(int x)
    {
        return remove(find(x));
    }

    int size() const
    {
        SinglyLinkedListNode * p = head;
        int count = 0;
        while (p != NULL)
        {
            ++count;
            p = p->get_next();
        }
        return count;
    }

    int & operator[](int i) const
    {
        if (i < 0) throw ValueError();

        SinglyLinkedListNode * p = head;
        for (int j = 0; j < i; ++j)
        {
            if (p == NULL)
            {
                throw ValueError();
            }
            p = p->get_next();
        }
        if (p == NULL)
        {
            throw ValueError();
        }
        else
        {
            return p->get_data();
        }
    }
    
private:
    SinglyLinkedListNode * head;
};


#endif
