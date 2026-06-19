# 穴埋め問題用のプログラム
class Neighbor:
    def __init__(self, id, label):
        self.id = id  # 隣接ノードのID
        self.label = label  # 隣接ノードと接続するエッジのラベル

class Graph:
    def __init__(self):
        self.node_list = {}  # グラフ上のノードリスト(辞書：key=ノードID, value=近傍)
        self.num_nodes = 0  # グラフ上のノードの数
        self.num_edges = 0  # グラフ上のエッジの数

    def add_node(self, id):  # グラフにノードを追加するメソッド
        if id not in self.node_list:  # ノードリストにidのノードが無ければ
            self.node_list[id] = []  # ノードリストにidのノードを追加する．ただし、近傍はないので[]を代入
            self.num_nodes += 1  # ノードの数をインクリメント

    def add_directed_edge(self, sid, tid, label):  # グラフに有向エッジを追加するメソッド
        if sid not in self.node_list:  # 始点のノードが無ければ追加
            self.add_node(sid)
        if tid not in self.node_list:  # 終点のノードが無ければ追加
            self.add_node(tid)
        self.node_list[sid].insert(0, Neighbor(tid, label))  # 近傍リストに終点のノードを追加
        self.num_edges += 1  # エッジの数をインクリメント

    def add_undirected_edge(self, sid, tid, label):  # グラフに無向エッジを追加するメソッド
        self.add_directed_edge(sid, tid, label)  # 両方向にエッジを追加
        self.add_directed_edge(tid, sid, label)
        self.num_edges -= 1  # エッジの数が重複するのでデクリメント

    def get_node_list(self):
        return self.node_list

    def get_neighborhood(self, id):
        if id in self.node_list:
            return self.node_list[id]
        else:
            return None

    def get_num_nodes(self):
        return self.num_nodes

    def get_num_edges(self):
        return self.num_edges

    def print_graph(self):  # 隣接リストを表示するメソッド
        for id in self.get_node_list():
            for neighbor in self.get_neighborhood(id):
                print('{} is connected to {} by {}.'.format(id, neighbor.id, neighbor.label))

if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('kyotocitybus_line.dat', 'r', encoding = 'utf-8')
    bus_network = Graph()
    lines = fi.readlines()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        bus_network.add_undirected_edge(items[0], items[1], items[3])  # 無向エッジを追加
    print('ノード(バス停)の数は{}個'.format(bus_network.get_num_nodes()))
    print('エッジ(バス停間のリンク)の数は{}個'.format(bus_network.get_num_edges()))
    bus_network.print_graph()
    fi.close()
