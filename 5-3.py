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

class DBwRecursiveSearch(DB): # 線形探索用のクラス
    def search(self, query):
        # 1. リストが空になった（見つからなかった）場合の終了条件を追加
        if not self.list:
            return None
            
        if self.list[0].id == query:
            return self.list[0].name
        else:
            self.list.pop(0)
            # 2. self を削除し、再帰の結果を return するように修正
            return self.search(query)

class DBwBinarySearch(DB): # 線形探索用のクラス
    def search(self, query, left=0, right=None):
        # 初回呼び出し時（rightがNone）は、探索範囲をリスト全体に設定
        if right is None:
            right = len(self.list) - 1
            
        # ベースケース1: 探索範囲が逆転した場合はデータなし
        if left > right:
            return None
            
        # 中央のインデックスを計算
        mid = (left + right) // 2
        
        # ベースケース2: 中央のデータが一致した場合
        if int(self.list[mid].id[5:]) == int(query[5:]):
            return self.list[mid].name
            
        # 再帰ステップ1: 目的のIDが中央より小さい場合、左側を探索
        elif int(self.list[mid].id[5:]) > int(query[5:]):
            return self.search(query, left, mid -1)
            
        # 再帰ステップ2: 目的のIDが中央より大きい場合、右側を探索
        else:
            return self.search(query, mid + 1, right)
             

fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
lines = fi.readlines()
queries = ['ED01_1653', 'ED01_4089', 'ED01_5000']
db1 = DBwBinarySearch()
db2 = DBwLinerSearch()
db3 = DBwBinarySearch()
for line in lines:
    line = line.rstrip()
    items = line.split(' ') # 1行を半角スペースで区切ってitemsリストに代入
    db1.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:])) # StopオブジェクトをDBwLinerSearchのインスタンスに追加
    db2.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:])) # StopオブジェクトをDBwLinerSearchのインスタンスに追加
    db3.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:])) # StopオブジェクトをDBwLinerSearchのインスタンスに追加
for query in queries:
    start = time.perf_counter() # 探索前の時間を記録
    result = db1.search(query)
    elapsed_time =  time.perf_counter() - start  # 探索後の時間から探索前の時間を引き、実行時間を計測
    print("ID:{}は{}です。{}は{}秒かかりました。".format(query, result, db1.__class__.__name__, elapsed_time)) # 「オブジェクト名.__class__.__name__」でオブジェクトのクラス名を取得
for query in queries:
    start = time.perf_counter() # 探索前の時間を記録
    result = db2.search(query)
    elapsed_time =  time.perf_counter() - start  # 探索後の時間から探索前の時間を引き、実行時間を計測
    print("ID:{}は{}です。{}は{}秒かかりました。".format(query, result, db2.__class__.__name__, elapsed_time)) # 「オブジェクト名.__class__.__name__」でオブジェクトのクラス名を取得
for query in queries:
    start = time.perf_counter() # 探索前の時間を記録
    result = db3.search(query)
    elapsed_time =  time.perf_counter() - start  # 探索後の時間から探索前の時間を引き、実行時間を計測
    print("ID:{}は{}です。{}は{}秒かかりました。".format(query, result, db3.__class__.__name__, elapsed_time)) # 「オブジェクト名.__class__.__name__」でオブジェクトのクラス名を取得

fi.close()
