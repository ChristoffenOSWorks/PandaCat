number_of_times = int(raw_input("Please enter the number of pairs you want drawn"))
time_current = 0

while (time_current < number_of_times):
    print "Please enter X value of the first pair"
    point_x1 = float(raw_input("    >> "))

    print "Please enter Y value of the first pair"
    point_y1 = float(raw_input("    >> "))
    
    print "cairo_line_to(cr, " + str(point_x1) + ", " + str(point_y1) + ");\n"

    time_current += 1
	



