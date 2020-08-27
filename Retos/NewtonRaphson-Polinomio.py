def f(x): return x**3 - 2*x**2 + 4/3*x - 8/27
def df(x): return 3*x**2 - 4*x + 4/3

def newtonRaphson(x,tol=1.0e-9):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i
    print ('Too many iterations\n')
root,numIter = newtonRaphson(0.81)
print ('Root =',root)
print ('Number of iterations =',numIter)
