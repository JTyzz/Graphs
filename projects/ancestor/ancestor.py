class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

#def earliest_ancestor(ancestors, starting_node):
 #   ancestor_paths = {}
#
#    graph = {}
#
#    for relation in ancestors:
#        if relation[1] not in graph:
#            graph[relation[1]] = set()
#        if relation[0] not in graph:
#            graph[relation[0]] = set()
#        
#        graph[relation[1]].add(relation[0])
#   if graph[starting_node] == set():
#       return -1
#
#    q = Queue()
#
#    visited = []
#
#    q.enqueue(starting_node)
#    ancestor_paths[starting_node] = [starting_node]
#    while q.size() > 0:
#        current = q.eueue[0]
#        visited.append(current)
#        for parent in graph[current]:
#            if parent not in visited:
#                ancestor_paths[parent]



class Graph:
    def __init__(self):
        self.vertices = {} # Set

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):

        # if v2 not in self.vertices.get(v1):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    ancestor_paths = {}

    graph = {}

    for relation in ancestors:
        if relation[1] not in graph:
            graph[relation[1]] = set()
        # We want to make sure the parent is in there too, even if it doesn't have parents
        if relation[0] not in graph:
            graph[relation[0]] = set()
        
        graph[relation[1]].add(relation[0])

    # If starting node has no parents, return -1
    if graph[starting_node] == set():
        return -1

    q = Queue()

    visited = []

    q.enqueue(starting_node)
    ancestor_paths[starting_node] = [starting_node]



def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    max_path_len = 1
    earliest_ancestor = -1
    visited = set()
    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) == max_path_len and v < earliest_ancestor) or len(path) > max_path_len:
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor