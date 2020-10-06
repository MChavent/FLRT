from numpy  import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

fig = matplotlib.pyplot.figure(figsize=(6, 6))

# DPPC TMHJM 
list_name = ("md.flrt2TMH_jx_martini_DPPC_1_cross.dat", "md.flrt2TMH_jx_martini_DPPC_2_cross.dat", "md.flrt2TMH_jx_martini_DPPC_3_cross.dat", "md.flrt2TMH_jx_martini_DPPC_4_cross.dat", "md.flrt2TMH_jx_martini_DPPC_5_cross.dat", "md.flrt2TMH_jx_martini_DPPC_7_cross.dat", "md.flrt2TMH_jx_martini_DPPC_8_cross.dat", "md.flrt2TMH_jx_martini_DPPC_9_cross.dat", "md.flrt2TMH_jx_martini_DPPC_11_cross.dat", "md.flrt2TMH_jx_martini_DPPC_12_cross.dat", "md.flrt2TMH_jx_martini_DPPC_15_cross.dat", "md.flrt2TMH_jx_martini_DPPC_17_cross.dat", "md.flrt2TMH_jx_martini_DPPC_18_cross.dat", "md.flrt2TMH_jx_martini_DPPC_20_cross.dat", "md.flrt2TMH_jx_martini_DPPC_21_cross.dat", "md.flrt2TMH_jx_martini_DPPC_22_cross.dat", "md.flrt2TMH_jx_martini_DPPC_24_cross.dat", "md.flrt2TMH_jx_martini_DPPC_25_cross.dat", "md.flrt2TMH_jx_martini_DPPC_26_cross.dat", "md.flrt2TMH_jx_martini_DPPC_27_cross.dat", "md.flrt2TMH_jx_martini_DPPC_28_cross.dat",  "md.flrt2TMH_jx_martini_DPPC_29_cross.dat", "md.flrt2TMH_jx_martini_DPPC_30_cross.dat")
list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
list_color = ("blue","red","gold","midnightblue","lime","skyblue","firebrick","olive","teal","grey","wheat","slateblue","lightcoral","green","darkslategrey","steelblue","pink","darkkhaki","salmon", "mediumpurple", "darkcyan", "orange", "dimgray")
fig, ax = plt.subplots(5, 5, sharex='col', sharey='row')

fig.subplots_adjust(hspace=0.1, wspace=0.1)
liste_tot = []
min_x = -80
max_x = 80
for name, pos_nb, color_hist, i, j in zip(list_name, list_plot_pos, list_color, list_i, list_j):
	fichier = open(name, "r")

	liste_x = []

	for line in fichier.readlines():
	    listeValeur = float(line)
	    liste_x.append(listeValeur)
	    liste_tot.append(listeValeur)

	liste_x1 = np.array(liste_x)

	ax[i,j].hist(liste_x1, 80, range=(min_x,max_x), histtype='bar', fc=str(color_hist), ec=str(color_hist), normed=True)
	ax[i,j].set_xticks(np.arange(min_x,max_x,20))
	ax[i,j].set_yticks(np.arange(0,0.155,0.05))
	ax[i,j].set_xticks(np.arange(-80,80,40))
	ax[i,j].set_xlim(-80,80)
	ax[i,j].set_ylim(0,0.15)
	
	fig.savefig('cross_all.svg', dpi=200)


fig2 = matplotlib.pyplot.figure()
ax2 = fig2.add_subplot(111)

array_tot = np.array(liste_tot)
n, bins, patches=ax2.hist(array_tot, 80, range=(min_x,max_x), fc="lightsteelblue", ec="midnightblue", normed=True)

ax2.set_xlabel('Crossing Angle')
ax2.set_ylabel('density')
ax2.set_yticks(np.arange(0,0.07,0.01))
ax2.set_xticks(np.arange(min_x,max_x,10))
fig2.savefig('cross_average.svg', dpi=200)
