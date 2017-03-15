def moveTo():
	print "Enter the starting X value"
	startx = int(raw_input("    >> "))

	print "Enter the starting Y value"
	starty = int(raw_input("    >> "))

	moveToStart = "cairo_move_to(cr, "
	moveToStop = ");"
	end = ", "
	x = str(startx)
	y = str(starty)

	print moveToStart + x + end + y + moveToStop

moveTo()



