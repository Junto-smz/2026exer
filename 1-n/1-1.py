# 穴埋め問題用プログラム
fi = open('../kyotocitybus_stop.dat', 'r', encoding = 'utf-8')
lines = fi.readlines()
for line in lines:    
    line = line.rstrip()
    items = line.split(' ')  # 1行を半角スペースで区切ってitems リストに代入
    print(','.join(items))  # カンマを区切り文字としてitemsリストの要素を連結
fi.close()