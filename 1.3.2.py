from PIL import Image
from numpy import *
from matplotlib.pylab import *
im= array(Image.open("test.jpg").convert('L'))
im2=255-im #对图像进行反向处理
im3=(100.0/255)*im+100 #将图像的像素值变到100-200的区间内
im4=255.0*(im/255.0)**2#对图像的像素值求平方后得到的图像
figure("origin-im")
imshow(im)
figure("im-2")
imshow(im2)
figure("im-3")
imshow(im3)
figure("im-4")
imshow(im4)
print(im.min(),im.max())#输出最小值以及最大值
pil_im=Image.fromarray(uint8(im))#array的反向转换,如果不是uint8的数据类型应将其转换为uint8的数据类型

