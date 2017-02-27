"""
Usage : python Paths.py width height '0 0 0 1' .. obstructions details
output : Total number of paths possible
"""

import sys
import numpy as np

width = int(sys.argv[1])+1
height = int(sys.argv[2])+1
arr = np.zeros((width+1,height+1))
mapping = np.ones((width+1,height+1,width+1,height+1))
strings = []
length = 0

# Getting details of Objestructions
if(len(sys.argv)>3):
	strings = sys.argv[3:]
	length = len(strings)
for i in range(length):
	string = strings[i].split(' ')
	string = [int(s) for s in string]
	mapping[string[0],string[1],string[2],string[3]]=0
	mapping[string[2],string[3],string[0],string[1]]=0

#calculating number of paths possible
def noPaths(width, height):
	arr[1,1]=1;
	left = 0;
	down = 0;
	for j in xrange (1,height+1):
		for i in xrange(1,width+1):
			left = 0;
			down = 0;
			if mapping[i-1,j,i,j]==1:
				left = arr[i-1,j];
			if mapping[i,j-1,i,j]==1:
				down = arr[i,j-1];
			arr[i,j] = left+down+arr[i,j];
noPaths(width,height)

print arr[width,height]