from PIL import Image
from numpy import *
#pca算法的目的：在尽可能保持训练数据信息的情况下降低维度
def pca(x):
    num_data,dim=x.shape
    #获取为数
    mean_x=x.mean(axis=0)
    x=x-mean_x#对数据进行中心化处理
    if dim>num_data:
        m=dot(x,x.T) #获取协方差矩阵
        e,EV=linalg.eigh(m) #获取特征值和特征向量
        tmp = dot(x.T,EV).T
        V=tmp[::-1]
        S=sqrt(e)[::-1]
    else:
        U,S,V=linalg.svd(x)
        V=V[:num_data] #仅仅返回前nun_data维的数据
    return V,S,mean_x

