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
        alfa = alfa*norm_g/1000 #test1 for adaptative alpha
        #alfa = alfa*log(norm_g+100) #test2 for adaptative alpha
        print("Iteration = "+ str(i)+" | gradient norm = "+ str(round(norm_g,3))+
              " | Position = "+"("+str(round(x1,3))+","+ str(round(x2,3))+")"+
              " | Alpha = "+alfa)
        i += 1
        x1,x2 = x1-alfa*g[0], x2-alfa*g[1]

    return x1,x2