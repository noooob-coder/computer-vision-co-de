from matplotlib.pylab import *
from PIL import Image
im=array(Image.open("test.jpg"))
imshow(im)
print("进行三次点击")
x=ginput(3)
#ginput获取点击的三个点的坐标并存入x列表
print(x)
