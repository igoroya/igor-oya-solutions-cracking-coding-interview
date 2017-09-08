'''
Created on 6 Sep 2017

The idea is to use a digraph, representing the elements to compile as nodes
and the dependencies as edges


@author: igoroya
'''
import networkx as nx
import collections
from enum import Enum

def is_compilable(my_dg):
    """
    This corresponds to the classical solution using a topological sort
    of a graph
    """

    build_list = []
    # find all nodes without parents and put into the list. Take nodes out of graph
    while len(my_dg) > 1:
        selected_nodes = []
        for node in my_dg:
            if len(my_dg.predecessors(node)) == 0:
                selected_nodes.append(node)

        if len(selected_nodes) == 0:
            #we found no nodes without parents, means it is not compilable
            return False

        for node in selected_nodes:
            build_list.append(node)
            my_dg.remove_node(node)

    return (True, build_list)


def is_compilable_dfs(my_dg):
    """
    This corresponds to the alternative solution using a topological sort
    of a graph using a depth first search
    """
    compiling_stack = collections.deque()
    # we store the compiling order in a stack (using a deque)



    #we go over all the elements in the digraph, visitig each node once
    visit_state = {node:State.NOT_VISITED for node in my_dg}

    try:
        for node in my_dg:
            if visit_state[node] is State.VISITED:
                continue
            visit_node(node, visit_state, compiling_stack)
    except CircularDependencyError:
        print("Circular Dependency!!")
        return False

    #present results
    while len(compiling_stack) > 0:
        print(compiling_stack.pop())
    return True


def visit_node(node, visit_state, compiling_stack):
    visit_state[node] = State.VISITING
    for successor in my_dg.successors(node):
        if visit_state[successor] is State.VISITING:
            raise CircularDependencyError()
        elif visit_state[successor] is State.VISITED:
            continue
        else:
            visit_node(successor, visit_state, compiling_stack)
    visit_state[node] = State.VISITED
    compiling_stack.append(node)

class State(Enum):
    NOT_VISITED = 1
    VISITING = 2
    VISITED = 3

class CircularDependencyError(Exception):
    pass

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
    print("Graph noded: {}, edges: {}".format(my_dg.nodes(), my_dg.edges()))
    print(is_compilable_dfs(my_dg))

    print(is_compilable(my_dg))