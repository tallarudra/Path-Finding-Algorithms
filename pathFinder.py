__author__ = 'Krishna Sai Tallapragada'
queue=[]
goalFound=False
import sys
class Node:
    def __init__(self, name):
        pass
        self.name = name
        self.child = []
        self.childNames = []
    
    def updateName(self, name):
        self.name = name

    def updateParent(self, parent):
        self.parent = parent

    def updateState(self, state):
        self.state.append(state)

    def addChild(self, child):
        self.child.append(child)

def ignoreNode():
    global queue
    queue.reverse()
    queue.pop()
    queue.reverse()
    
def sort(nodes):
    openNames=[]
    for count in range(len(nodes) - 1, 0, -1):
        for i in range(count):
            if nodes[i].cost > nodes[i + 1].cost:
                nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]
    for i in range (0,len(nodes)):
        openNames.append(nodes[i].name)
    
    return nodes,openNames

def sortHeuristic(nodes):
    openNames=[]
    for count in range(len(nodes) - 1, 0, -1):
        for i in range(count):
            if nodes[i].heuristic > nodes[i + 1].heuristic:
                nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]
    for i in range (0,len(nodes)):
        openNames.append(nodes[i].name)
    
    return nodes,openNames

def Expand(currnode):
    queue=[]
    dele=[]
    global liveFeed
    for line in liveFeed[:]:
        if (line[0].rstrip() == currnode.name):
            newChild = Node(line[1])
            newChild.cost = 1 + currnode.cost
            newChild.parent=currnode
            newChild.state = currnode.state + [currnode.name + " " + str(currnode.cost)]
            queue.append(newChild)
    return queue

def UCSExpand(currnode):
    queue=[]
    dele=[]
    global liveFeed
    for line in liveFeed:
        if (line[0].rstrip() == currnode.name):
            newChild = Node(line[1])
            newChild.cost = int(line[2]) + currnode.cost
            newChild.parent=currnode
            newChild.state = currnode.state + [currnode.name + " " + str(currnode.cost)]
            queue.append(newChild)
    return queue

def AExpand(currnode):
    queue=[]
    dele=[]
    global liveFeed
    
    for line in liveFeed:
        if (line[0].rstrip() == currnode.name):
            for it in sundayFeed:
                if (it[0] == line[1]):
                    heur = it[1]
                    break
            newChild = Node(line[1])
            newChild.cost = int(line[2]) + currnode.cost
            newChild.parent=currnode
            newChild.heuristic = int(heur) + newChild.cost
            newChild.state = currnode.state + [currnode.name + " " + str(currnode.cost)]
            queue.append(newChild)
    return queue

def DFS1(nodeToBeExpanded):
    queueTemp = []
    if (nodeToBeExpanded.name == goalState.rstrip()):
        global goalFound, queue
        goalFound = True
        output_file = open("output.txt", "w")
        for i in range(0, len(nodeToBeExpanded.state) - 1):
            output_file.write(nodeToBeExpanded.state[i])
            output_file.write("\n")
        output_file.write(nodeToBeExpanded.state[len(nodeToBeExpanded.state) - 1])

    else:
        queue.reverse()
        queue.pop()
        for line in liveFeed:
            if (line[0].rstrip() == nodeToBeExpanded.name):
                newChild = Node(line[1])
                newChild.cost = 1 + nodeToBeExpanded.cost
                newChild.state = nodeToBeExpanded.state + [newChild.name + " " + str(newChild.cost)]
                queueTemp.append(newChild)
        queueTemp.reverse()
        queue = queue + queueTemp
        queue.reverse()
        
def search():
    openList=[]
    openNames=[]
    root = Node(startState.rstrip())
    root.cost = 0
    root.parent=Node("root")
    root.state = [startState.rstrip() + " " + str(root.cost)]
    openList.append(root)
    openNames.append(root.name)
    closed=[]
    closedNames=[]
    while (True):
        if (len(openList)==0):
            return 0
        currnode=openList.pop(0)
        openNames.pop(0)
        if (currnode.name.rstrip()==goalState.rstrip()):
            return currnode
        children=Expand(currnode)
        while len(children)!=0:
            child=children.pop(0)
            if (child.name not in openNames) and (child.name not in closed):
                openList.append(child)
                openNames.append(child.name)
            elif (child.name in openNames):
                index=openNames.index(child.name)
                if (child.cost<openList[index].cost):
                    openNames.remove(openList[index].name)
                    openNames.append(child.name)
                    openList.remove(openList[index])
                    openList.append(child)
            elif (child.name in closed):
                index=closedNames.index(child.name)
                if (child.cost < closed[index].cost):
                    closedNames.remove(closed[index].name)
                    closed.remove(closed[index])
                    openList.append(child)
                    openNames.append(child.name)
        closed.append(currnode)
        closedNames.append(currnode.name)
     

def UCS():
    openList=[]
    openNames=[]
    root = Node(startState.rstrip())
    root.cost = 0
    root.parent=Node("root")
    root.state = [startState.rstrip() + " " + str(root.cost)]
    openList.append(root)
    openNames.append(root.name)
    closed=[]
    closedNames=[]
    while (True):
        if (len(openList)==0):
            return 0
        currnode=openList.pop(0)
        openNames.pop(0)
        if (currnode.name.rstrip()==goalState.rstrip()):
            return currnode
        children=UCSExpand(currnode)
        while len(children)!=0:
            child=children.pop(0)
            if (child.name not in openNames) and (child.name not in closed):
                openList.append(child)
                openNames.append(child.name)
            elif (child.name in openNames):
                index=openNames.index(child.name)
                if (child.cost<openList[index].cost):
                    openNames.remove(openList[index].name)
                    openNames.append(child.name)
                    openList.remove(openList[index])
                    openList.append(child)
            elif (child.name in closed):
                index=closedNames.index(child.name)
                if (child.cost < closed[index].cost):
                    closedNames.remove(closed[index].name)
                    closed.remove(closed[index])
                    openList.append(child)
                    openNames.append(child.name)
        closed.append(currnode)
        closedNames.append(currnode.name)
        openList, openNames=sort(openList)

def A():
    openList=[]
    openNames=[]
    root = Node(startState.rstrip())
    root.cost = 0
    root.parent=Node("root")
    root.state = [startState.rstrip() + " " + str(root.cost)]
    openList.append(root)
    openNames.append(root.name)
    closed=[]
    closedNames=[]
    while (True):
        if (len(openList)==0):
            return 0
        currnode=openList.pop(0)
        openNames.pop(0)
        if (currnode.name.rstrip()==goalState.rstrip()):
            return currnode
        children=AExpand(currnode)
        while len(children)!=0:
            child=children.pop(0)
            if (child.name not in openNames) and (child.name not in closed):
                openList.append(child)
                openNames.append(child.name)
            elif (child.name in openNames):
                index=openNames.index(child.name)
                if (child.heuristic<openList[index].heuristic):
                    openNames.remove(openList[index].name)
                    openNames.append(child.name)
                    openList.remove(openList[index])
                    openList.append(child)
                    
            elif (child.name in closed):
                index=closedNames.index(child.name)
                if (child.heuristic < closed[index].heuristic):
                    closedNames.remove(closed[index].name)
                    closed.remove(closed[index])
                    openList.append(child)
                    openNames.append(child.name)
        closed.append(currnode)
        closedNames.append(currnode.name)
        openList, openNames=sortHeuristic(openList)

def DFS():
    root = Node(startState.rstrip())
    root.cost = 0
    root.state = [startState.rstrip() + " " + str(root.cost)]
    closed = []
    start = 0
    global goalFound, queue
    queue.append(root)
    while (not goalFound):
        queueNames = []
        for item in queue:
            queueNames.append(item.name)
        if (start == 0):
            closed.append(queue[0].name)
            DFS1(queue[0])
            start = 1
        else:
            if (queue[0].name not in closed and queue[0].name not in queueNames[1:]):
                closed.append(queue[0].name)
                DFS1(queue[0])
            elif (queue[0].name not in closed and queue[0].name in queueNames[1:]):
                for i in range(1, len(queue)):
                    if queue[i].name == queue[0].name:
                        index = i
                        if ((queue[index].cost) > (queue[0].cost)):
                            queue[index].cost = queue[0].cost
                            queue[index].state = queue[0].state
                ignoreNode()
            else:
                ignoreNode()
filename=raw_input("Enter file name for reading:")
input_file = open(filename)
lines = input_file.readlines()

i = 0
j = 0
startState = lines[0]
goalState = lines[1]
numLive = lines[2]
algo=raw_input("Enter Algorithm to use: DFS, BFS, A* or UCS:")
liveFeed = [[0 for x in range(3)] for y in range(int(numLive))]
for k in range(3, int(numLive) + 3):
    j = 0
    part = lines[k].split()
    for eachPart in part:
        liveFeed[i][j] = eachPart
        j += 1
    i += 1
    
numSunday = lines[3 + int(numLive)]

i = 0
j = 0
sundayFeed = [[0 for x in range(2)] for y in range(int(numSunday))]
for k in range(int(numLive) + 4, int(numLive) + 4 + int(numSunday)):
    j = 0
    part = lines[k].split()
    for eachPart in part:
        sundayFeed[i][j] = eachPart
        j += 1
    i += 1

if (algo.rstrip() == "BFS"):
    a=search()
elif (algo.rstrip() == "DFS"):
    DFS()
elif (algo.rstrip() == "UCS"):
    a=UCS()
elif (algo.rstrip() == "A*"):
    a=A()
if (algo.rstrip() !="DFS"):
    b=a.parent
    sol=[]
    sol.append(a.name + " " + str(a.cost))
    while (b.name!="root"):
        sol.append(b.name + " " + str(b.cost))
        b=b.parent
    sol.reverse()

    output_file = open("output.txt", "w")
    for i in range(0, len(sol) - 1):
        output_file.write(sol[i])
        output_file.write("\n")
    output_file.write(sol[len(sol)-1])
    output_file.close()
