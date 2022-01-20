import numpy as np

class Functions:
    # 1
    def Rastrigin(self,X):
        d = 10.0
        return 10*d + sum([(x**2 - 10 * np.cos(2 * np.pi * x)) for x in X])

    # 2
    def Ackley(self, X):
        return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (X[0]**2 + X[1]**2))) - np.exp(0.5 * (np.cos(2* np.pi * X[0]) + np.cos(2 * np.pi * X[1]))) + np.e + 20.0
    #3
    def Rosenbrock(self, X):
        _sum = 0.0
        for i in range(0,len(X)-1):
            _sum += ( 100 * (X[i+1] - X[i]**2)**2 + (1-X[i])**2)
        
        return _sum
    
    #4
    def Beale(self,X):
        return (1.5 - X[0] +X[0]*X[1])**2 + (2.25 - X[0] + X[0]*X[1]**2)**2 + (2.625 -X[0] + X[0]*X[1]**3)**2

    #5
    def Goldstein_Price(self,X):
        return (1 + (X[0]+X[1]+1)**2 * (19-14*X[0]+3*X[0]**2-14*X[1]+6*X[0]*X[1]+3*X[1]**2))*(30 + (2*X[0]-3*X[1])**2 * (18-32*X[0]+12*X[0]**2+48*X[1]-36*X[0]*X[1]+27*X[1]**2))

    #6
    def Booth(self, X):
        return (X[0]+2*X[1]-7)**2 + (2*X[0] + X[1] - 5)**2

    #7
    def Bukin(self,X):
        return 100*np.sqrt(np.abs(X[1]-0.01*X[0]**2))+0.01*(np.abs(X[0]+10))

    #8
    def Matyas(self,X):
        return .26*(X[0]**2 + X[1]**2) - .48*X[0]*X[1]

    #9
    def Sphere(self, X):
        return sum([x**2 for x in X])
    
    #10
    def Himmelblau(self,X):
        return (X[0]**2 + X[1] - 11)**2 + (X[0] + X[1]**2 - 7)**2
