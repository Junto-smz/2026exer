import matplotlib.pyplot as plt

class Stop:
    def __init__(self, id, name, lat, lng,route): # 初期化メソッド
        self.id = id # インスタンス変数に値を代入
        self.name = name
        self.lat = lat
        self.lng = lng
        self.route = route
    
    def count_routes(self):
        return len(self.route)

with open(r'C:\courses\2026exer\kyotocitybus_stop.dat','r',encoding='utf-8') as f1:
    lines = f1.readlines()
    
lats = list()
lngs = list()
nums = list()
for line in lines:
    line.rstrip()
    items = line.split(' ')
    items[1] = Stop(items[0],items[1],float(items[2]),float(items[3]),items[4:])
    lats.append(items[1].lat)
    lngs.append(items[1].lng)
    nums.append(items[1].count_routes())
    
plt.scatter(lngs,lats,s = nums)
plt.show()
