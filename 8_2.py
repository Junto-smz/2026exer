# 穴埋め問題用のプログラム
from def_stop import Stop  # Stopクラスの読み込み
from def_heap import Heap  # Heapクラスの読み込み
from def_queue_stack import Queue  # Queueクラスの読み込み
from def_db import DB  # DBクラスの読み込み
import time  # 実行時間を計測するためのモジュール


class DBwMergeSort(DB):  # ヒープソート用のクラス
    def __init__(self):
        super().__init__()  # 親クラスの__init()__の呼び出し
          # キューのインスタンスを生成

    def sort(self,list=None):

        size = self.count()
        if size <= 1:
            return self.list
        middle = size // 2
        left = self.list[0:middle]
        right = self.list[middle:size-1]
        
        left = self.sort(left)
        right = self.sort(right)
        
        self.merge(left,right)
    
    def merge(self,left,right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].lng < right[j].lng:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        if i == len(left):
            while j <= len(right):
                result.append(right[j])
                j += 1
        else:
            while i <= len(left):
                result.append(left[i])  
                i += 1
        return result
                


if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    db = DBwMergeSort()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        db.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))  # Stopオブジェクトを各DBインスタンスに追加
    start = time.time()  # ソート前の時間を記録（time()は現在時刻を返すメソッド）
    db.sort()  # データのソートを実行
    elapsed_time = time.time() - start  # ソート後の時間からソート前の時間を引き実行時間計測
    db.display()
    if db.is_sorted():
        print("ソートが完了しました！{}は{}秒かかりました。".format(db.__class__.__name__, elapsed_time))  # __class__はインスタンスのクラスを返し、__name__はそのクラスの名前を返す
    fi.close()
