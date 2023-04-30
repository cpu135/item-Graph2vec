import random
import numpy as np
import argparse
import itertools
from multiprocessing import Pool,Lock

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
#type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('--m',dest='m',type=int,help='多少个用户')
parser.add_argument('--n',dest='n',type=int,help='每个用户多少部电影')
parser.add_argument('--den',dest='density',type=float,help='密度')
args = parser.parse_args()

m=args.m
n=args.n
den=args.density
# m=10000
# n=10000
# den=0.001
x_shape=(m,n)
num=m*n*den  #看过的个数
matr = np.zeros(x_shape, int)
file = 'train_'+str(int(m/10000))+'_'+str(int(n/10000))+'_'+str(den*100)+'%'
lock = Lock()
def load(k,pronum,matr):
    sum=k
    with open(file, 'w') as fp:
        while sum<len(matr):
            temp = []
            for row in range(len(matr[sum])):
                if matr[sum][row] == 1:
                    temp.append(row)
            lock.acquire()
            for k in temp:
                fp.write('%s ' % (k))
            fp.write('\n')
            print(sum)
            sum+=pronum
            lock.release()

def run():
    processNum = 1
    pool = Pool(processes=processNum)
    for k in range(processNum):
        pool.apply_async(func=load,args=(k,processNum,matr))
    pool.close()
    pool.join()

if __name__=='__main__':
    for k in range(int(num)):
        while True:
            a = random.randint(0, m-1)
            b = random.randint(0, n-1)
            if matr[a][b] == 0:
                matr[a][b] += 1
                break
            else:
                continue
    run()


