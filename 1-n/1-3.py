# 穴埋め問題用プログラム
fi = open('../kyotocitybus_stop.dat', 'r', encoding = 'utf-8')
lines = fi.readlines()
for line in lines:    
    line = line.rstrip()
    items = line.split(' ')  # 1行を半角スペースで区切ってitems リストに代入
    if  items[1] =='立命館大学前':
        print(','.join(items[4:]))  # カンマを区切り文字としてitemsリストの要素を連結
        break
fi.close()