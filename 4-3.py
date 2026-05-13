# 穴埋め問題用のプログラム
# StopクラスおよびStopインスタンスのimport
from def_stop import Stop, ritsumeikan, doshisha, kyodai, kyosan, ryukoku
# Nodeクラスの定義をdef_node.pyからインポート
from def_node import Node

# Stackクラスの定義
class Quene:
    def __init__(self):
        self.top = None # 連結リストの先頭を指すリストヘッドのインスタンス変数
        self.rear = None
    def display(self):  # スタック内の連結リストを表示するメソッド
        print('======キューの先頭======')
        message = '{}(ID:{})のバス停の緯度経度は({},{})です。'
        p = self.top  # 走査用変数pを連結リストの先頭に設定する
        while p is not None:  # 走査用変数pが連結リストの終端でない限り、以下の処理を繰り返す
            print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
            p = p.next  # 走査用変数pを次の節に一つ進める
        print('======キューの底======')

    def enquene(self, data):  # enquneメソッド
        if(isinstance(data, Stop)):  # enquneするデータがStopインスタンスかどうか確認
            if self.top == None:
                self.top = Node(data,self.top)
                self.rear = self.top
            else:
                p = Node(data)
                self.rear.next = p
                self.rear = p
        else:
            print('Stopインスタンス以外はENQUENEできません。')
    
    def dequene(self):
        if self.top != None:
            p = self.top
            self.top = self.top.next
            p.next = None
            if self.top == None:
                self.rear == None
            return p
        else:
            print('キューが空でDEQUENEできません。')
            return None
            

s = Quene()  # スタック(Queneインスタンス)を生成

s.enquene(1)  # Stopインスタンス以外をenqune
s.enquene(ritsumeikan)  # スタックにStopインスタンスをenquneする
s.enquene(doshisha)
s.enquene(kyodai)
s.enquene(kyosan)
s.enquene(ryukoku)

s.display()  # スタックを表示する

message = '{}(ID:{})のバス停の緯度経度は({},{})です。'
while s is not None:
    p = s.dequene()
    if p is not None:
        print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
    else:
        break
