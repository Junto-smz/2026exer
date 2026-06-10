# 穴埋め問題用のプログラム
from def_stop import Stop # Stopクラスの読み込み
import time # 実行時間を計測するためのモジュール
import sys # 再帰呼び出し回数の上限を変更するためのモジュール
sys.setrecursionlimit(10000) # 再帰呼び出し回数の上限を10000回に変更

class DB: # DBクラスの定義
    def __init__(self):
        self.list = [] # データを格納するリスト

    def add(self, data):
        self.list.append(data) # データをリストの末尾に挿入


class DBwLinerSearch(DB): # 線形探索用のクラス
    def search(self, query):
        for item in self.list: # ループでリストの先頭からチェック
            if item.id == query:
                return item.name
        return None # ループを抜ければ、探しているデータはなし


fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
lines = fi.readlines()
queries = ['ED01_1653', 'ED01_4089', 'ED01_5000']
db = DBwLinerSearch()
for line in lines:
    line = line.rstrip()
    items = line.split(' ') # 1行を半角スペースで区切ってitemsリストに代入
    db.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:])) # StopオブジェクトをDBwLinerSearchのインスタンスに追加
for query in queries:
    start = time.perf_counter() # 探索前の時間を記録
    result = db.search(query)
    elapsed_time =  time.perf_counter() - start  # 探索後の時間から探索前の時間を引き、実行時間を計測
    print("ID:{}は{}です。{}は{}秒かかりました。".format(query, result, db.__class__.__name__, elapsed_time)) # 「オブジェクト名.__class__.__name__」でオブジェクトのクラス名を取得
fi.close()
