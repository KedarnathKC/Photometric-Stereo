import numpy as np

np.random.seed(1)
    
def rowsum(fx,s,e,r):
    return np.sum(fx[r,s:e])

def colsum(fy,s,e,c):
    return np.sum(fy[s:e,c])

def rowcolumn(fx,fy):
    h,w= fx.shape
    height = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            height[i,j]+=rowsum(fx,0,j,0)
            height[i,j]+=colsum(fy,0,i,j) 
    return height

def columnrow(fx,fy):
    h,w = fx.shape
    height = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            height[i,j]+=colsum(fy,0,i,0)
            height[i,j]+=rowsum(fx,0,j,i)
    return height

def randompath1(fx,fy):
    h,w = fx.shape
    height = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            r=0
            c=0
            while(r==i or c==j):
                if(np.random.randint(100)%2==0): 
                    height[i,j]+=fx[r,c]
                    r+=1
                else:
                    height[i,j]+=fy[r,c]
                    c+=1    
            if(r==i):
                height[i,j]+=rowsum(fx,c,j,r)
            else:
                height[i,j]+=colsum(fy,r,i,c)
    return height
                        
def randompath2(fx,fy):
    h,w = fx.shape
    height = np.zeros((h,w))
    r=0
    c=0
    for i in range(h):
        for j in range(w):
            while(r==h or c==w):
                if(np.random.randint(100)%2!=0):
                    height[i,j]+=fx[r,c]
                    r+=1
                else:
                    height[i,j]+=fy[r,c]
                    c+=1    
            if(r==h):
                height[i,j]+=rowsum(fx,c,j,r)
            else:
                height[i,j]+=colsum(fy,r,i,c)
    return height



def getSurface(surfaceNormals, method):
    h,w,_ = surfaceNormals.shape
    height = np.zeros((h,w))
    surfaceNormals2D=surfaceNormals.reshape(h*w,3)
    fx = np.zeros((h,w))
    fy = np.zeros((h,w))
    for i in range(h*w):
        fx[i//w,i%w]=surfaceNormals2D[i,0]/surfaceNormals2D[i,2]
        fy[i//w,i%w]=surfaceNormals2D[i,1]/surfaceNormals2D[i,2]
    if method == 'row-column':
        height = rowcolumn(fx,fy)
    if method == 'column-row':
        height = columnrow(fx,fy)
    if method == 'average':
        average = 2*np.ones(height.shape)
        height=rowcolumn(fx,fy)
        height+=columnrow(fx,fy)
        height=np.divide(height,average)
    if method == 'random':
        average = 4*np.ones(height.shape)
        height=rowcolumn(fx,fy)
        height+=columnrow(fx,fy)
        height+=randompath1(fx,fy)
        height+=randompath2(fx,fy)
        height=np.divide(height,average)
    return height