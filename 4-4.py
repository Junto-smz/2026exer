from def_stop import Stop

class ListStack():
    def __init__(self):
        self.list = []
    
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        if len(self.list) != 0:
            return self.list.pop()
        else:
            print('スタックが空でPOPできません。')
            return None
    
    def display(self):
        print('=====スタックの先頭=====')
        message = '{}(ID:{})のバス停の緯度経度は({},{})です。'
        for i in reversed(self.list):
            print(message.format(i.name,i.id,i.lat,i.lng))
        print('=====スタックの底=====')

class ListQuene():
    def __init__(self):
        self.list = []
    
    def enqueue(self,data):
        self.list.append(data)
        
    def dequeue(self):
        if len(self.list) != 0:
            return self.list.pop(0)
        else:
            print('キューが空でDEQUENEできません。')
            return None
        
s = ListStack()
q = ListQuene()

with open('kyotocitybus_stop.dat', 'r', encoding='utf_8') as f1:
    lines = f1.readlines()
    for line in lines:
        line.rstrip()
        items = line.strip().split()
        items = Stop(items[0],items[1],float(items[2]),float(items[3]),items[4:])
        s.push(items)
        q.enqueue(items)
        
message = '{}(ID:{})のバス停の緯度経度は({},{})です。'
while True:
        i = s.pop()
        if i is not None:
            print(message.format(i.name,i.id,i.lat,i.lng))
        else:
            break
        
while True:
        k = q.dequeue()
        if k is not None:
            print(message.format(k.name,k.id,k.lat,k.lng))
        else:
            break