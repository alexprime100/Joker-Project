import numpy as np

class Node:
    def __init__(self, name):
        self.Name = name
        #a part of step 1 in Dijkstra's algorithm is made in the constructor
        self.Distance = np.inf
        self.Status = False        #false corresponds to temporary and true to permanent
        self.previous = None

def Program(file):
    matrix = loadMatrix(file)
    list_of_nodes = loadNodes()
    start = int(input("enter the starting point"))
    end = int(input("enter the ending point"))
    path = Dijkstra(list_of_nodes, matrix, start - 1,end - 1)
    for i in range(0,len(path)):
        print(path[i].Name)

def loadMatrix(file):
    reader = open(file, 'r')
    content = reader.read().split("\n")   #we separate the lines
    matrix = np.zeros((10,10))
    for k in range(0, len(content)):
        line = content[k]
        if len(line) > 0:
            elements = line.split(";")
            i = int(elements[0]) - 1
            j = int(elements[1]) - 1
            distance = float(elements[2])
            matrix[i,j] = distance
            #print(matrix)
    for j in range(0,10):
        for i in range(j+1, 10):
            matrix[i,j] = matrix[j,i]
    matrix = loadMatrix2(matrix)
    return matrix

def loadMatrix2(matrix):
    for i in range(0, len(matrix[0])):
        for j in range(i+1, len(matrix[0])):
            if matrix[i,j] == 0:
                matrix[i,j] = np.inf
                matrix[j,i] = np.inf
    return matrix

def loadNodes():
    list_of_nodes = []
    for i in range(0,10):
        newNode = Node(i)
        list_of_nodes.append(newNode)
    return list_of_nodes

def Dijkstra(list_of_nodes, matrix, start, end):
    #step1
    list_of_nodes[start].Distance = 0
    list_of_nodes[start].Status = True
    path = []
    current = start
    #step2
    while list_of_nodes[end].Status == False:
        print("current node = ", list_of_nodes[current].Name)
        #the next current node is the one that has the smallest distance at the end of an iteration
        #the program is always searching for it
        nextCurrent = -1
        for i in range(0, len(matrix[current])):         #the program analyzes each edge of the current node
            if matrix[current,i] < np.inf and matrix[current,i] >0 and list_of_nodes[i].Status == False:
                list_of_nodes[i].Distance = min(list_of_nodes[i].Distance, list_of_nodes[current].Distance + matrix[current,i]) #the distance is updated
                if list_of_nodes[i].Distance == list_of_nodes[current].Distance + matrix[current,i]:   #if the distance has changed, then the previous node in the shortest path has changed too
                    list_of_nodes[i].previous = list_of_nodes[current]
                if nextCurrent == -1 or list_of_nodes[i].Distance < list_of_nodes[nextCurrent].Distance:    #if this node has a smaller distance than the previous ones, then he is the new potential next current node
                    nextCurrent = i
        current = nextCurrent      #the current node is updated, and his status too
        list_of_nodes[current].Status = True
    #now the program can easuly find the shortest path
    path.append(list_of_nodes[end])
    while path[0].Name != list_of_nodes[start].Name:
        path.insert(0, path[0].previous)
    return path


dataset = "dataset2.txt"

Program(dataset)