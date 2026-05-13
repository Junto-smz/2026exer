from def_node import Node
from def_listqueue import ListQueue
from exam1 import Song

objects = []
with open('song.dat','r',encoding='utf_8') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.rstrip()
        items = line.split(',')
        items[1] = Song(items[1],items[2:])  
        objects.append(items[1])

q = ListQueue()
for i in range(40,46):
    q.enqueue(objects[i])

for i in range(3):
    q.dequeue()
    
q.display()
