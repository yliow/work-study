#include <iostream>
#include <set> // <- note multiset is in set

void print(std::multiset< int > & X)
{
    std::cout << "inorder traversal: ";
    for (std::set< int >::iterator p = X.begin();
         p != X.end();
         ++p)
    {
        std::cout << *p << ' ';
    }
    std::cout << '\n';
}

int main()
{
    std::multiset< int > tree;
    tree.insert(9999);
    tree.insert(9999);
    tree.insert(9999);
    print(tree);
 
    std::cout << "tree.size(): " << tree.size() << '\n';
    for (int i = 0; i < 5; ++i)
    {
        std::cout << "tree.insert(" << i << ")\n";
        tree.insert(i);
        std::cout << "tree.size(): " << tree.size() << '\n';
    }
    print(tree);

    std::cout << "find 3\n";
    std::multiset< int >::iterator p = tree.find(3);
    if (p == tree.end())
    {
        std::cout << "3 not found\n";
    }
    else
    {
        std::cout << "3 is found ... *p:" << *p << '\n';
    }

    p = tree.find(100);
    if (p == tree.end())
    {
        std::cout << "100 not found\n";
    }
    else
    {
        std::cout << "100 is found ... *p:" << *p << '\n';
    }
    
    std::cout << "erase 3\n";
    tree.erase(3);
    print(tree);

    std::cout << "erase 1 by iterator\n";
    p = tree.find(1);
    if (p != tree.end())
    {
        tree.erase(p);
    }
    print(tree);

    std::cout << "erase a range\n";
    p = tree.begin();
    ++p;
    auto q = tree.end();
    tree.erase(p, q);
    print(tree);
    
    return 0;
}
