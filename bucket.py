import numpy
import random
from time import time
from os import path
palettes = [0,1]
row = 700
column = 700
null = set()
grid = numpy.zeros((row,column))
'''for x,vx in enumerate(grid):
    for y,vy in enumerate(vx):
        grid[x][y] = random.choice(palettes)'''

def bucket(seq,pos,max_x,max_y,col = 2):
    pset = {pos}
    tempset = {pos}
    x,y = pos
    old_col = seq[x][y]
    while len(tempset):
        for i in tempset: #pos
            x,y = i
            seq[x][y] = col
            #up
            if x > 0:
                if seq[x-1][y] == old_col:
                    pset.add((x-1,y))
            #down
            if x < max_x:
                if seq[x+1][y] == old_col:
                    pset.add((x+1,y))
            #left
            if y > 0:
                if seq[x][y-1] == old_col:
                    pset.add((x,y-1))
            #right
            if y < max_y:
                if seq[x][y+1] == old_col:
                    pset.add((x,y+1))
            pset.remove(i) #pset new positions
        #tempset has old positions
        tempset = null.symmetric_difference(pset)
    return seq

print(f'old grid is \n{grid}' )            
t = time()
ngrid = bucket(grid,(0,0),row-1,column-1,2)
dt = time() - t
print(f'new grid is \n{ngrid}')
print(f'Time taken = {dt}')
dir_ = path.dirname(__file__)
print(dir_)