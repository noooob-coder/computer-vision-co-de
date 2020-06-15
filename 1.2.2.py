from matplotlib.pylab import *
from PIL import Image
im=array(Image.open("test.jpg").convert('L'))#将图片以灰度的形式打开并存放到数组中
figure()
#figure函数的解读：
#其作用是创建一个新的窗口
#figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
#num:图像编号或名称，数字为编号 ，字符串为名称
#figsize:指定figure的宽和高，单位为英寸；
#dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张
#facecolor:背景颜色
#edgecolor:边框颜色
#frameon:是否显示边框
gray() #不使用颜色信息，将图片设置为灰色
contour(im,origin='image')#设置在原点的左上方显示图像的轮廓
axis('equal')
axis('off')#不显示坐标轴
figure()#再新建一个窗口
hist(im.flatten(),128)
#利用hist函数绘制直方图
#hist函数的第二个参数指定小区间的数目
#hist只接受一维数组作为输入，所以在绘制直方图之前先对图像进行压平处理
#flatten方法将任意数组按照行优先准则转换成一维数组
show()