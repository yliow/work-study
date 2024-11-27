// File: BinarySearchTree.h

#ifndef BINARYSEARCHTREE_H
#define BINARYSEARCHTREE_H

#include "BinarySearchTreeNode.h"

class ValueError{};

class BinarySearchTree
{
public:
    BinarySearchTree()
        : root(NULL)
    {}
    
    BinarySearchTree(const BinarySearchTree & bst)
    {}
    
    ~BinarySearchTree()
    {}
    
    BinarySearchTree & operator=(const BinarySearchTree & bst)
    {}
    
    BinarySearchTreeNode * get_root() const
    {
        return root;
    }
    
    // Returns true if the tree is empty
    bool is_empty() const
    {}
    
    // Returns the height of the tree. Note that the height of an
    // empty tree is -1.
    int height() const
    {}
    
    // Returns a pointer to the node containing x. If x is not in the tree,
    // NULL is returned.
    BinarySearchTreeNode * find(int x)
    {}
    
    // Returns the minimum value in the tree. If the tree is empty,
    // a ValueError exception object is thrown.
    int min() const
    {}

    // Returns the maximum value in the tree. If the tree is empty,
    // a ValueError exception object is thrown.
    int max() const
    {}

    // Inserts x into the tree. If x is already in the tree, a ValueError
    // exception object is thrown.
    void insert(int x)
    {
        bool success = ::insert(root, x);
        if (!success) throw ValueError();
    }
    
    // Remove x from the tree. If x is not in the tree, a ValueError
    // exception object is thrown.
    void remove(int x)
    {}
    
private:
    BinarySearchTreeNode * root;
};

void print_inorder(const BinarySearchTree & bst);
void print_preorder(const BinarySearchTree & bst);
void print_postorder(const BinarySearchTree & bst);

#endif
