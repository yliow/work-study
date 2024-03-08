from latextool_basic import *
print(shell(['g++ main2.cpp -I/opt/ssl/include/ -L/opt/ssl/lib/ -lcrypto', './a.out'], fontsize=r'\scriptsize'))

