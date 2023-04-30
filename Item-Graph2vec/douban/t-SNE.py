from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import gensim.models.keyedvectors as word2vec
from category import id_category
import plotly
import numpy as np
import plotly.graph_objs as go
from sklearn.decomposition import PCA
# x=range(1,300)
# y=range(1,300)
# c=range(1,300)
#
# plt.scatter(x,y,s=40,c=c)
# plt.show()
#输出结果的t-SNE图！！! ! !

# from orgdata import color,dict

# color={'犯罪':300, '爱情':0, '喜剧':150, '音乐':120, '纪录片':180, '动作':220, '冒险':240, '动画':270,
# '科幻':90}
color={'犯罪':'c', '爱情':'y', '喜剧':'g', '纪录片':'r', '动作':'b', '动画':'k'}
#电影及对应的类型 id_category
#筛选之后的向量
filename = '../models/item2vec-douban-model.vec'
#filename='../models/Graph-item2vec-douban-model.emb'
modelX = word2vec.KeyedVectors.load_word2vec_format(filename)    #单词向量的加载
words = list(modelX.index_to_key)   #压缩成2堆
del(words[0])
z=[]                #对应的颜色标号
list = []

for word in words:
    if id_category.get(int(word)) in color.keys():
        z.append(color.get(id_category.get(int(word))))
    else:
        list.append(word)

for i in list:
    words.remove(i)

num={}
for word in words:
    if id_category.get(int(word)) in num.keys():
        num[id_category.get(int(word))] = num[id_category.get(int(word))] + 1
    else:
        num[id_category.get(int(word))] = 1
print(num)
X = modelX[words]
X_tsne = TSNE(n_components=2,n_iter=1000).fit_transform(X)
plt.figure(figsize=(30,15))
plt.scatter(X_tsne[:,0],X_tsne[:,1],s=15,c=z)
plt.title('Graph_item2vec')
plt.show()

# for i in range(len(X_tsne)):
#     x=X_tsne[i][0]
#     y=X_tsne[i][1]
#     plt.text(x,y,list[i],size=16)


