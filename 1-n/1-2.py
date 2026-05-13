# 穴埋め問題用プログラム
fi = open('../kyotocitybus_stop.dat', 'r', encoding = 'utf-8')
lines = fi.readlines()
fi.close()
with open('kyotocitybus_stop_commma.dat','w',encoding='utf-8') as f2:
    for line in lines:    
        line = line.rstrip()
        items = line.split(' ')  # 1行を半角スペースで区切ってitems リストに代入
        f2.write(','.join(items))
        f2.write('\n')