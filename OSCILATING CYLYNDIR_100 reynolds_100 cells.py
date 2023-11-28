

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import pyplot
import math


plot_every= 10
def distance(x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2 +(y2-y1)**2)

def main():
    Nx= 400
    Ny=100
    tau=0.53
    Nt=40000
    a=Nx/5
    b=Ny/2
    count=1
    som=2
    lol=-1
  



    
    Nl=9
    cxs=np.array([0,0,1,1,1,0,-1,-1,-1])
    cys=np.array([0,1,1,0,-1,-1,-1,0,1])
    weights=np.array([4/9,1/9,1/36,1/9,1/36,1/9,1/36,1/9,1/36])
    F=np.ones((Ny,Nx,Nl))+.01*np.random.randn(Ny,Nx,Nl)
    
    cde=np.ones(Nt)
    
    timestep=np.ones(Nt)

    F[:,:,3]=2.5
    rho=np.sum(F,2)
    pre=np.sum(F,2)/3
    ux=np.sum(F*cxs,2) / rho
    uy = np.sum(F* cys,2) / rho
    mx=np.sum(F*cxs,2)
    
    cylyndir=np.full((Ny,Nx),False)
   
    
    for it in range(40000):
        print(it)
  
        
        
        
        
     
        
        
        for y in range(0,Ny):
            for x in range(0,Nx):
               if(it%1==0):
                   if (count%2==0):
                       if(distance(a,b+(som*0.05),x,y)<12):
                           cylyndir [y][x]=True

                             
                        
                
                   elif(count%2!=0):
                
                        if(distance(a,b+(som*0.05),x,y)<12):
                            cylyndir [y][x]=True
        
        som=som+(lol**count) 
        if(it%400==0):
           count=count+1
         
           
           
           
                    
                    
        
        F[:,-1,[6,7,8]]=F[:,-2,[6,7,8]]
        F[:,0,[2,3,4]]=F[:,1,[2,3,4]]
        F[-1,:,[8,1,2]]=F[-2,:,[8,1,2]]
        F[0,:,[6,5,4]]=F[1,:,[6,5,4]]
        
        
        for i,cx,cy in zip(range(Nl), cxs , cys):
            F[:,:,i]=np.roll(F[:,:,i],cx,axis =1 )
            F[:,:,i]=np.roll(F[:,:,i],cy,axis =0 )
        
        bndryF=F[cylyndir,:]
        bndryF=bndryF[:,[0,5,6,7,8,1,2,3,4]]
        
        rho=np.sum(F,2)
        pre=np.sum(F,2)/3
        ux=np.sum(F*cxs,2) / rho
        uy = np.sum(F* cys,2) / rho
        mx=np.sum(F*cxs,2)
        cd= (((np.sum(mx[:,20])/100)-(np.sum(mx[:,300])/100))/(0.5*rho[20,20]*ux[20,20]*ux[20,20]*0.5))+1
        
        cde[it]=cd
        timestep[it]=it
        
        
         
        F[cylyndir,:]=bndryF
        ux[cylyndir]=0
        uy[cylyndir]=0
        
        Feq=np.zeros(F.shape)
        for i, cx,cy,w in zip(range(Nl),cxs,cys,weights):
            Feq[:,:,i]=rho*w*(1+3*(cx*ux + cy*uy)+9*(cx*ux+cy*uy)**2 / 2-3*(ux**2+uy**2)/2)
            
        
        F=F + -(1/tau)*(F-Feq)
        cylyndir=np.full((Ny,Nx),False)
        if(it%50== 0):
                  pyplot.imshow(np.sqrt(ux**2+uy**2), cmap='jet')
                  pyplot.pause(0.00001)
                  pyplot.cla()
        if(it%1000== 0):
            plt.plot(timestep,cde)
            plt.show()
            
        
        
        
        
    if(it%plot_every == 0):
              
              
              im = plt.imshow((ux**2+uy**2), cmap='jet')
              plt.colorbar(im)
              plt.show()
        
          
     
      
       
            

        
if __name__ =="__main__":
    main()
    
    
        
        
    
            
            
            