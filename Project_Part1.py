import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Edge:
    def __init__(self, node1, node2, value):
        self.Value = value
        self.Node1 = node1
        self.Node2 = node2

def Program(file):
    edges = loadFile(file)
    list_of_nodes = listNodes(edges)
    ToGraph(edges, list_of_nodes)
    path = kruskal(edges, list_of_nodes)
    cost = 0
    for i in range(0, len(path)):
        print(path[i].Node1 + "-" + path[i].Node2)
        cost += path[i].Value
    print("Total cost : ")
    print(cost)

def ToGraph(edges, list_of_nodes):
    #draws the graph using networkx library
    G = nx.Graph()
    for j in range(0, len(list_of_nodes)):
        G.add_nodes_from(list_of_nodes[j])

    for i in range(0, len(edges)):
        G.add_weighted_edges_from([(edges[i].Node1, edges[i].Node2, edges[i].Value*1.0)])
    #print(G.edges())
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def kruskal(edges, list_nodes):
    path = []
    print(list_nodes)
    for i in range(0, len(edges)):
        node1 = edges[i].Node1
        node2 = edges[i].Node2
        if grouped(list_nodes, node1, node2) == False:
            i1 = search(list_nodes, node1)
            i2 = search(list_nodes, node2)
            list_nodes = fusion(list_nodes, i1, i2)
            #print(list_nodes)
            path.append(edges[i])
    return path

def loadFile(file):
    #puts each edge in a list
    reader = open(file, 'r')
    content = reader.read().split("\n")   #we separate the lines
    edges = []
    for i in range(0, len(content)):
        line = content[i]
        if len(line)>0:
            if line[0] != "#":
                elements = line.split(";")           #the edge's information are separated by a ";" in the dataset
                node1 = elements[0]
                node2 = elements[1]
                value = elements[2]
                value2 = float(value)
                newEdge = Edge(node1, node2, value2)
                #we insert the edge in a sorted list
                j = 0
                while(j < len(edges) and newEdge.Value > edges[j].Value):       #we search for the right position for this edge
                    j+=1
                if j == len(edges):            #if it is the new edge with the greatest value
                    edges.append(newEdge)
                else:
                    edges.insert(j,newEdge)
    return edges

def listNodes(edges):
    #puts each node in a list that we put in a list of list on order to use Kruskal's algorith just after
    Nodes = []
    for i in range(0, len(edges)):
        node1 = []
        node1.append(edges[i].Node1)
        if Nodes.count(node1) == 0:     #if this node is not already in the list, we add it in
            Nodes.append(node1)
        node2 = []
        node2.append(edges[i].Node2)
        if Nodes.count(node2) == 0:
            Nodes.append(node2)
    return Nodes

def fusion(tab, i, j):
    #concatenates 2 groups of nodes when we use Kruskal's algorithm
    for k in range(0, len(tab[j])):
        tab[i].append(tab[j][k])
    tab.remove(tab[j])
    return tab        

def search(tab, node):
    #returns the node's index in the nodes' list
    index = 0
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])):
            if tab[i][j] == node:
                index=i
    return index

def grouped(Nodes, node1, node2):
    #returns true if both nodes are in the same group
    answer = False
    for i in range(0, len(Nodes)):
        if exist(Nodes[i], node1):
            if exist(Nodes[i], node2):
                answer = True
    return answer

def exist(tab, node):
    #returns true if the node belongs to tab
    answer = False
    for i in range(0, len(tab)):
        if tab[i] == node:
            answer = True
            i = len(tab)
    return answer


dataset = "dataset1.txt"
Program(dataset)