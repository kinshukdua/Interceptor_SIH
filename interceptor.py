from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize as opt

range_ = np.sqrt(109)
class Interceptor:
    def __init__(self,latitude,longitude,range_):
        self.x = latitude
        self.y = longitude
        self.r = range_
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def in_range(self,missile):
        x0 = self.x
        y0 = self.y
        x1 = missile.get_x()
        y1 = missile.get_y()
        z1 = missile.get_z()
        r = self.r
        return (x1-x0)**2+(y1-y0)**2+z1**2 <= r**2
class Missile: 
    def __init__(self,latitude,longitude,altitude):
        self.x = latitude
        self.y = longitude
        self.z = altitude
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z

def exp(x,a,b,c):
    return a * np.exp(-b * x) + c
def exp_prime(x,a,b,c):
    return -a * b * np.exp(-b * x) + c
dic = {}
interceptors = [(8.62, 1.92),
 (0.44, 3.68),
 (8.59, 9.29),
 (8.64, 4.74),
 (2.32, 7.25),
 (9.96, 1.09),
 (9.1, 5.35),
 (3.83, 2.39),
 (1.51, 5.73),
 (5.97, 3.17)]

missiles = [(0.29, 3.32, 8.78),
 (6.39, 0.62, 4.08),
 (5.44, 8.41, 8.66),
 (1.2, 6.22, 4.94),
 (7.87, 5.05, 3.85),
 (8.17, 3.59, 9.28),
 (0.41, 2.77, 8.58),
 (9.1, 0.16, 7.85),
 (1.22, 3.15, 4.24),
 (8.99, 8.61, 0.43),
 (1.39, 0.68, 8.6),
 (4.35, 3.29, 2.34),
 (4.75, 0.99, 0.91),
 (8.34, 0.48, 6.34),
 (9.56, 6.7, 6.75),
 (2.8, 6.24, 1.89),
 (9.59, 6.32, 0.93),
 (6.12, 9.7, 0.29),
 (7.67, 1.09, 4.69),
 (7.88, 9.42, 4.22)]
 
interceptors = [Interceptor(i[0],i[1],range_) for i in interceptors]
missiles = [Missile(m[0],m[1],m[2]) for m in missiles]

target_dic = {i:tuple([m for m in missiles if i.in_range(m)]) for i in interceptors}


"""

sums = []
sums_inv = []
ns = []
def in_range(missile,interceptor):
    x0 = interceptor[0]
    y0 = interceptor[1]
    x = missile[0]
    y = missile[1]
    z = missile[2]
    return (x-x0)**2+(y-y0)**2+z**2 <= range_
def func(x, a, b, c):
    return a * np.exp(-b * x) + c
'''
def optimize(ns,sums_inv):
    for i in range(len(sums_inv)-1):
        if abs(sums_inv[i+1]-sums_inv[i]) < 0.00001:
            return ns[i]
'''

interceptors = [(8.62, 1.92),
 (0.44, 3.68),
 (8.59, 9.29),
 (8.64, 4.74),
 (2.32, 7.25),
 (9.96, 1.09),
 (9.1, 5.35),
 (3.83, 2.39),
 (1.51, 5.73),
 (5.97, 3.17)]
dic = {i:[] for i in interceptors}
missiles = [(0.29, 3.32, 8.78),
 (6.39, 0.62, 4.08),
 (5.44, 8.41, 8.66),
 (1.2, 6.22, 4.94),
 (7.87, 5.05, 3.85),
 (8.17, 3.59, 9.28),
 (0.41, 2.77, 8.58),
 (9.1, 0.16, 7.85),
 (1.22, 3.15, 4.24),
 (8.99, 8.61, 0.43),
 (1.39, 0.68, 8.6),
 (4.35, 3.29, 2.34),
 (4.75, 0.99, 0.91),
 (8.34, 0.48, 6.34),
 (9.56, 6.7, 6.75),
 (2.8, 6.24, 1.89),
 (9.59, 6.32, 0.93),
 (6.12, 9.7, 0.29),
 (7.67, 1.09, 4.69),
 (7.88, 9.42, 4.22)]
temp = missiles.copy()
for i in interceptors:
    for m in missiles:
        if in_range(m,i):
            dic[i].append(m)
x = list(dic.items())
x.sort(key=lambda x: len(x[1]),reverse=True)
final = []
flag = False
for e in x:
    if flag:
        break
    final.append(e[0])
    for m in e[1]:
        if m in missiles:
            missiles.remove(m)
    if not missiles:
            print("all incoming missiles targetted")
            flag = True
            break
if flag:
    print("minimum interceptors required:",final)
    missiles = temp
    for n in range(1,len(interceptors)+1):
        m_prob = {x:0 for x in missiles}
        sum_ = 0
        for e in x[:n]:
            for m in e[1]:
                
                #IMPORTANT VARIABLE m_prob[] == ????
                
                m_prob[m] += 1
        ns.append(n)
        for i in m_prob.values():
            sum_ += i**2
        sums.append(sum_)
        sums_inv.append(1/(sum_))       
    #plt.plot(ns,sums_inv)
    #plt.plot(ns,sums)
    delta = [sums_inv[i+1]-sums_inv[i] for i in range(0,len(sums)-1)]
    popt, pcov = opt.curve_fit(func, ns, sums_inv)
    def func2(x):
        return popt[0]*np.exp(-popt[1]*x)+popt[2]
    y = [func2(i) for i in ns]
    plt.plot(ns,y)
    plt.title('Optimal Interceptors')
    plt.ylabel('Inverse of probability')
    plt.xlabel('Number of interceptors')
    ind = round(float(opt.minimize(func2,x0=(len(final)+1),bounds = ((1,len(interceptors)+1),)).x))
    optim = opt.minimize(func2, x0=(len(final)), bounds = ((1, len(interceptors) + 1),)).x
    optim = round(optim[0])
    plt.scatter(optim,func2(optim),marker='x',color='black',s=150)
    #plt.savefig('4.png')
    print("Optimal solution require these",ind,"interceptors: ")
    result = [i[0] for i in x[:ind]]
    print(result)
    print("In order of importance")
    plt.show()
else:
    print("Some missiles out of range.")
#print(delta)
#plt.plot(ns,delta+[0])
#deltadelta = [delta[i+1]-delta[i] for i in range(0,len(delta)-1)]
#print(deltadelta)
#plt.plot(ns,deltadelta+[0,0])
#deltadeltadelta = [deltadelta[i+1]-deltadelta[i] for i in range(0,len(deltadelta)-1)]
#print(deltadeltadelta)
#plt.plot(ns,deltadeltadelta+[0,0,0])
#master = [ns,sums,delta+[0],deltadelta+[0,0],deltadeltadelta+[0,0,0]]
#print(max(deltadeltadelta))

"""