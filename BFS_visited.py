from collections import deque
GRAPH0 = {0: set([1]),
          1: set([0, 2]),
          2: set([1, 3]),
          3: set([2])}
GRAPH1 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3])}

GRAPH4 = {0: set([1, 2, 3, 4]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0]),
          5: set([6, 7]),
          6: set([5]),
          7: set([5])}

def bfs_visited(graph,node):
    Q=deque()
    visited=deque()
    visited.append(node)
    Q.append(node)
    while len(Q)>0:
        temp=Q.pop()
        for i in graph[temp]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
    return set(visited)
            
def cc_visited(graph):
    CC_ret=deque()
    rem_nodes=set(graph.keys())
    while rem_nodes:
        for i in rem_nodes:
            W=bfs_visited(graph,i)
        CC_ret.append(W)
        rem_nodes=rem_nodes-set(W)
    return (CC_ret)
        
#print cc_visited(GRAPH4)
def largest_cc_size(graph):
    maximam=deque()
    for i in cc_visited(graph):
        maximam.append(len(i))
    return max(maximam)
def compute_resilience(ugraph, attack_order):
    ret_value=deque()
    ret_value.append(largest_cc_size(ugraph))
    for i in attack_order:
        
        
   
    
    
        
#print largest_cc_size(GRAPH4)
    
    
#print largest_cc_size(GRAPH0)
