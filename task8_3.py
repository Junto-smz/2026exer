from def_stop import Stop  # Stopクラスの読み込み
from def_heap import Heap  # Heapクラスの読み込み
from def_queue_stack import Queue  # Queueクラスの読み込み
from def_db import DB  # DBクラスの読み込み
import time  # 実行時間を計測するためのモジュール


class DBwQuickSort(DB):  # クイックソート用のクラス
    def __init__(self):
        super().__init__()  # 親クラスの__init()__の呼び出し

    def sort(self, target_list=None):
        # 初回呼び出し（引数なし）の時は、DBが持つ全体のリストを対象にする
        if target_list is None:
            target_list = self.list

        # ベースケース：要素数が1以下ならそのまま返す
        size = len(target_list)
        if size <= 1:
            return target_list

        # ピボット（基準値）として中央の要素を選択
        pivot_stop = target_list[size // 2]
        pivot_val = pivot_stop.lng

        left = []    # ピボットより小さい要素のリスト
        middle = []  # ピボットと等しい要素のリスト
        right = []   # ピボットより大きい要素のリスト

        # 各要素をピボットと比較して3つのグループに分配
        for stop in target_list:
            if stop.lng < pivot_val:
                left.append(stop)
            elif stop.lng > pivot_val:
                right.append(stop)
            else:
                middle.append(stop)

        # 左右のリストを再帰的にソートし、結合する
        sorted_list = self.sort(left) + middle + self.sort(right)

        # 最上位の呼び出し（全体のソート）が終わったら、元の self.list を更新する
        if len(target_list) == len(self.list):
            self.list = sorted_list

        return sorted_list


if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    
    # ここでインスタンス化するクラスを DBwQuickSort に変更
    db = DBwQuickSort()
    
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        db.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))  # Stopオブジェクトを各DBインスタンスに追加
        
    start = time.time()  # ソート前の時間を記録
    db.sort()  # ポリモーフィズムにより、どのソートクラスでも同じ呼び出し方になります
    elapsed_time = time.time() - start  # 実行時間計測
    
    db.display()
    if db.is_sorted():
        # クラス名が自動的に「DBwQuickSort」と出力されます
        print("ソートが完了しました！{}は{}秒かかりました。".format(db.__class__.__name__, elapsed_time))
    fi.close()
