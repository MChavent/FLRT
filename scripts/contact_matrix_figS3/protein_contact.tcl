# calculate the distance between 2 proteins.
# Create input files for the script contact.py
# Matthieu Chavent 2020
 
####------------------------------------------------------------
#   
#
#    Functions useful and used in the main function at the end
#
#
####-------------------------------------------------------------


# fill the list with relevant data (ie contact nb)
# molID: ID of the molecule
# selec1: VMD selection for the protein
# selec2: VMD selection for the molecules in interaction (ie lipids)
# first_res: first res nb
# length: length of the protein
# step: stepsize
# starting_time: interaction time calculated with interaction_time function - see before 
# cutoff: cutoff distance
# list: list to fill

# find the frame where the TM start to interact
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

# create the ouput files to use for the python script
proc create_file {filename list} {

    set data_file [open $filename w]    
    set list_length [llength $list]
  
  	for { set i 0 } { $i < $list_length } { incr i 1 } {
  	  
  		puts $data_file [lindex $list $i]	
  	}
  	 	close $data_file
}


# create a list filled with 0
proc create_list_dist {length1 length2} {

    set list {}
 	
  	for { set index1 0 } { $index1 < $length1 } { incr index1 1 } {
	
		set list_temp {}

		for { set index2 0 } { $index2 < $length2 } { incr index2 1 } {
		
  			lappend list_temp 0
		}

		lappend list $list_temp
  	}			     
 		
 	return $list	
	
}


proc find_min_dist {molID sel1 sel2 frame} {

	set distance 10.0

	set list_index1 [$sel1 get index]
	set list_index2 [$sel2 get index]

	foreach index1 $list_index1 {

		foreach index2 $list_index2 {
	
			set index1_sel [atomselect $molID "index $index1" frame $frame]
			set index2_sel [atomselect $molID "index $index2" frame $frame]
		
			set coord_index1 [$index1_sel get {x y z}]
			set coord_index2 [$index2_sel get {x y z}]

			set distance_temp [vecdist [lindex $coord_index1 0] [lindex $coord_index2 0]]
			
			if {$distance_temp < $distance} {
				set distance $distance_temp
			}	
		}
	}	
	return $distance
}


proc dist_map_frame {molID selec1 selec2 first_res1 length1 first_res2 length2 frame output_name} {
    
  set distance_list {}
  set res_list1 {}  
		     	
 	for { set res_index1 $first_res1 } { $res_index1 < [expr $length1+$first_res1]  } { incr res_index1 1 } {

  	    set temp_list {}	
	    set res_list2 {}
	    set res_name1 ""
	    set res_id1 ""

	    for { set res_index2 $first_res2 } { $res_index2 < [expr $length2+$first_res2]  } { incr res_index2 1 } {
			set sel1 [atomselect $molID "$selec1 and resid $res_index1" frame $frame]
			set sel2 [atomselect $molID "$selec2 and resid $res_index2" frame $frame]

			set res_name1 [lindex [$sel1 get resname] 0]
			set res_id1 [lindex [$sel1 get resid] 0]
			set res_name2 [lindex [$sel2 get resname] 0]
			set res_id2 [lindex [$sel2 get resid] 0]

			#set CoM1 [measure center $sel1]
			#set CoM2 [measure center $sel2]
			#set distance [vecdist $CoM1 $CoM2]
			set distance [find_min_dist $molID $sel1 $sel2 $frame] 

			lappend temp_list $distance
			lappend res_list2 "$res_name2 $res_id2" 

			# empty memory space
			$sel1 delete
			$sel2 delete

			
 		}

	lappend res_list1 "$res_name1 $res_id1"
 	lappend distance_list [lreverse $temp_list]

 	}


     create_file "seq1_$output_name.txt" $res_list1
     create_file "seq2_$output_name.txt" $res_list2
     create_file "dist_matrix_$output_name.txt" $distance_list

    exec python /data/VERITY/script/matrix_distance.py "dist_matrix_$output_name.txt" "seq1_$output_name.txt" "seq2_$output_name.txt" $output_name
	
}

proc dist_map_time {molID selec1 selec2 first_res1 length1 first_res2 length2 frame distance_list} {
    
  set distance_list2 ""
  set res_list1 {}  
  set counter_res1 0	
	     	
 	for { set res_index1 $first_res1 } { $res_index1 < [expr $length1+$first_res1]  } { incr res_index1 1 } {

	    set temp_list [lreverse [lindex $distance_list $counter_res1]]
	    set res_list2 {}
	    set res_name1 ""
	    set res_id1 ""
	    set counter_res2 0

	    for { set res_index2 $first_res2  } { $res_index2 < [expr $length2+$first_res2] } { incr res_index2 1 } {

			set sel1 [atomselect top "($selec1) and resid $res_index1" frame $frame]
			set sel2 [atomselect top "($selec2) and resid $res_index2" frame $frame]

			set res_name1 [lindex [$sel1 get resname] 0]
			set res_id1 [lindex [$sel1 get resid] 0]
			set res_name2 [lindex [$sel2 get resname] 0]
			set res_id2 [lindex [$sel2 get resid] 0]

			set distance [find_min_dist $molID $sel1 $sel2 $frame] 
			set total_distance [expr [lindex $temp_list $counter_res2]+$distance] 
			set temp_list [lreplace $temp_list $counter_res2 $counter_res2 $total_distance] 

			lappend res_list2 "$res_name2 $res_id2" 

			$sel1 delete
			$sel2 delete
			incr counter_res2 1

 		}

	lappend res_list1 "$res_name1 $res_id1"
 	lappend distance_list_2 [lreverse $temp_list]
	incr counter_res1 1
 	}

     create_file "seq1.txt" $res_list1
     create_file "seq2.txt" $res_list2 
     return $distance_list_2 	
}

proc dist_map_avg {molID selec1 selec2 first_res1 length1 first_res2 length2 start_frame end_frame dt output_name} {
    
	set list_dist_tot [create_list_dist [expr $length1] [expr $length2]] 
	set list_dist_tot2 ""

	for { set frame $start_frame } { $frame < $end_frame  } { incr frame $dt } {
		puts $frame
		set list_dist_tot [dist_map_time $molID $selec1 $selec2 $first_res1 $length1 $first_res2 $length2 $frame $list_dist_tot]
					  

 	}
	
	puts $list_dist_tot
	set scale_nb [expr (($end_frame - $start_frame)*1.0)/($dt*1.0)]	
	puts $scale_nb
	
	for { set index1 0 } { $index1 < [llength $list_dist_tot]  } { incr index1 1 } {
	
		set list_temp [lindex $list_dist_tot $index1]
		#puts $list_temp
		
		for { set index2 0 } { $index2 < [llength $list_temp]  } { incr index2 1 } {

			set temp_val [expr [lindex $list_temp $index2] / $scale_nb]
			
			set list_temp [lreplace $list_temp $index2 $index2 $temp_val]

		}
		#puts $list_temp
		lappend list_dist_tot2 $list_temp
		#puts ""
	}
     puts "   "
     puts $list_dist_tot2
     create_file $output_name $list_dist_tot2

#exec python /data/CR3/scripts/matrix_distance.py "dist_matrix.txt" "seq1.txt" "seq2.txt" $output_name
}


proc dist_vs_time {molID selec1 selec2 first_res1 length1 first_res2 length2 start_frame end_frame dt} {

	for { set frame $start_frame } { $frame < $end_frame  } { incr frame $dt } {
		set nb [format "%05d" $frame] 
		dist_map_frame $molID $selec1 $selec2 $first_res1 $length1 $first_res2 $length2 $frame "inter_$nb"
		puts "frame $frame" 
	}
}



		

# DPPC TMJX sel1: index 0 to 71 sel2: index 72 to 143
# DPPC TMJX
for { set nb 1 } { $nb < 31 } { incr nb 1 } {

	set intert 0	
	set gro_name "../../models/CG/sims_DPPC/protein.gro"
	set xtc_name [join [concat "../../models/CG/sims_DPPC/md.flrt2TMH_jx_martini_DPPC_$nb" ".xtc"] ""]
	set data_name [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_inter.dat"] ""]
	set inter_time_name [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_inter_time.dat"] ""]
	
	set molid [mol new $gro_name type gro first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all]
	mol addfile  $xtc_name type xtc first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
	set frames_end [molinfo $molid get numframes]

	set intert [interaction_time "index 8 to 59" "index 80 to 131" $molid $frames_end 10]
	puts $intert


	if {$intert > 0} { 
		set inter_weight [expr ($frames_end - $intert)/2.0]
		create_file $inter_time_name $inter_weight
		dist_map_avg top "index 0 to 71" "index 72 to 143" 1 32 1 32 $intert $frames_end 2 $data_name
		lappend list_files "md.flrt2TMH_jx_martini_DPPC_$nb , "
	}
	mol delete $molid

	puts $list_files
}

