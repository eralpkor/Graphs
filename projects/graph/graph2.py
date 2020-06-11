from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    # undirected graph
    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.vertices[v1].add(v2)

    def get_ancestor(self, vertex_id):
        return self.vertices[vertex_id]

    def bfs(self, starting_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        longest_path_length = 1 # path to the next vertex
        earliest_ancestor = -1
        # while queue size is not empty
        while queue.size() > 0:
            path_to_current_node = queue.dequeue() # get queue node FIFO and populate to path list
            current_node = path_to_current_node[-1] # get latest node from end of list
            # if path is grater than longest path or "=" to longest path and current vertex < earliest_anc
            if len(path_to_current_node) > longest_path_length or \
                    ((len(path_to_current_node) == longest_path_length and current_node < earliest_ancestor)):
                longest_path_length = len(path_to_current_node) # update
                earliest_ancestor = current_node

            for ancestor in self.get_ancestor(current_node):
                path_to_ancestor = [*path_to_current_node, ancestor] # find the ancestor of current node
                queue.enqueue(path_to_ancestor) # and append the value to the queue

        return earliest_ancestor