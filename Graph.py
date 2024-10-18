# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
class Graph:
    def __init__(self):
        self.graph = {}
   
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
   
    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            #self.graph[node2].append(node1)  
        else:
            print(f"One of {node1} or {node2} values are missing.")
       
    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
   
    def does_not_trust(self):
        nodes_that_dont_trust = [node for node, neighbors in self.graph.items() if not neighbors]
        if nodes_that_dont_trust:
            print(f"Nodes that do not trust: {nodes_that_dont_trust}")
        else:
            print("-1")


g = Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1,3)
g.add_edge(2,3)
g.print_graph()
g.does_not_trust()