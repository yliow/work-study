# Makefile for test
# Y. Liow
#------------------------------------------------------------------------------
# Macros
#------------------------------------------------------------------------------
CXX       = g++
CXXFLAGS  = -g -Wall
LINK      = g++
LINKFLAGS = 
OBJS      = BinarySearchTree.o test.o BinarySearchTreeNode.o
EXE       = test.exe

#------------------------------------------------------------------------------
# Executable
#------------------------------------------------------------------------------
$(EXE):	$(OBJS)
	$(LINK) $(LINKFLAGS) $(OBJS) -o $(EXE)

#------------------------------------------------------------------------------
# Object files
#------------------------------------------------------------------------------
BinarySearchTree.o:	BinarySearchTree.cpp BinarySearchTree.h BinarySearchTreeNode.h
	$(CXX) $(CXXFLAGS) BinarySearchTree.cpp -c -o BinarySearchTree.o

test.o:	test.cpp BinarySearchTreeNode.h BinarySearchTree.h
	$(CXX) $(CXXFLAGS) test.cpp -c -o test.o

BinarySearchTreeNode.o:	BinarySearchTreeNode.cpp BinarySearchTreeNode.h
	$(CXX) $(CXXFLAGS) BinarySearchTreeNode.cpp -c -o BinarySearchTreeNode.o

#------------------------------------------------------------------------------
# Utilities
#------------------------------------------------------------------------------
clean:
	rm $(OBJS) $(EXE)
c:
	rm $(OBJS) $(EXE)

run:
	./$(EXE)
r:
	./$(EXE)
