#------------------------------------------------------------------------------
#
# NMOS Pcell for NCH_SVT_1.8V device. 
#	Create a Pcell with parameters w (width of gate),
#	l (length of gate), m (number of gates).
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *

# The entry point. The function name *must* match the filename.
def NCH_SVT_1P8V(cv, w=0.42, l=0.18, m=1, polyCnt=0, leftCnt=1, rightCnt=1) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()
	tech = lib.tech()
	width = int(w * dbu)
	length = int(l * dbu)
	fingers = int(m)

	# Some predefined rules
	cont_width = int(0.22 * dbu)
	cont_space = int(0.25 * dbu)
	sdpwell_ovlp_pdiff = int(0.12 * dbu)
	poly_to_cont = int(0.16 * dbu)
	active_ovlp_cont = int(0.10 * dbu)

	diff_to_diff_space = int(0.28 * dbu)
	ndiff_ovlp_pwell = int(0.43 * dbu)
	poly_extn_diff = int(0.22 * dbu)
	pdiff_ovlp_pwell = int(0.12 * dbu)
	ndiff_ovlp_nimp = int(0.18 * dbu)
	pdiff_BgCont_ovlp_pimp = int(0.02 * dbu)

	poly_ovlp_cont = int(0.10 * dbu)
	metal_ovlp_cont = int(0.005 * dbu)
	poly_via_size = cont_width + (2 * poly_ovlp_cont)
	poly_via_neck_offset = poly_via_size / 2 - length / 2

	# Create DIFF
	tech = lib.tech()
	diff = tech.getLayerNum("DIFF", "drawing")
	height = active_ovlp_cont*2 + cont_width*(fingers + 1) + poly_to_cont*2*fingers + length*fingers
	r = Rect(-height/2, -width/2, height/2, width/2)
	diff = cv.dbCreateRect(r, diff);

	# Create PWELL
	pwell = tech.getLayerNum("PWELL", "drawing")
	r = Rect(-height/2 - ndiff_ovlp_pwell,
		-width/2 - ndiff_ovlp_pwell,
		height/2 + ndiff_ovlp_pwell,
		+width/2 + ndiff_ovlp_pwell,)
	pwell = cv.dbCreateRect(r, pwell);
	net = cv.dbCreateNet("B")
	pin = cv.dbCreatePin("B", net, DB_PIN_INPUT)
	cv.dbCreatePort(pin, pwell)

	# Create NIMP
	nimp = tech.getLayerNum("NIMP", "drawing")
	r = Rect(-height/2 - ndiff_ovlp_nimp, 
		 -width/2 - ndiff_ovlp_nimp, 
		 height/2 + ndiff_ovlp_nimp,
		 width/2 + ndiff_ovlp_nimp)
	cv.dbCreateRect(r, nimp);
	
	# Create poly fingers
	poly = tech.getLayerNum("POLY", "drawing")
	metal1 = tech.getLayerNum("MET1", "drawing")
	cont = tech.getLayerNum("CONT", "drawing")
	xoffset = active_ovlp_cont + cont_width + poly_to_cont -height/2
	for i in range(fingers) :
		p = Rect(xoffset, 
			-width/2 -poly_extn_diff,
			(xoffset + length),
			width/2 + poly_extn_diff)
		gate = cv.dbCreateRect(p, poly)
		net = cv.dbCreateNet("G")
		pin = cv.dbCreatePin("G", net, DB_PIN_INPUT)
		
		cv.dbCreatePort(pin, gate)
		xoffset = xoffset + length + 2*poly_to_cont + cont_width						

		# Create S/D contacts
	cont = tech.getLayerNum("CONT", "drawing")
	
	if w < 0.5 :
		numCuts = 1
		yfudge = 0
		xoffset = active_ovlp_cont - height/2
	else :
		numCuts = width / (cont_width + cont_space)
		yfudge = (width - numCuts * (cont_width + cont_space)) / 2
		xoffset = active_ovlp_cont - height/2
	if (leftCnt and rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cont + yfudge -width/2 
			for j in range(numCuts) :
				cut = Rect(0, 0, cont_width, cont_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cont_width + cont_space
			xoffset = xoffset + length + 2*poly_to_cont + cont_width
	if (leftCnt and not rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cont + yfudge -width/2
			for j in range(numCuts) :
				cut = Rect(0, 0, cont_width, cont_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cont_width + cont_space
			xoffset = xoffset + length + 2*poly_to_cont + cont_width
	if (not leftCnt and rightCnt) :
		for i in range(fingers+1) :
			yoffset = active_ovlp_cont + yfudge -width/2
			for j in range(numCuts) :
				cut = Rect(0, 0, cont_width, cont_width)
				cut.offset(xoffset, yoffset)
				cv.dbCreateRect(cut, cont)
				yoffset = yoffset + cont_width + cont_space
			xoffset = xoffset + length + 2*poly_to_cont + cont_width

			# Create metal
	metal1 = tech.getLayerNum("MET1", "drawing")
	xoffset = active_ovlp_cont - metal_ovlp_cont - height/2
	for i in range(fingers+1) :
		met = Rect(0, -width/2, cont_width + 2*metal_ovlp_cont, width/2)
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
		xoffset = xoffset + length + 2*poly_to_cont + cont_width

	
	# Update the bounding box
	cv.update()
