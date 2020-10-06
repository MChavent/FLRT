 

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


proc create_file {filename list} {

    set data_file [open $filename w]   
    set list_length [llength $list]
  
  	for { set i 0 } { $i < $list_length } { incr i 1 } {
  	  
  		puts $data_file [lindex $list $i]  	
  	}
  	 	close $data_file
}

proc principal_axe {molid sel frame} {

	set selection [atomselect $molid $sel frame $frame]
	set inertia [measure inertia $selection]
	set dir [lindex [lindex $inertia 1] 2] 	

	$selection delete

	return $dir

}

proc VecN {molid sel1 sel2 frame} {
	set selection1 [atomselect $molid $sel1 frame $frame]
	set selection2 [atomselect $molid $sel2 frame $frame]
	set Vn [vecnorm [vecsub [measure center "$selection2"] [measure center "$selection1"]]]

	return $Vn

}



proc axe {molid sel frame} {

	set vector [vecnorm [principal_axe $molid "$sel" $frame]]
	#plot_vec $molid $sel $frame $vector

	#set costetha [vecdot "[lindex $vector 0] [lindex $vector 1] [lindex $vector 2]" "0 0 1"]
	#set Smol [expr (3*$costetha*$costetha-1)/2]

	return $vector
}

proc crossing_angle {molid sel1 sel2 frame} {


	set v1 [axe $molid $sel1 $frame]	
	set v2 [axe $molid $sel2 $frame]	
	set angle [expr (180*acos([vecdot "[lindex $v1 0] [lindex $v1 1] [lindex $v1 2]" "[lindex $v2 0] [lindex $v2 1] [lindex $v2 2]"]))/3.14159]
	set cross [veccross "[lindex $v1 0] [lindex $v1 1] [lindex $v1 2]" "[lindex $v2 0] [lindex $v2 1] [lindex $v2 2]"]
	set Vn [VecN $molid $sel1 $sel2 $frame]
	set sign [vecdot $cross $Vn]
	if {$sign < 0} {
		set angle [expr -$angle]	
	}
	
	if {$angle > 90} {
		set angle [expr $angle-180]	
	}

	if {$angle < -90} {
		set angle [expr $angle+180]	
	}

	return "$angle"

}


proc cross_vs_time {molid sel1 sel2 start end dt filename} {

	set list_angle ""
	set list_frame ""

	for {set frame $start} {$frame < $end} {incr frame $dt} {

		set angle [crossing_angle $molid $sel1 $sel2 $frame]
		lappend list_angle $angle
		lappend list_frame $frame
	}

	create_file $filename $list_angle 
	#exec python histo_cross.py $filename "-80" "80" $filename ".svg"
	#set plothandle [multiplot -x $list_frame -y $list_angle -title "Crossing Angle vs time" -lines -linewidth 3 -marker point -plot]
}

proc save_frames {molid sel1 sel2 start end dt min_angle max_angle} {

	set frame_list ""

	for {set frame $start} {$frame < $end} {incr frame $dt} {

		set angle [crossing_angle $molid $sel1 $sel2 $frame]

		if {$angle < $max_angle && $angle > $min_angle} {
			lappend frame_list $frame
		}

	}

	return $frame_list
}

# DPPC TMJX sel1: index 0 to 71 sel2: index 72 to 143
# DPPC TMJX

for { set nb 1 } { $nb < 31 } { incr nb 1 } {

	set gro_name "../../models/CG/sims_DPPC/protein.gro"
	set xtc_name [join [concat "../../models/CG/sims_DPPC/md.flrt2TMH_jx_martini_DPPC_$nb" ".xtc"] ""]
	set data_name [join [concat "md.flrt2TMH_jx_martini_DPPC_$nb" "_cross.dat"] ""]


	set molid [mol new $gro_name type gro first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all]
	mol addfile  $xtc_name type xtc first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
	set frames_end [molinfo $molid get numframes]

	set intert [interaction_time "index 8 to 59" "index 80 to 131" $molid $frames_end 10]
	puts $intert
	if {$intert > 0} {
		cross_vs_time $molid "index 8 to 59 and type BB" "index 80 to 131 and type BB" $intert $frames_end 1 $data_name
	}
	mol delete $molid
}

