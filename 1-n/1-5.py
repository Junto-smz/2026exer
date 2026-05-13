import matplotlib.pyplot

x = list()
height = list()
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
        x.append(key)
        height.append(item_dict[key])
matplotlib.pyplot.bar(x,height,width= 0.9)
matplotlib.pyplot.show()