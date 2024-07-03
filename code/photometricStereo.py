import numpy as np
from scipy.linalg import lstsq

def photometricStereo(imarray, lightdirs):
    h , w , n = imarray.shape
    pixels = h*w
    albedo = np.zeros((h,w))
    normals = np.zeros((h,w,3))
    imarry2D = imarray.reshape(pixels,n)
    for i in range(pixels):
        I=imarry2D[i,:]
        g, _,_,_ = lstsq(lightdirs,I)
        albedo[i//w,i%w] = np.linalg.norm(g)
        normals[i//w,i%w,:]= g/albedo[i//w,i%w]
    return albedo,normals
