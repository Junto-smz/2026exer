# 穴埋め問題用のプログラム
from def_graph import Graph  # Graphクラスの読み込み

class GraphWalk(Graph):
    def walk_along_route(self, start, step, route):
        visited = [start]  # 開始地点のノードIDを訪問済みリストに追加
        parents = {start:None}  # 直前のノードとそれに接続するエッジのペア（タプル）を格納する辞書（key=訪問中ノードID、value=(直前のノードID, エッジラベル)）
        current = start  # 開始地点のノードIDを探索基点のノードに設定
        for i in range(step):  # step分、訪問を繰り返す
            if current not in self.node_list:  # 訪問中ノードが存在しなければ
                print('{}のノードがグラフ上に存在しません。'.format(current))
                return
            neighbors = self.get_neighborhood(current)  # 訪問中ノードの隣接ノードを取得
            if neighbors != []:  # 隣接ノードがあれば以下を実行
                for i in range(len(neighbors)):
                    if neighbors[i].id not in visited and (neighbors[i].label == route):
                        visited.append(neighbors[i].id)  # 次の訪問先を訪問する
                        parents[neighbors[i].id] = (current, neighbors[i].label)  # 訪問中ノードIDとそれに接続するエッジをparents辞書に追加
                        current = neighbors[i].id  # 訪問先候補を次の訪問先に決定
                        break
            else:  # 隣接ノードが無ければ終了
                print('{}から{}ステップ分進むパスはありません。'.format(start, step))
                return
        # 訪問したノードを訪問順に表示する
        path = visited[0]  # 最初に訪問したノードをpathに代入
        for v in visited[1:]:  # 訪問した順にノードを取得
            path = path + ' --[' + parents[v][1] +']--> ' + v  # 次の訪問先と辿ったエッジをpathに連結
        print(path)


if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
    fi = open('kyotocitybus_line.dat', 'r', encoding = 'utf-8')
    bus_network = GraphWalk()
    lines = fi.readlines()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
        bus_network.add_undirected_edge(items[0], items[1], items[3])  # 無向エッジを追加
    bus_network.walk_along_route('ED01_1914', 5, '快速202号系統')
    fi.close()
