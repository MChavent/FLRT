# FLRT
material and scripts used to create figures of the bioRxiv preprint: "The guidance and adhesion protein FLRT2 dimerizes in cis via dual Small-X3-Small transmembrane motifs" Verity Jackson et al. , BioRxiv 2020 

If you are using these scripts please cite: 
Verity Jackson et al. , BioRxiv 2020 

Scripts to analyse data in the models/CG/sims_DPPC/ repository
xtc and gro files contain only TM dimers to reduce the size of each file.

distance bars figure 1-D
------------------------
vmd -dispdev text -e calculate_distance.tcl
python python_matrix.py


crossing angle figure 2-A
-------------------------
vmd -dispdev text -e crossing_angle_all.tcl

python histo_cross_all.py


crossing Vs distance angle figure 2-A
-------------------------------------
vmd -dispdev text -e distance_CA.tcl

python plot_CAvsD.py   (averaged density)

python plot_CAvsD_eachsim.py (single simulation data on top of the averaged data)


TM contact 2-B
--------------
vmd -dispdev text -e protein_contact.tcl 

python matrix_distance_TM_avg.py 


Density 3-B
-----------
vmd -dispdev text -e get_density_TM.tcl

python plot_density_all.py 


display main representations as figures 2B and S12B
---------------------------------------------------
open VMD

   for CG: File -> Load Visualization state -> TM_main_struct_XXX.vmd
   
   for AT: File -> Load Visualization state -> XXX_AT_end.vmd
