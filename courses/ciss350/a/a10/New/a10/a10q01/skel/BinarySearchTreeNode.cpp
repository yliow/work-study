// File: BinarySearchTreeNode.cpp

#include "BinarySearchTreeNode.h"


std::ostream & operator<<(std::ostream & cout,
                          const BinarySearchTreeNode & node)
{
    cout << "<Node: " << &node
         << ", key:" << node.key() 
         << ", parent:" << node.parent() 
         << ", left:" << node.left()
         << ", right:" << node.right() << '>';
    return cout;
}


void print_inorder(const BinarySearchTreeNode * node)
{
    if (node == NULL) return;
    print_inorder(node->left());
    std::cout << (*node) << '\n';
    print_inorder(node->right());
}


bool insert(BinarySearchTreeNode * & node, int x)
{
    return true;
}
