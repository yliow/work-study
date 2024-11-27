// File: test.cpp

#include <iostream>
#include "BinarySearchTreeNode.h"
#include "BinarySearchTree.h"

int main()
{
    std::cout << "testing BinarySearchTreeNode ...\n";
    
    BinarySearchTreeNode * n = new BinarySearchTreeNode(5);
    print_inorder(n);

    std::cout << "\n\n";
    insert(n, 3);
    print_inorder(n);
    
    std::cout << "\n\n";
    insert(n, 0);
    print_inorder(n);
    
    std::cout << "\n\n";
    insert(n, 1);
    print_inorder(n);
    
    std::cout << "\n\n";
    insert(n, 4);
    print_inorder(n);
    
    std::cout << "\n\n";
    insert(n, 8);
    print_inorder(n);

    std::cout << "testing BinarySearchTree ... \n";
    BinarySearchTree bst;
    print_inorder(bst); std::cout << '\n';
    
    bst.insert(5); print_inorder(bst); std::cout << '\n';
    bst.insert(0); print_inorder(bst); std::cout << '\n';
    bst.insert(2); print_inorder(bst); std::cout << '\n';
    bst.insert(-2); print_inorder(bst); std::cout << '\n';
    bst.insert(10); print_inorder(bst); std::cout << '\n';
    bst.insert(8); print_inorder(bst); std::cout << '\n';
    bst.insert(9); print_inorder(bst); std::cout << '\n';
    bst.insert(7); print_inorder(bst); std::cout << '\n';
    try
    {
        std::cout << "testing duplicate insert ... ";
        bst.insert(7); 
    }
    catch (ValueError & e)
    {
        std::cout << "pass" << std::endl;
    }
    return 0;
}
