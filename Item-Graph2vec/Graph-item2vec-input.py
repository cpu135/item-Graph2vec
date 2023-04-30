import csv
import pandas as pd
import sys
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

# python item2vec-input.py Anime
if len(sys.argv) < 2:
    print("Please provide a valid argument: Douban, Movielens or Anime")
    sys.exit()

arg = sys.argv[1]

if arg == 'Douban':
    def run():
        with open('item2vec-Douban-input.txt') as f, open('Graph-item2vec-Douban-input', 'w') as fp:
            lines = f.readlines()
            dict = defaultdict(int)  # 初始化为0
            load(lines, dict)
            for key in dict:
                fp.write('%s\t%s\t%d\n' % (key[0], key[1], dict[key]))


    if __name__ == '__main__':
        run()

elif arg == 'Movielens':
    def run():
        with open('item2vec-Movielens-input.txt') as f, open('Graph-item2vec-Movielens-input', 'w') as fp:
            lines = f.readlines()
            dict = defaultdict(int)  # 初始化为0
            load(lines, dict)
            for key in dict:
                fp.write('%s\t%s\t%d\n' % (key[0], key[1], dict[key]))


    if __name__ == '__main__':
        run()

elif arg == 'Anime':
    def run():
        with open('item2vec-Anime-input.txt') as f, open('Graph-item2vec-Anime-input', 'w') as fp:
            lines = f.readlines()
            dict = defaultdict(int)  # 初始化为0
            load(lines, dict)
            for key in dict:
                fp.write('%s\t%s\t%d\n' % (key[0], key[1], dict[key]))

    if __name__ == '__main__':
        run()

else:
    print("Please provide a valid argument: Douban, Movielens or Anime")











