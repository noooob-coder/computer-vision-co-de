from PIL import Image
from matplotlib.pylab import *
im = array(Image.open("test.jpg"))
print("im",im.shape,im.dtype)
im_L = array(Image.open(("test.jpg")).convert("L"),'f')
#'f'参数，是以浮点数的形式存入数组
print("im_L",im_L.shape,im_L.dtype)
#shape输出图像的数组（行，列，颜色通道），dtype输出数组数据类型
value= im[100,120,2]
#取出坐标为（100，120）的第二个颜色通道的值
print(value)
#一些数组的操作
im_L[4,:]=im_L[5,:]
#将第5行的数值赋给第4行
im_L[:,6]=100
#将第6列的所有值置为100
im_L[:100,:50].sum()
#计算前100行前50列所有值的和
im_L[4].mean()
#计算第四行的平均数
im_L[:,-1]#最后一列
im_L[-2,:]#倒数第二行
