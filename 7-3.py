from def_stop import Stop  # Stopクラスの読み込み
import sys  # 再帰呼び出し回数の上限を変更するためのモジュール
sys.setrecursionlimit(10000)  # 再帰呼び出し回数の上限を10,000回に変更


class Heap:  # Heapクラスの定義
    def __init__(self):
        self.list = [0]  # データを格納するリスト。0番目の要素は使わないため0を代入。
        self.size = 0

    def insert(self, data):
        self.list.append(data)  # データをヒープの最後の要素の次に挿入
        self.size += 1  # ヒープサイズを1増やす
        self.shift_up(self.size)  # 挿入した要素をシフトアップする

    def shift_up(self, num):  # num番目の要素をシフトアップ
        # num番目の要素が根でなく、num番目の要素の親の方が大きい場合、親子を入れ替え
        if (num > 1) and (self.list[num //2].lng > self.list[num].lng):
            self.list[num], self.list[num//2] = self.list[num//2], self.list[num]
            self.shift_up(num//2)  # 入れ替え後に、引き続き新しい親のシフトアップ

    def show_tree(self, num):  # num番目の要素を根とする木（もしくは部分木）を表示するメソッド
        if num <= self.size:  # 要素numがヒープサイズの範囲内である限り
            self.show_tree(num * 2 + 1)  # 要素numの右子を根とする部分木を表示
            i = num
            space = ''
            while i // 2 > 0:  # 要素numの深さ分だけ半角スペース2個を連結
                space += '  '
                i = i // 2
            print('{}{}:{}'.format(space, self.list[num].name, self.list[num].lng))  # 連結されたタブ（インデント）と要素numのバス停の名前と経度を表示
            self.show_tree(num * 2) # 要素numの左子を根とする部分木を表示

    def is_heap(self):  # ヒープ条件のチェック
        for i in range(self.size, 1, -1):
            if self.list[i].lng < self.list[i//2].lng:
                return False
        return True
 
    def shift_down(self,num):
        left = num*2
        if left > self.size:
            return
        
        smaller = left 
        right = left + 1
        
        if right <= self.size and self.list[right].lng < self.list[left].lng:
            smaller = right
        
        if self.list[num].lng > self.list[smaller].lng:
            self.list[num], self.list[smaller] = self.list[smaller],self.list[num]
            self.shift_down(smaller)
            
    def delete_min(self):
        self.list[1],self.list[-1] = self.list[-1],self.list[1]
        p = self.list.pop(-1)
        self.shift_down(1)
        return p
    
    def build_heap(self,list):
        self.size = len(list) - 1
        for num in range(self.size//2,0,-1):
            self.shift_down(num)
            
        
if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('allkyotobus_stop.dat', 'r', encoding = 'utf-8')
    lines = fi.readlines()
    heap = Heap()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        # StopインスタンスをHeapインスタンスに挿入
        heap.list.append(Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))

    
    heap.build_heap(heap.list)
    if heap.is_heap():
        heap.show_tree(1)