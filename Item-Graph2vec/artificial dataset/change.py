import itertools
import numpy as np
from collections import defaultdict

def load(lines, dict):
    for m in range(len(lines)):
        temp = lines[m].strip().split(' ')
        list1 = list(itertools.combinations(temp, 2))
        for k in list1:
            dict[k]+=1
            ##dict[k]=dict.get(k,0)+1
        print(m)

def run():
    #item-item2是原数据即每个用户看的所有电影 ， 以pecanpy数据形式写进25_pecan里
    with open('train_1_1_0.1%') as f, open('graph_1_1_0.1%', 'w') as fp:
        lines = f.readlines()
        dict = defaultdict(int) #初始化为0
        load(lines,dict)
        for key in dict:
            fp.write('%s\t%s\t%d\n' % (key[0], key[1], dict[key]))

if __name__=='__main__':
    run()




