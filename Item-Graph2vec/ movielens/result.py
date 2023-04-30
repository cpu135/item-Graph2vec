# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import numpy as np
from scipy import stats
import os
import math
import json
import argparse
import random
import heapq
import importlib,sys
from log_tool import data_process_logger as logger
import csv

genres = {}
with open('../ml-25m/movies.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过第一行
    for row in reader:
        genres[int(row[0])] = row[2].split('|')

#25M数据
VecFile = '../models/item2vec-movielens-model.vec'
VecFile2 = '../models/Graph-item2vec-movielens-model.emb'
importlib.reload(sys)

class minHeap():
    def __init__(self, k):
        self._k = k
        self._heap = []

    def add(self, item):
        if len(self._heap) < self._k:
            self._heap.append(item)
            heapq.heapify(self._heap)
        else:
            if item > self._heap[0]:
                self._heap[0] = item
                heapq.heapify(self._heap)

    def get_min(self):
        if len(self._heap) > 0:
            return self._heap[0]
        else:
            return -2

    def get_all(self):
        return self._heap

def similarity(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return np.dot(v1, v2) / n1 / n2

def load_vectors(input_file):
    vectors = {}
    with open(input_file) as fopen:
        fopen.readline()
        for line in fopen:
            line_list = line.strip().split()
            if not line_list[0].isdigit():
                continue
            movie_id = int(line_list[0])
            vec = np.array([float(_) for _ in line_list[1:]], dtype=float)
            if not movie_id in vectors:
                vectors[movie_id] = vec
    return vectors

def topk_like(cur_movie_id, vector,k=5, print_log=False)->int:
    global sum
    min_heap = minHeap(k)
    like_candidates = []
    #logger.debug('vecotrs size=%d' % (len(vectors)))
    #logger.debug('cur_movie_name %s, %s' % (cur_movie_name, type(cur_movie_name)))
    if isinstance(cur_movie_id, str):
        cur_movie_name = cur_movie_id.encode('utf8')

    # if cur_movie_id not in vectors:
    #     return []
    cur_vec = vector[cur_movie_id]
    if print_log:
        logger.info('[%d] %s top %d likes:' % (cur_movie_id,genres[cur_movie_id],k))
    for movie_id, vec in vector.items():
        if movie_id == cur_movie_id:
            continue
        sim = similarity(cur_vec, vec)
        if len(like_candidates) < k or sim > min_heap.get_min():
            min_heap.add(sim)
            like_candidates.append((movie_id, sim))
    num = 0
    #print(len(like_candidates))
    if print_log:
        for t in sorted(like_candidates, reverse=True, key=lambda _:_[1])[:k]:
            logger.info('         [%d] %f  %s' % (t[0], t[1],genres[t[0]]))
            for genre in genres[cur_movie_id]:
                if genre in genres[t[0]]:
                    num=num+1
                    break
    if k > len(like_candidates):
        k = len(like_candidates)
    sum=sum+num/k
    #return sorted(like_candidates, reverse=True, key=lambda _:_[1])[:k]

vectors = load_vectors(VecFile)
vectors2=load_vectors(VecFile2)
sum=0
parser = argparse.ArgumentParser(description='命令行中传入一个数字')
#type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('--top',dest='top',type=int,help='选择每部电影列出的top几')
parser.add_argument('--num',dest='num',type=int,help='随机挑选多少部电影')
args = parser.parse_args()


if __name__ == '__main__':
    #随机100个种子电影 --seed
    k = args.top  # top几
    num = args.num
    accurancy1 = []
    accurancy2 = []
    num=100
    for k in range(1,2):
        seed = []
        sum = 0
        for i in range(0, 1000):
            temp = random.choice(list(vectors.keys()))
            if temp in vectors2.keys():
                seed.append(temp)
        movie_ids = seed[:num]
        for movie_id in movie_ids:
            topk_like(movie_id, vectors, k, print_log=True)
        accurancy1.append(sum / num)
        sum = 0
        for movie_id in movie_ids:
            topk_like(movie_id, vectors2, k, print_log=True)
        accurancy2.append(sum / num)

    for acc1 in accurancy1:
        print("item2vec--%d个电影top%d的精度：%f"%(num,k,acc1))
        k+=1
    k=1
    for acc2 in accurancy2:
        print("graph2vec--%d个电影top%d的精度：%f"%(num,k,acc2))
        k+=1
    # k = 1
    # for i in accurancy:
    #     print("100个电影top%d的精度：%f" % (k, i))
    #     k += 1
