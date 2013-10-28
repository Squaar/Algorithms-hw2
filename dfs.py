#! /usr/bin/python

import sys

class BoardSpace:
	letter = None
	x = None
	y = None

	def __init__(self, let, x, y):
		self.letter = let
		self.x = x;
		self.y = y;
	
	def __repr__(self):
		return "{" + self.letter + "," + str(self.x) + "," + str(self.y) + "}"

def parseBoard(br):
	#print(br)
	gr = []
	for i in range(len(br)):
		for j in range(len(br[i])):
			#print(str(i) + ", " + str(j) + "\t" + br[i][j])
			gg = []
			gg.append(BoardSpace(br[i][j], i, j))
			if i > 0:
				gg.append(BoardSpace(br[i-1][j], i-1, j))
			if i < len(br)-1:
				gg.append(BoardSpace(br[i+1][j], i+1, j))
			if j > 0:
				gg.append(BoardSpace(br[i][j-1], i, j-1))
			if j < len(br[i])-1:
				gg.append(BoardSpace(br[i][j+1], i, j+1))
			gr.append(gg)
	return gr

def scoreNode(node, graph):
	return scoreNode_h(node, graph, [False for i in range(len(graph))])

def scoreNode_h(node, graph, visited):
	if visited[node[0].y*9+node[0].x]:
		return "V"
	else:
		visited[node[0].y*9+node[0].x] = True
	
	if node[0].letter == "B":
		return "B"
	elif node[0].letter == "W":
		return "W"
	
	prev = node[0].letter
	for n in node[1:len(node)]:
		if not visited[n.y*9+n.x]:
			cur = scoreNode_h(graph[n.y*9+n.x], graph, visited)
			if cur == "W" and prev == "B" or cur == "B" and prev == "W":
				return "X"
			elif cur == "W" or cur == "B":
				prev = cur
	
	return prev

fil = open(sys.argv[1], "r")
board = fil.read()
fil.close()

bb = board.split("\n");

graph = parseBoard(bb[0:len(bb)-1])
#print(graph)

black = 0
white = 0

for i in range(len(graph)):
	if graph[i][0].letter == "E":
		player = scoreNode(graph[i], graph)
		if player == "B":
			black += 1
		elif player == "W":
			white += 1
		else:
			print(player)
print("Black: " + str(black) + "\nWhite:" + str(white))

