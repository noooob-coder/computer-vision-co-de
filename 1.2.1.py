from PIL import Image
from matplotlib.pylab import *
im = array(Image.open("test.jpg"))#将图像读取到数组中
imshow(im)  #绘制图像
x=[100,100,200,200]
y=[150,150,200,200]
plot(x,y,"g*",linewidth=2) #对坐标点标红
#g*的解
#linewidth表示线的粗细
#其中g标志绘制的颜色，g-绿色，b-蓝色等
#*表示绘制的形状，.表示点，v表示实心倒三角，o表示实心圆等
plot(x,y,"g--")  #绘制x，y的连线
#对g--参数的解读，g表颜色同上
#--表示绘制类型，-表实线，--表示虚线，-.表示点划线
title('plotting') #设置图像的标题
axis('off')#不显示坐标轴
show()  #将图像展示出来
#show命令打开GUI，然后新建一个图像窗口，该图形用户界面会循环阻断脚本，然后暂停，知道最后一个图像窗口关闭
#在每个脚本里只能调用一次show命令