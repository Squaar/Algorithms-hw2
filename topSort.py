#!/usr/bin/python

def calcDegrees(): #calculate degrees of all nodes
	for i in graph:
		if i is not None:
			for j in range(1, len(i)):
				inDegrees[i[j]] += 1

	for i in range(1, len(inDegrees)):
		if inDegrees[i]==0:
			if i not in degreeZero:
				degreeZero.append(i)


def removeNode(n): #removes node n from all lists
	degreeZero.remove(n)

	inDegrees[n] = None
	for i in range(len(inDegrees)):
		if inDegrees[i] is not None:
			inDegrees[i] = 0

	graph[n-1] = None
	for i in range(len(graph)):
		if graph[i] is not None:
			try:
				graph[i].remove(n)
			except ValueError:
				pass




#graph = [[1,2,3,4], [2,3,5], [3,4,5], [4,5], [5]] #graph to sort
graph = [[1, 2], [2, 4, 5, 6], [3, 1, 4], [4, 7], [5], [6, 5], [7, 8], [8, 6]] #this graph almost works...
print "Graph: ", graph

degreeZero = [] #queue of nodes with degree 0
inDegrees = [None] + [0] * len(graph) #there is no 0 node
ans = []

calcDegrees()

while len(degreeZero) > 0:
	ans.append(degreeZero[0])
	removeNode(degreeZero[0])
	calcDegrees()

print "Sorted: ", ans
