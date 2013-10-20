#!/usr/bin/python

def calcDegrees():
	pass

def removeNode(n):
	pass

graph = [[1,2,3,4],[2,3,5],[3,4,5],[4,5],[5]]

degreeZero = []
inDegrees = []
ans = []

calcDegrees()

while len(degreeZero) > 0:
	ans.append(degreeZero[0])
	removeNode(degreeZero[0])
	calcDegrees()

print(ans)
