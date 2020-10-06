from numpy  import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

width = 1.0


min_x = int(sys.argv[2])
max_x = int(sys.argv[3])
filename = sys.argv[4]
extension = sys.argv[5]


fichier = open(str(sys.argv[1]), "r")
liste_x = []

for line in fichier.readlines():
    listeValeur = float(line)
    if listeValeur > 90:
	listeValeur = listeValeur - 180 
    liste_x.append(listeValeur)

liste_x1 = np.array(liste_x)

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)

n, bins, patches=ax.hist(liste_x1, 60, range=(min_x,max_x), histtype='stepfilled', alpha=0.3, normed=True)

ax.set_xlabel('Crossing Angle')
ax.set_ylabel('density')
ax.set_xticks(np.arange(min_x,max_x,10))
#ax.set_yticks(np.arange(0,1.2,0.1))
#ax.set_xlim (first_res,last_res_five)
#ax.set_ylim(0, 1.05 )
#ax.grid(True)
#plt.grid(True)
#ax.legend([rect1],[str(sys.argv[3])] ) 

figure_name = filename+extension
fig.savefig(figure_name)
