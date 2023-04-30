import json
MovieFile = '../datas/corpus/movie_0804_09.json'
DoulistFile = '../datas/corpus/doulist_0804_09.json'
name_category={}
with open(MovieFile,'r') as fopen:
    for line in fopen:
        movie_dict = json.loads(line.strip())
        name_category[movie_dict['movie_name']]=movie_dict['movie_category']

# name  ----- category

# name   ----- id
min_word_freq=0
movie_counter = {}
with open(DoulistFile) as fopen:
    for line in fopen:
        doulist_dict = json.loads(line.strip())
        for movie_name in doulist_dict['movie_names']:
            if movie_name not in movie_counter:
                movie_counter[movie_name] = 0
            movie_counter[movie_name] += 1
movie_freq = filter(lambda _: _[1] >= min_word_freq, movie_counter.items())
movie_counter_sorted = sorted(movie_freq, key=lambda x: (-x[1], x[0]))
movies, _ = list(zip(*movie_counter_sorted))
movie_name_id_dict = dict(zip(movies, range(len(movies))))
movie_name_id_dict['<unk>'] = len(movies)

#id -- category
id_category={}
for i in movie_name_id_dict.keys():
    if i in name_category.keys():
        id_category[movie_name_id_dict[i]]=name_category[i]
    else:
        id_category[movie_name_id_dict[i]]='未知'


num={}
for i in id_category.values():
    if i not in num.keys():
        num[i]=1
    else:
        num[i]=num[i]+1

