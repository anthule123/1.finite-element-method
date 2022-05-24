# %%
import numpy as np
import matplotlib.pyplot as plt
import gauss_quad_lib 
import element_lib2
from mpl_toolkits.mplot3d import Axes3D


# %%
N= 10
[a,b,c,d] = [0,1,0,1]
di = (b-a)/N
dj = (d-c)/N
root = [0,0]

# %%
nut = np.zeros( ((N+1)*(N+1), 2))
for i in range(0,N+1):
    for j in range(0,N+1):
        id = int( (N+1)*j+i)
        nut[id] = [di*i + root[0], dj*j + root[1]] 

# %%
so_tam_giac = N*N*4
triangle = np.zeros((so_tam_giac,3))
for i in range(0,N):
    for j in range(0,N):
        id1 = int(i*(N+1) + j)
        id2 = int(i*(N+1) + j+1)
        id3 = int((i+1)*(N+1) + j)
        id4 = int((i+1)*(N+1) + j+1)
        triangle[2*(N*i + j)] = [id1,id3,id4]
        triangle[2*(N*i+j)+1] = [id1,id2,id4]

# %%
#set Dirichlet nut
so_nut = (N+1)**2
Dirichlet = np.zeros(so_nut)  #dang boolean
val_Dirichlet = np.zeros(so_nut) #gia tri khoi tao

independ_re_index = np.zeros(so_nut)     # danh so lai cho nut doc lap
run = 0
for i in range(0, so_nut):
    if(i%(N+1)==0 or i%(N+1)==N or i<=N or i>=N*(N+1)):
        Dirichlet[i] = 1
        val_Dirichlet[i] = 0
    else: 
        independ_re_index[i] = int(run)
        run +=1
Global_matrix_vt = np.zeros((run, run))


# %%

for i in range(0, so_tam_giac):
    for j in range(0, 3):
        p1 = int(triangle[i][j])
        for k in range(j+1,3):
            p2 = int(triangle[i][k])
            p3 = 100
            if(j==0 and k== 1):
                p3 = int(triangle[i][2])
            if(j==0 and k== 2):
                p3 = int(triangle[i][1])
            if(j==1 and k== 2):
                p3 = int(triangle[i][0])    
            if(Dirichlet[p1]==0 and Dirichlet[p2]==0):
                q1 = int(independ_re_index[p1])
                q2 = int(independ_re_index[p2])                
                val= element_lib2.Element_Stiff(nut[p1][0],nut[p1][1],
                                                                       nut[p2][0],nut[p2][1],
                                                                     nut[p3][0],nut[p3][1])
                Global_matrix_vt[q1][q2] +=val
                Global_matrix_vt[q2][q1] +=val
            

# %%
for i in range(0, so_tam_giac):
    for j in range(0, 3):
        p1 = int(triangle[i][j])
        if(Dirichlet[p1]==0):
            p2=0
            p3=0
            if(j==0):
                p2 = int(triangle[i][1])  
                p3 = int(triangle[i][2])  
            if(j==1):
                p2 = int(triangle[i][0])  
                p3 = int(triangle[i][2]) 
            if(j==2):
                p2 = int(triangle[i][1])  
                p3 = int(triangle[i][0])     
            val= element_lib2.Element_Stiff_self(nut[p1][0],nut[p1][1],
                                                                       nut[p2][0],nut[p2][1],
                                                                     nut[p3][0],nut[p3][1])
            q1 = int(independ_re_index[p1])
            Global_matrix_vt[q1][q1]+=val    
        

# %%
a = np.zeros(5)
b = list(a)
b.remove(0)
b

# %%
np.linalg.matrix_rank (Global_matrix_vt)

# %%
Global_matrix_vt

# %%
b =[1,2,3,4]
x = np.linalg.solve(Global_matrix_vt,b)

# %%

# %%
f = lambda x,y: -2*x*(x-1) -2*y*(y-1)

# %%
ve_phai = np.zeros(run)
for i in range(0, so_tam_giac):
    for j in range(0, 3):
        p1 = int(triangle[i][j])
        if(Dirichlet[p1]==0):
            p2=0
            p3=0
            if(j==0):
                p2 = int(triangle[i][1])  
                p3 = int(triangle[i][2])  
            if(j==1):
                p2 = int(triangle[i][0])  
                p3 = int(triangle[i][2]) 
            if(j==2):
                p2 = int(triangle[i][1])  
                p3 = int(triangle[i][0])     
            phi= element_lib2.Element_Linear_Polynomial(nut[p1][0],nut[p1][1],
                                                                       nut[p2][0],nut[p2][1],
                                                                     nut[p3][0],nut[p3][1])
            q1 = int(independ_re_index[p1])
            ham= lambda x,y: phi(x,y)*f(x,y)
            ve_phai[q1]+=gauss_quad_lib.integrate_gauss_quad_triangle(ham,nut[p1][0],nut[p1][1],
                                                                       nut[p2][0],nut[p2][1],
                                                                     nut[p3][0],nut[p3][1])  
        

# %%
u_cord = np.linalg.solve(Global_matrix_vt, ve_phai)

# %%

fig =plt.figure(figsize=(5,5))
ax = fig.add_subplot(projection = '3d')
for i in range(0, so_nut):
    if(Dirichlet[i]):
        ax.scatter(nut[i][0],nut[i][1],0)
    else:
        q1= int(independ_re_index[i])
        ax.scatter(nut[i][0],nut[i][1], u_cord[q1])
plt.show()

# %%



