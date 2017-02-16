#!/usr/bin/python

import sys

fileName = sys.argv[1]
searchString = sys.argv[2]
linesRemoved = 0

print 'Reading file ', fileName; 
print 'Script will remove all ocurrences of: ', searchString

file = open(fileName,"r+")
lines = file.readlines()

file.seek(0)
for line in lines:
    if searchString not in line:
        file.write(line)
    else:
        linesRemoved = linesRemoved + 1
print 'File cleaned saving changes...'

file.truncate()
file.close()

print 'Completed, lines removed ', linesRemoved