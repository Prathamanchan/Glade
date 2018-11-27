#------------------------------------------------------------------------------
#
# MOSCAP Pcell example. 
#	Create a Pcell with parameters w (width of gate), l (length of gate)
#
# Note: The first argument is always the cellView of the subMaster.
#       All subsequent arguments should have default values and will
#       be passed by name. Each argument should be seperated by a comma
#	and whitespace.
#
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *

# The entry point. The function name *must* match the filename.
def nmoscap(cv, w=2.0, l=2.0) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()
	width = int(w * dbu)
	length = int(l * dbu)

	# Area capacitance for this capacitor in F/um^2
	areacap = 1.15e-14
	# Perimeter capacitance for this capacitor in F/um
	pericap = 1.50e-14
	
	# Some predefined rules
	cut_width = int(0.16 * dbu)
	cut_space = int(0.18 * dbu)
	nwell_ovlp_active = int(0.31 * dbu)
	poly_to_cut = int(0.11 * dbu)
	active_ovlp_cut = int(0.07 * dbu)
	poly_ovlp_active = int(0.18 * dbu)
	poly_ovlp_cut = int(0.07 * dbu)
	pplus_ovlp_active = int(0.18 * dbu)
	metal_ovlp_cut = int(0.07 * dbu)
	poly_via_size = cut_width + 2 * poly_ovlp_cut
	poly_via_neck_offset = poly_via_size / 2 - length / 2

	# Create active
	tech = lib.tech()
	od = tech.getLayerNum("od", "drawing")
	height = active_ovlp_cut*2 + cut_width*2 + poly_to_cut*2
	r = Rect(0, 0, length + height, width)
	active = cv.dbCreateRect(r, od);

	# Create nwell
	nwell = tech.getLayerNum("nwell", "drawing")
	r.bias(nwell_ovlp_active)
	nwell = cv.dbCreateRect(r, nwell);
	net = cv.dbCreateNet("B")
	pin = cv.dbCreatePin("B", net, DB_PIN_INPUT)
	cv.dbCreatePort(pin, nwell)

	# Create cap recognition region
	cap = tech.getLayerNum("cap", "drawing")
	cv.dbCreateRect(r, cap);

	# Create pplus
	pimp = tech.getLayerNum("pimp", "drawing")
	r = Rect(- pplus_ovlp_active, 
		 - pplus_ovlp_active, 
		 length + height + pplus_ovlp_active,
		 width + pplus_ovlp_active)
	cv.dbCreateRect(r, pimp);

	# Create poly 
	poly = tech.getLayerNum("polyg", "drawing")
	metal1 = tech.getLayerNum("metal1", "drawing")
	cont = tech.getLayerNum("cont", "drawing")
	xoffset = active_ovlp_cut + cut_width + poly_to_cut
	p = Rect(xoffset, 
		-poly_ovlp_active,
		xoffset + length,
		width + poly_ovlp_active)
	gate = cv.dbCreateRect(p, poly)
	net = cv.dbCreateNet("PLUS")
	pin = cv.dbCreatePin("PLUS", net, DB_PIN_INPUT)
	# Poly contact 
	numCuts = length / (cut_width + cut_space)
	xoffset = active_ovlp_cut + cut_width + poly_to_cut
	q = Rect(xoffset,
		 width + poly_ovlp_active,
		 xoffset + length,
		 width + poly_ovlp_active + poly_via_size)
	cv.dbCreateRect(q, poly)
	metpin = cv.dbCreateRect(q, metal1)
	cv.dbCreatePort(pin, metpin)
	xfudge = (length - numCuts * (cut_width + cut_space)) / 2
	xoffset = active_ovlp_cut + cut_width + poly_to_cut + poly_ovlp_cut + xfudge
	for i in range(numCuts) :
		r = Rect(xoffset,
			 width + poly_ovlp_active + poly_ovlp_cut,
			 xoffset + cut_width,
			 width + poly_ovlp_active + poly_ovlp_cut + cut_width)
		cv.dbCreateRect(r, cont)
		xoffset = xoffset + cut_width + cut_space

	# Create S/D contacts
	cont = tech.getLayerNum("cont", "drawing")
	numCuts = width / (cut_width + cut_space)
	yfudge = (width - numCuts * (cut_width + cut_space)) / 2
	xoffset = active_ovlp_cut
	yoffset = active_ovlp_cut + yfudge
	for i in range(numCuts) :
		cut = Rect(0, 0, cut_width, cut_width)
		cut.offset(xoffset, yoffset)
		cv.dbCreateRect(cut, cont)
		yoffset = yoffset + cut_width + cut_space
	xoffset = xoffset + cut_width + poly_to_cut*2 + length
	yoffset = active_ovlp_cut + yfudge
	for i in range(numCuts) :
		cut = Rect(0, 0, cut_width, cut_width)
		cut.offset(xoffset, yoffset)
		cv.dbCreateRect(cut, cont)
		yoffset = yoffset + cut_width + cut_space
			
	# Create metal
	metal1 = tech.getLayerNum("metal1", "drawing")
	xoffset = active_ovlp_cut - metal_ovlp_cut
	met = Rect(0, 0, cut_width + 2*metal_ovlp_cut, width)
	met.offset(xoffset, 0)
	source = cv.dbCreateRect(met, metal1)
	net = cv.dbCreateNet("MINUS")
	pin = cv.dbCreatePin("MINUS", net, DB_PIN_INOUT)
	cv.dbCreatePort(pin, source)

	xoffset = xoffset + cut_width + poly_to_cut*2 + length
	met.offset(xoffset, 0)
	source = cv.dbCreateRect(met, metal1)
	cv.dbCreatePort(pin, source)
	
	# Now compute c
	area = w * l
	perimeter = 2 * (w + l)
	c = areacap * area + pericap * perimeter

	# Update the master pcell property.
	# NB dbAddProp will replace an existing property of same name.
	cv.dbAddProp("c", c)
	
	# Update the bounding box
	cv.update()
