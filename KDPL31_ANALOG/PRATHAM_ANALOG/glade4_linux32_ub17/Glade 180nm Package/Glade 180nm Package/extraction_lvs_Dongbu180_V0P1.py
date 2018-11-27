# Extraction Deck for Dongbu-Hitek 180nm Process

# Initialise boolean package. 
from ui import *
ui = cvar.uiptr
cv = ui.getEditCellView()
geomBegin(cv)
lib = cv.lib()

print "\n# Loading pcells"
ui.loadPCell(lib.libName(), "NCH_SVT_1P8V_EX")
ui.loadPCell(lib.libName(), "PCH_SVT_1P8V_EX")
ui.loadPCell(lib.libName(), "RES_PP1_EX")
ui.loadPCell(lib.libName(), "RES_NW_EX")
ui.loadPCell(lib.libName(), "NCH_SVT_5P0V_EX")
ui.loadPCell(lib.libName(), "PCH_SVT_5P0V_EX")

# Get raw layers
NWELL     = geomGetShapes("NWELL", "drawing")
PWELL     = geomGetShapes("PWELL", "drawing")
CONT   = geomGetShapes("CONT", "drawing")
V2 = geomGetShapes("V2", "drawing")
V5 = geomGetShapes("V5", "drawing")
V7 = geomGetShapes("V7", "drawing")
ISO_V7 = geomGetShapes("ISO_V7", "drawing")
V12 = geomGetShapes("V12", "drawing")
V20 = geomGetShapes("V20", "drawing")
V30 = geomGetShapes("V30", "drawing")
ISO_V30 = geomGetShapes("ISO_V30", "drawing")
PDT = geomGetShapes("PDT", "drawing")
NDT     = geomGetShapes("NDT", "drawing")
DNW     = geomGetShapes("DNW", "drawing")
SDNW     = geomGetShapes("SDNW", "drawing")
SDPW     = geomGetShapes("SDPW", "drawing")
NIMP     = geomGetShapes("NIMP", "drawing")
PIMP     = geomGetShapes("PIMP", "drawing")
POLY      = geomGetShapes("POLY", "drawing")
DIFF    = geomGetShapes("DIFF", "drawing")
SAB     = geomGetShapes("SAB", "drawing")
MET2    = geomGetShapes("MET2", "drawing")
VIA1     = geomGetShapes("VIA1", "drawing")
MET4    = geomGetShapes("MET4", "drawing")
VIA3     = geomGetShapes("VIA3", "drawing")
MET3    = geomGetShapes("MET3", "drawing")
VIA2    = geomGetShapes("VIA2", "drawing")
NOGRID     = geomGetShapes("NOGRID", "drawing")
MET1    = geomGetShapes("MET1", "drawing")
SRAM      = geomGetShapes("SRAM", "drawing")
MET5    = geomGetShapes("MET5", "drawing")
VIA4    = geomGetShapes("VIA4", "drawing")
MET6    = geomGetShapes("MET6", "drawing")
VIA5    = geomGetShapes("VIA5", "drawing")
TGOX50     = geomGetShapes("TGOX50", "drawing")
ESDMY = geomGetShapes("ESDMY", "drawing")
SAB = geomGetShapes("SAB", "drawing")
POR = geomGetShapes("POR", "drawing")
SEALRING = geomGetShapes("SEALRING", "drawing")
BOND = geomGetShapes("BOND", "drawing")
BLKWELL    = geomGetShapes("BLKWELL", "drawing")
NWRES      = geomGetShapes("NWRES","drawing")
DWELL      = geomGetShapes("DWELL", "drawing")
HRI        = geomGetShapes("HRI", "drawing")

# Form global derived layers


# If there are no poly resistors, don't bother to process them.
if geomNumShapes(SAB) > 0 :
	PRES      = geomAnd(POLY,SAB)
	POLYG     = geomAndNot(POLY, SAB)

else :
	POLYG = POLY
GATE = geomAnd(POLYG, DIFF)
MOSSD = geomAndNot(DIFF, GATE)
NDIFF = geomAndNot(MOSSD,NIMP )
PDIFF = geomAndNot(MOSSD,PIMP )
POLYDIFF = geomAnd(POLY,DIFF )
POLYDIFFNOT50 = geomAndNot(POLYDIFF, TGOX50)
NMOSPOLYGATE = geomAnd(POLYDIFFNOT50,geomAnd(NIMP,geomOr(PWELL,SDPW )))
PMOSPOLYGATE = geomAnd(POLYDIFFNOT50,geomAnd(PIMP,geomOr(NWELL,SDNW )))
NMOSPOLYGATE5V = geomAnd(geomAnd(POLYDIFF,TGOX50),geomAnd(NIMP,geomOr(PWELL,SDPW )))
PMOSPOLYGATE5V = geomAnd(geomAnd(POLYDIFF,TGOX50),geomAnd(PIMP,geomOr(NWELL,SDNW )))
POLYGATE     = geomOr(NMOSPOLYGATE,PMOSPOLYGATE )
FIELD = geomNot(DIFF)
DIFFCONT =  geomAnd(DIFF,CONT)
POLYCONT =  geomAnd(POLY,CONT)
TAPDIFF = geomOr(geomAnd(geomAnd(PIMP,geomOr(PWELL,SDPW)),DIFF),geomAnd(geomAnd(NIMP,geomOr(NWELL,SDNW)),DIFF))
TAPDIFFCONT =  geomAnd(TAPDIFF,CONT)

if geomNumShapes(NWRES) > 0 :
	NWELLRES     = geomAnd(NWELL,NWRES)
	NWELL     = geomAndNot(NWELL, NWRES)
	
else :

	NWELL = NWELL
# gate      = geomAnd(POLYG, DIFF)
# diffsd      = geomAndNot(DIFF, gate)
# ndiff     = geomAnd(diffsd, NIMP)
# pdiff     = geomAnd(diffsd, PIMP)
# ntap      = geomAnd(ndiff, NWELL)
# ptap      = geomAndNot(pdiff, NWELL)


print "# Label nodes"
# This must be done BEFORE geomConnect.
#geomLabel(polyg, "potxt", "drawing")
geomLabel(MET1, "MET1", "text")
geomLabel(MET2, "MET2", "text")
geomLabel(MET3, "MET3", "text")
geomLabel(MET4, "MET4", "text")
geomLabel(MET5, "MET5", "text")
geomLabel(MET6, "MET6", "text")

print "# Form connectivity"
geomConnect( [
              [TAPDIFF, PDIFF, PWELL],
              [TAPDIFF, NDIFF, NWELL],
              [CONT, NDIFF, PDIFF, POLYG, MET1],
              [VIA1, MET1, MET2],
              [VIA2, MET2, MET3],
              [VIA3, MET3, MET4],
              [VIA4, MET4, MET5],
              [VIA5, MET5, MET6],		  
			  ] )

# Save connectivity to extracted view. Saved layers must be
# ones previously connected by geomConnect. Any derived
# layers must be saved to a named layer (e.g. psub below)
print "# Save interconnect"
saveInterconnect([
        [PWELL, "PWELL"],
		[NWELL, "NWELL"],
        [SDNW, "SDNW"],
		[SDPW, "SDPW"],		
		[NIMP, "NIMP"],
		[PIMP, "PIMP"],
		[NDIFF, "DIFF"],
		[PDIFF, "DIFF"],
		[POLYG, "POLY"],
		[TGOX50, "TGOX50"],
		CONT,
		MET1,
		VIA1,
		MET2,
		VIA2,
		MET3,
		VIA3,
		MET4,
		VIA4,
		MET5,
		VIA5,
		MET6])

# Extract MOS devices. Device terminal layers *must* exist in
# the extracted view as a result of saveInterconnect.
# In this case we are using pcell devices which will be
# created according to the recognition region polygon.
print "# Extract MOS devices"
extractMOS("NCH_SVT_1P8V_EX", NMOSPOLYGATE, POLYG, NDIFF, PWELL)
extractMOS("PCH_SVT_1P8V_EX", PMOSPOLYGATE, POLYG, PDIFF, NWELL)
extractMOS("NCH_SVT_5P0V_EX", NMOSPOLYGATE5V, POLYG, NDIFF, PWELL)
extractMOS("NCH_SVT_5P0V_EX", PMOSPOLYGATE5V, POLYG, PDIFF, NWELL)

# Extract resistors. Device terminal layers must exist in
# extracted view as a result of saveInterconnect.
if geomNumShapes(SAB) > 0 :
	print "# Extract poly resistors"
	extractRes("RES_PP1_EX", PRES, POLYG)

if geomNumShapes(NWRES) > 0 :
	print "# Extract nwell resistors"
	extractRes("RES_NW_EX", NWELLRES, NWELL)	
# Exit boolean package, freeing memory
print "# Extraction completed."
geomEnd()

# Open the extracted view
ui.openCellView(lib.libName(), cv.cellName(), "extracted")
