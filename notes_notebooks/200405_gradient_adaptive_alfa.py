# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# The objective of this notebook is to create a gradient descent algorithm with changing alfa, that is alfa is bigger if the gradient's module is bigger.

# %%
import random
import numpy as np
from numpy import linalg


# %%
def func(x1,x2):
    ff =(x1-3)**2 + (x2-2)**2
    return ff


# %%
def gradFunc(x1,x2):
    g1 = 2*(x1-3)
    g2 = 2*(x2-2)
    return g1, g2


# %%



# %%
def grad_optim(func,gradFunc):  
    itmax = 1000 #maximum nº of steps
    normagrad = 1e-3 #minimum norm of gradient
    alfa = 0.1 #rate of learning
    x1,x2 = random.uniform(-2,2),random.uniform(-2,2)
    i = 0
    g = gradFunc(x1,x2)
    norm_g = linalg.norm(g)
    while (norm_g > normagrad) & (i < itmax):
        f = func(x1,x2)
        g = gradFunc(x1,x2)
        norm_g = linalg.norm(g)
        print("Iteration = "+ str(i)+" | gradient norm = "+ str(round(norm_g,3))+
              " | Position = "+"("+str(round(x1,3))+","+ str(round(x2,3))+")")
        i += 1
        x1,x2 = x1-alfa*g[0], x2-alfa*g[1]

    return x1,x2


# %%
grad_optim(func,gradFunc)


# %%



# %%



# %%


# %% [markdown]
# The following is an adaptative alfa test:

# %%
def grad_optim_ada(func,gradFunc):  
    itmax = 1000 #maximum nº of steps
    normagrad = 1e-3 #minimum norm of gradient
    alfa = 0.1 #rate of learning
    x1,x2 = random.uniform(-2,2),random.uniform(-2,2)
    i = 0
    g = gradFunc(x1,x2)
    norm_g = linalg.norm(g)
    while (norm_g > normagrad) & (i < itmax):
        f = func(x1,x2)
        g = gradFunc(x1,x2)
        norm_g = linalg.norm(g)
        alfa = norm_g/10 #test1 for adaptative alpha
        #alfa = alfa*log(norm_g+100) #test2 for adaptative alpha
        print("Iteration = "+ str(i)+" | gradient norm = "+ str(round(norm_g,3))+
              " | Position = "+"("+str(round(x1,3))+","+ str(round(x2,3))+")"+
              " | Alpha = "+ str(round(alfa,7)))
        i += 1
        x1,x2 = x1-alfa*g[0], x2-alfa*g[1]

    return x1,x2


# %%
grad_optim_ada(func,gradFunc)


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



