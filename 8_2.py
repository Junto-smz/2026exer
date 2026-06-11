from def_stop import Stop  # Stopクラスの読み込み
from def_heap import Heap  # Heapクラスの読み込み
from def_queue_stack import Queue  # Queueクラスの読み込み
from def_db import DB  # DBクラスの読み込み
import time  # 実行時間を計測するためのモジュール


class DBwMergeSort(DB):  # マージソート用のクラス
    def __init__(self):
        super().__init__()  # 親クラスの__init()__の呼び出し

    def sort(self, target_list=None):
        # 初回呼び出し（引数なし）の時は、DBが持つ全体のリストを対象にする
        if target_list is None:
            target_list = self.list

        # self.count() ではなく、引数で渡されたリストのサイズを計測する
        size = len(target_list)
        if size <= 1:
            return target_list
            
        middle = size // 2
        # スライスの範囲を正しく修正（末尾まで含める）
        left = target_list[0:middle]
        right = target_list[middle:size]
        
        # 分割したリストを再帰的にソート
        left = self.sort(left)
        right = self.sort(right)
        
        # ソート済みの左右のリストをマージ
        merged_list = self.merge(left, right)
        
        # 最上位の呼び出し（全体のソート）が終わったら、元の self.list を更新する
        if len(target_list) == len(self.list):
            self.list = merged_list
            
        return merged_list
    
    def merge(self, left, right):
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
        
        # 不等号を < に修正して IndexError を防止
        if i == len(left):
            while j < len(right):
                result.append(right[j])
                j += 1
        else:
            while i < len(left):
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
