import numpy as np

def prepareData(imArray, ambientImage):
    for i in range(imArray.shape[2]):
        imArray[:,:,i] -= ambientImage
        imArray[:,:,i][imArray[:,:,i]<0]=0
    maxIntensity=np.max(imArray)
    return imArray/maxIntensity