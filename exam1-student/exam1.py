class Song():
    def __init__(self,name,artists):
        self.name = name
        self.artists = artists
    
    def count_artists(self):
        return len(self.artists)
        
objects = []
with open(r'C:\courses\2026exer\exam1-student\song.dat','r',encoding='utf_8') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.rstrip()
        items = line.split(',')
        items[1] = Song(items[1],items[2:])  
        objects.append(items[1])

message = '{}には{}組のアーティストが参加しています。'
for i in range(1,6):
    print(message.format(objects[i].name,objects[i].count_artists()))
    