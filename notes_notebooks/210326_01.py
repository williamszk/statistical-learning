# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# gradient descent from scratch


# %%
import numpy as np


# %%
import matplotlib.pyplot as plt


# %%
import seaborn as sns
sns.set()


# %%
# number of observations
n = 200


# %%
X = np.random.randn(n)*2+1


# %%
y = 10 + 8*X + 2*X**2 + np.random.randn(n)*11


# %%
plt.plot(X,y, ".")


# %%
# the loss function


# %%
# set initial values for parameters
theta = np.random.rand(3)


# %%
# choose a model
# quadradic linear model
y_hat = theta[0] + theta[1]*X + theta[2]*X**2


# %%
delta = .1


# %%
for i in range(n):
    error_now = np.sum((y - y_hat)**2)
    


# %%
error_now


# %%
theta


# %%
ltheta


# %%
list(range(ltheta))


# %%
h_changes = []
ltheta = len(theta)
for i in range(ltheta):
    #h_changes[i] = 
    pass
    


# %%
delta_vec = np.array([delta]*ltheta)


# %%
delta_vec[i] *= -1


# %%
theta + delta_vec


# %%
delta


# %%
theta


# %%
def all_possible_combinations(delta, theta):    


# %%
ltheta = len(theta)
base_vector = [-delta]*ltheta
variacoes_delta = [base_vector]
lrounds = ltheta*2
cj_possi = set()

for i in range(lrounds):
    j = i%ltheta
    base_vector = base_vector.copy()
    base_vector[j] += delta
    
    if i in (ltheta-1, lrounds-1):
        variacoes_delta.append(base_vector)
    else:
        base_vector
        print(base_vector)
        cj_possi.add(tuple(base_vector))
        
        
        


# %%
cj_possi


# %%
# função que criar todas as possiveis combinações de tuplas
# rodando os valore dentro da lista
def rodar_valores(base_vector):
    


# %%
base_vector = [delta, 0, ]


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



