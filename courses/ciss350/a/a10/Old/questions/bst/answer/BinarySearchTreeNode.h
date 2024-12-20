// File: BinarySearchTreeNode.h

#ifndef BINARYSEARCHTREENODE_H
#define BINARYSEARCHTREENODE_H

#include <iostream>

class BinarySearchTreeNode
{
public:
    BinarySearchTreeNode(int data0,
                         BinarySearchTreeNode * parent0=NULL,
                         BinarySearchTreeNode * left0=NULL,
                         BinarySearchTreeNode * right0=NULL)
        : data(data0), parent(parent0), left(left0), right(right0)
    {}
    
    int get_data() const
    {
        return data;
    }
    
    void set_data(int data0)
    {
        data = data0;
    }
    
    BinarySearchTreeNode * get_parent() const
    {
        return parent;
    }
    
    void set_parent(BinarySearchTreeNode * parent0)
    {
        parent = parent0;
    }
    
    BinarySearchTreeNode * get_left() const
    {
        return left;
    }
    
    void set_left(BinarySearchTreeNode * left0)
    {
        left = left0;
    }
    
    BinarySearchTreeNode * get_right() const
    {
        return right;
    }
    
    void set_right(BinarySearchTreeNode * right0)
    {
        right = right0;
    }
    
private:
    int data;
    BinarySearchTreeNode * parent;
    BinarySearchTreeNode * left;
    BinarySearchTreeNode * right;
};

std::ostream & operator<<(std::ostream &,
                          const BinarySearchTreeNode &);

void print_inorder(const BinarySearchTreeNode *);
bool insert(BinarySearchTreeNode * &, int);

#endif
