

proc create_file {filename list1 list2} {

    set data_file [open $filename w]   
    set list_length [llength $list1]
  
  	for { set i 0 } { $i < $list_length } { incr i 1 } {
  	  
  		puts $data_file "[lindex $list1 $i]\t [lindex $list2 $i]"  	
  	}
  	 	close $data_file
}

proc distance {sel sel2 molid_sel frames_begin frames_end dt filename} {

	set list_time ""
	set list_distance ""
	set counter 0

	for { set f1 $frames_begin } { $f1 < $frames_end } { incr f1 $dt } {
 	 		
			set sel_1 [atomselect $molid_sel $sel frame $f1 ]
			set sel_2 [atomselect $molid_sel $sel2 frame $f1]

			set resname1 [lindex [$sel_1 get resname] 0]
			set resname2 [lindex [$sel_2 get resname] 0]
			
			if {$counter == 0 } {
				puts "distance $resname1 - $resname2"
			}			
		
			set coord1 [measure center $sel_1] 
   			set coord2 [measure center $sel_2]

   			set distance [veclength [vecsub "[lindex $coord2 0] [lindex $coord2 1] [lindex $coord2 2]" "[lindex $coord1 0] [lindex $coord1 1] [lindex $coord1 2]"]]

			lappend list_time $f1
			lappend list_distance $distance
			incr counter 1

        }
	
	create_file $filename $list_time $list_distance
	#set plothandle [multiplot -x $list_time -y $list_distance -lines -linewidth 3 -marker point -plot -ymin 0]

}

# DPPC TMJX sel1: index 0 to 71 sel2: index 72 to 143
# DPPC TMJX

for { set nb 1 } { $nb < 31 } { incr nb 1 } {
	puts $nb
	set gro_name "../../models/CG/sims_DPPC/protein.gro"
	set xtc_name [join [concat "../../models/CG/sims_DPPC/md.flrt2TMH_jx_martini_DPPC_$nb" ".xtc"] ""]

	set molid [mol new $gro_name type gro first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all]
	mol addfile  $xtc_name type xtc first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
	distance "index 0 to 71" "index 72 to 143" $molid 1 1001 1 distance_TMJ_$nb.dat
	mol delete $molid
}

