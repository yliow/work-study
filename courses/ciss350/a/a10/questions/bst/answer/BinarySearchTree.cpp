// File: BinarySearchTree.cpp

#include "BinarySearchTree.h"

void print_inorder(const BinarySearchTree & bst)
{
    print_inorder(bst.get_root());
}

