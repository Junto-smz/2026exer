# 穴埋め用のプログラム
# StopクラスおよびStopインスタンスの定義をdef_stop.pyからインポート
from def_stop import Stop

# Nodeクラスの定義
class Node:
    def __init__(self, data, next=None):
    # nextにデフォルト値（何も値が渡されなかった時に設定される値）を設定
        self.data = data  # データを格納するインスタンス変数
        self.next = next  # 連結される次の節を指すインスタンス変数
        
stops = []
node_flag = True
with open(r'C:\courses\2026exer\kyotocitybus_stop.dat', 'r', encoding='utf_8') as f1:
    lines = f1.readlines()
    for line in lines:
        line.rstrip()
        items = line.split(' ')
        items[1] = Stop(items[0],items[1],float(items[2]),float(items[3]),items[4:])
        if node_flag:
            top = Node(items[1])
            node_flag = False
        else:
            top = Node(items[1],top)


print('{}({})のバス停の緯度経度は({},{})です。'.format(top.data.name,top.data.id,top.data.lat,top.data.lng))