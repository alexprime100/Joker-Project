from random import *

class Member:
    def __init__(self, id, fname, lname):
        self.ID = id
        self.fName = fname
        self.lName = lname

def Program(file):
    database = LoadRandomMembers(file)
    displayDatabase(database)
    memberID = randint(0, len(database)-1)
    print("we search the member with this id : ", memberID)
    i1 = findID(database, memberID)
    print("with 1st method we find this member at position : ",i1,"it is", database[i1].ID,database[i1].fName, database[i1].lName)
    i2 = DAC_find_ID(database, memberID, 0, len(database)-1)
    print("with 2nd method we find this member at position : ",i2,"it is", database[i2].ID,database[i2].fName, database[i2].lName)
    print(Sort_and_find(database, memberID))
    
def findID(database, index):             #complexity O(n) in the worst case
    id = -1
    for i in range(0, len(database)):
        if database[i].ID == index:
            id = i
    return id

def DAC_find_ID(database, index, start = 0, end = -1):
    if end == -1:
        end = len(database)
    if end== start:
        if database[start].ID == index:
            return start
        else:
            return -1
    else:
        i = DAC_find_ID(database, index, start, (start+end)//2)
        if i > -1:
            return i
        else:
            i = DAC_find_ID(database, index, ((start+end)//2) + 1, end)
            if i > -1:
                return i
            else:
                return -1

def Dichotomy(database, index, start=0, end=-1):
    if end == -1:
        end = len(database)-1
    #print("i= ",(start+end)//2, " id= ", database[(start+end)//2].ID)
    if start == end:
        return -1
    if database[(start+end)//2].ID == index:
        return (start+end)//2
    if database[(start+end)//2].ID < index:
        return Dichotomy(database, index, (start+end)//2, end)
    if database[(start+end)//2].ID > index:
        return Dichotomy(database, index, start, (start+end)//2)

def Sort_and_find(database, index):
    mergeSort(database)
    displayDatabase(database)
    id = Dichotomy(database, index)
    return id

def mergeSort(database):
    if len(database) > 1:
        mid = len(database)//2
        L = database[:mid]
        R = database[mid:]

        mergeSort(L)
        mergeSort(R)
        database = fusionSort(L,R, database)

def fusionSort(L,R, tab):
    i = j = k = 0
    
    # Copy data to temp arrays L[] and R[] 
    while i < len(L) and j < len(R): 
        if L[i].ID < R[j].ID: 
            tab[k] = L[i]
            i+=1
        else: 
            tab[k] = R[j]
            j+=1
        k+=1
          
    # Checking if any element was left 
    while i < len(L): 
        tab[k] = L[i]
        i+=1
        k+=1
          
    while j < len(R): 
        tab[k] = R[j]
        j+=1
        k+=1
    return tab

def loadSortedMembers(file):
    reader = open(file, 'r')
    content = reader.read().split("\n")   #we separate the lines
    members = []
    for i in range(0, len(content)):
        line = content[i]
        elements = line.split(";")
        newMember = Member(elements[0], elements[1], elements[2])
        members.append(newMember)
    return members

def LoadRandomMembers(file):
    reader = open(file, "r")
    content = reader.read().split("\n")
    members = []
    while (content != []):
        i = randint(0, len(content)-1)
        line = content[i]
        elements = line.split(";")
        newMember = Member(int(elements[0]), elements[1], elements[2])
        members.append(newMember)
        content.remove(content[i])
    return members

def displayDatabase(database):
    for i in range(0, len(database)):
        print(database[i].ID,";",database[i].fName,"",database[i].lName)
    
dataset = "dataset3.txt"
Program(dataset)