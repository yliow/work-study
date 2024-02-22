'''
TODO: allow use to specify heap by array or by tree.
'''

from latextool_basic import *

def drawheap(p, edges, node=None, node_hsep=None, include_array=True):
    BinTree.node_hsep = 0.6
    BinTree.node = node
    if node_hsep: BinTree.node_hsep = node_hsep
    BinTree.node_width = 0.35    
    pos = BinTree.run(p, edges)

    if include_array:
        keys = pos.keys()
        values = []
        for v in edges.values(): values += v
        root = [k for k in keys if k not in values][0]

        # bfs
        s = [root]
        results = []
        while len(s) > 0:
            x = s.pop(0); results.append(x)
            s += edges.get(x, [])
        
        # smallest y in pos
        y = min([y for (_,y) in pos.values()])
        y -= 1
        n = len(results)
        x,_ = pos[root]
        width = 0.6; height = 0.6
        x -= n / 2.0 * width
        p += Array2d(x, y, width=width, height=height, 
                     xs=[results])

    return pos
     

def array_to_edges(xs):
    '''
    Returns edges from array xs
    '''
    edges = {}
    def left(i): return 2 * i + 1
    def right(i): return 2 * i + 2
    todo = [0] # list of indices
    n = len(xs)
    while len(todo) > 0:
        i,todo = todo[0],todo[1:]
        #print "i:", i, left(i), right(i), xs[left(i)], xs[right(i)]
        if right(i) <= n - 1:
            edges[xs[i]] = [xs[left(i)], xs[right(i)]]
            todo.append(left(i))
            todo.append(right(i))
        elif left(i) <= n - 1:
            edges[xs[i]] = [xs[left(i)]]
            todo.append(left(i))
    return edges
