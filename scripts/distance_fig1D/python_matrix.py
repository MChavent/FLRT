from numpy  import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import matplotlib.cm as cm


# DPPC double mutant TMJX (30 sims)
list_name = ("distance_TMJ_1.dat", "distance_TMJ_2.dat", "distance_TMJ_3.dat", "distance_TMJ_4.dat", "distance_TMJ_5.dat", "distance_TMJ_6.dat", "distance_TMJ_7.dat", "distance_TMJ_8.dat", "distance_TMJ_9.dat","distance_TMJ_10.dat", "distance_TMJ_11.dat","distance_TMJ_12.dat","distance_TMJ_13.dat","distance_TMJ_14.dat","distance_TMJ_15.dat","distance_TMJ_16.dat","distance_TMJ_17.dat","distance_TMJ_18.dat","distance_TMJ_19.dat", "distance_TMJ_20.dat", "distance_TMJ_21.dat", "distance_TMJ_22.dat", "distance_TMJ_23.dat", "distance_TMJ_24.dat", "distance_TMJ_25.dat", "distance_TMJ_26.dat", "distance_TMJ_27.dat", "distance_TMJ_28.dat", "distance_TMJ_29.dat", "distance_TMJ_30.dat")
list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)


figure = p.figure()


for name, pos_nb in zip(list_name, list_plot_pos):
	fichier = open(name, "r")
	liste_x =[]
	liste_y =[]
	counter = 0


	for line in fichier.readlines():
	    if counter > 1: 
	      listeValeur = line.split()
	      #print(listeValeur)
	      listeValeurF = [float(x) for x in listeValeur]
	      liste_x.append(listeValeurF[0])
	      liste_y.append(listeValeurF[1])
	    counter+=1

	liste_x = np.array(liste_x)

	liste_y2 =[]
	for i in range(300):
	    liste_y2.append(liste_y)


	liste_y2 = np.asarray(liste_y2)
	print(liste_y2.shape)

	ax = figure.add_subplot(31,1,pos_nb)
	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)
	cax = ax.imshow(liste_y2, vmin=0, vmax=90,cmap='afmhot')
	if pos_nb == 30:
		ax.axes.get_xaxis().set_visible(True)
	ax.set_aspect(0.3)
	#matplotlib.pyplot.colorbar(cax)


figure.subplots_adjust(hspace=.0)
figure.savefig('distance_vs_time_all.svg', dpi=200)	
