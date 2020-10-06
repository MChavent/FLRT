from numpy  import *
import numpy as np
import matplotlib
import matplotlib.pyplot as p
import matplotlib.cm as cm
import sys


# DPPC TMHJM (30 sims)
list_name = ("md.flrt2TMH_jx_martini_DPPC_1", "md.flrt2TMH_jx_martini_DPPC_2", "md.flrt2TMH_jx_martini_DPPC_3", "md.flrt2TMH_jx_martini_DPPC_4", "md.flrt2TMH_jx_martini_DPPC_5", "md.flrt2TMH_jx_martini_DPPC_7", "md.flrt2TMH_jx_martini_DPPC_8", "md.flrt2TMH_jx_martini_DPPC_9", "md.flrt2TMH_jx_martini_DPPC_11", "md.flrt2TMH_jx_martini_DPPC_12", "md.flrt2TMH_jx_martini_DPPC_15", "md.flrt2TMH_jx_martini_DPPC_17", "md.flrt2TMH_jx_martini_DPPC_18", "md.flrt2TMH_jx_martini_DPPC_20", "md.flrt2TMH_jx_martini_DPPC_21", "md.flrt2TMH_jx_martini_DPPC_22", "md.flrt2TMH_jx_martini_DPPC_24", "md.flrt2TMH_jx_martini_DPPC_25", "md.flrt2TMH_jx_martini_DPPC_26", "md.flrt2TMH_jx_martini_DPPC_27", "md.flrt2TMH_jx_martini_DPPC_28", "md.flrt2TMH_jx_martini_DPPC_29", "md.flrt2TMH_jx_martini_DPPC_30") 
list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
fig, ax = p.subplots(5, 5, sharex='col', sharey='row')
fig.subplots_adjust(hspace=0.1, wspace=0.1)


liste_name_seq1 = []
liste_name_seq2 = []


fichier_seq1 = open("seq1.txt", "r")

for line in fichier_seq1.readlines():
	liste_name_seq1.append(line.split()[0])
	print (line.split()[0])


fichier_seq2 = open("seq2.txt", "r")

for line in fichier_seq2.readlines():
	liste_name_seq2.append(line.split()[0])


length_seq1 = len(liste_name_seq1)
length_seq2 = len(liste_name_seq2)

array_final = np.zeros((length_seq2,length_seq1))

time_tot = 0.0
caxi = []


for name, pos_nb, i, j in zip(list_name, list_plot_pos, list_i, list_j):

	filename_dist = str(name+"_inter.dat")
	filename_time = str(name+"_inter_time.dat")

	fichier_dist = open(filename_dist, "r")
	fichier_time = open(filename_time, "r")

	liste_y =[]
	time = 0.0

	for line in fichier_time.readlines():
		listeValeur = line.split()
		listeValeurF = [float(x) for x in listeValeur]
		time = float(listeValeurF[0])
	
	time_tot= time_tot+time

	for line in fichier_dist.readlines():
		listeValeur = line.split()
		listeValeurF = [float(x) for x in listeValeur]
		liste_y.append(listeValeurF[0:])

	array_y = np.transpose(np.array(liste_y))
	array_final = array_final + (array_y*time)

	#ax[i,j].set_xticks(np.arange(length_seq1-1,0,-4))
	#ax[i,j].set_yticks(np.arange(length_seq1-1,0,-4))
	ax[i,j].set_xticks(np.arange(0,32,1))
	ax[i,j].set_yticks(np.arange(0,32,1))
	#ax[i,j].set_xticklabels(liste_name_seq1,rotation='vertical')
	#ax[i,j].set_yticklabels(reversed(liste_name_seq2))
	#ax[i,j].set_xticks([]) 
	#ax[i,j].set_yticks([])	
	caxi = ax[i,j].imshow(array_y, interpolation='nearest', vmin=6, vmax=9,cmap='Blues_r')

matplotlib.pyplot.colorbar(caxi)
fig.savefig('inter_all.svg', dpi=200)


fig2 = matplotlib.pyplot.figure()
ax2 = fig2.add_subplot(111)

array_final = array_final/float(time_tot)

print(liste_name_seq1)
ax2.set_xticks(np.arange(0,32,1))
ax2.set_yticks(np.arange(0,32,1))
ax2.set_xticklabels(liste_name_seq1,rotation='vertical')
ax2.set_yticklabels(reversed(liste_name_seq2))

cax = ax2.imshow(array_final, interpolation='nearest', vmin=6, vmax=9,cmap='Blues_r')

matplotlib.pyplot.colorbar(cax)
fig2.savefig('inter_avg.svg', dpi=400)
