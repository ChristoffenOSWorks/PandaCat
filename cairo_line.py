def lineTo():
	print "Please enter the number of pairs you want drawn"
	number_of_times = int(raw_input("    >> "))
	time_current = 0

	while (time_current < number_of_times):
		print "Please enter X value of the first pair"
		point_x1 = float(raw_input("    >> "))

		print "Please enter Y value of the first pair"
		point_y1 = float(raw_input("    >> "))

		lineToStart = "cairo_line_to(cr, "
		lineToEnd = ");\n"
		end = ", "
		x1 = str(point_x1)
		y1 = str(point_y1)
	
		with open('out.txt', 'a') as f:
			print >> f, lineToStart + x1 + end + y1 + lineToEnd
		f.close()
		time_current += 1

	if (time_current == number_of_times):
		with open('out.txt', 'a') as f:
			print >> f, "cairo_close_path(cr);"
		f.close()



















	



