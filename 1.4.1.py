from PIL import Image
from numpy import *
from scipy.ndimage import filters
from matplotlib.pylab import *
def First():
    im=array(Image.open('test.jpg').convert('L'))
    im2=filters.gaussian_filter(im,5)
    imshow(im2)

def Second():
    im = array(Image.open('test.jpg'))
    im2 = zeros(im.shape)
    for i in range(3):
        im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 5)
    im2 = uint8(im2)
    imshow(im2)
