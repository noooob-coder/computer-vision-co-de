from PIL import Image
from numpy import *
def compute_average(imlist):
    averageim=array(Image.open(imlist[0]),'f')
    for imname in imlist[1:]:
        try:
            averageim +=array(Image.open(imname))
        except:
            print(imname+'...skipped')
    averageim /=len(imlist)
    return array(averageim,'uint8')