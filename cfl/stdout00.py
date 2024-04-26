from latextool_basic import *
print(automata(layout=r'''
   A  B
S  
   C
''',
S = 'label=$S$',
A = 'label=$A$',
B = 'label=$B$',
C = 'label=$C$',
edges='S,,A|S,,C|A,,B|A,,C'))
