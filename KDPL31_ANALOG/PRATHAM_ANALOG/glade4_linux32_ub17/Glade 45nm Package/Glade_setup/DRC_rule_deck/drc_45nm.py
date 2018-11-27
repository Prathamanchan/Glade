# 0.45nm DRC deck

def printErrors(msg) :
	n = geomGetCount()
	if n > 0 :
		print n, msg

# Initialise DRC package. 
from ui import *



cv = ui().getEditCellView()
geomBegin(cv)

# Get raw layers
nwell     = geomGetShapes("nwell", "drawing")
pwell     = geomGetShapes("pwell", "drawing")
active    = geomGetShapes("active", "drawing")
poly      = geomGetShapes("poly", "drawing")
nimplant  = geomGetShapes("nimplant", "drawing")
pimplant  = geomGetShapes("pimplant", "drawing")
vtg	  = geomGetShapes("vtg","drawing")
vth	  = geomGetShapes("vth","drawing")	
contact   = geomGetShapes("contact", "drawing")
metal1    = geomGetShapes("metal1", "drawing")
via1      = geomGetShapes("via1", "drawing")
metal2    = geomGetShapes("metal2", "drawing")
via2      = geomGetShapes("via2", "drawing")
metal3    = geomGetShapes("metal3", "drawing")
via3      = geomGetShapes("via3", "drawing")
metal4    = geomGetShapes("metal4", "drawing")
via4      = geomGetShapes("via4", "drawing")
metal5    = geomGetShapes("metal5", "drawing")
via5      = geomGetShapes("via5", "drawing")
metal6    = geomGetShapes("metal6", "drawing")
via6      = geomGetShapes("via6", "drawing")
metal7    = geomGetShapes("metal7", "drawing")
via7      = geomGetShapes("via7", "drawing")
metal8    = geomGetShapes("metal8", "drawing")
via8      = geomGetShapes("via8", "drawing")
metal9    = geomGetShapes("metal9", "drawing")
via9      = geomGetShapes("via9", "drawing")
metal10   = geomGetShapes("metal10", "drawing")

# Form derived layers
gate      		= geomAnd(poly, active)
polycon   		= geomAnd(poly, contact)
fieldpoly 		= geomAndNot(poly,gate)
activecon 		= geomAnd(active, contact)
allcon    		= geomOr(polycon, activecon)
badcon    		= geomAndNot(allcon, metal1)
badcon    		= geomAndNot(contact, metal1)
implant   		= geomOr(nimplant, pimplant)
diff      		= geomAndNot(active, gate)
ndiff     		= geomAnd(diff, nimplant)
pdiff     		= geomAnd(diff, pimplant)
well      		= geomOr(nwell,pwell)
ntap      		= geomAnd(ndiff, nwell)
ptap      		= geomAndNot(pdiff, nwell)
vt        		= geomOr(vtg,vth)
active_well 		= geomAndNot(active,well)
impoverlap		= geomAnd(nimplant, pimplant)
welloverlap		= geomAnd(nwell, pwell)
contactenc1 		= geomOr(active,poly)
contactenc 		= geomAnd(contactenc1,metal1)
contact_enclosure	= geomAndNot(contact,contactenc)
metal1_badvia1		= geomAndNot(via1,metal1)
metal2_badvia1	 	= geomAndNot(via1,metal2)
metal2_badvia2		= geomAndNot(via2,metal2)
metal3_badvia2		= geomAndNot(via2,metal3)
metal3_badvia3		= geomAndNot(via3,metal3)
metal4_badvia3		= geomAndNot(via3,metal4)
metal4_badvia4		= geomAndNot(via4,metal4)
metal5_badvia4		= geomAndNot(via4,metal5)
metal5_badvia5		= geomAndNot(via5,metal5)
metal6_badvia5		= geomAndNot(via5,metal6)
metal6_badvia6		= geomAndNot(via6,metal6)
metal7_badvia6		= geomAndNot(via6,metal7)
metal7_badvia7		= geomAndNot(via7,metal7)
metal8_badvia7		= geomAndNot(via7,metal8)
metal8_badvia8		= geomAndNot(via8,metal8)
metal9_badvia8		= geomAndNot(via8,metal9)
metal9_badvia9		= geomAndNot(via9,metal9)
metal10_badvia9		= geomAndNot(via9,metal10)
active_con		= geomCoincident(active,contact)
poly_con		= geomCoincident (poly,contact)
act_poly		= geomCoincident (active,poly)
metal4_via3		= geomCoincident(metal4,via3)
metal4_via4		= geomCoincident(metal4,via4)
metal5_via4		= geomCoincident(metal5,via4)
metal5_via5		= geomCoincident(metal5,via5)
metal6_via5		= geomCoincident(metal6,via5)
metal6_via6		= geomCoincident(metal6,via6)
metal7_via6		= geomCoincident(metal7,via6)
metal7_via7		= geomCoincident(metal7,via7)
metal8_via7		= geomCoincident(metal8,via7)
metal8_via8		= geomCoincident(metal8,via8)
metal9_via8		= geomCoincident(metal9,via8)
metal9_via9		= geomCoincident(metal9,via9)
metal10_via9		= geomCoincident(metal10,via9)
active_135_shrink	= geomSize(active,-0.067)
active_135_grow		= geomSize (active_135_shrink,0.067)
active_135		= geomAnd(active,active_135_grow)
active_lt135		= geomAndNot(active_135,active)
cont_135                = geomAnd (contact, active_135)
active_135_shrink_5nm	= geomSize(active_135,-0.005)
active_shrink_con_layer = geomAndNot(cont_135,active_135_shrink_5nm)


#from connectivity

geomConnect( [
              [ntap, ndiff, nwell],
 	      [ptap, pdiff, pwell],
              [contact, ndiff, pdiff, poly, metal1],
              [via1, metal1, metal2],
              [via2, metal2, metal3],
	      [via3, metal3, metal4],
              [via4, metal4, metal5],
              [via5, metal5, metal6],
	      [via6, metal6, metal7],
              [via7, metal7, metal8],
              [via8, metal8, metal9],
	      [via9, metal9, metal10],

	     ] )







print "Check well"
saveDerived(welloverlap,"WELL.1: nwell & pwell must not overlap")
geomSpace(well,0.225,0,"WELL.2: Min spacing of nwell/pwell must be 0.225um")
geomWidth(well, 0.2, "WELL.4: Minimum width of nwell/pwell must be 0.2um ")


print "Check poly"
geomWidth(poly, 0.05,"POLY.1: Minimum width of poly must be 0.05um")
geomSpace(gate, 0.14,0,"POLY.2: Min spacing of gate poly must be 0.14um")
saveDerived(act_poly,"POLY.3A: Keep Min overhang of poly past active")
geomExtension(poly, active, 0.05,"POLY.3B: Min extension of poly past active must be 0.05um")
geomExtension(active, gate, 0.07,"POLY.4: Min  active enclosure of gate must be 0.07um")
geomSpace(poly, active, 0.03,0,"POLY.5: Min spacing of poly active must be 0.03um")
geomSpace(fieldpoly, 0.075,0,"POLY.6: Min spacing of fieldpoly must be 0.075um")

print "Check active"
geomWidth(active, 0.09,"ACTIVE.1: Minimum width of active must be 0.09um")
geomSpace(active, 0.08,0,"ACTIVE.2: Minimum spacing of active areas must be 0.08um")
geomEnclose(well, active, 0.055, "ACTIVE.3: Minimum well enclosure of active must be 0.055um")
saveDerived(active_well,"ACTIVE.4: Active must be inside well")

print "Check implant"
geomEnclose(implant,gate,0.07,"IMPLANT.1: Minimum spacing of implant to gate must be 0.07um")
geomSpace(implant,contact,0.025,0,"IMPLANT.2: Minimum spacing of implant to contact must be 0.025um")
geomSpace(implant,0.045,0,"IMPLANT.3:Minimum spacing of implant must be 0.045um")
geomWidth(implant, 0.045,"IMPLANT.4: Minimum spacing of implant must be 0.045um")
saveDerived(impoverlap,"IMPLANT.6: nimplant & pimplant must not overlap")

print "Check contact"
geomWidth(contact, 0.07,"CONTACT.1: Minimum width of contact must be 0.07um")
geomSpace(contact, 0.075,0,"CONTACT.2:  Minimum spacing of contact must be 0.075um")
saveDerived(contact_enclosure, "CONTACT.3: Contact must be inside metal1 and active or poly")
saveDerived(active_con,"CONTACT.4A:keep min enclosure of active to contact")
saveDerived(active_shrink_con_layer,"CONTACT.4B keep an enclosure of 0.005um exact of active to contact for active width>0.135um when two opposite sides are 0.035um")
geomEnclose(active_lt135,contact,0.005,"CONTACT.4C: Minimum active enclosure of contact must be 0.005um on all sides for active width<0.135um")
geomEnclose(active_135_shrink_5nm,cont_135,0.030,"CONTACT.4D: Minimum active enclosure of contact must be 0.035um on two opposite sides")
saveDerived(poly_con,"CONTACT.5A:keep min enclosure & extension of poly to contact")
geomEnclose(poly, contact, 0.005,"CONTACT.5B: Minimum poly enclosure of contact must be 0.005um")
geomSpace(poly, contact, 0.035,0,"CONTACT.6: Minimum spacing of contact to poly must be 0.035um")


print "Check metal1"
geomWidth(metal1, 0.07,"Metal1.1: Minimum width of metal1 must be 0.07um")
geomSpace(metal1,0.07,0,"Metal1.2:Minimum spacing of metal1 must be 0.07um")
geomExtension(metal1, contact, 0.035,"Metal1.3: Minimum metal1 extension of contact must be 0.035um")
geomExtension(metal1, via1, 0.035,"Metal1.4: Minimum metal1 extension of via1 must be 0.035um")

print "Check via1"
geomWidth(via1, 0.07,"VIA1.1: Minimum width of via1 must be 0.07um")
geomSpace(via1, 0.075,0,"VIA1.2: Minimum spacing of via1 must be 0.075um")
saveDerived(metal1_badvia1,"VIA1.3: Via1 must be inside metal1")
saveDerived(metal2_badvia1,"VIA1.4: Via1 must be inside metal2")

print "Check metal2"
geomWidth(metal2, 0.07,"Metal2.1: Minimum width of metal2 must be 0.07um")
geomSpace(metal2,0.07,0,"Metal2.2: Minimum spacing of metal2 must be 0.07um")
geomExtension(metal2, via1, 0.035,"Metal2.3: Minimum metal2 extension of via1 must be 0.035um")
geomExtension(metal2, via2, 0.035,"Metal2.4: Minimum metal2 extension of via4 must be 0.035um")

print "Check via2"
geomWidth(via2, 0.07,"VIA2.1: Minimum width of via2 must be 0.07um")
geomSpace(via2, 0.085,0,"VIA2.2: Minimum spacing of via2 must be 0.085um")
saveDerived(metal2_badvia2,"VIA2.3: Via2 must be inside metal2")
saveDerived(metal3_badvia2,"VIA2.4: Via2 must be inside metal3")


print "Check metal3"
geomWidth(metal3, 0.07,"Metal3.1: Minimum width of metal3 must be 0.07um")
geomSpace(metal3,0.07,0,"Metal3.2: Minimum spacing of metal3  must be 0.07um")
geomExtension(metal3, via2, 0.035,"Metal3.3: Minimum metal3 extension of via2 must be 0.035um")
geomExtension(metal3, via3, 0.035,"Metal3.4: Minimum metal3 extension of via3 must be 0.035um")

print "Check via3"
geomWidth(via3, 0.07,"VIA3.1: Minimum width of via3 must be 0.07um")
geomSpace(via3, 0.085,0,"VIA3.2: Minimum spacing of via2 must be 0.085um")
saveDerived(metal3_badvia3,"VIA3.3: Via3  must be inside metal3")
saveDerived(metal4_badvia3,"VIA3.4A: Via3  must be inside metal4")
saveDerived(metal4_via3,"Via3.4B:keep min enclosure of metal4 to via3")


print "Check metal4"
geomWidth(metal4, 0.14,"Metal4.1: Minimum width of metal4 must be 0.14um")
geomSpace(metal4,0.14,0,"Metal4.2: Minimum spacing of metal4 must be 0.14um")
geomEnclose(metal4, via3, 0.003,"Metal4.3: Minimum enclosure of metal4 around via3 must be 0.0025um")

print "Check via4"
geomWidth(via4, 0.14,"VIA4.1: Minimum width of via4  must be 0.14um")
geomSpace(via4, 0.16,0,"VIA4.2: Minimum spacing of via4 must be 0.16um")
saveDerived(metal4_badvia4,"VIA4.3A: Via4  must be inside metal4")
saveDerived(metal4_via4,"Via4.3B:keep min enclosure & extension of metal4 to via4")
saveDerived(metal5_badvia4,"VIA4.4A: Via4  must be inside metal5")
saveDerived(metal5_via4,"Via4.4B:keep min enclosure of metal5 to via4")


print "Check metal5"
geomWidth(metal5, 0.14,"Metal5.1: Minimum width of metal5 must be 0.14um")
geomSpace(metal5,0.14,0,"Metal5.2: Minimum spacing of metal5 must be 0.14um")
geomEnclose(metal5, via4, 0.003,"Metal5.3: Minimum enclosure of metal5 around via4 must be 0.0025um")

print "Check via5"
geomWidth(via5, 0.14,"VIA5.1: Minimum width of via5 must be 0.14um")
geomSpace(via5, 0.16,0,"VIA5.2: Minimum spacing of via5 must be 0.16um")
saveDerived(metal5_badvia5,"VIA5.3A: Via5  must be inside metal5")
saveDerived(metal5_via5,"Via5.3B:keep min enclosure of metal5 to via5")
saveDerived(metal6_badvia5,"VIA5.4A: Via5  must be inside metal6")
saveDerived(metal6_via5,"Via5.4B:keep min enclosure of metal6 to via5")

print "Check metal6"
geomWidth(metal6, 0.14,"Metal6.1: Minimum width of metal6 must be 0.14um")
geomSpace(metal6,0.14,0,"Metal6.2: Minimum spacing of metal6 must be 0.14um")
geomEnclose(metal6, via5, 0.003,"Metal6.3: Minimum enclosure of metal6 around via5 must be 0.0025um")

print "Check via6"
geomWidth(via6, 0.14,"VIA6.1: Minimum width of via6  must be 0.14um")
geomSpace(via6, 0.16,0,"VIA6.2: Minimum spacing of via6  must be 0.16um")
saveDerived(metal6_badvia6,"VIA6.3A: Via6  must be inside metal6")
saveDerived(metal6_via6,"Via6.3B:keep min enclosure & extension of metal6 to via6")
saveDerived(metal7_badvia6,"VIA6.4A: Via6  must be inside metal7")
saveDerived(metal7_via6,"Via6.4B:keep min enclosure of metal7 to via6")

print "Check metal7"
geomWidth(metal7, 0.4,"Metal7.1: Minimum width of metal7 must be 0.4um")
geomSpace(metal7,0.4,0,"Metal7.2: Minimum spacing of metal7 must be 0.4um")
geomEnclose(metal7, via6, 0.003,"Metal7.3: Minimum enclosure of metal7 around via6 must be 0.0025um")

print "Check via7"
geomWidth(via7, 0.4,"VIA7.1: Minimum width of via7 must be 0.4um")
geomSpace(via7, 0.44,0,"VIA7.2: Minimum spacing of via5 must be 0.44um")
saveDerived(metal7_badvia7,"VIA7.3A: Via7 must be inside metal7")
saveDerived(metal7_via7,"Via7.3B:keep min enclosure of metal7 to via7")
saveDerived(metal8_badvia7,"VIA7.4A: Via7 must be inside metal8")
saveDerived(metal8_via7,"Via7.4B:keep min enclosure of metal8 to via7")

print "Check metal8"
geomWidth(metal8, 0.4,"Metal8.1: Minimum width of metal8 must be 0.4um")
geomSpace(metal8,0.4,0,"Metal8.2: Minimum spacing of metal8 must be 0.4um")
geomEnclose(metal8, via7, 0.003,"Metal8.3: Minimum enclosure of metal8 around via7 must be 0.0025um")

print "Check via8"
geomWidth(via8, 0.4,"VIA8.1: Minimum width of via8  must be 0.4um")
geomSpace(via8, 0.44,0,"VIA8.2: Minimum spacing of via8  must be 0.44um")
saveDerived(metal8_badvia8,"VIA8.3A: Via8  must be inside metal8")
saveDerived(metal8_via8,"Via8.3B:keep min enclosure of metal8 to via8")
saveDerived(metal9_badvia8,"VIA8.4A: Via8  must be inside metal9")
saveDerived(metal9_via8,"Via8.4B:keep min enclosure of metal9 to via8")

print "Check metal9"
geomWidth(metal9, 0.8,"Metal9.1: Minimum width of metal9 must be 0.8um")
geomSpace(metal9,0.8,0,"Metal9.2: Minimum spacing of metal9 must be 0.88um")
geomEnclose(metal9, via8, 0.003,"Metal9.3: Minimum enclosure of metal9 around via8 must be 0.0025um")


print "Check via9"
geomWidth(via9, 0.8,"VIA9.1: Minimum width of via9 must be 0.8um")
geomSpace(via9, 0.88,0,"VIA9.2: Minimum spacing of via9 must be 0.88um")
saveDerived(metal9_badvia9,"VIA9.3A: Via9 must be inside metal9")
saveDerived(metal9_via9,"Via9.3B:keep min enclosure of metal9 to via9")
saveDerived(metal10_badvia9,"VIA9.4A: Via9 must be inside metal10")
saveDerived(metal10_via9,"Via9.4B:keep min enclosure of metal10 to via9")

print "Check metal10"
geomWidth(metal10, 0.8,"Metal10.1: Minimum width of metal10 must be 0.8um")
geomSpace(metal10,0.8,0,"Metal10.2: Minimum spacing of metal10 must be 0.88um")
geomEnclose(metal10, via9,0.003,"Metal10.3: Minimum enclosure of metal10 around via9 must be 0.0025um")








#print "check griderrors"

#Offgrid checks have been commented as we are not sure about grid value mentioned in calibreDRC.rul

geomOffGrid(active,0.001,0.001,"GRID.1:activemustbeona 1nm grid")
geomOffGrid(implant,0.001,0.001,"GRID.2:implantmustbeona 1nm grid")
geomOffGrid(well,0.001,0.001,"GRID.3:wellmustbeona 1nm grid")
geomOffGrid(contact,0.001,0.001,"GRID.4:contactmustbeona 1nm grid")
geomOffGrid(poly,0.001,0.001,"GRID.5:polymustbeona 1nm grid")
geomOffGrid(metal1,0.001,0.001,"GRID.6:metal1mustbeona 1nm grid")
geomOffGrid(via1,0.001,0.001,"GRID.7:via1mustbeona 1nm grid")
geomOffGrid(metal2,0.001,0.001,"GRID.8:metal2mustbeona 1nm grid")
geomOffGrid(via2,0.001,0.001,"GRID.9:via2mustbeona 1nm grid")
geomOffGrid(metal3,0.001,0.001,"GRID.10:metal3mustbeona 1nm grid")
geomOffGrid(via3,0.001,0.001,"GRID.11:via3mustbeona 1nm grid")
geomOffGrid(metal4,0.001,0.001,"GRID.12:metal4mustbeona 1nm grid")
geomOffGrid(via4,0.001,0.001,"GRID.13:via4mustbeona 1nm grid")
geomOffGrid(metal5,0.001,0.001,"GRID.14:metal5mustbeona 1nm grid")
geomOffGrid(via5,0.001,0.001,"GRID.15:via5mustbeona 1nm grid")
geomOffGrid(metal6,0.001,0.001,"GRID.16:metal6mustbeona 1nm grid")
geomOffGrid(via6,0.001,0.001,"GRID.17:via6mustbeona 1nm grid")
geomOffGrid(metal7,0.001,0.001,"GRID.18:metal7mustbeona 1nm grid")
geomOffGrid(via7,0.001,0.001,"GRID.19:via7mustbeona 1nm grid")
geomOffGrid(metal8,0.001,0.001,"GRID.20:metal8mustbeona 1nm grid")
geomOffGrid(via8,0.001,0.001,"GRID.21:via8mustbeona 1nm grid")
geomOffGrid(metal9,0.001,0.001,"GRID.22:metal9mustbeona 1nm grid")
geomOffGrid(via9,0.001,0.001,"GRID.23:via9mustbeona 1nm grid")
geomOffGrid(metal10,0.001,0.001,"GRID.24:metal10mustbeona 1nm grid")
geomOffGrid(vtg,0.001,0.001,"GRID.25:vtgmustbeona 1nm grid")
geomOffGrid(vth,0.001,0.001,"GRID.26:vthmustbeona 1nm grid")

# Exit DRC package, freeing memory

geomEnd()
ui().winFit()

