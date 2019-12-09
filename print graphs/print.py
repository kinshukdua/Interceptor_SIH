from matplotlib import pyplot as plt
from matplotlib import patches as pt
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
imp = [(3.83, 2.39), (5.97, 3.17)]
opt = [(3.83, 2.39), (5.97, 3.17), (8.64, 4.74), (9.1, 5.35), (8.62, 1.92), (2.32, 7.25), (1.51, 5.73), (0.44, 3.68)]
fig, ax = plt.subplots()
x1 = [i[0]*10 for i in interceptors]
y1 = [i[1]*10 for i in interceptors]
x2 = [i[0]*10 for i in imp]
y2 = [i[1]*10 for i in imp]
x3 = [i[0]*10 for i in opt]
y3 = [i[1]*10 for i in opt]
plt.xlabel('x co-ordinate (km)')
plt.ylabel('y co-ordinate (km)')
plt.title('All Interceptors (Blue)',color = 'blue')
plt.scatter(x1,y1,s=100,marker='x')
plt.title('Optimal Interceptors (Green)',color = 'green')
plt.scatter(x3,y3,s=100,color = 'green',marker='x')
plt.title('Minimum Interceptors (Red)',color = 'red')
plt.scatter(x2,y2,s=100,color = 'red',marker='x')
plt.grid()
ax.add_patch(pt.Polygon(interceptors,True))
plt.savefig('7.png')
