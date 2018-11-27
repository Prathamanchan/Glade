#------------------------------------------------------------------------------
#
# NMOS Pcell example. 
#	    Create a Pcell with parameters w (width of gate),
#	    l (length of gate), m (number of gates).
#
# Note: The first argument is always the cellView of the subMaster.
#       All subsequent arguments should have default values and will
#       be passed by name. Each argument should be seperated by a comma
#	    and whitespace. 
#       This Pcell uses w/l units of metres. This is compatible with schematics
#       where the symbols have values of e.g. w=2u (spice syntax)
#
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *

# The entry point. The function name *must* match the filename.
def nch(cv, w=1.1e-6, l=0.13e-6, m=1, polyCnt=0, leftCnt=1, rightCnt=1) :
	lib = cv.lib()
	dbu = float(lib.dbuPerUU())
	width = int(w * 1.0e6 * dbu )
	length = int(l * 1.0e6 * dbu )
	fingers = int(m)

	# Some predefined rules
	cut_width = int(0.16 * dbu)
	cut_space = int(0.18 * dbu)
	pwell_ovlp_active = int(0.31 * dbu)
	poly_to_cut = int(0.11 * dbu)
	active_ovlp_cut = int(0.07 * dbu)
	poly_ovlp_active = int(0.18 * dbu)
	poly_ovlp_cut = int(0.07 * dbu)
	nplus_ovlp_active = int(0.18 * dbu)
	metal_ovlp_cut = int(0.07 * dbu)
	poly_via_size = cut_width + 2 * poly_ovlp_cut
	poly_via_neck_offset = poly_via_size / 2 - length / 2

	# Create active
	tech = lib.tech()
	od = tech.getLayerNum("od", "drawing")
	height = active_ovlp_cut*2 + cut_width*(fingers + 1) + poly_to_cut*2*fingers + length*fingers
	r = Rect(-height/2, -width/2, height/2, width/2)
	active = cv.dbCreateRect(r, od);

	# Create pwell
	pwell = tech.getLayerNum("psub", "drawing")
	r.bias(pwell_ovlp_active)
	pwell = cv.dbCreateRect(r, pwell);
	net = cv.dbCreateNet("B")
	pin = cv.dbCreatePin("B", net, DB_PIN_INPUT)
	cv.dbCreatePort(pin, pwell)

	# Create nplus
	nimp = tech.getLayerNum("nimp", "drawing")
	r = Rect(-height/2 - nplus_ovlp_active, 
		 -width/2 - nplus_ovlp_active, 
		 height/2 + nplus_ovlp_active,
		 width/2 + nplus_ovlp_active)
	cv.dbCreateRect(r, nimp);

	# Create poly fingers
	poly = tech.getLayerNum("polyg", "drawing")
	metal1 = tech.getLayerNum("metal1", "drawing")
	cont = tech.getLayerNum("cont", "drawing")
	xoffset = active_ovlp_cut + cut_width + poly_to_cut -height/2
	for i in range(fingers) :
		p = Rect(xoffset, 
			-width/2 -poly_ovlp_active,
			xoffset + length,
			width/2 + poly_ovlp_active)
		gate = cv.dbCreateRect(p, poly)
		net = cv.dbCreateNet("G")
		pin = cv.dbCreatePin("G", net, DB_PIN_INPUT)
		if polyCnt :
			numCuts = length / (cut_width + cut_space)
			xoffset = active_ovlp_cut + cut_width + poly_to_cut -height/2
			if width < poly_via_size :
				q = Rect(xoffset - poly_via_neck_offset,
					 width/2 + poly_ovlp_active,
					 xoffset + length + poly_via_neck_offset,
					 width/2 + poly_ovlp_active + poly_via_size)
				cv.dbCreateRect(q, poly)
				metpin = cv.dbCreateRect(q, metal1)
				cv.dbCreatePort(pin, metpin)
			else :
				q = Rect(xoffset,
					 width/2 + poly_ovlp_active,
					 xoffset + length,
					 width/2 + poly_ovlp_active + poly_via_size)
				cv.dbCreateRect(q, poly)
				metpin = cv.dbCreateRect(q, metal1)
				cv.dbCreatePort(pin, metpin)
			xfudge = (length - numCuts * (cut_width + cut_space)) / 2
			xoffset = active_ovlp_cut + cut_width + poly_to_cut + poly_ovlp_cut + xfudge -height/2
			for j in range(numCuts) :
				r = Rect(xoffset,
				 	width/2 + poly_ovlp_active + poly_ovlp_cut,
				 	xoffset + cut_width,
				 	width/2 + poly_ovlp_active + poly_ovlp_cut + cut_width)
				cv.dbCreateRect(r, cont)
				xoffset = xoffset + cut_width + cut_space
		else :
			cv.dbCreatePort(pin, gate)
		xoffset = xoffset + length + 2*poly_to_cut + cut_width

	# Create S/D contacts
	cont = tech.getLayerNum("cont", "drawing")
	numCuts = (width - 2*active_ovlp_cut + cut_space) / (cut_width + cut_space)
	yfudge = (width - numCuts * (cut_width + cut_space)) / 2
	xoffset = active_ovlp_cut - height/2
	if (leftCnt and rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cut + yfudge -width/2 
			for j in range(numCuts) :
				cut = Rect(0, 0, cut_width, cut_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cut_width + cut_space
			xoffset = xoffset + length + 2*poly_to_cut + cut_width
	if (leftCnt and not rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cut + yfudge -width/2
			for j in range(numCuts) :
				cut = Rect(0, 0, cut_width, cut_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cut_width + cut_space
			xoffset = xoffset + length + 2*poly_to_cut + cut_width
	if (not leftCnt and rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cut + yfudge -width/2
			for j in range(numCuts) :
				cut = Rect(0, 0, cut_width, cut_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cut_width + cut_space
			xoffset = xoffset + length + 2*poly_to_cut + cut_width
			
	# Create metal
	metal1 = tech.getLayerNum("metal1", "drawing")
	xoffset = active_ovlp_cut - metal_ovlp_cut - height/2
	for i in range(fingers+1) :
		met = Rect(0, -width/2, cut_width + 2*metal_ovlp_cut, width/2)
		met.offset(xoffset, 0)
		if (i+1) % 2 :
			source = cv.dbCreateRect(met, metal1)
			net = cv.dbCreateNet("S")
			pin = cv.dbCreatePin("S", net, DB_PIN_INOUT)
			cv.dbCreatePort(pin, source)
		else :
			drain = cv.dbCreateRect(met, metal1)
			net = cv.dbCreateNet("D")
			pin = cv.dbCreatePin("D", net, DB_PIN_INOUT)
			cv.dbCreatePort(pin, drain)
		xoffset = xoffset + length + 2*poly_to_cut + cut_width
	
	# Device type
	cv.dbAddProp("type", "mos")

	# Update the bounding box
	cv.update()
