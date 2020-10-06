#importing numpy
import numpy as np
import math

# importing matplotlib to perform figures
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

import sys

# DPPC TMHJM (30 sims)
list_name = ("md.flrt2TMH_jx_martini_DPPC_1", "md.flrt2TMH_jx_martini_DPPC_2", "md.flrt2TMH_jx_martini_DPPC_3", "md.flrt2TMH_jx_martini_DPPC_4", "md.flrt2TMH_jx_martini_DPPC_5","md.flrt2TMH_jx_martini_DPPC_6","md.flrt2TMH_jx_martini_DPPC_7","md.flrt2TMH_jx_martini_DPPC_8","md.flrt2TMH_jx_martini_DPPC_9", "md.flrt2TMH_jx_martini_DPPC_10","md.flrt2TMH_jx_martini_DPPC_11","md.flrt2TMH_jx_martini_DPPC_12", "md.flrt2TMH_jx_martini_DPPC_13","md.flrt2TMH_jx_martini_DPPC_14", "md.flrt2TMH_jx_martini_DPPC_15", "md.flrt2TMH_jx_martini_DPPC_16", "md.flrt2TMH_jx_martini_DPPC_17", "md.flrt2TMH_jx_martini_DPPC_18", "md.flrt2TMH_jx_martini_DPPC_19", "md.flrt2TMH_jx_martini_DPPC_20","md.flrt2TMH_jx_martini_DPPC_21","md.flrt2TMH_jx_martini_DPPC_22", "md.flrt2TMH_jx_martini_DPPC_23", "md.flrt2TMH_jx_martini_DPPC_24", "md.flrt2TMH_jx_martini_DPPC_25", "md.flrt2TMH_jx_martini_DPPC_26", "md.flrt2TMH_jx_martini_DPPC_27", "md.flrt2TMH_jx_martini_DPPC_28", "md.flrt2TMH_jx_martini_DPPC_29", "md.flrt2TMH_jx_martini_DPPC_30") 

list_x=[]
list_y=[]


for name in list_name:

	filename_x = str(name+"_dist.dat")
	filename_y = str(name+"_cross.dat")

	file = open(filename_x, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x.append(values[0])

	file = open(filename_y, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y.append(values[0])     

for id_sim in range(0,len(list_name)):
	print(id_sim)

	name=list_name[id_sim]
	filename_x_sim = str(name+"_dist.dat")
	filename_y_sim = str(name+"_cross.dat")

	list_x_sim=[]
	list_y_sim=[]

	colors=[]
	counter=0

	file = open(filename_x_sim, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_sim.append(values[0])
		colors.append(counter)
		counter=counter+1



	file = open(filename_y_sim, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_sim.append(values[0])
	fig2 = matplotlib.pyplot.figure()
	ax2 = fig2.add_subplot(111)
	bin_num=20
	
	array_op_tot,xedges,yedges = np.histogram2d(list_x,list_y, bins=bin_num,range=[[4,10],[-40,40]])
	max_array_tot=max(array_op_tot.flatten())
	array_avg_tot = array_op_tot/(max_array_tot)


	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]

	cax=ax2.imshow(array_avg_tot.T,extent=extent,interpolation='bicubic',origin='lower',cmap='Blues', vmin=0, vmax=1.0)
	cax = ax2.scatter(list_x_sim, list_y_sim, c=colors, s=10, cmap="plasma",  alpha=0.5, lw=0)



	ax2.set_aspect(0.12)
	ax2.set_yticks(np.arange(-40,40,10))
	ax2.set_xticks(np.arange(4,10,1))
	ax2.set_xlim(4,10)
	ax2.set_ylim(-40,40)
	cbar= plt.colorbar(cax)
	name_fig="density_CAvsD_TMH_20CHOL_XXX_"+str(id_sim)+".svg"
	fig2.savefig(name_fig, dpi=200)


