#! /usr/bin/python

import sys

def parseBoard(br):
	print(br)
	gr = []
	for i in range(len(br)):
		for j in range(len(br[i])):
			print(str(i) + ", " + str(j) + "\t" + br[i][j])
			gg = []
			gg.append(br[i][j])
			if i > 0:
				gg.append(br[i-1][j])
			if i < len(br)-1:
				gg.append(br[i+1][j])
			if j > 0:
				gg.append(br[i][j-1])
			if j < len(br[i])-1:
				gg.append(br[i][j+1])
			gr.append(gg)
	return gr

fil = open(sys.argv[1], 'r')
board = fil.read()
fil.close()

bb = board.split('\n');

graph = parseBoard(bb[0:len(bb)-1])
print(graph)
