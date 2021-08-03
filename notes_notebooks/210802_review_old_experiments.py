"""
The objective of this script is to review some old code 
and study notebooks and try to understand and run them again.
"""

########################################################################

#original code in matlab
# %**********************************************************
# % Disciplina Aprendizado de Máquina
# % Exemplo Algoritmo do Gradiente Descente com passo fixo
# % Problema de otimização
# %               min f(x(1),x(2))= (x(1)-3)^2 + (x(2)-2)^2
# % Exemplo
# %        example_grad - não precisa definir o valor de x
# %        exampe_grad([0 0]) - ponto inicial x =[0 0]
# %**********************************************************

# function example_grad_fixo(x)
# % Definição de parâmetros
# itmax = 1000;     % Numero máximo de iterações
# normagrad = 1e-3; % Norma mínima do gradiente
# alfa = 0.1;       % taxa de aprendizado
# %Valor inicial para x
# if nargout<1
#     x = rands(2,1);
# end
# % Avalia a função e cálcula o gradiente
# [f,g,~]=calc_derivada(x);
# % Definição do valor iteração inicial
# it = 0;
# % Verifica critério de parada (numero de iterações ou norma do gradiente)
# while it<itmax & norm(g)>normagrad
#     % Imprime na tela
#     fprintf('Iterações = %d, norma do gradiente =%1.4f,  x = [%2.5f %2.5f] \n',it,norm(g),x(1),x(2))
#     %Incrementa o numero de iterações
#     it = it + 1;
#     % Atualiza
#     x = x - alfa*g;
#     % Avalia a função e cálcula do gradiente
#     [f,g,~]=calc_derivada(x);
# end


# function [f,g,h]=calc_derivada(x)
# f = (x(1)-3)^2+(x(2)-2)^2;
# g = [2*(x(1)-3);2*(x(2)-2)];
# h = [2 0;0 2];


# function to be minimized 
# f(x1,x2) = (x1-3)**2 + (x2-2)**2


import random
import numpy as np
from numpy import linalg

def func(x1,x2):
    ff =(x1-3)**2 + (x2-2)**2
    return ff

def grad_func(x1,x2):
    g1 = 2*(x1-3)
    g2 = 2*(x2-2)
    return g1, g2

# to understand this code I need to remember 
# how gradient descend works

def grad_optim(func,grad_func):  
    itmax = 1000 # maximum nº of steps
    normagrad = 1e-3 # minimum norm of gradient
    alfa = 0.1 # rate of learning
    x1,x2 = random.uniform(-2,2),random.uniform(-2,2)
    i = 0
    g = grad_func(x1,x2)
    norm_g = linalg.norm(g)
    while (norm_g > normagrad) & (i < itmax):
        f = func(x1,x2)
        g = grad_func(x1,x2)
        norm_g = linalg.norm(g)
        print("Iteration = "+ str(i)+" | gradient norm = "+ str(round(norm_g,3))+
              " | Position = "+"("+str(round(x1,3))+","+ str(round(x2,3))+")")
        i += 1
        x1,x2 = x1-alfa*g[0], x2-alfa*g[1]

    return x1,x2

grad_optim(func,grad_func)




