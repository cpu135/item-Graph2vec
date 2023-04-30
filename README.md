# item-Graph2vec

a Fast and Efficient Method for Item Embedding from the Item Co-occurrence Graph, with Applications to Collaborative Filtering

## Usage

###Anime dataset

1. Compile [fasttext](https://github.com/facebookresearch/fastText) under root of the project

2. Download Anime dataset:
https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020

    Data initialization
    
    ```
    $ python item2vec-input.py Anime && python Graph-item2vec-input.py Anime
    ```

3. Train model by running fasttext and pecanpy.

    ```
    $ ./fastText/fasttext skipgram -input ./item2vec-Anime-input.txt -output ./models/item2vec-Anime-model -minCount 5 -epoch 50 -neg 100
    ```
    ```
    $ pecanpy --input Graph-item2vec-Anime-input.txt --output ./models/Graph-item2vec-Anime-model.emb --mode SparseOTF --verbose --weighted --directed --p 1 --q 0.001 --walk-length 200 --num-walks 40 --dimensions 100
    ```
  
4. Anime accuracy testing

    ```
    $ cd ./Anime
    $ python genre.py 
    $ python result.py --top 1 -- num 10
    ```

###Movielens dataset

1. Download movielens dataset:
https://grouplens.org/datasets/movielens/25m/
    Data initialization
    
    ```
    $ python item2vec-input.py Movielens && python Graph-item2vec-input.py Movielens
    ```

3. Train model by running fasttext and pecanpy.

    ```
    $ ./fastText/fasttext skipgram -input ./item2vec-Movielens-input.txt -output ./models/item2vec-Movielens-model -minCount 5 -epoch 50 -neg 100
    ```
    ```
    $ pecanpy --input Graph-item2vec-Movielens-input.txt --output ./models/Graph-item2vec-Movielens-model.emb --mode SparseOTF --verbose --weighted --directed --p 1 --q 0.001 --walk-length 200 --num-walks 40 --dimensions 100
    ```
  
4. Movielens accuracy testing

    ```
    $ cd ./movielens
    $ python result.py --top 1 -- num 10
    ```

###Douban dataset

The operation is similar to the previous two data sets，specific can refer to: https://github.com/lujiaying/MovieTaster-Open

###t-SNE 

After performing Douban data accuracy test   

    ```
    $ cd ./douban
    $ python t-SNE.py 
    ```
    
    
###artificial dataset

    ```
    $ cd ./artificial dataset
    $ python deal.py --m 10000 --n 10000 --den 0.001
    $ python change.py 
    ```
   Then, the model is still generated using fasttext and pecanpy，refer to above.
    
##Related environment configuration

This code base is implemented in Python 3.6 and up

