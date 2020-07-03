from PIL import Image
from matplotlib.pylab import *
import pickle
with open("test.pkl",'wb') as f:
    im_data=Image.open("test.jpg")
    pickle.dump(im_data,f)#将数据存入f打开的文件中

with open("test.pkl",'rb') as f_r:
    im_recive=array(pickle.load(f_r))
    imshow(im_recive)
    f_r.close()
