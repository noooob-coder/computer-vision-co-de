from PIL import Image
import os
img=Image.open("test.jpg")
#返回只img是一个pil图像对象
#默认将图片以RGB格式打开

img_L=Image.open("test.jpg").convert('L')
#此时返回的是灰度图
#图片颜色的转换用convert方法来实现
#以下为convert方法介绍
#模式“1”为二值图像（非黑即白）
#模式“L”为灰度图，每个像素包含8个bit，0表示黑，255表示白
#“RGB”转“L"通过L=R*299/1000+G*587/1000+B*114/1000
#模式“P”为8位彩色图像，它的每个像素用8个bit表示，其对应的彩色值是按照调色板查询出来的。
#模式“RGBA”为32位彩色图像，它的每个像素用32个bit表示，其中24bit表示红色、绿色和蓝色三个通道，另外8bit表示alpha通道，即透明通道。
#模式“CMYK”为32位彩色图像，它的每个像素用32个bit表示。模式“CMYK”就是印刷四分色模式，它是彩色印刷时采用的一种套色模式，利用色料的三原色混色原理，加上黑色油墨，共计四种颜色混合叠加，形成所谓“全彩印刷”。
#四种标准颜色是：C：Cyan = 青色，又称为‘天蓝色’或是‘湛蓝’M：Magenta = 品红色，又称为‘洋红色’；Y：Yellow = 黄色；K：Key Plate(blacK) = 定位套版色（黑色）。
#从实例中可以得知PIL中“RGB”转换为“CMYK”的公式如下：
#C = 255 - R
#M = 255 - G
# Y = 255 - B
# K = 0
#模式“YCbCr”为24位彩色图像，它的每个像素用24个bit表示。YCbCr其中Y是指亮度分量，Cb指蓝色色度分量，而Cr指红色色度分量。人的肉眼对视频的Y分量更敏感，因此在通过对色度分量进行子采样来减少色度分量后，肉眼将察觉不到的图像质量的变化。
# 模式“RGB”转换为“YCbCr”的公式如下：
# Y= 0.257*R+0.504*G+0.098*B+16
# Cb = -0.148*R-0.291*G+0.439*B+128
# Cr = 0.439*R-0.368*G-0.071*B+128
# 模式“I”为32位整型灰色图像，它的每个像素用32个bit表示，0表示黑，255表示白，(0,255)之间的数字表示不同的灰度。在PIL中，从模式“RGB”转换为“I”模式是按照下面的公式转换的：
# I = R * 299/1000 + G * 587/1000 + B * 114/1000
# 模式“F”为32位浮点灰色图像，它的每个像素用32个bit表示，0表示黑，255表示白，(0,255)之间的数字表示不同的灰度。在PIL中，从模式“RGB”转换为“F”模式是按照下面的公式转换的：
# F = R * 299/1000+ G * 587/1000 + B * 114/1000
# 模式“F”与模式“L”的转换公式是一样的，都是RGB转换为灰色值的公式，但模式“F”会保留小数部分
#注：部分内容转自：https://blog.csdn.net/icamera0/article/details/50843172

img_L.save("test_L.jpg")
#pil通过save方法将一个图像对象进行保存

img_L.thumbnail((64,64))
img_L.save("test_thumbnail.jpg")
#pil通过thumbnail方法进行图像的缩放
#thumbnail方法接受一个元组参数，该参数指定生成缩略图的大小
#该方法是对调用该方法的图像进行缩略，其返回值为null


box=(20,20,50,50)
region=img.crop(box)
region.save("region.jpg")
#crop方法是从一副图像中裁剪指定区域
#该区域使用4元组来指定。分别是（左，上，右，下）。同时PIL指定左上角为（0，0）
#其中box的具体定义见图1-1，box（b1,a1,b2,a2）
img.paste(region,box)
#paste方法是将一个图片放到另一个图片的指定区域，其中region为图片，box为区域大小（其定义同上）


img_resize=img.resize((64,64))
img_resize.save("resize.jpg")
# resize()方法可以缩小也可以放大，而thumbnail()方法只能缩小；
# resize()方法不会改变对象的大小，只会返回一个新的Image对象，而thumbnail()方法会直接改变对象的大小，返回值为none；
# resize()方法中的size参数直接规定了修改后的大小，而thumbnail()方法按比例缩小，size参数只规定修改后size的最大值。
# resize()中的size参数直接设定了resize之后图片的规格,而thumbnail()中的size参数则是设定了x/y上的最大值. 也就是说, 经过resize()处理的图片可能会被拉伸,而经过thumbnail()处理的图片不会被拉伸

img_rotate=img.rotate(45)
img_rotate.save("rotate.jpg")
#rotate方法将图片进行逆时针旋转，接受的参数为旋转角度




