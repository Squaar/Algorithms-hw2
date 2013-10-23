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
	if node[0].letter == 'B':
		return 'B'
	elif node[0].letter == 'W':
		return 'W'
	
	surround = 'E'
	for n in node[1:len(node)]:
		if n.letter == 'W' and surround == 'B' or n.letter == 'B' and surround == 'W':
			return 'X'
		else:
			surround = n.letter;
		

fil = open(sys.argv[1], 'r')
board = fil.read()
fil.close()

bb = board.split('\n');

graph = parseBoard(bb[0:len(bb)-1])
#print(graph)

black = 0
white = 0

for i in range(len(graph)):
	if graph[i][0].letter == "E":
		player = scoreNode(graph[i][0], graph)
		if player == 'B':
			black += 1
		elif player == 'W':
			white += 1
print("Black: " + str(black) + "\nWhite:" + str(white))

