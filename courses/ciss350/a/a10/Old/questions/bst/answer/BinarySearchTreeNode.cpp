// File: BinarySearchTreeNode.cpp

#include "BinarySearchTreeNode.h"


std::ostream & operator<<(std::ostream & cout,
                          const BinarySearchTreeNode & node)
{
    cout << "<Node: " << &node
         << ", data:" << node.get_data() 
         << ", parent:" << node.get_parent() 
         << ", left:" << node.get_left()
         << ", right:" << node.get_right() << '>';
    return cout;
}


void print_inorder(const BinarySearchTreeNode * node)
{
    if (node == NULL) return;
    print_inorder(node->get_left());
    std::cout << (*node) << '\n';
    print_inorder(node->get_right());
}


bool insert(BinarySearchTreeNode * & node, int x)
{
    if (node == NULL)
    {
        node = new BinarySearchTreeNode(x);
        return true;
    }
    
    int node_data = node->get_data();
    if (node_data == x)
    {
        return false;
    }
    else
    {
        BinarySearchTreeNode * next;
        next = (node_data < x ? node->get_right() : node->get_left());
        
        if (next == NULL)
        {
            BinarySearchTreeNode * newnode = new BinarySearchTreeNode(x,
                                                                      node);
            if (node_data < x)
            {
                node->set_right(newnode);
            }
            else
            {
                node->set_left(newnode);
            }
            return true;
        }
        else
        {
            return insert(next, x);
        }
    }
}
