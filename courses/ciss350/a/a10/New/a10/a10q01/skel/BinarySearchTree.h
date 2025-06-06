// File: BinarySearchTree.h

#ifndef BINARYSEARCHTREE_H
#define BINARYSEARCHTREE_H

#include <vector>
#include "BinarySearchTreeNode.h"

class ValueError{};

class BinarySearchTree
{
public:
    BinarySearchTree()
        : root_(NULL)
    {}

    // Put x[0], x[1], ..., x[size - 1] into the tree
    BinarySearchTree(int x[], int size)
    {}

    // TODO
    BinarySearchTree(const BinarySearchTree & bst)
    {}

    // TODO
    ~BinarySearchTree()
    {}

    BinarySearchTreeNode * root() const
    {
        return root_;
    }

    // TODO
    // [HINT: Traverse *this and bst.]
    BinarySearchTree & operator=(const BinarySearchTree & bst)
    {
        return (*this);
    }

    BinarySearchTreeNode * get_root() const
    {
        return root_;
    }

    // TODO:
    void clear()
    {
    }
    
    // Returns true if the tree is empty
    bool is_empty() const
    {
        return true;
    }

    // TODO
    // Returns the height of the tree. Note that the height of an
    // empty tree is -1.
    int height() const
    {
        return 0;
    }

    // TODO:
    // Returns the depth of the node pointer p parameter. This is the number
    // of edges from the root to the node that p points to.
    int depth(BinarySearchTreeNode * p)
    {
        return 0;
    }

    // TODO
    // Returns the number of nodes in this tree.
    int size() const
    {
        return 0;
    }

    // TODO
    // Returns a pointer to the node containing x. If x is not in the tree,
    // NULL is returned.
    BinarySearchTreeNode * find(int x)
    {
        return NULL;
    }

    // TODO
    // Returns the minimum value in the tree. If the tree is empty,
    // a ValueError exception object is thrown.
    int min() const
    {
        return 0;
    }

    // TODO
    // Returns the maximum value in the tree. If the tree is empty,
    // a ValueError exception object is thrown.
    int max() const
    {
        return 0;
    }

    // TODO
    // Returns true if *this and t are the same trees, i.e., the
    // values and structure of *this and t are the same.
    bool operator==(const BinarySearchTree & t)
    {
        return true;
    }

    // TODO
    // Inserts x into the tree. If x is already in the tree, a ValueError
    // exception object is thrown.
    void insert(int x)
    {
        bool success = ::insert(root_, x);
        if (!success) throw ValueError();
    }
    
    // Remove x from the tree. If x is not in the tree, a ValueError
    // exception object is thrown.
    void remove(int x)
    {}

    // TODO
    // Returns a vector of integers built by traversing the tree
    // using inorder traversal
    std::vector< int > inorder() const
    {
        std::vector< int > ret;
        return ret;
    }

    // TODO
    // Returns a vector of integers built by traversing the tree
    // using preorder traversal
    std::vector< int > preorder() const
    {
        std::vector< int > ret;
        return ret;
    }

    // TODO
    // Returns a vector of integers built by traversing the tree
    // using postorder traversal
    std::vector< int > postorder() const
    {
        std::vector< int > ret;
        return ret;
    }

    // TODO
    // Returns a vector of integers built by traversing the tree
    // using breadth first traversal
    std::vector< int > breadthfirst() const
    {
        std::vector< int > ret;
        return ret;
    }

    // TODO
    // Return pointer to k-th ordered node
    // [HINT: Use a traversal]
    BinarySearchNode * select(int k)
    {
        return NULL;
    }
    
    // TODO
    // Return vector of integers in tree with key values <= m and < M.
    std::vector< int > range(int m, int M)
    {
        std::vector< int > ret;
        return ret;
    }
    
    /**************************************************************************
    // The following iterators are optional. (These are somewhat challenging.)
    // This is how the iterator would be used:
    //
    //   BinarySearchTree::inorder_iterator p = tree.begin();
    //   while (p != tree.end())
    //   {
    //       std::cout << *p << std::endl;
    //       p++;
    //   }
    //
    // Note that you should be as memory efficient as possible. So for instance
    // Performing a complete traversal, storing a vector of the nodes, and
    // iterating through this vector is not allowed.
    
    class inorder_iterator
    {
    public:
        BinarySearchTreeNode * operator*()
        {}
        void operator++()
        {}
        void operator++(int)
        {}
        void operator--()
        {}
        void operator--(int)
        {}
        // etc.
    };

    class preorder_iterator
    {};

    class postorder_iterator
    {};

    class breadth_first_iterator
    {};
    
    **************************************************************************/
    
private:
    BinarySearchTreeNode * root_;
};

void print_inorder(const BinarySearchTree & bst);
void print_preorder(const BinarySearchTree & bst);
void print_postorder(const BinarySearchTree & bst);

#endif
