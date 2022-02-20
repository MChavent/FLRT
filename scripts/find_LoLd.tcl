
proc create_file {filename list} {

    set data_file [open $filename w]   
    set list_length [llength $list]
  
  	for { set i 0 } { $i < $list_length } { incr i 1 } {
  	  
  		puts $data_file [lindex $list $i]  	
  	}
  	 	close $data_file
}

proc LovsLd {molid sel start end dt filename } {

	set list_perc ""

	for {set frame $start} {$frame < $end} {incr frame $dt} {

		puts $frame
		set DPPC [atomselect top "(resname DPPC and type PO4) and within 10 of $sel" frame $frame]
		set DIPC [atomselect top "(resname DIPC and type PO4) and within 10 of $sel" frame $frame]
		
		set nb_DPPC [$DPPC num]
		set nb_DIPC [$DIPC num]
		
		set perc [expr $nb_DIPC/double($nb_DPPC+$nb_DIPC)]
		
		lappend list_perc "$frame  $perc"
	}

	create_file $filename $list_perc
	
}
