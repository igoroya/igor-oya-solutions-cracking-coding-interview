'''
Created on 25 Aug 2017

Route between nodes

I used the networkx for the graph usage

To learn:
-networkx
- for a digraph, I just need to know: loop over it, get "successors" (or "predecessors)

@author: igoroya
'''
import networkx as nx
import collections

def has_route(my_digraph, node1, node2):
    """
    This uses the networkx package for the graph usage, but only to
    use the minimal features incorporated. The search algorithm is based in
    a bread first search
    """

    if (node1 not in my_digraph) or (node2 not in my_digraph):
        return False


    my_queue = collections.deque()

    my_queue.append(node1)

    my_way = collections.deque()

    while len(my_queue) > 0:
        node = my_queue.pop()
        my_way.append(node)
        my_digraph.node[node] = True
        if node is node2:
            print("Connected. way from {} to {}: {}".format(node1, node2, my_way))
            return True
        for succesor in my_digraph.successors(node):
            if my_digraph.node[succesor] is not True:
                my_queue.append(succesor)
    return False

if __name__ == '__main__':
    my_dg = nx.DiGraph()
    my_dg.add_edge("A", "B")
    my_dg.add_edge("B", "C")
    my_dg.add_edge("B", "D")
    my_dg.add_edge("B", "E")
    my_dg.add_edge("E", "F")
    my_dg.add_edge("F", "G")
    my_dg.add_edge("W", "X")
    my_dg.add_edge("X", "Y")
    my_dg.add_edge("F", "Y")
    #my_dg.add_edge("A", "G")
    print("Graph edges: {}".format(my_dg.edges()))

    has_route(my_dg, "A", "Y")