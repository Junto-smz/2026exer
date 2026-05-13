item_dict = dict()
with open('../kyotocitybus_stop.dat', 'r', encoding = 'utf-8') as fi:
    lines = fi.readlines()
    for line in lines:    
        line = line.rstrip()
        items = line.split(' ') 
        num = len(items[4:])
        if num not in item_dict:
            item_dict[num] = 1
        else:
            item_dict[num] += 1
    for key in item_dict:
        print(f'{key}本のバス路線が通っている停留所の合計は{item_dict[key]}個です。')