class Stop:
    def __init__(self, id, name, lat, lng,route): # 初期化メソッド
        self.id = id # インスタンス変数に値を代入
        self.name = name
        self.lat = lat
        self.lng = lng
        self.route = route

with open('../kyotocitybus_stop.dat','r',encoding='utf-8') as f1:
    lines = f1.readlines()
    
names = list()
for line in lines:
    line.rstrip()
    items = line.split(' ')
    items[1] = Stop(items[0],items[1],float(items[2]),float(items[3]),items[4:])
    names.append(items[1])

num = names[-100]    
message = '{}(ID:{})のバス停の緯度経度は({},{})です。{}のバスが停まります。'
print(message.format(num.name, num.id, num.lat, num.lng, ','.join(num.route)))