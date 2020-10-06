
# create the ouput files to use for the python script
proc create_file {filename list} {

    set data_file [open $filename w]   
    set list_length [llength $list]
  
  	for { set i 0 } { $i < $list_length } { incr i 1 } {
  	  
  		puts $data_file [lindex $list $i]  	
  	}
  	 	close $data_file
}



proc interaction_time {sel sel2 molid_sel frames_end cutoff} {

	set counter 0
	set inter_time 0

	for { set f1 0} { $f1 < $frames_end } { incr f1 1 } {
 	 		
			set sel_1 [atomselect $molid_sel $sel frame $f1 ]
			set sel_2 [atomselect $molid_sel $sel2 frame $f1]

			set resname1 [lindex [$sel_1 get resname] 0]
			set resname2 [lindex [$sel_2 get resname] 0]		
		
			set coord1 [measure center $sel_1] 
   			set coord2 [measure center $sel_2]

   			set distance [veclength [vecsub "[lindex $coord2 0] [lindex $coord2 1] [lindex $coord2 2]" "[lindex $coord1 0] [lindex $coord1 1] [lindex $coord1 2]"]]

			if {$distance < $cutoff} {
				incr counter 1	
				set inter_time $f1
			}

			if {$counter > 15} {
				return $inter_time
				break
			}
        }

}


# align_start TM segment
proc align_start {sel_ref sel molid_ref molid} {

	set ref [atomselect $molid_ref $sel_ref frame 0 ]
	set sel_to_align [atomselect $molid $sel frame 0 ]
 	set transfo [measure fit $sel_to_align $ref]
	set sel_all [atomselect $molid "all" frame 0]

	$sel_all move $transfo

}

# align TM segment
proc align {molid sel_ref sel1 frames_begin frames_end dt} {

	set ref [atomselect $molid $sel_ref frame 0 ]

	for { set f1 $frames_begin } { $f1 < $frames_end } { incr f1 $dt } {

		set sel_to_align [atomselect $molid $sel1 frame $f1 ]
 		set transfo [measure fit $sel_to_align $ref]
		set sel_all [atomselect $molid "all" frame $f1]

		$sel_all move $transfo
	}
}

# create the ouput files to use for the python script
proc get_xy {sel molid_sel frames_begin frames_end dt filename_x filename_y} {

	set list_x ""
	set list_y ""

	for { set f1 $frames_begin } { $f1 < $frames_end } { incr f1 $dt } {

		set sel1 [atomselect $molid_sel $sel frame $f1 ]
		set x_value [$sel1 get {x}]
		set y_value [$sel1 get {y}]
		lappend list_x $x_value
		lappend list_y $y_value

		#puts $f1

	}
	set list_x [concat {*}$list_x]
	set list_y [concat {*}$list_y]
	

	create_file $filename_x $list_x
	create_file $filename_y $list_y


}

# DPPC TMJX sel1: index 0 to 71 sel2: index 72 to 143
# DPPC TMJX
for { set nb 1 } { $nb < 31 } { incr nb 1 } {
	puts $nb
	set gro_name "../../models/CG/sims_DPPC/protein_center.pdb"
	set xtc_name [join [concat "../../models/CG/sims_DPPC/md.flrt2TMH_jx_martini_DPPC_$nb" ".xtc"] ""]

	set data_name_TM1_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_x.dat"] ""]
	set data_name_TM1_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_y.dat"] ""]
	set data_name_TM2_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM2_x.dat"] ""]
	set data_name_TM2_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM2_y.dat"] ""]

	set data_name_TM1_A544_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_A544_x.dat"] ""]
	set data_name_TM1_A544_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_A544_y.dat"] ""]
	set data_name_TM1_G548_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G548_x.dat"] ""]
	set data_name_TM1_G548_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G548_y.dat"] ""]

	set data_name_TM1_G545_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G545_x.dat"] ""]
	set data_name_TM1_G545_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G545_y.dat"] ""]
	set data_name_TM1_G549_x [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G549_x.dat"] ""]
	set data_name_TM1_G549_y [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_density_TM1_G549_y.dat"] ""]

	set out_name_TM1 [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_plot_TM1.svg"] ""]
	set out_name_TM2 [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_plot_TM2.svg"] ""]
	set out_name_TM2 [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_plot_TM2.svg"] ""]


	set molid [mol new $gro_name type pdb first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all]
	mol addfile  $xtc_name type xtc first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
	set frames_end [molinfo $molid get numframes]	

	align $molid "index 7 to 54 and type BB" "index 7 to 54 and type BB" 1  $frames_end 1
	
	set intert [interaction_time "index 8 to 59" "index 80 to 131" $molid $frames_end 10]


	if {$intert > 0} {
		get_xy "index 7 to 54 and type BB" $molid $intert $frames_end 1 $data_name_TM1_x $data_name_TM1_y
		get_xy "index 79 to 126 and type BB" $molid $intert $frames_end 1 $data_name_TM2_x $data_name_TM2_y

		get_xy "index 15" $molid $intert $frames_end 1 $data_name_TM1_A544_x $data_name_TM1_A544_y
		get_xy "index 16" $molid $intert $frames_end 1 $data_name_TM1_G545_x $data_name_TM1_G545_y	
		get_xy "index 21" $molid $intert $frames_end 1 $data_name_TM1_G548_x $data_name_TM1_G548_y
		get_xy "index 22" $molid $intert $frames_end 1 $data_name_TM1_G549_x $data_name_TM1_G549_y			
	}
	mol delete $molid
}


