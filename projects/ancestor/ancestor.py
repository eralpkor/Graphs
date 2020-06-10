# You need to be in this dir to execute this code and test file

import sys
sys.path.append("../graph") # go to parent dir
from graph2 import *


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # add all pairs
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0]) # see comments in graph2.py

    return graph.bfs(starting_node)



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),\
     (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))

