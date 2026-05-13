from def_node import Node,print_linked_list
from exam1 import Song

objects = []
with open(r'C:\courses\2026exer\exam1-student\song.dat','r',encoding='utf_8') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.rstrip()
        items = line.split(',')
        objects.append(Song(items[1],items[2:]))

top1 = None
top2 = None
for i in range(1,5):
    top1 = Node(objects[i],top1)

for i in range(6,8):
    top2 = Node(objects[i],top2)
    

print('L1\':')
print_linked_list(top1)

print('L2\':')
print_linked_list(top2)

top2.next.next = top1.next.next
top1.next.next = top2

print('L1\'')
print_linked_list(top1)
