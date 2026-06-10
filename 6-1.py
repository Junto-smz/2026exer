# 穴埋め問題用のプログラム
from def_stop import Stop  # Stopクラスの読み込み
import time  # 実行時間を計測するためのモジュール


class DB:  # DBクラスの定義
    def __init__(self):
        self.list = []  # データを格納するリスト

    def add(self, data):
        self.list.append(data)  # データをリストの末尾に挿入

    def display(self):
        message = '{}: {}(ID:{})のバス停の緯度経度は({},{})です。'
        j = 1
        for i in self.list:
            print(message.format(j, i.name, i.id, i.lat, i.lng))
            j += 1

    def count(self):  # データの件数を返す
        return len(self.list)

    def sort(self):  # データを昇順にソートする
        pass

    def is_sorted(self, descent = False):  # 降順の場合は引数にTrue
        for i in range(self.count()-1):
            if not descent and (self.list[i].lng > self.list[i+1].lng or self.list[i].id == self.list[i+1].id):
                return False
            elif descent and (self.list[i].lng < self.list[i+1].lng or self.list[i].id == self.list[i+1].id):
                return False
        return True


class DBwBubbleSort(DB):  # バブルソート用のクラス
    def sort(self):
        n = self.count()  # データ件数を取得
        for i in range(n-1, 0, -1):  # 右端から順に2番目の要素まで最大値を確定させていく
            for j in range(i):  # 左端から順に比較＆入換えを繰り返す
                if self.list[j].lng > self.list[j+1].lng:  # 左側の方が大きい場合
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]  # スワップ

if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    db = DBwBubbleSort()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        db.add(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))  # Stopインスタンスをdbに追加
    start = time.time()  # ソート前の時間を記録（time()は現在時刻を返すメソッド）
    db.sort()  # データのソートを実行
    elapsed_time = time.time() - start  # ソート後の時間からソート前の時間を引き、実行時間を計測
    db.display()
    if db.is_sorted():
        print("ソートが完了しました！{}は{}秒かかりました。".format(db.__class__.__name__, elapsed_time))  # __class__はインスタンスのクラスを返し、__name__はそのクラスの名前を返す
    fi.close()
