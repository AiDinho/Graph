"""Python for project1"""

EX_GRAPH0= {0:set([1,2]),
           1:set([]),
           2:set([])
           }
EX_GRAPH1={0:set([ 1 , 5 , 4 ]),
            1 :set([2 , 6 ]),
            2 :set([ 3 ]),
            3 :set([ 0 ]),
            4 :set([ 1 ]),
            5 :set([ 2 ]),
            6 :set([])
           }
EX_GRAPH2={0:set([1,5,4]),
           1:set([2,6]),
           2:set([3,7]),
           3:set([7]),
           4:set([1]),
           5:set([2]),
           6:set([]),
           7:set([3]),
           8:set([1,2]),
           9:set([0,3,4,5,6,7])
           }

           
def make_graph(num_nodes):
    """Helper function to make_complete_graph
       takes no of nodes and provide a complete graph
    """
    graph={}
    val=[temp for temp in range(num_nodes)]
    for attri in val:
        graph[attri]=set(val[:attri]+val[(attri+1):])
    
    return graph
def make_complete_graph(num_nodes):
    """ main function to create complete graph
        uses make_graph and creates a complete graph when
        no of nodes is positive
    """
    if num_nodes >0:
        return make_graph(num_nodes)
    else:
        return {}

def compute_in_degrees(digraph):
    """ computes in degrees of a given graph and return a 
        dictionary where each node is key and their corresponding 
        in-degree is value
    """
    counts=dict([temp1,0] for temp1 in digraph)
    for hold in digraph.values():
        for tem in hold:
            counts[tem]+=1
    
    return counts

def in_degree_distribution(digraph):
    """computes the in degree distribution.returns a dict with in-degrees as key
       and no of nodes with that in degree as value
    """
    counts=compute_in_degrees(digraph)
    distri={}
    for key,vals in counts.iteritems():
        distri[vals]=distri.get(vals,0)+1
    
    
    return distri
    
    
    
        


  
    
    
         
        


        
    