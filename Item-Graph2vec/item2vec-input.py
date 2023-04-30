import csv
import pandas as pd
import sys

# python item2vec-input.py Anime
if len(sys.argv) < 2:
    print("Please provide a valid argument: Douban, Movielens or Anime")
    sys.exit()

arg = sys.argv[1]

if arg == 'Douban':
    # 读取CSV文件，假设文件中有以下列：user_id, movie_id, rating
    df = pd.read_csv('ratings.csv')
    # 将数据按照 user_id 进行分组
    grouped = df.groupby('userId')
    # 遍历每个分组，将每个分组中的 movie_id 放入一个 list 中
    # 将每个 userId 的 movieId 放入同一个列表中，并将每个列表作为一行写入文件
    with open('item2vec-Douban-input.txt', 'w') as file:
        for name, group in grouped:
            movie_list = list(group['movieId'])
            movie_list = [str(item) for item in movie_list]
            line = ' '.join(movie_list)
            file.write(line + '\n')

    print("Running Movielens code...")

elif arg == 'Movielens':
    # 读取CSV文件，假设文件中有以下列：user_id, movie_id, rating
    df = pd.read_csv('./ml-25m/ratings.csv')
    # 将数据按照 user_id 进行分组
    grouped = df.groupby('userId')
    # 遍历每个分组，将每个分组中的 movie_id 放入一个 list 中
    # 将每个 userId 的 movieId 放入同一个列表中，并将每个列表作为一行写入文件
    with open('item2vec-Moivelens-input.txt', 'w') as file:
        for name, group in grouped:
            movie_list = list(group['movieId'])
            movie_list = [str(item) for item in movie_list]
            line = ' '.join(movie_list)
            file.write(line + '\n')

    print("Running Movielens code...")

elif arg == 'Anime':
    # 读取CSV文件，假设文件中有以下列：user_id, movie_id, rating
    df = pd.read_csv('./archive/rating_complete.csv')
    # 将数据按照 user_id 进行分组
    grouped = df.groupby('user_id')
    # 遍历每个分组，将每个分组中的 movie_id 放入一个 list 中
    # 将每个 userId 的 movieId 放入同一个列表中，并将每个列表作为一行写入文件
    with open('item2vec-Anime-input.txt', 'w') as file:
        for name, group in grouped:
            movie_list = list(group['anime_id'])
            movie_list = [str(item) for item in movie_list]
            line = ' '.join(movie_list)
            file.write(line + '\n')

    print("Running Anime code...")

else:
    print("Please provide a valid argument: Douban, Movielens or Anime")
