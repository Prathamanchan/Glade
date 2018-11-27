#------------------------------------------------------------------------------
#
# MOS capacitor Pcell for extraction
#
# Note: The first argument is always the cellView of the subMaster.
#       All subsequent arguments should have default values and will
#       be passed by name. Each argument must be seperated by a comma
#	and whitespace.
#
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *
from math import *

# The entry point. The function name *must* match the filename.
#
def nmoscap_ex(cv, ptlist=[[0,0],[1000,0],[1000,1000],[0,1000]], area=1.0, perim=1.0) :
	lib = cv.lib()
	dbu = float(lib.dbuPerUU())
	npts = len(ptlist)

	# Area capacitance for this capacitor in F/um^2
	areacap = 1.15e-14
	# Perimeter capacitance for this capacitor in F/um
	pericap = 1.50e-14

	# Now compute c
	c = areacap * area + pericap * perim

	# Update the master pcell property.
	# NB dbAddProp will replace an existing property of same name.
	cv.dbAddProp("c", c)

	# Create the recognition region shape
	xpts = intarray(npts)
	ypts = intarray(npts)
	for i in range (npts) :
		xpts[i] = ptlist[i][0]
		ypts[i] = ptlist[i][1]
	# for
	cv.dbCreatePolygon(xpts, ypts, npts, TECH_Y0_LAYER);
	# Create pins
	plus_net = cv.dbCreateNet("G")
	cv.dbCreatePin("G", plus_net, DB_PIN_INPUT)
	minus_net = cv.dbCreateNet("S")
	cv.dbCreatePin("S", minus_net, DB_PIN_INPUT)

	# Set the device modelName property for netlisting
	cv.dbAddProp("modelName", "nmoscap")

	# Update the bounding box
	cv.update()
#
