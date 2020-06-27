from PIL import Image
from numpy import *
import matplotlib.pylab as plt
def imresize(im,sz): #定义一个放缩函数
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))
def histeq(im,nbr_bins=256):#对一幅灰灰度图进行直方图均衡化
    imhist,bins=histogram(im.flatten(),nbr_bins,normed=True)#计算图像的直方图的数值
#numpy.histogram函数
#histogram(a, bins=10, range=None, normed=False, weights=None, density=None)
#a是待统计数据的数组；
#bins指定统计的区间个数；
#range是一个长度为2的元组，表示统计范围的最小值和最大值，默认值None，表示范围由数据的范围决定
#weights为数组的每个元素指定了权值,histogram()会对区间中数组所对应的权值进行求和
#density为True时，返回每个区间的概率密度；为False，返回每个区间中元素的个数
#返回值的解读imhist表明个数，bins表明区间
#flatten方法的解读:
#返回一个折叠成一维的数组
    cdf=imhist.cumsum()
#cumsum是将当前列之前的数加到当前列
    cdf=255*cdf/cdf[-1] #进行归一化,取最后一个元素，将其归一道0-1的范围之内
    im2=interp(im.flatten(),bins[:-1],cdf)
    #interp函数解读：
    #主要使用场景为一维线性插值
    #interp(x, xp, fp, left=None, right=None, period=None)
    #x: 数组，待插入数据的横坐标。
    #xp: 一维浮点数序列，原始数据点的横坐标，如果period参数没有指定那么就必须是递增的。否则，在使用xp = xp % period正则化之后，xp在内部进行排序.
    #fp: 一维浮点数或复数序列，原始数据点的纵坐标，和xp序列等长。
    #left: 可选参数，类型为浮点数或复数（对应于fp值），当x < xp[0]时的插值返回值，默认为fp[0]
    #right: 可选参数，类型为浮点数或复数（对应于fp值），当x > xp[-1]时的插值返回值，默认为fp[-1]
    #period: None或者浮点数，可选参数. 横坐标的周期. 此参数使得可以正确插入angular x-coordinates. 如果该参数被设定，那么忽略left参数和right参数
    #返回值，浮点数或复数（对应于fp值）或ndarray. 插入数据的纵坐标，和x形状相同。
    return im2.reshape(im.shape),cdf
def histeq_rest():
    im=plt.array(Image.open("test.jpg").convert('L'))
    im2,cdf=histeq(im)
    plt.figure("函数图像对比")
    plt.subplot(221)
    plt.imshow(im)
    plt.set_cmap('gray')
    plt.axis('off')
    plt.title('before')
    plt.subplot(223)
    plt.imshow(im2)
    plt.set_cmap('gray')
    plt.axis('off')
    plt.title('after')
    plt.subplot(222)
    plt.hist(im.flatten())
    plt.title('before')
    plt.subplot(224)
    plt.hist(cdf)
    plt.title('after')
    plt.show()
histeq_rest()
