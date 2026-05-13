# 穴埋め用のプログラム
# StopクラスおよびStopインスタンスの定義をdef_stop.pyからインポート
from def_stop import Stop, ritsumeikan, doshisha, kyodai, kyosan, ryukoku


# Nodeクラスの定義
class Node:
    def __init__(self, data, next=None):
    # nextにデフォルト値（何も値が渡されなかった時に設定される値）を設定
        self.data = data  # データを格納するインスタンス変数
        self.next = next  # 連結される次の節を指すインスタンス変数


# 連結リストを末尾の「龍谷大学前」から順に作成する
top = Node(ryukoku)  # Nodeインスタンスを作成し、連結リストのリストヘッドtopに代入
p = Node(kyosan)  # Nodeインスタンスを作成
p.next = top  # 作成したNodeインスタンス(p)の次に連結リストの先頭(top)を連結
top = p  # 作成したNodeインスタンス(p)が連結リストの先頭となるようにリストヘッドtopを更新
p = None  # 不要になった変数pをNoneに更新
top = Node(kyodai, top)  # 連結リストの先頭（top）の前にNodeインスタンスを挿入し、そのNodeインスタンスが連結リストの先頭となるようにリストヘッドtopを更新（上記5行分を簡潔に1行で記述）
top = Node(doshisha, top)  # 上と同様
top = Node(ritsumeikan, top)  # 上と同様

message = '{}(ID:{})のバス停の緯度経度は({},{})です。'
p = top
print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
p = p.next
print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
p = p.next
print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
p = p.next
print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
p = p.next
print(message.format(p.data.name, p.data.id, p.data.lat, p.data.lng))
