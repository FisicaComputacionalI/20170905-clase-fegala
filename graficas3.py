import pylab as pl
x = [100, 200, 300, 400, 500]
y = [300, 500, 600, 900, 1600]
pl.plot(x, y)
x1 = [200, 300, 500, 600, 1600]
y1 = [500, 800, 1500, 1600, 2200]
pl.plot(x1, y1)
pl.xlabel('voltaje')
pl.ylabel('eficiencia')
pl.savefig('2graficas.png')
