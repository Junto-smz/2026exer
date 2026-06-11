from def_stop import Stop  # Stopクラスの読み込み
from def_heap import Heap  # Heapクラスの読み込み
from def_queue_stack import Queue  # Queueクラスの読み込み
from def_db import DB  # DBクラスの読み込み
import time  # 実行時間を計測するためのモジュール
from task8_1 import DBwHeapSort
from task8_2 import DBwMergeSort
from task8_3 import DBwQuickSort

if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    
    # ここでインスタンス化するクラスを DBwQuickSort に変更
    dbs = [DBwHeapSort(),DBwMergeSort(),DBwQuickSort()]
    
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        for db in dbs:
            db.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))  # Stopオブジェクトを各DBインスタンスに追加
    
    for db in dbs:
        start = time.time()  # ソート前の時間を記録
        db.sort()  # ポリモーフィズムにより、どのソートクラスでも同じ呼び出し方になります
        elapsed_time = time.time() - start  # 実行時間計測
        if db.is_sorted():
            # クラス名が自動的に「DBwQuickSort」と出力されます
            print("ソートが完了しました！{}は{}秒かかりました。".format(db.__class__.__name__, elapsed_time))
        fi.close()
