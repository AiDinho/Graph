"""Code for project which computes BFS,Connected Component
   largest Connected Component size and resilience
"""
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
    """Given a graph and a node gives the BFS tree"""
    bfs_tree=deque()
    visited=deque()
    visited.append(node)
    bfs_tree.append(node)
    while len(bfs_tree)>0:
        temp=bfs_tree.pop()
        for temp1 in graph[temp]:
            if temp1 not in visited:
                visited.append(temp1)
                bfs_tree.append(temp1)
    return set(visited)        
                   
def cc_visited(graph):
    """given a graph returns its connected component"""
    cc_ret=deque()
    rem_nodes=set(graph.keys())
    while rem_nodes:
        for node in rem_nodes:
            bfs_tree=bfs_visited(graph,node)
        cc_ret.append(bfs_tree)
        rem_nodes=rem_nodes-set(bfs_tree)
    return list(cc_ret)
        
#print cc_visited(GRAPH4)
def largest_cc_size(graph):
    """Given a graph computed the largest connected component size"""
    maximam=deque()
    for temp in cc_visited(graph):
        maximam.append(len(temp))
    try:
        return max(maximam)
    except ValueError:
        return 0
def compute_resilience(ugraph, attack_order):
    """given a graph and a set of nodes calculates the resilience
       and returns the largest cc size after each node is deleted
    """
    ret_value=deque()
    graph_processed=ugraph
    ret_value.append(largest_cc_size(graph_processed))
    
    for nodes in attack_order:
        del graph_processed[nodes]
        for key,value in graph_processed.items():
            if nodes in value:
                graph_processed[key]=value-set([nodes])
        
        
        ret_value.append(largest_cc_size(graph_processed))
    return  list(ret_value)

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}     
        
#print compute_resilience(GRAPH2,[1, 3, 5, 7, 2, 4, 6, 8])
    
    
#print largest_cc_size(GRAPH0)
