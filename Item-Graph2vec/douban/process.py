#coding: utf-8
import csv
import json
import itertools
import numpy as np
VecFile='../models/item2vec-douban-model.vec'

DoulistFile = '../datas/corpus/doulist_0804_09.json'
MovieFile = '../datas/corpus/movie_0804_09.json'
DoulistCorpusIdFile = DoulistFile.replace('json', 'movie_id')
DoulistCorpusNameFile = DoulistFile.replace('json', 'movie_name')

def get_movie_name_id_dict(doulist_file=DoulistFile, min_word_freq=0):
    movie_counter = {}
    with open(doulist_file) as fopen:
        for line in fopen:
            doulist_dict = json.loads(line.strip())
            for movie_name in doulist_dict['movie_names']:
                movie_name = movie_name
                if movie_name not in movie_counter:
                    movie_counter[movie_name] = 0
                movie_counter[movie_name] += 1
    movie_freq = filter(lambda _:_[1] >= min_word_freq, movie_counter.items())
    movie_counter_sorted = sorted(movie_freq, key=lambda x: (-x[1], x[0]))
    movies, _ = list(zip(*movie_counter_sorted))
    movie_name_id_dict = dict(zip(movies, range(len(movies))))
    movie_name_id_dict['<unk>'] = len(movies)
    print('movie_name_id_dict is %d from [%s]' % (len(movie_name_id_dict), doulist_file))
    return movie_name_id_dict #按照电影的出现次数排序，依次标好id

def get_movie_id_name_dict(doulist_file=DoulistFile):
    movie_name_id_dict = get_movie_name_id_dict(doulist_file)
    movie_id_name_dict = dict([(_[1], _[0]) for _ in movie_name_id_dict.items()])
    print('movie_id_name_dict is %d from [%s]' % (len(movie_id_name_dict), doulist_file))
    return movie_id_name_dict

def get_movie_name_category_dict(moviefile=MovieFile):
    name_category = {}
    with open(moviefile, 'r') as fopen:
        for line in fopen:
            movie_dict = json.loads(line.strip())
            name_category[movie_dict['movie_name']] = movie_dict['movie_category']
        #csv文件读写
        # f_csv=csv.reader(fopen)
        # header=next(f_csv)
        # for line in f_csv:
        #     temp=line[8]
        #     temp=temp.strip().split('/')
        #     name_category[line[1]]=temp

    return name_category

def get_movie_id_category_dict(moviefile=MovieFile):
    name_category=get_movie_name_category_dict()
    id_category = {}
    movie_name_id_dict=get_movie_name_id_dict()
    for name in movie_name_id_dict.keys():
        if name in name_category.keys():
            id_category[movie_name_id_dict[name]] = name_category[name]
        else:
            id_category[movie_name_id_dict[name]] = '未知'
    return  id_category

def get_movie_user_name_dict(doulist_file=DoulistFile):
    user_moviename={}
    with open(doulist_file) as fopen:
        for line in fopen:
            doulist_dict = json.loads(line.strip())
            if len(doulist_dict['movie_names'])>=20:
                user_moviename[doulist_dict['list_id']]=doulist_dict['movie_names']

def load_vectors(input_file=VecFile):
    vectors = {}
    with open(VecFile) as fopen:
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

def process2corpus():
    movie_name_id_dict = get_movie_name_id_dict()
    print('total movie is %d from [%s], [%s]' % (len(movie_name_id_dict), DoulistFile, MovieFile))
    unk_id = 0

    vec=load_vectors(VecFile)
    with open(DoulistFile) as fopen, open(DoulistCorpusNameFile, 'w') as fwrite, open(DoulistCorpusIdFile, 'w') as fwrite_1,open('douban_pecan','w') as fp:
        dict={}
        for line in fopen:
            move = []
            doulist_dict = json.loads(line.strip())
            doulist_movies = [_ for _ in doulist_dict['movie_names']]
            doulist_movie_ids = [int(movie_name_id_dict[_]) for _ in doulist_movies]
            fwrite.write('%s\n' % ('\t'.join(str(doulist_movies))))
            fwrite_1.write('%s\n' % (' '.join(str(doulist_movie_ids))))
            temp=sorted(doulist_movie_ids)

            for id in temp:  # 只保留跟item2vec训练出来的模型相同的id
                if id not in vec.keys():
                    move.append(id)
            for id in move:
                temp.remove(id)
            list1 = list(itertools.combinations(temp, 2))
            for k in list1:
                if k in dict:
                    dict[k] += 1
                else:
                    dict[k] = 1
        for key in dict:
            fp.write('%s\t%s\t%d\n' % (key[0], key[1], dict[key]))

if __name__ == '__main__':
   process2corpus()
   get_movie_name_category_dict()