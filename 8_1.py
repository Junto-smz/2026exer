# 穴埋め問題用のプログラム
from def_stop import Stop  # Stopクラスの読み込み
from def_heap import Heap  # Heapクラスの読み込み
from def_queue_stack import Queue  # Queueクラスの読み込み
from def_db import DB  # DBクラスの読み込み
import time  # 実行時間を計測するためのモジュール


class DBwHeapSort(DB):  # ヒープソート用のクラス
    def __init__(self):
        super().__init__()  # 親クラスの__init()__の呼び出し
        self.heap = Heap()  # ヒープのインスタンスを生成
        self.queue = Queue()  # キューのインスタンスを生成

    def sort(self):
        self.heap.build_heap(self.list)  # self.listからヒープを構築
        min = self.heap.delete_min()  # ヒープの根を取得
        while min is not None:  # ヒープの根が取得できる限り繰り返す
            self.queue.enqueue(min)  # ヒープの根をキューに追加
            min = self.heap.delete_min()  # ヒープの根を取得する
        i = 0
        min = self.queue.dequeue()  # キューからデータを取り出す
        while min is not None:  # キューからデータを取り出せる限り繰り返す
            self.list[i] = min  # 取り出したデータをDBのリストに追加する
            i += 1
            min = self.queue.dequeue()  # キューからデータを取り出す


if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    db = DBwHeapSort()
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
