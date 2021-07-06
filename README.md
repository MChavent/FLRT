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


crossing angle figure 3-A
-------------------------
vmd -dispdev text -e crossing_angle_all.tcl

python histo_cross_all.py


crossing Vs distance angle figure 3-A
-------------------------------------
vmd -dispdev text -e distance_CA.tcl

python plot_CAvsD.py   (averaged density)

python plot_CAvsD_eachsim.py (single simulation data on top of the averaged data)


TM contact 3-B
--------------
vmd -dispdev text -e protein_contact.tcl 


Density 4-B
-----------
vmd -dispdev text -e get_density_TM.tcl

python plot_density_all.py 

Note: this tcl script was also used to display lipid densities for the PM-like system (see Fig. 2-B)


Most representative structures for TM dimer in PM membrane
---------------------------------------------

the coordinates of the main representative structures for RH1 and RH2 configurations in a PM membrane are available in the folder Models/PM


Starting coordinates for CG-FEP calculations
---------------------------------------------

the starting coordinates of the systems for CG-FEP calculations are available in the Models/FEP folder


display main representations 
----------------------------
open VMD

   for CG: File -> Load Visualization state -> TM_main_struct_XXX.vmd
   
   for AT: File -> Load Visualization state -> XXX_AT_end.vmd
