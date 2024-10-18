from PIL import Image
import numpy as np

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []
        self.visited = False

    def add_neighbour(self, neighbour):
        if (neighbour not in self.neighbours):
            self.neighbours.append(neighbour)
        else:
            print(f'Node: ({self.x}, {self.y}) already has neighbour: ({neighbour.x}, {neighbour.y})')
            
    def remove_neightbour(self, neighbour):
        if (neighbour in self.neighbours):
            self.neighbours.remove(neighbour)
        else:
            print(f'Node: ({self.x}, {self.y}) does not have neighbour: ({neighbour.x}, {neighbour.y})')

    def __str__(self):
        return f'Node: ({self.x}, {self.y})'
    
class Graph:
    def __init__(self):
        self.nodes = []
        self.node_dict = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.node_dict[(node.x, node.y)] = node

    def add_edge(self, node1, node2):
        node1.add_neighbour(node2)
        node2.add_neighbour(node1)
        
    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del self.node_dict[(node.x, node.y)]
        
    def remove_edge(self, node1, node2):
        node1.remove_neighbour(node2)
        node2.remove_neighbour(node1)


def main():
    # load img to array
    img = Image.open('intersecting_cropped.png')
    arr = np.array(img)
    print(arr.shape)
    
    # fill graph
    graph = Graph()
    for j in range(arr.shape[0]):
        for i in range(arr.shape[1]):
            if arr[j, i] == 0:
                graph.add_node(Node(i, j))
                
    # add edges
    for node in graph.nodes:
        x, y = node.x, node.y
        # Check and add edges for adjacent nodes (up, down, left, right)
        if (x - 1, y) in graph.node_dict:
            graph.add_edge(node, graph.node_dict[(x - 1, y)])
        if (x + 1, y) in graph.node_dict:
            graph.add_edge(node, graph.node_dict[(x + 1, y)])
        if (x, y - 1) in graph.node_dict:
            graph.add_edge(node, graph.node_dict[(x, y - 1)])
        if (x, y + 1) in graph.node_dict:
            graph.add_edge(node, graph.node_dict[(x, y + 1)])
    
    # debugging  
    print(f"{len(graph.nodes)} / {arr.shape[0] * arr.shape[1]} pixels added as nodes")
    
    neighbour_freq = [0, 0, 0, 0, 0]    
    for node in graph.nodes:
        neighbour_freq[len(node.neighbours)] += 1
        
    print(f"Neighbour frequencies: {neighbour_freq}")


if __name__ == '__main__':
    main()
