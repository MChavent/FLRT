#importing numpy
import numpy as np
import math

# importing matplotlib to perform figures
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

import sys

xmin = -20
xmax = 20
ymin = -20
ymax = 20



# DPPC TMHJM (30 sims)
list_name = ("md.flrt2TMH_jx_martini_DPPC_1", "md.flrt2TMH_jx_martini_DPPC_2", "md.flrt2TMH_jx_martini_DPPC_3", "md.flrt2TMH_jx_martini_DPPC_4", "md.flrt2TMH_jx_martini_DPPC_5", "md.flrt2TMH_jx_martini_DPPC_7","md.flrt2TMH_jx_martini_DPPC_8","md.flrt2TMH_jx_martini_DPPC_9","md.flrt2TMH_jx_martini_DPPC_11","md.flrt2TMH_jx_martini_DPPC_12", "md.flrt2TMH_jx_martini_DPPC_15", "md.flrt2TMH_jx_martini_DPPC_17", "md.flrt2TMH_jx_martini_DPPC_18", "md.flrt2TMH_jx_martini_DPPC_20","md.flrt2TMH_jx_martini_DPPC_21","md.flrt2TMH_jx_martini_DPPC_22","md.flrt2TMH_jx_martini_DPPC_24", "md.flrt2TMH_jx_martini_DPPC_25", "md.flrt2TMH_jx_martini_DPPC_26", "md.flrt2TMH_jx_martini_DPPC_27", "md.flrt2TMH_jx_martini_DPPC_28", "md.flrt2TMH_jx_martini_DPPC_29", "md.flrt2TMH_jx_martini_DPPC_30") 
list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
fig, ax = plt.subplots(5, 5, sharex='col', sharey='row')
fig.subplots_adjust(hspace=0.1, wspace=0.1)

# POPC TMHJM (30 sims)
#list_name = ("md.f2j_M_POPC_4","md.f2j_M_POPC_7","md.f2j_M_POPC_10", "md.f2j_M_POPC_11", "md.f2j_M_POPC_13", "md.f2j_M_POPC_15", "md.f2j_M_POPC_18", "md.f2j_M_POPC_19", "md.f2j_M_POPC_20", "md.f2j_M_POPC_21", "md.f2j_M_POPC_24", "md.f2j_M_POPC_25", "md.f2j_M_POPC_26", "md.f2j_M_POPC_28") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(5, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# 20CHOL TMHJM (30 sims)
#list_name = ("md.f2j_M_20CHOL_1", "md.f2j_M_20CHOL_3", "md.f2j_M_20CHOL_4", "md.f2j_M_20CHOL_5", "md.f2j_M_20CHOL_7", "md.f2j_M_20CHOL_8", "md.f2j_M_20CHOL_9", "md.f2j_M_20CHOL_10", "md.f2j_M_20CHOL_11",  "md.f2j_M_20CHOL_12",  "md.f2j_M_20CHOL_13",  "md.f2j_M_20CHOL_14",  "md.f2j_M_20CHOL_15",  "md.f2j_M_20CHOL_16",  "md.f2j_M_20CHOL_17",  "md.f2j_M_20CHOL_18",  "md.f2j_M_20CHOL_19",  "md.f2j_M_20CHOL_20",   "md.f2j_M_20CHOL_21",   "md.f2j_M_20CHOL_22",   "md.f2j_M_20CHOL_24",   "md.f2j_M_20CHOL_25",   "md.f2j_M_20CHOL_26",   "md.f2j_M_20CHOL_27",   "md.f2j_M_20CHOL_28",   "md.f2j_M_20CHOL_29",   "md.f2j_M_20CHOL_30") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
#list_i = (0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4)
#list_j = (0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5)
#fig, ax = plt.subplots(5, 6, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)


# DPPC A544I TMHJM (30 sims)
#list_name = ("md.f2j_A544I_M_DPPC_1", "md.f2j_A544I_M_DPPC_2", "md.f2j_A544I_M_DPPC_7", "md.f2j_A544I_M_DPPC_9", "md.f2j_A544I_M_DPPC_11", "md.f2j_A544I_M_DPPC_12", "md.f2j_A544I_M_DPPC_13", "md.f2j_A544I_M_DPPC_15", "md.f2j_A544I_M_DPPC_17", "md.f2j_A544I_M_DPPC_19", "md.f2j_A544I_M_DPPC_21", "md.f2j_A544I_M_DPPC_25", "md.f2j_A544I_M_DPPC_26", "md.f2j_A544I_M_DPPC_28", "md.f2j_A544I_M_DPPC_30") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
#list_i = (0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4)
#list_j = (0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3)
#fig, ax = plt.subplots(4, 4, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# DPPC A544I_G548I TMHJM (30 sims)
#list_name = ("md.f2j_A544I_G548I_M_DPPC_1" ,  "md.f2j_A544I_G548I_M_DPPC_2" ,  "md.f2j_A544I_G548I_M_DPPC_3" ,  "md.f2j_A544I_G548I_M_DPPC_4" ,  "md.f2j_A544I_G548I_M_DPPC_5" ,  "md.f2j_A544I_G548I_M_DPPC_7" ,  "md.f2j_A544I_G548I_M_DPPC_13" ,  "md.f2j_A544I_G548I_M_DPPC_16" , "md.f2j_A544I_G548I_M_DPPC_17" ,  "md.f2j_A544I_G548I_M_DPPC_18" ,  "md.f2j_A544I_G548I_M_DPPC_20" ,  "md.f2j_A544I_G548I_M_DPPC_21" ,  "md.f2j_A544I_G548I_M_DPPC_22" ,  "md.f2j_A544I_G548I_M_DPPC_23" ,  "md.f2j_A544I_G548I_M_DPPC_24" ,  "md.f2j_A544I_G548I_M_DPPC_26" ,  "md.f2j_A544I_G548I_M_DPPC_28" ,  "md.f2j_A544I_G548I_M_DPPC_29" ,  "md.f2j_A544I_G548I_M_DPPC_30" ) 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(4, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# DPPC G545V TMHJM (30 sims)
#list_name = ("md.f2j_G545V_M_DPPC_3" , "md.f2j_G545V_M_DPPC_4" , "md.f2j_G545V_M_DPPC_6" , "md.f2j_G545V_M_DPPC_8" , "md.f2j_G545V_M_DPPC_9" , "md.f2j_G545V_M_DPPC_10" , "md.f2j_G545V_M_DPPC_14" , "md.f2j_G545V_M_DPPC_17" , "md.f2j_G545V_M_DPPC_18" , "md.f2j_G545V_M_DPPC_19" , "md.f2j_G545V_M_DPPC_21" , "md.f2j_G545V_M_DPPC_22" , "md.f2j_G545V_M_DPPC_24" , "md.f2j_G545V_M_DPPC_25" , "md.f2j_G545V_M_DPPC_26" , "md.f2j_G545V_M_DPPC_27" , "md.f2j_G545V_M_DPPC_28" , "md.f2j_G545V_M_DPPC_30" ) 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(4, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# DPPC G545I_G549I TMHJM (30 sims)
#list_name = ("md.f2j_G545I_G549I_M_DPPC_1" , "md.f2j_G545I_G549I_M_DPPC_4" , "md.f2j_G545I_G549I_M_DPPC_5" , "md.f2j_G545I_G549I_M_DPPC_6" , "md.f2j_G545I_G549I_M_DPPC_10" , "md.f2j_G545I_G549I_M_DPPC_11" , "md.f2j_G545I_G549I_M_DPPC_13" , "md.f2j_G545I_G549I_M_DPPC_14" , "md.f2j_G545I_G549I_M_DPPC_15" , "md.f2j_G545I_G549I_M_DPPC_16" , "md.f2j_G545I_G549I_M_DPPC_17" , "md.f2j_G545I_G549I_M_DPPC_20" , "md.f2j_G545I_G549I_M_DPPC_21" , "md.f2j_G545I_G549I_M_DPPC_23" , "md.f2j_G545I_G549I_M_DPPC_24" , "md.f2j_G545I_G549I_M_DPPC_25" , "md.f2j_G545I_G549I_M_DPPC_26" , "md.f2j_G545I_G549I_M_DPPC_27" , "md.f2j_G545I_G549I_M_DPPC_29" , "md.f2j_G545I_G549I_M_DPPC_30") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(4, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# A544I_G545I_G548I_G549I TMHJM (30 sims)
#list_name = ("double_mut1" , "double_mut2" , "double_mut3" , "double_mut4" , "double_mut7" , "double_mut8" , "double_mut9" , "double_mut10" , "double_mut11" , "double_mut13" , "double_mut14" , "double_mut15" , "double_mut16" , "double_mut17" , "double_mut18" , "double_mut19" , "double_mut20" , "double_mut21" , "double_mut22" , "double_mut24" , "double_mut25" , "double_mut27" , "double_mut28" , "double_mut29" , "double_mut30") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(5, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)

# DPPC TMHJM2 (30 sims)
#list_name = ("md.flrt2TMH_jx_martini_DPPC_3""md.flrt2TMH_jx_martini_DPPC_3", "md.flrt2TMH_jx_martini_DPPC_4", "md.flrt2TMH_jx_martini_DPPC_5", "md.flrt2TMH_jx_martini_DPPC_8", "md.flrt2TMH_jx_martini_DPPC_17", "md.flrt2TMH_jx_martini_DPPC_21", "md.flrt2TMH_jx_martini_DPPC_22", "md.flrt2TMH_jx_martini_DPPC_24", "md.flrt2TMH_jx_martini_DPPC_25", "md.flrt2TMH_jx_martini_DPPC_26", "md.flrt2TMH_jx_martini_DPPC_27", "md.flrt2TMH_jx_martini_DPPC_28", "md.flrt2TMH_jx_martini_DPPC_29", "md.flrt2TMH_jx_martini_DPPC_30") 
#list_plot_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
#list_i = (0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
#list_j = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)
#fig, ax = plt.subplots(5, 5, sharex='col', sharey='row')
#fig.subplots_adjust(hspace=0.1, wspace=0.1)


list_tot_x = []
list_tot_y = []

list_tot_x_TM1 = []
list_tot_y_TM1 = []

list_tot_x_A544 = []
list_tot_y_A544 = []

list_tot_x_G545 = []
list_tot_y_G545 = []

list_tot_x_G548 = []
list_tot_y_G548 = []

list_tot_x_G549 = []
list_tot_y_G549 = []

for name, pos_nb, i, j in zip(list_name, list_plot_pos, list_i, list_j):

	print(name)
	list_x=[]
	list_y=[]

	list_x_TM1=[]
	list_y_TM1=[]

	list_x_A544 = []
	list_y_A544 = []

	list_x_G545 = []
	list_y_G545 = []

	list_x_G548 = []
	list_y_G548 = []

	list_x_G549 = []
	list_y_G549 = []

	colors=[]
	counter=0

	filename_x = str(name+"_density_TM2_x.dat")
	filename_y = str(name+"_density_TM2_y.dat")

	file = open(filename_x, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x.append(values[0])
		list_tot_x.append(values[0])
		colors.append(counter)
		counter=counter+1

	file = open(filename_y, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y.append(values[0])   
		list_tot_y.append(values[0])   

	filename_x_TM1 = str(name+"_density_TM1_x.dat")
	filename_y_TM1 = str(name+"_density_TM1_y.dat")

	
	file = open(filename_x_TM1, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_TM1.append(values[0])
		list_tot_x_TM1.append(values[0])

	file = open(filename_y_TM1, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_TM1.append(values[0])   
		list_tot_y_TM1.append(values[0])  

	center_TM1_x = np.average(list_x_TM1)
	center_TM1_y = np.average(list_y_TM1)



	filename_x_A544 = str(name+"_density_TM1_A544_x.dat")
	filename_y_A544 = str(name+"_density_TM1_A544_y.dat")

	file = open(filename_x_A544, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_A544.append(values[0])
		list_tot_x_A544.append(values[0])

	file = open(filename_y_A544, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_A544.append(values[0])   
		list_tot_y_A544.append(values[0])   

	center_A544_x = np.average(list_x_A544)
	center_A544_y = np.average(list_y_A544)



	filename_x_G548 = str(name+"_density_TM1_G548_x.dat")
	filename_y_G548 = str(name+"_density_TM1_G548_y.dat")

	file = open(filename_x_G548, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_G548.append(values[0])
		list_tot_x_G548.append(values[0])

	file = open(filename_y_G548, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_G548.append(values[0])   
		list_tot_y_G548.append(values[0])   

	center_G548_x = np.average(list_x_G548)
	center_G548_y = np.average(list_y_G548)

	circle_TM1 = plt.Circle((center_TM1_x, center_TM1_y), 4, color='silver', ec='black')
	circle_A544 = plt.Circle((center_A544_x, center_A544_y), 0.5, color='green', alpha=0.5)
	circle_G548 = plt.Circle((center_G548_x, center_G548_y), 0.5, color='lime', alpha=0.5)



	filename_x_G545 = str(name+"_density_TM1_G545_x.dat")
	filename_y_G545 = str(name+"_density_TM1_G545_y.dat")

	file = open(filename_x_G545, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_G545.append(values[0])
		list_tot_x_G545.append(values[0])

	file = open(filename_y_G545, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_G545.append(values[0])   
		list_tot_y_G545.append(values[0])   

	center_G545_x = np.average(list_x_G545)
	center_G545_y = np.average(list_y_G545)


	filename_x_G549 = str(name+"_density_TM1_G549_x.dat")
	filename_y_G549 = str(name+"_density_TM1_G549_y.dat")

	file = open(filename_x_G549, "r")

	for line in file.readlines():
		line_values = line.split()
		values = [float(x) for x in line_values]
		list_x_G549.append(values[0])
		list_tot_x_G549.append(values[0])

	file = open(filename_y_G549, "r")

	for line in file.readlines():

		line_values = line.split()
		values = [float(x) for x in line_values]
		list_y_G549.append(values[0])   
		list_tot_y_G549.append(values[0])   

	center_G549_x = np.average(list_x_G549)
	center_G549_y = np.average(list_y_G549)


	circle_TM1 = plt.Circle((center_TM1_x, center_TM1_y), 4, color='silver', ec='black')
	circle_A544 = plt.Circle((center_A544_x, center_A544_y), 0.5, color='green', alpha=0.5)
	circle_G548 = plt.Circle((center_G548_x, center_G548_y), 0.5, color='lime', alpha=0.5)
	circle_G545 = plt.Circle((center_G545_x, center_G545_y), 0.5, color='red', alpha=0.5)
	circle_G549 = plt.Circle((center_G549_x, center_G549_y), 0.5, color='salmon', alpha=0.5)

	bin_num=40

	array_op,xedges,yedges = np.histogram2d(list_x,list_y, bins=bin_num,range=[[xmin,xmax],[ymin,ymax]])


	max_array=max(array_op.flatten())
	array_avg = array_op/max_array
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]

	#ax[i,j].imshow(array_avg.T,extent=extent,interpolation='bicubic',origin='lower',cmap='BuPu', vmin=0, vmax=1)
	#ax[i,j].scatter(list_x, list_y, c=colors, s=1, cmap="plasma",  alpha=0.5, lw=0)
	ax[i,j].add_artist(circle_TM1)
	ax[i,j].add_artist(circle_A544)
	ax[i,j].add_artist(circle_G548)
	ax[i,j].add_artist(circle_G545)
	ax[i,j].add_artist(circle_G549)
	ax[i,j].set_aspect('equal')
	ax[i,j].set_yticks(np.arange(-20,20,10))
	ax[i,j].set_xticks(np.arange(-20,20,10))
	ax[i,j].set_xlim(-20,20)
	ax[i,j].set_ylim(-20,20)
	
	#fig.savefig('density_all.svg', dpi=200)


fig2 = matplotlib.pyplot.figure()
ax2 = fig2.add_subplot(111)
bin_num=40

center_TM1_x_tot = np.average(list_tot_x_TM1)
center_TM1_y_tot = np.average(list_tot_y_TM1)

center_A544_x_tot = np.average(list_tot_x_A544)
center_A544_y_tot = np.average(list_tot_y_A544)

center_G548_x_tot = np.average(list_tot_x_G548)
center_G548_y_tot = np.average(list_tot_y_G548)

center_G545_x_tot = np.average(list_tot_x_G545)
center_G545_y_tot = np.average(list_tot_y_G545)

center_G549_x_tot = np.average(list_tot_x_G549)
center_G549_y_tot = np.average(list_tot_y_G549)


circle_TM1_tot = plt.Circle((center_TM1_x_tot, center_TM1_y_tot), 4, color='silver', ec='black')
circle_A544_tot = plt.Circle((center_A544_x_tot, center_A544_y_tot), 1, color='green', alpha=0.5)
circle_G548_tot = plt.Circle((center_G548_x_tot, center_G548_y_tot), 1, color='lime', alpha=0.5)
circle_G545_tot = plt.Circle((center_G545_x_tot, center_G545_y_tot), 1, color='red', alpha=0.5)
circle_G549_tot = plt.Circle((center_G549_x_tot, center_G549_y_tot), 1, color='salmon', alpha=0.5)

array_op_tot,xedges,yedges = np.histogram2d(list_tot_x,list_tot_y, bins=bin_num,range=[[xmin,xmax],[ymin,ymax]])
max_array_tot=max(array_op_tot.flatten())
#print(max_array_tot)
#print(len(list_tot_x))
#array_avg_tot = array_op_tot/max_array_tot

max_array_tot=3206
scale=1.0
array_avg_tot = array_op_tot/(max_array_tot*scale)

extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]

cax=ax2.imshow(array_avg_tot.T,extent=extent,interpolation='bicubic',origin='lower',cmap='BuPu', vmin=0, vmax=1)
ax2.add_artist(circle_TM1_tot)
ax2.add_artist(circle_A544_tot)
ax2.add_artist(circle_G548_tot)
ax2.add_artist(circle_G545_tot)
ax2.add_artist(circle_G549_tot)
ax2.set_aspect('equal')
ax2.set_yticks(np.arange(-20,20,10))
ax2.set_xticks(np.arange(-20,20,10))
ax2.set_xlim(-20,20)
ax2.set_ylim(-20,20)
cbar= plt.colorbar(cax)
fig2.savefig('density_average_TMJH_DPPC.svg', dpi=200)


