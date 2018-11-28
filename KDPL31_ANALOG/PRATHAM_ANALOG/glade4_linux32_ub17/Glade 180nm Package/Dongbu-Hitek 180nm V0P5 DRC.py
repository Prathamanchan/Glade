# Dongbu 180nm DRC deck
#
# Coded by:
# Abhishek K
# Bidhan C Roy 
# Ramdas Khaladkar
# Keerthan

def printErrors(msg) :
	n = geomGetCount()
	if n > 0 :
		print n, msg

# Initialise DRC package. 
from ui import *
cv = ui().getEditCellView()
geomBegin(cv)

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
NDIFF = geomAnd(DIFF,NIMP )
PDIFF = geomAnd(DIFF,PIMP )
POLYDIFF    =geomAnd(POLY,DIFF )
NMOSPOLYGATE = geomAnd(POLYDIFF,geomAnd(NIMP,geomOr(PWELL,SDPW )))
PMOSPOLYGATE = geomAnd(POLYDIFF,geomAnd(PIMP,geomOr(NWELL,SDNW )))
POLYGATE     = geomOr(NMOSPOLYGATE,PMOSPOLYGATE )
FIELD = geomNot(DIFF)
DIFFCONT =  geomAnd(DIFF,CONT)
POLYCONT =  geomAnd(POLY,CONT)
TAPDIFF = geomOr(geomAnd(geomAnd(NIMP,geomOr(PWELL,SDPW)),DIFF),geomAnd(geomAnd(PIMP,geomOr(NWELL,SDNW)),DIFF))
TAPDIFFCONT =  geomAnd(TAPDIFF,CONT)
DIFFMET_OR_POLYMET = geomOr(geomAnd(DIFF,MET1),geomAnd(POLY,MET1))

# diff derived layer
DIFF_IMP                         = geomInside(geomOr(PIMP,NIMP),DIFF)
NDIFF_IMP                        = geomAnd(NIMP,DIFF)
NDIFF_IMP_V2                     = geomAnd(NDIFF_IMP,V2)
NDIFF_IMP_V5                     = geomAnd(NDIFF_IMP,V5)
NDIFF_IMP_V7                     = geomAnd(NDIFF_IMP,V7)
NDIFF_IMP_ISO_V7                 = geomAnd(NDIFF_IMP,ISO_V7)
NDIFF_IMP_V12                    = geomAnd(NDIFF_IMP,V12)
NDIFF_IMP_V20                    = geomAnd(NDIFF_IMP,V20)
NDIFF_IMP_V30                    = geomAnd(NDIFF_IMP,V30)
NDIFF_IMP_ISO_V30                = geomAnd(NDIFF_IMP,ISO_V30)
NDIFF_IMP_V2_V5_V7_ISO_V7        = geomOr(geomOr(geomOr(NDIFF_IMP_V2,NDIFF_IMP_V5),NDIFF_IMP_V7),NDIFF_IMP_ISO_V7)
NDIFF_IMP_V20_V30_ISO_V30_NO     = geomAndNot(NDIFF_IMP,geomOr(NDIFF_IMP_V2_V5_V7_ISO_V7,NDIFF_IMP_V12))
PDIFF_IMP                        = geomAnd(PIMP,DIFF)
PDIFF_IMP_V2                     = geomAnd(PDIFF_IMP,V2)
PDIFF_IMP_V5                     = geomAnd(PDIFF_IMP,V5)
PDIFF_IMP_V7                     = geomAnd(PDIFF_IMP,V7)
PDIFF_IMP_ISO_V7                 = geomAnd(PDIFF_IMP,ISO_V7)
PDIFF_IMP_V12                    = geomAnd(PDIFF_IMP,V12)
PDIFF_IMP_V20                    = geomAnd(PDIFF_IMP,V20)
PDIFF_IMP_V30                    = geomAnd(PDIFF_IMP,V30)
PDIFF_IMP_ISO_V30                = geomAnd(PDIFF_IMP,ISO_V30)
PDIFF_IMP_V2_V5_V7               = geomOr(geomOr(PDIFF_IMP_V2,PDIFF_IMP_V5),PDIFF_IMP_V7)
PDIFF_IMP_V20_V30_ISO_V30_NO     = geomAndNot(PDIFF_IMP,geomOr(PDIFF_IMP_V2_V5_V7,PDIFF_IMP_V12))
DIFF_INSIDE_IMP_V2               = geomInside(geomOr(PIMP,NIMP),geomAnd(V2,DIFF))
DIFF_INSIDE_IMP_V5               = geomInside(geomOr(PIMP,NIMP),geomAnd(V5,DIFF))
DIFF_INSIDE_IMP_V2_TOUCH_POLY    = geomOverlapping(POLY,DIFF_INSIDE_IMP_V2)
DIFF_INSIDE_IMP_V5_TOUCH_POLY    = geomOverlapping(POLY,DIFF_INSIDE_IMP_V5)
DIFF_INSIDE_IMP                  = geomAndNot(geomInside(geomOr(PIMP,NIMP),DIFF),geomOr(DIFF_INSIDE_IMP_V2,DIFF_INSIDE_IMP_V5))
DIFF_INSIDE_IMP_TOUCH_POLY       = geomOverlapping(POLY,DIFF_INSIDE_IMP)
DIFF_OUTSIDE_TGOX50              = geomAndNot(DIFF_IMP,geomAnd(DIFF_IMP,TGOX50))
DIFF_INSIDE_TGOX50               = geomInside(TGOX50,DIFF_IMP)
NDIFF_OUTSIDE_SRAM_PW            = geomAndNot(NDIFF_IMP,geomAnd(NDIFF_IMP,geomOr(SRAM,PWELL)))
POLYGATE_NIMP                    = geomAnd(geomAnd(DIFF,POLY),NIMP)
POLYGATE_PIMP                    = geomAnd(geomAnd(DIFF,POLY),PIMP)
PDIFF_BUTT_NDIFF                 = geomButting(NDIFF_IMP,PDIFF_IMP) 
NDIFF_BUTT_PDIFF                 = geomButting(PDIFF_IMP,NDIFF_IMP) 
POLYGATE                         = geomAnd(geomAnd(DIFF,POLY),geomOr(NIMP,PIMP))
NW_PW_SDNW_SDPW_NDT_PDT_DWELL    = geomOr(geomOr(geomOr(geomOr(geomOr(geomOr(NWELL,PWELL),SDNW),SDPW),NDT),PDT),DWELL) 
DIFF_SHRINK_60                   = geomSize(DIFF,-60)

#SDNW derived layers
SDNW_V2        =  geomAnd(V2,SDNW)
SDNW_V5        =  geomAnd(V5,SDNW)
SDNW_V7        =  geomAnd(V7,SDNW)
SDNW_ISO_V7    =  geomAnd(ISO_V7,SDNW)
SDNW_V20       =  geomAnd(V20,SDNW)
SDNW_V12       =  geomAnd(V12,SDNW)
SDNW_V30       =  geomAnd(V30,SDNW)
SDNW_ISO_V30   =  geomAnd(ISO_V30,SDNW)

# TGOX50 derived layers
POLYGATE_1P8V = geomAnd(POLYGATE,V2 )
POLYGATE_5P0V = geomAnd(POLYGATE,V5 )

# PIMP derived layers
PW_SDPW= geomOr(PWELL ,SDPW )
NDIFF_IN_PW_SDPW = geomInside(PW_SDPW,NDIFF )
NDIFF_OUT_PW_SDPW = geomOutside(PW_SDPW,NDIFF)
BUTTED_DIFF_PIMP = geomButting(NIMP,PIMP )
NW_SDNW= geomOr(NWELL ,SDNW )
PDIFF_IN_NW_SDNW = geomInside(NW_SDNW,PDIFF )
PDIFF_IN_PW_SDPW = geomInside(PW_SDPW,PDIFF )
NDIFF_IN_NW_SDNW = geomInside(NW_SDNW,NDIFF )

#PWELL Derived Layers
PWELL_diff_pot = geomInside(geomHoles(geomOr(NWELL,SDNW)),geomInside(DNW,PWELL))
Vl2 = geomOr(geomOr(V12,V20),geomOr(V30,ISO_V30))

#SDPW Derived Layers
SDPW_diff_pot = geomInside(geomHoles(geomOr(NWELL,SDNW)),geomInside(DNW,SDPW))
Vl1 = geomOr(geomOr(geomOr(V2,V5),geomOr(V7,V12)),geomOr(V20,V30))
Vl3 = geomOr(geomOr(Vl1,ISO_V7),ISO_V30)

#CONTACT Derived layers
CONT_p14=geomSize(CONT,0.14)
CONT_m11=geomSize(CONT_p14,-.25)		#This will remove all single contacts
CONT_m36=geomSize(CONT_p14,-.5)			#This will remove all 2X2 contacts
CONT_m61=geomSize(CONT_p14,-.75)		#This will remove all 3X3 contacts

#BLKWELL Derived layers
BLKWELL_IN_PWELL    = geomAnd(BLKWELL,PWELL)
BLKWELL_IN_SDPW     = geomAnd(BLKWELL,SDPW)

#from connectivity
geomConnect([
            [CONT, NWELL, V2],
            [CONT, NWELL, V5],
            [CONT, NWELL, V7],
            [CONT, NWELL, ISO_V7],
            [CONT, NWELL, V12],
            [CONT, NWELL, V20],
            [CONT, NWELL, V30],
            [CONT, NWELL, ISO_V30],
            [CONT, NDT, V2],
            [CONT, NDT, V5],
            [CONT, DNW, V2],
            [CONT, DNW, V5],
            [CONT, SDNW, V2],
            [CONT, SDNW, V5],
            [geomAnd(PWELL_diff_pot,V2),PWELL_diff_pot,V2],
 	    [geomAnd(PWELL_diff_pot,V5),PWELL_diff_pot,V5],
	    [geomAnd(PWELL_diff_pot,V7),PWELL_diff_pot,V7],
	    [geomAnd(PWELL_diff_pot,V12),PWELL_diff_pot,V12],
 	    [geomAnd(PWELL_diff_pot,V20),PWELL_diff_pot,V20],
	    [geomAnd(PWELL_diff_pot,V30),PWELL_diff_pot,V30],
	    [geomAnd(SDPW_diff_pot,V2),SDPW_diff_pot,V2],
 	    [geomAnd(SDPW_diff_pot,V5),SDPW_diff_pot,V5],
	    [geomAnd(SDPW_diff_pot,V7),SDPW_diff_pot,V7],
	    [geomAnd(SDPW_diff_pot,V12),SDPW_diff_pot,V12],
 	    [geomAnd(SDPW_diff_pot,V20),SDPW_diff_pot,V20],
	    [geomAnd(SDPW_diff_pot,V30),SDPW_diff_pot,V30],
            [geomAnd(SDNW,V2), SDNW, V2],
            [geomAnd(SDNW,V5), SDNW, V5],
            [geomAnd(SDNW,V7), SDNW, V7],
            [geomAnd(SDNW,ISO_V7), SDNW, ISO_V7],
            [geomAnd(SDNW,V12), SDNW, V12],
            [geomAnd(SDNW,V20), SDNW, V20],
            [geomAnd(SDNW,V30), SDNW, V30],
            [geomAnd(SDNW,ISO_V30), SDNW, ISO_V30],
            [geomAnd(POLYGATE,V2 ), POLYGATE,V2 ],
            [geomAnd(POLYGATE,V5 ), POLYGATE,V5 ],
            [geomAnd(V2,SDNW),V2,SDNW], 
            [geomAnd(V5,SDNW),V5,SDNW],
            [geomAnd(V7,SDNW),V7,SDNW], 
            [geomAnd(V12,SDNW),V12,SDNW],
            [geomAnd(ISO_V7,SDNW),ISO_V7,SDNW],
            [geomAnd(V20,SDNW),V20,SDNW], 
            [geomAnd(V30,SDNW),V30,SDNW],
            [geomAnd(ISO_V30,SDNW),ISO_V30,SDNW],
            [CONT, SDNW, V20]    	     
     ] )

#DRC Checks

#NWELL DRC Checks
print "Checking NWELL"
geomWidth(NWELL, 0.86, "2w2a:NW width > 0.86")
geomSpace(NWELL, 1.4, diffnet, "2s2a:NWELL to NWELL of DIFFerent net should be >1.4")
geomSpace(geomOutside(V12,NWELL),geomOr( geomOverlapping(V12,NWELL), geomTouching(V12,NWELL)), 2.4, 0, "2s2b:V12NWELL to V2,V5,V7 NWELL of DIFFerent net should be >2.4")
geomSpace(geomOutside(V20,NWELL),geomOr( geomOverlapping(V20,NWELL), geomTouching(V20,NWELL)), 3.4, 0, "2s2c:V20NWELL to V2,V5,V7,ISO_V7,V12 NWELL of DIFFerent net should be >3.4")
geomSpace(geomOutside(geomOr(V30,ISO_V30),NWELL),geomOr( geomOverlapping(geomOr(V30,ISO_V30),NWELL), geomTouching(geomOr(V30,ISO_V30),NWELL)), 4.4, 0, "2s2d:Distance from V30 and isoV30 NWELL to V2,V5,V7,,ISO_V7,V12,V20 NWELL of DIFFerent net should be >4.4")
geomSpace(NWELL, 0.6, samenet, "2s2e:Distance between two NWELL on samenet should be >0.6 ")
saveDerived(geomOr(geomOverlapping(PDT, NWELL), geomCoincident(PDT, NWELL)),"2Ra: PDT and NWELL should not overlap and coincident")
geomOffGrid(NWELL, 0.005, 0.005, "2Ga:NWELL must be on a 5nm grid")

#PWELL DRC Checks
print "Check PWELL"
geomWidth(PWELL,0.86,"1W1a: min. width of a PW is 0.86um")
geomSpace(PWELL_diff_pot,1.4,diffnet,"1S1a: min. space between two PW Different node (V2, V5, V7, No voltage tag) is 1.40um")
geomSpace(geomOr(geomOverlapping(V12,PWELL_diff_pot),geomTouching(V12,PWELL_diff_pot)),geomOutside(V12,PWELL_diff_pot),2.4,0,"PWELL 1S1b: min. space between two PW Different node (V12) is 2.40um")
geomSpace(geomOr(geomOverlapping(V20,PWELL_diff_pot),geomTouching(V20,PWELL_diff_pot)),geomOutside(V20,PWELL_diff_pot),3.4,0,"PWELL 1S1c: min. space between two PW Different node (V20) is 3.40um")
geomSpace(geomOr(geomOverlapping(V30,PWELL_diff_pot),geomTouching(V30,PWELL_diff_pot)),geomOutside(V30,PWELL_diff_pot),4.4,0,"PWELL 1S1d: min. space between two PW Different node (V30) is 4.40um")
geomSpace(PWELL_diff_pot,0.6,samenet,"1S1e: min. space between two PW Same node is 0.6")
geomSpace(geomOutside(geomOr(geomOr(V12,V20),geomOr(V30,ISO_V30)),PWELL_diff_pot),NWELL,0,0,"PWELL NWELL 1S2a: min. space NW to PW In V2, V5, V7, ISO_V7, including no voltage tag is 0um")
geomSpace(geomOr(geomOverlapping(V12,PWELL_diff_pot),geomTouching(V12,PWELL_diff_pot)),NWELL,0.5,0,"PWELL NWELL 1S2b: min. space NW to PW In V12 is 0.5um")
geomSpace(geomOr(geomOverlapping(V20,PWELL_diff_pot),geomTouching(V20,PWELL_diff_pot)),NWELL,1,0,"PWELL NWELL 1S2c: min. space NW to PW In V20 is 1um")
geomSpace(geomOr(geomOverlapping(V30,PWELL_diff_pot),geomTouching(V30,PWELL_diff_pot)),geomOr(geomHoles(NWELL),NWELL),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(V30,PWELL_diff_pot),geomTouching(V30,PWELL_diff_pot)),geomNoHoles(NWELL),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(V30,PWELL_diff_pot),geomTouching(V30,PWELL_diff_pot)),geomAndNot(NWELL,ISO_V30),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,PWELL_diff_pot),geomTouching(ISO_V30,PWELL_diff_pot)),geomOr(geomHoles(NWELL),NWELL),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In ISO_V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,PWELL_diff_pot),geomTouching(ISO_V30,PWELL_diff_pot)),geomNoHoles(NWELL),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In ISO_V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,PWELL_diff_pot),geomTouching(ISO_V30,PWELL_diff_pot)),geomAndNot(NWELL,ISO_V30),1.5,0,"PWELL NWELL 1S2d: min. space NW to PW In ISO_V30 is 1.5um")
saveDerived(geomAnd(NWELL,PWELL),"PWELL NWELL 1Rb: PW and NW must not be overlapped or coincident.") 
saveDerived(geomCoincident(NWELL,geomOr(geomOverlapping(Vl2,PWELL),geomTouching(Vl2,PWELL))),"PWELL NWELL 1Rb: PW and NW must not be overlapped or coincident.") 
saveDerived(geomOr(geomOverlapping(PDT,PWELL),geomTouching(PDT,PWELL)),"PWELL PDT 1Rc: PW and PDT must not be overlapped or coincident.") 
geomOffGrid(geomOutside(NOGRID,PWELL),0.005,0.005,"1Ga: Drawn PW must conform to a 0.005um on-grid rule")
	
#DNW DRC Checks
print "Check DNW"
geomWidth(DNW,3.00,"22W22a:Minimum width of DNW must be 3.00um") 
geomSpace(DNW,5.00,0,"22S22a:Minimum space between two DNW must be 5.00um ")
geomExtension(NWELL,geomAndNot(DNW,geomAnd(DNW,ESDMY)),1.50,"22X2a:Minimum Extension of NWELL beyond DNW must be 1.50um ") 
geomOverlap(NWELL,geomAndNot(DNW,geomAnd(DNW,ESDMY)),2.00,"22O2a:Minimum Overlap of NWELL beyond DNW must be 2.00um ")
geomSpace(NWELL,DNW,3.5,0,"22S2a:Minimum Space between NWELL to DNW is 3.50")
saveDerived(geomAndNot(DNW,geomInside(geomOr(NWELL,SDNW),DNW)),"22Ra: All DNW must be Inside NWELL or SDNW")
geomOffGrid(geomAndNot(DNW,geomAnd(DNW,NOGRID)),0.005,0.005,"Minimum Grid value is 5nm") 

#SDNW DRC Checks
print "SD-NWELL"
geomWidth(SDNW, 0.86, "SD-NWELL.24W24a: Minimum width of SDNW(SD-NWELL) must be 0.86um ")
geomSpace(SDNW ,1.4,diffnet,"SD-NWELL.24S24a: Min spacing of SDNW to diff nets must be 1.4um")
geomSpace(geomOr(geomOverlapping(V12,SDNW),geomTouching(V12,SDNW)),geomOutside(V12,SDNW) ,2.4,0,"SD-NWELL.24S24b: Min spacing of SDNW to diff nets must be 2.4um")
geomSpace(geomOr(geomOverlapping(V20,SDNW),geomTouching(V20,SDNW)),geomOutside(V20,SDNW),3.4,0,"SD-NWELL.24S24c: Min spacing of SDNW to diff nets must be 3.4um")
geomSpace(geomOr(geomOverlapping(V30,SDNW),geomTouching(V30,SDNW)),geomOutside(V30,SDNW) ,4.4,0,"SD-NWELL.24S24d: Min spacing of SDNW to diff nets must be 4.4um")
geomSpace(geomOr(geomOverlapping(ISO_V30 ,SDNW),geomTouching(ISO_V30 ,SDNW)),geomOutside(ISO_V30,SDNW),4.4,0,"SD-NWELL.24S24d: Min spacing of SDNW to diff nets must be 4.4um")
geomSpace(geomOr(geomOverlapping(SDNW ,SDNW),geomTouching(SDNW ,SDNW)),SDNW,4.4,0,"SD-NWELL.24S24d: Min spacing of SDNW to diff nets must be 4.4um")
geomSpace(SDNW ,0.6,samenet,"SD-NWELL.24S24e: Min spacing of SDNW to same nets must be 0.6um")
saveDerived(geomOr(geomOverlapping(SDNW,PWELL),geomCoincident(SDNW,PWELL)),"SD-NWELL.24Ra: SDNW and PWELL(PW) must not be overlapped or coincident")
saveDerived(geomOr(geomOverlapping(SDNW,PDT),geomCoincident(SDNW,PDT)),"SD-NWELL.24Rb: SDNW and PDT must not be overlapped or coincident")
geomOffGrid(geomOutside(NOGRID,SDNW),0.005,0.005,"24Ga:SDNW must be on a 5nm grid")
geomSpace(SDNW_V2,NWELL,1.40,0,"24S2a:Minimum Space between SDNW(V2) to NWELL is 1.40um")
geomSpace(SDNW_V5,NWELL,1.40,0,"24S2a:Minimum Space between SDNW(V5) to NWELL is 1.40um")
geomSpace(SDNW_V7,NWELL,1.40,0,"24S2a:Minimum Space between SDNW(V7) to NWELL is 1.40um")
geomSpace(SDNW_ISO_V7,NWELL,1.40,0,"24S2a:Minimum Space between SDNW(ISO_V7) to NWELL is 1.40um")
geomSpace(SDNW_V12,NWELL,2.40,0,"24S2b:Minimum Space between SDNW(V12) to NWELL is 1.40um")
geomSpace(SDNW_V20,NWELL,3.40,0,"24S2c:Minimum Space between SDNW(V20) to NWELL is 1.40um")
geomSpace(SDNW_V30,NWELL,4.40,0,"24S2d:Minimum Space between SDNW(V30) to NWELL is 1.40um")
geomSpace(SDNW_ISO_V30,NWELL,4.40,0,"24S2d:Minimum Space between SDNW(ISO_V30) to NWELL is 1.40um")
geomSpace(SDNW,NWELL,2.90,samenet,"24S2e:Minimum Space between SDNW to NWELL is 2.90um")
saveDerived(geomAnd(SDNW_V2,PWELL),"24S1a:SDNW(V2) and PWELL should not overlap")
saveDerived(geomAnd(SDNW_V5,PWELL),"24S1a:SDNW(V5) and PWELL should not overlap")
saveDerived(geomAnd(SDNW_V7,PWELL),"24S1a:SDNW(V7) and PWELL should not overlap")
saveDerived(geomAnd(SDNW_ISO_V7,PWELL),"24S1a:SDNW(ISO_V7) and PWELL should not overlap")
geomSpace(SDNW_V12,PWELL,0.50,0,"24S1b:Minimum Space between SDNW(V12) to PWELL is 0.50um")
geomSpace(SDNW_V20,PWELL,1.00,0,"24S1c:Minimum Space between SDNW(V20) to PWELL is 1.00um")
geomSpace(SDNW_V30,PWELL,1.50,0,"24S1d:Minimum Space between SDNW(V30) to PWELL is 1.50um")
geomSpace(SDNW_ISO_V30,geomAndNot(PWELL,geomAnd(PWELL,ISO_V30)),1.50,0,"24S1d:Minimum Space between SDNW(ISO_V30) to PWELL is 1.50um")

#SDPWELL DRC Checks
print "Check SDPWELL"
geomWidth(SDPW,0.86,"23W23a: min. width of a SDPW is 0.86um")
geomSpace(SDPW_diff_pot,1.4,diffnet,"23S23a: min. space between two SDPW Different node (V2, V5, V7) is 1.40um")
geomSpace(geomOr(geomOverlapping(V12,SDPW_diff_pot),geomTouching(V12,SDPW_diff_pot)),geomOutside(V12,SDPW_diff_pot),2.4,0,"SDPW 23S23b: min. space between two SDPW Different node (V12) is 2.40um")
geomSpace(geomOr(geomOverlapping(V20,SDPW_diff_pot),geomTouching(V20,SDPW_diff_pot)),geomOutside(V20,SDPW_diff_pot),3.4,0,"SDPW 23S23c: min. space between two SDPW Different node (V20) is 3.40um")
geomSpace(geomOr(geomOverlapping(V30,SDPW_diff_pot),geomTouching(V30,SDPW_diff_pot)),geomOutside(V30,SDPW_diff_pot),4.4,0,"SDPW 23S23d: min. space between two SDPW Different node (V30) is 4.40um")
geomSpace(geomOr(geomOverlapping(Vl1,SDPW_diff_pot),geomTouching(Vl1,SDPW_diff_pot)),geomOutside(Vl1,SDPW_diff_pot),4.4,0,"SDPW 23S23d: min. space between two SDPW Different node (No voltage tag) is 4.40um")
geomSpace(SDPW_diff_pot,0.6,samenet,"23S23e: min. space between two SDPW Same node is 0.6")
geomSpace(geomOutside(geomOr(geomOr(V12,V20),geomOr(V30,ISO_V30)),SDPW_diff_pot),NWELL,0,0,"SDPW NWELL 23S2a: min. space NW to PW In V2, V5, V7, ISO_V7, is 0um")
geomSpace(geomOr(geomOverlapping(V12,SDPW_diff_pot),geomTouching(V12,SDPW_diff_pot)),NWELL,0.5,0,"SDPW NWELL 23S2b: min. space NW to SDPW In V12 is 0.5um")
geomSpace(geomOr(geomOverlapping(V20,SDPW_diff_pot),geomTouching(V20,SDPW_diff_pot)),NWELL,1,0,"SDPW NWELL 23S2c: min. space NW to SDPW In V20 is 1um")
geomSpace(geomOr(geomOverlapping(V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomOr(geomHoles(NWELL),NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomNoHoles(NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomAndNot(NWELL,ISO_V30),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomOr(geomHoles(NWELL),NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In ISO_V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomNoHoles(NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In ISO_V30 is 1.5um")
geomSpace(geomOr(geomOverlapping(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY)),geomTouching(ISO_V30,geomAndNot(SDPW_diff_pot,ESDMY))),geomAndNot(NWELL,ISO_V30),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In ISO_V30 is 1.5um")
geomSpace(geomOutside(Vl3, geomAndNot(SDPW_diff_pot,ESDMY)),geomOr(geomHoles(NWELL),NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In No voltage tag is 1.5um")
geomSpace(geomOutside(Vl3, geomAndNot(SDPW_diff_pot,ESDMY)),geomNoHoles(NWELL),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In No voltage tag is 1.5um")
geomSpace(geomOutside(Vl3, geomAndNot(SDPW_diff_pot,ESDMY)),geomAndNot(NWELL,ISO_V30),1.5,0,"SDPW NWELL 23S2d: min. space NW to SDPW In No voltage tag is 1.5um")
geomSpace(geomOr(geomOverlapping(V2,SDPW_diff_pot),geomTouching(V2,SDPW_diff_pot)),geomOutside(V2,PWELL_diff_pot),1.4,0,"SDPW PWELL 23S1a: min. space of SDPW to PW Different node (V2, V5, V7) is 1.40um")
geomSpace(geomOr(geomOverlapping(V5,SDPW_diff_pot),geomTouching(V5,SDPW_diff_pot)),geomOutside(V5,PWELL_diff_pot),1.4,0,"SDPW PWELL 23S1a: min. space of SDPW to PW Different node (V2, V5, V7) is 1.40um")
geomSpace(geomOr(geomOverlapping(V7,SDPW_diff_pot),geomTouching(V7,SDPW_diff_pot)),geomOutside(V7,PWELL_diff_pot),1.4,0,"SDPW PWELL 23S1a: min. space of SDPW to PW Different node (V2, V5, V7) is 1.40um")
geomSpace(geomOr(geomOverlapping(V12,SDPW_diff_pot),geomTouching(V12,SDPW_diff_pot)),geomOutside(V12,PWELL_diff_pot),2.4,0,"SDPW PWELL 23S1b: min. space of SDPW to PW Different node (V12) is 2.40um")
geomSpace(geomOr(geomOverlapping(V12,PWELL_diff_pot),geomTouching(V12,PWELL_diff_pot)),geomOutside(V12,SDPW_diff_pot),2.4,0,"SDPW PWELL 23S1b: min. space of SDPW to PW Different node (V12) is 2.40um")
geomSpace(geomOr(geomOverlapping(V20,SDPW_diff_pot),geomTouching(V20,SDPW_diff_pot)),geomOutside(V20,PWELL_diff_pot),3.4,0,"SDPW PWELL 23S1c: min. space of SDPW to PW Different node (V20) is 3.40um")
geomSpace(geomOr(geomOverlapping(V20,PWELL_diff_pot),geomTouching(V20,PWELL_diff_pot)),geomOutside(V20,SDPW_diff_pot),3.4,0,"SDPW PWELL 23S1c: min. space of SDPW to PW Different node (V20) is 3.40um")
geomSpace(geomOr(geomOverlapping(V30,SDPW_diff_pot),geomTouching(V30,SDPW_diff_pot)),geomOutside(V30,PWELL_diff_pot),4.4,0,"SDPW PWELL 23S1d: min. space of SDPW to PW Different node (V30) is 4.40um")
geomSpace(geomOr(geomOverlapping(V30,PWELL_diff_pot),geomTouching(V30,PWELL_diff_pot)),geomOutside(V30,SDPW_diff_pot),4.4,0,"SDPW PWELL 23S1d: min. space of SDPW to PW Different node (V30) is 4.40um")
geomSpace(geomOr(geomOverlapping(Vl3,PWELL_diff_pot),geomTouching(Vl3,PWELL_diff_pot)),geomOutside(Vl3,SDPW_diff_pot),2.9,0,"SDPW PWELL 23S1e: min. space of SDPW to PW Different node (No voltage tag) is 2.9um")
geomSpace(geomOr(geomOverlapping(Vl3,SDPW_diff_pot),geomTouching(Vl3,SDPW_diff_pot)),geomOutside(Vl3,PWELL_diff_pot),2.9,0,"SDPW PWELL 23S1e: min. space of SDPW to PW Different node (No voltage tag) is 2.9um")
geomSpace(SDPW,SDNW,0,0,"SDPW SDNW 23S24a: min. space of SDPW to SDNW is 0.0um")
saveDerived(geomAnd(SDPW,SDNW),"SDPW SDNW 23Rb: SDPW and SDNW must not be overlapped or coincident.") 
saveDerived(geomAnd(SDPW,NWELL),"SDPW NWELL 23Rc: SDPW and NW must not be overlapped or coincident.") 
saveDerived(geomCoincident(NWELL,geomOr(geomOverlapping(Vl2,SDPW),geomTouching(Vl2,SDPW))),"SDPW NWELL 23Rc: SDPW and NW must not be overlapped or coincident.") 
saveDerived(geomOr(geomOverlapping(PDT,SDPW),geomTouching(PDT,SDPW)),"SDPW PDT 23Rd: SDPW and PDT must not be overlapped or coincident.") 
geomOffGrid(geomOutside(NOGRID,SDPW),0.005,0.005,"23Ga: Drawn SDPW must conform to a 0.005um on-grid rule")

#NDT DRC Checks
print "Checking NDT"
geomWidth(NDT, 0.8, "100W100a:NDT width > 0.86")
geomSpace(NDT, 6, diffnet, "100S100a:Distance between NDT to NDT of DIFFerent net should be >6.0")
geomSpace(NDT, 0.8, samenet, "100S100b:Distance between NDT to NDT of same net should be >0.8")
geomSpace(NDT, NWELL, 4.4, diffnet, "100S2a:Distance between NDT to NWELL of DIFFerent net should be >4.4")
geomSpace(NDT, PWELL, 2.0, 0,"100S1a:Distance between NDT to PWELL should be >2.0")
geomSpace(NDT, DNW, 5.9, diffnet, "100S22a:Distance between NDT to DNW of DIFFerent net should be >5.9")
geomSpace(NDT, SDNW, 4.4, diffnet, "100S24a:Distance between NDT to SDNW of DIFFerent net should be >4.4")
geomSpace(NDT, SDPW, 2, 0, "100S23a:Distance between NDT to SDPW should be >4.4")
saveDerived(geomOr(geomOverlapping(NDT, PWELL), geomCoincident(NDT, PWELL)),"100Rb: NDT and PWELL should not overlap and coincident")
saveDerived(geomOr(geomOverlapping(NDT, SDPW), geomCoincident(NDT, SDPW)),"100Rc: NDT and SDPW should not overlap and coincident")
saveDerived(geomOr(geomOverlapping(NDT, PDT), geomCoincident(NDT, PDT)),"100Rd: NDT and PDT should not overlap and coincident")
geomOffGrid(NDT, 0.005, 0.005, "100Ga:NDT must be on a 5nm grid")

#DIFF DRC Checks
print "Checking Diffusion Rules"
geomWidth(DIFF_INSIDE_IMP_V2_TOUCH_POLY,0.22,"3W3a:Min width of a DIFF for 1.8V CMOS is 0.22um") 
geomWidth(DIFF_INSIDE_IMP_V5_TOUCH_POLY,0.22,"3W3b:Min width of a DIFF for 5V CMOS is 0.22um")
geomWidth(DIFF_INSIDE_IMP_TOUCH_POLY,0.42,"3W3:Min width of a DIFF for CMOS is 0.42um")
geomWidth(geomAndNot(DIFF_INSIDE_IMP,geomAnd(DIFF_INSIDE_IMP,SRAM)),0.22,"3W3c:Min width of a DIFF for interconnect is 0.22um")
geomSpace(geomAndNot(DIFF_OUTSIDE_TGOX50,geomAnd(DIFF_OUTSIDE_TGOX50,SRAM)),0.28,0,"3S3a:Min Space between two DIFF is 0.28um")
geomSpace(DIFF_INSIDE_TGOX50,0.42,0,"3S3b:Min Space between two DIFF inside TGOX50 is 0.42um ")
geomEnclose(NWELL,geomAnd(NWELL,NDIFF_IMP),0.12,"3E2a:Min Enclosure of NDIFF by NWELL must be 0.12um")
saveDerived(geomCoincident(NWELL,NDIFF_IMP),"3E2a:NDIFF should not coincide with NWELL")
geomEnclose(PWELL,geomAnd(PWELL,PDIFF_IMP),0.12,"3E1a:Min Enclosure of PDIFF by PWELL must be 0.12um")
saveDerived(geomCoincident(PWELL,PDIFF_IMP),"3E1a:PWELL and PDIFF should not coincide")
geomEnclose(SDNW,geomAnd(SDNW,NDIFF_IMP_V2_V5_V7_ISO_V7),0.12,"3E24a:Min Enclosure of NDIFF(V2,V5,V7,ISO_V7) by SDNW must be 0.12um")
saveDerived(geomCoincident(SDNW,NDIFF_IMP_V2_V5_V7_ISO_V7),"3E24a:SDNW and NDIFF should not coincide")
geomEnclose(SDNW,geomAnd(SDNW,NDIFF_IMP_V12),0.5,"3E24b:Min Enclosure of NDIFF(V12) by SDNW must be 0.5um")
saveDerived(geomCoincident(SDNW,NDIFF_IMP_V12),"3E24b:SDNW and NDIFF should not coincide")
geomEnclose(SDNW,geomAnd(SDNW,NDIFF_IMP_V20_V30_ISO_V30_NO),1,"3E24c:Min Enclosure of NDIFF(V20,V30,ISO_V30,No_Volt_Tag) by SDNW must be 1um")
saveDerived(geomCoincident(SDNW,NDIFF_IMP_V20_V30_ISO_V30_NO),"3E24c:SDNW and NDIFF(V20,V30,ISO_V30,No Volt Tag) should not coincide")
geomEnclose(SDPW,geomAnd(SDPW,PDIFF_IMP_V2_V5_V7) ,0.12,"3E23a:Min Enclosure of PDIFF(V2,V5,V7) by SDNW must be 0.12um")
geomEnclose(SDPW,geomAnd(SDPW,PDIFF_IMP_V12),0.5,"3E23b:Min Enclosure of PDIFF(V12) by SDNW must be 0.5um")
geomEnclose(SDPW,geomAnd(PDIFF_IMP_V20_V30_ISO_V30_NO,SDPW),1,"3E23c:Min Enclosure of PDIFF(V20,V30,No_Volt_Tag) by SDNW must be 1um") 
saveDerived(geomCoincident(SDPW,PDIFF_IMP_V2_V5_V7),"3E23a:SDPW and PDIFF should not coincide")
saveDerived(geomCoincident(SDPW,PDIFF_IMP_V12),"3E23a:SDPW and PDIFF should not coincide")
saveDerived(geomCoincident(SDPW,PDIFF_IMP_V20_V30_ISO_V30_NO),"3E23a:SDPW and PDIFF should not coincide") 
geomSpace(NDIFF_OUTSIDE_SRAM_PW,NWELL,0.43,0,"3S2a:Min Space between NDIFF and NWELL Outside SRAM and PWELL is 0.43um ") 
geomSpace(geomAnd(NDIFF_IMP,SDPW),NWELL,0.70,0,"3S2d:Min Space between NDIFF in SDNW and NWELL is 0.70um ")
geomEnclose(NWELL,geomAnd(NWELL,geomAndNot(PDIFF_IMP,geomAnd(PDIFF_IMP,SRAM))),0.43,"3E2c:Min Enclosure of PDIFF outside the SRAM by NWELL must be 0.43um")
saveDerived(geomCoincident(NWELL,geomAndNot(PDIFF_IMP,geomAnd(PDIFF_IMP,SRAM))),"3E2c:NWELL and PDIFF should not coincide") 
saveDerived(geomAndNot(geomOverlapping(NWELL,geomAndNot(PDIFF_IMP,geomAnd(PDIFF_IMP,SRAM))),NWELL),"3E2c:NWELL and PDIFF should not Overlap")
geomEnclose(PWELL,geomAndNot(NDIFF_IMP,geomAnd(NDIFF_IMP,SRAM)),0.43,"3E1e:Min Enclosure of NDIFF outside the SRAM by PWELL must be 0.43um")
saveDerived(geomCoincident(PWELL,geomAndNot(NDIFF_IMP,geomAnd(NDIFF_IMP,SRAM))),"3E1e:PWELL and NDIFF should not coincide")
saveDerived(geomAndNot(geomOverlapping(PWELL,geomAndNot(NDIFF_IMP,geomAnd(NDIFF_IMP,SRAM))),PWELL),"3E1e:PWELL and NDIFF should not Overlap")
geomEnclose(SDNW,geomAnd(SDNW,PDIFF_IMP),0.70,"3E24l:Min Enclosure of PDIFF by SDNW must be 0.70um")
saveDerived(geomCoincident(SDNW,PDIFF_IMP),"3E24l:SDNW and PDIFF should not coincide")
saveDerived(geomAndNot(geomOverlapping(SDNW,PDIFF_IMP),SDNW),"13E24l:SDNW and PDIFF should not Overlap")
geomEnclose(SDPW,geomAnd(SDPW,NDIFF_IMP),0.70,"3E23i:Min Enclosure of NDIFF by SDPW must be 0.70um")
saveDerived(geomCoincident(SDPW,NDIFF_IMP),"3E23i:SDPW and NDIFF should not coincide")
saveDerived(geomAndNot(geomOverlapping(SDPW,NDIFF_IMP),SDPW),"3E23i:SDPW and NDIFF should not Overlap")
geomSpace(geomAnd(NDIFF_IMP,SDPW),SDNW,0.7,0,"3S24a:Min Space between NDIFF in SDPW and SDNW is 0.70um ")
geomSpace(geomAnd(NDIFF_IMP,PWELL),SDNW,0.43,0,"3S24b:Min Space between NDIFF in PWELL and SDNW is 0.43um ")
geomSpace(geomAndNot(geomAnd(PDIFF_IMP,NWELL),geomAnd(geomAnd(PDIFF_IMP,NWELL),SRAM)),PWELL,0.43,0,"3S1a:Min Space between PDIFF in NWELL and PWELL is 0.43um ")
geomSpace(geomAnd(PDIFF_IMP,SDNW),PWELL,0.70,0,"3S1c:Min Space between PDIFF in SDNW and PWELL is 0.70um ")
geomSpace(geomAnd(PDIFF_IMP,SDNW),SDPW,0.70,0,"3S23a:Min Space between PDIFF in SDNW and SDPW is 0.70um ")
geomSpace(geomAnd(PDIFF_IMP,NWELL),SDPW,0.43,0,"3S23b:Min Space between PDIFF in NWELL and SDPW is 0.43um ")
geomSpace(PDIFF_BUTT_NDIFF,POLYGATE_NIMP,0.32,0,"3S3d:Min Space between POLYGATE in NIMP to butted PDIFF is 0.32um ")
geomSpace(NDIFF_BUTT_PDIFF,POLYGATE_PIMP,0.32,0,"3S3d:Min Space between POLYGATE in PIMP to butted NDIFF is 0.32um ")
geomWidth(PDIFF_BUTT_NDIFF,0.42,"3W3d:Min width of a Butted PDIFF is 0.42um")
geomWidth(NDIFF_BUTT_PDIFF,0.42,"3W3d:Min width of a Butted NDIFF is 0.42um")
geomArea(geomAndNot(DIFF,geomOverlapping(POLY,DIFF)),0.2025,999999,"Minimum Area of DIFF is 0.2025") 
saveDerived(geomAnd(PDIFF_IMP,NDIFF_IMP),"3Ra:PDIFF and NDIFF should not Overlap ")
saveDerived(geomSize(DIFF_SHRINK_60,60),"3Rb:DIFF Width should be less than 120um")
geomSpace(POLYGATE,geomAnd(SDPW,PWELL),0.50,0,"3Rc:Min Space between POLYGATE to common area of SDPW and PWELL is 0.50um")
saveDerived(geomAnd(POLYGATE,geomAnd(SDPW,PWELL)),"3Rc:POPLYGATE and common area between SDPW and PWELL shold not overlap")
saveDerived(geomButting(POLYGATE,geomAnd(SDPW,PWELL)),"3Rc:POPLYGATE and common area between SDPW and PWELL shold not Coincide")
geomSpace(POLYGATE,geomAnd(SDNW,NWELL),0.50,0,"3Rd:Min Space between POLYGATE to common area of SDNW and NWELL is 0.50um")
saveDerived(geomAnd(POLYGATE,geomAnd(SDNW,NWELL)),"3Rd:POPLYGATE and common area between SDNW and NWELL shold not overlap")
saveDerived(geomButting(POLYGATE,geomAnd(SDNW,NWELL)),"3Rd:POPLYGATE and common area between SDNW and NWELL shold not Coincide")
saveDerived(geomAndNot(DIFF,geomAnd(DIFF,NW_PW_SDNW_SDPW_NDT_PDT_DWELL)),"3Re:All DIFF should be inside NWELL or PWELL or SDNW or SDPW or PDT or NDT or DWELL")
saveDerived(geomAndNot(DIFF,geomAnd(DIFF,geomOr(NIMP,PIMP))),"3Rf:All DIFF should be inside NIMP or PIMP")
geomOffGrid(geomAndNot(DIFF,geomAnd(DIFF,NOGRID)),0.005,0.05,"Minimum Grid value is 5nm") 
#saveDerived(geomSize(DIFF,-1.0),"3W3e: max. width of DIFF is 2.0um.")

# Thick Gate Oxide (TGOX50)
print "TGOX50"
geomWidth(TGOX50, 0.45, "111W111a : Minimum width of TGOX50 must be 0.45um ")
geomSpace(TGOX50,0.45,0,"111S111a : Min spacing of TGOX50 to TGOX50 nets must be 0.45um")
geomEnclose(TGOX50,DIFF,0.32,"111E3a : Minimum Encloser of TGOX50 to DIFF must be 0.32um")
geomSpace(DIFF,TGOX50,0.32,0,"111S3a : Min spacing of DIFF to TGOX50 nets must be 0.32um")
geomSpace(POLYGATE_1P8V,TGOX50,0.40,0,"111S3b : Min spacing of POLYGATE_1P8V to TGOX50 nets must be 0.40um")
geomEnclose(TGOX50,POLYGATE_5P0V,0.40,"111E3b : Min Encloser of POLYGATE_5P0V to TGOX50 nets must be 0.40um")
geomOffGrid(geomOutside(NOGRID,TGOX50),0.005,0.005,"111Ga :TGOX50 must be on a 5nm grid")

#POLY DRC Checks
print "Check POLY"
geomWidth(geomOutside(SRAM,geomAnd(POLY,FIELD)),0.18,"POLY 6W6a: min. width of a POLY Interconnect is 0.18um")
geomWidth(geomOr(geomOverlapping(V2,POLYDIFF),geomTouching(V2,POLYDIFF)),0.18,"POLY 6W6b 6W6e: min. width of a POLY in 1.8V NMOS gate length and 1.8V PMOS gate length is 0.18um")
geomWidth(geomInside(TGOX50,geomOr(geomOverlapping(V5,POLYDIFF),geomTouching(V5,POLYDIFF))),0.5,"POLY 6W6d 6W6g: min. width of a POLY in 5.0V NMOS gate length and 5.0V PMOS gate length is 0.5um")
saveDerived(geomOverlapping(geomSpace(POLYDIFF,0.375,0,""),CONT),"6S6a: min. space between two POLY on DIFF with contacts in the spacing is 0.375um")
geomSpace(POLYDIFF,0.25,0,"POLYDIFF 6S6b: min. space between two POLY on DIFF without contacts in the spacing is 0.25um")
geomSpace(geomOutside(SRAM,geomAnd(POLY,FIELD)),0.25,0,"POLY 6S6c: min. space between two POLY on field oxide area is 0.25um")
geomSpace(geomOutside(SRAM,geomAnd(POLY,FIELD)),DIFF,0.1,0,"POLY 6S3a: min. space between DIFF and POLY on field oxide is 0.1um")
geomExtension(DIFF,geomOutside(SRAM,POLY),0.32,"6X3a: min. extension from DIFF to related POLY is 0.32um") 
geomExtension(geomOutside(SRAM,POLY),DIFF,0.22,"6X3b: min. extension of a POLY beyond DIFF into field oxide (ENDCAP) is 0.22um")
geomOffGrid(geomOutside(NOGRID,POLY),0.005,0.005,"6Ga: Drawn POLY must conform to a 0.005um on-grid rule")

#NIMP DRC Checks
print "Checking NIMP"
geomWidth(NIMP, 0.44, "8W8a :NIMP width > 0.44")
geomSpace(NIMP, 0.44, 0, "8S8a :Space between NIMP to NIMP should be >.44 or both should be merged together")
geomSpace(geomInside(geomOr(SDNW,NWELL),NIMP), geomInside(geomOr(SDNW,NWELL),PDIFF), 0.26, 0, "8S3a:Space between NIMPlant to PDIFF(inside SDNW or NWELL) should be >= 0.26")
geomSpace(NIMP, geomOutside(geomOr(SDNW,NWELL),PDIFF), 0.10, 0, "8S3b:Space between NIMPlant to PDIFF(outside SDNW or NWELL) should be >= 0.10")
geomSpace(POLYGATE, geomButting(geomAnd(PIMP, DIFF), NIMP), 0.32, 0, "8S6a:Space between butted DIFFusion and NIMPlant to pch_POLYGATE should be >= 0.32")
geomSpace(geomButting(geomAnd(NIMP, DIFF), PIMP), POLYGATE, 0.32, 0, "8S6b:Space between butted DIFFusion and PIMPlant to nch_POLYGATE should be >= 0.32")
geomWidth(geomAnd(NIMP, NDIFF), 0.23, "8O3a:min. overlap from NIMP edge to NDIFF > 0.23")
geomEnclose(NIMP, geomAnd(NDIFF,geomOr(PWELL, SDPW)), 0.18, "8E3a: min. enclosure of NDIFF (in PW or SDPW) by NIMP >= 0.18")
geomEnclose(NIMP, geomAnd(NDIFF,geomOr(NWELL, SDNW)), 0.02, "8E3b: min. enclosure of NDIFF (in NW or SDNW) by NIMP should be >= 0.02")
saveDerived(geomAnd(geomInside(geomOr(SDPW,PWELL),PDIFF), geomInside(geomOr(SDPW,PWELL),NDIFF)), "8S3c:min. space between NDIFF and butted PDIFF(inside PW or SDPW) >= 0")
saveDerived(geomAnd(geomInside(geomOr(SDNW,NWELL),NDIFF), geomInside(geomOr(SDNW,NWELL),PDIFF)), "8E3c:min. enclosure of the edge of a butted NDIFF/PDIFF by NIMP >= 0")
geomExtension(NIMP, POLY, 0.18,"8X6a: min. extension of NIMP beyond a POLY as a resistor >= 0.18")
geomArea(NIMP, 0.3844, 9e99, "8A8a: min. area of NIMP (um2) >= 0.3844 ")
saveDerived(geomOverlapping(NIMP, PIMP),"8Ra: NIMP overlapped with PIMP is not allowed")
geomOffGrid(NIMP, 0.005, 0.005, "8Ga:NIMP must be on a 5nm grid")

# P+ S/D Implant (PIMP)
print "Checking PIMP"
geomWidth(PIMP, 0.44, "7W7a  : Minimum width of PIMP must be 0.44um ")
geomSpace(PIMP,0.44,0,"7S7a : If Min spacing of PIMP to PIMP nets is 0.44um then merge the PIMP")
geomSpace(PIMP,NDIFF_IN_PW_SDPW,0.26,0,"7S3a : Min spacing of PIMP to NDIFF_IN_PW_SDPW nets must be 0.26um")
geomSpace(PIMP,NDIFF_OUT_PW_SDPW,0.10,0,"7S3b : Min spacing of PIMP to NDIFF_OUT_PW_SDPW nets must be 0.10um")
geomSpace(geomButting(NIMP,PIMP ),NMOSPOLYGATE,0.32,0,"7S6a : Min spacing of BUTTED_DIFF_PIMP to NMOSPOLYGATE nets must be 0.32um")
geomSpace(geomButting(PIMP,NIMP ),PMOSPOLYGATE,0.32,0,"7S6b : Min spacing of BUTTED_DIFF_PIMP to PMOSPOLYGATE nets must be 0.32um")
geomWidth(geomAnd(PIMP,PDIFF ), 0.23, "7O3a  :min. overlap from a PIMP edge to an PDIFF must be 0.23um")
geomEnclose(PIMP,PDIFF_IN_NW_SDNW,0.18,"7E3a: Min Encloser of PDIFF_IN_NW_SDNW to PIMP nets must be 0.18um")
geomEnclose(PIMP,PDIFF_IN_PW_SDPW,0.02,"7E3b: Min Encloser of PDIFF_IN_PW_SDPW to PIMP nets must be 0.02um")
geomSpace(PDIFF,geomInside(NW_SDNW,geomButting(NDIFF,PIMP )),0,0,"7S3c : Min spacing of BUTTED_NDIFF_PDIFF to PIMP nets must be 0um")
geomSpace(geomButting(NDIFF,PDIFF ),PIMP,0,0,"7E3c : Min spacing of BUTTED_NDIFF_PDIFF to PIMP nets must be 0um")
geomExtension(PIMP, POLY, 0.18,"7X6a: min. extension of PIMP beyond a POLY as a resistor must be 0.18um")
geomArea(PIMP,0.3844,99999,"7A7a:min. area of PIMP must be 0.3844 um2 ")
saveDerived(geomOverlapping(PIMP,NIMP), "7Ra:PIMP overlapped with NIMP is not allowed")
geomOffGrid(geomOutside(NOGRID,PIMP),0.005,0.005,"7Ga  :PIMP must be on a 5nm grid")

#HRI DRC Checks
print "Checking  High Resistor Implant "
geomWidth(HRI,0.44,"90W90a:Min width of a HRI is 0.44um and Please Merge if Width is less than 0.44um")
geomWidth(geomInside(HRI,POLY),0.42,"90W90b:Min width of a POLY in HRI is 0.42um")
geomEnclose(HRI,geomAnd(HRI,POLY),0.26,"90E6a:Min Enclosure of POLY by HRI must be 0.26um")
saveDerived(geomCoincident(HRI,POLY),"90E6a:POLY should not coincide with HRI")
saveDerived(geomAndNot(geomOverlapping(HRI,POLY),HRI),"90E6a:POLY should not Overlap with HRI")
geomSpace(HRI,0.44,0,"90S90a:Min Space between HRI is 0.44um ")
geomSpace(HRI,DIFF,0.50,0,"90S3a :Min Space between DIFF and HRI is 0.50um ") 
geomSpace(HRI,NIMP,0.50,0,"90S8a :Min Space between NIMP and HRI is 0.50um ") 
geomSpace(HRI,PIMP,0.50,0,"90S7a :Min Space between PIMP and HRI is 0.50um ") 
geomSpace(HRI,POLY,2.00,0,"90S6a :Min Space between POLY and HRI is 2.00um ") 
geomArea(HRI,0.3844,999999,"90A90a:Minimum Area of DIFF is 0.3844 um^2") 
saveDerived(geomAnd(geomAnd(HRI,NIMP),DIFF),"90Ra :Overlap of a NIMP and a HRI on a DIFF region is not allowed")
saveDerived(geomAnd(geomAnd(HRI,NIMP),geomInside(HRI,POLY)),"90Rb :Overlap of a NIMP and a HRI on the same POLY is not allowed")
geomOffGrid(geomAndNot(HRI,geomAnd(HRI,NOGRID)),0.005,0.05,"Minimum Grid value is 5nm") 

#SAB DRC Checks
print "Checking Salicide Block"
geomWidth(SAB, 0.43, "47W47a  :SAB width > 0.43")
geomSpace(SAB, 0.43, 0, "47S47a :Space between SAB to SAB should be >= 0.43 ")
geomSpace(SAB, DIFF, 0.22, 0, "47S3a  :Space between SAB to DIFF should be >= 0.22 ")
geomExtension(SAB, DIFF, 0.22,"47X3a: min. extension of SAB beyond a DIFFusion >= 0.22")
geomSpace(SAB, geomOr(POLY,geomAnd(POLY,DIFF)), 0.45, 0, "47S6a  :Space between SAB to POLY should be >= 0.45 ")
geomExtension(SAB, POLY, 0.22,"47X6a: min. extension of SAB beyond a field POLY >= 0.22")
geomSpace(SAB, CONT, 0.22, 0, "47S9a  :Spacing between SAB to CONT should be >= 0.22 ")
geomExtension(DIFF, SAB, 0.22,"47X6a: min. extension of DIFFusion beyond SAB >= 0.22")
geomWidth(geomAnd(SAB,geomAvoiding(POLY,DIFF)), 0.42, "47W47b  :POLY width > 0.42")
#geomWidth(geomAnd(SAB,POLY), 0.42, "47W47b  :POLY width > 0.42")
geomArea(SAB, 2, 9e99, "47A47a: min. area of SAB (um2) >= 2 ")
geomOffGrid(SAB, 0.005, 0.005, "47Ga:SAB must be on a 5nm grid")

#CONTACT DRC Checks
print "Check CONTACT"
geomWidth(CONT,0.22,"9W9a: min. & max. size of CONT is 0.22um.")
saveDerived(geomSize(CONT,-0.11),"CONT 9W9a: min. & max. size of CONT is 0.22um.")
geomSpace(CONT,0.25,0,"CONT 9S9a: min. space between two CONT is 0.25um.")
geomWidth(CONT_m11,.5,"CONT 9S9b: min. space between two CONT in a contact array with both row and column numbers equal to or larger than 4. is 0.28um")
geomWidth(CONT_m36,.5,"CONT 9S9b: min. space between two CONT in a contact array with both row and column numbers equal to or larger than 4. is 0.28um")
geomWidth(CONT_m61,.5,"CONT 9S9b: min. space between two CONT in a contact array with both row and column numbers equal to or larger than 4. is 0.28um")
geomWidth(CONT_p14,.5,"CONT 9S9b: min. space between two CONT in a contact array with both row and column numbers equal to or larger than 4. is 0.28um")
geomSpace(geomInside(DIFF,CONT),POLYGATE,0.16,0,"CONT 9S6a: min. space between CONT on DIFF and POLYGATE is 0.16um.")
geomSpace(geomInside(POLY,CONT),DIFF,0.2,0,"CONT 9S3a: min. space between CONT on POLY and DIFF is 0.2um.")
geomEnclose(geomAndNot(DIFF,TAPDIFF),geomOutside(SRAM,DIFFCONT),0.1,"CONT 9E3a: min. enclosure of DIFFCONT by DIFF is 0.1um") 
geomEnclose(POLY,geomOutside(SRAM,POLYCONT),0.1,"CONT 9E6a: min. enclosure of POLYCONT by POLY is 0.1um") 
geomEnclose(TAPDIFF,TAPDIFFCONT,0.1,"CONT 9E3b: min. enclosure of TAPDIFFCONT by TAPDIFF is 0.1um") 
geomSpace(CONT,TAPDIFF,0.1,0,"9S3b: min. space between CONT and TAPDIFF is 0.1um.")
saveDerived(geomAnd(CONT,POLYGATE),"CONT 9Ra: CONT on POLYGATE is forbidden")
saveDerived(geomAnd(CONT,SAB),"CONT 9Rb: CONT must be salicided.")
#saveDerived(geomAnd(geomNot(geomOr(geomAnd(DIFF,MET1),geomAnd(POLY,MET1))),CONT),"CONT 9Rc: CONT must be enclosed by (DIFF and M1) or (POLY and M1).")
saveDerived(geomAndNot(CONT, DIFFMET_OR_POLYMET),"CONT 9Rc: CONT must be enclosed by (DIFF and M1) or (POLY and M1).")
saveDerived(geomAnd(CONT,POLYDIFF),"CONT 9Re: CONT on POLYDIFF is not allowed.")
geomOffGrid(geomOutside(NOGRID,CONT),0.005,0.005,"9Ga: Drawn CONT must conform to a 0.005um on-grid rule")

# METAL-1 (M1)
print "Check METAL-1"
geomWidth(geomOutside(SRAM,MET1), 0.23, "10W10a   : Minimum width of MET1 must be 0.23um ")
geomSpace(MET1,0.23,0,"10S10a  : Min spacing of MET1 to MET1 nets must be 0.23um")
geomSpace(MET1,0.60,10,10,0,"10S10b  : min. space between M1 lines with one or both M1 line width are greater than 10um must be 0.60um")
geomEnclose(geomOutside(SRAM,MET1),CONT,0.005,"10E9a: Min Encloser of MET1 to CONT nets must be 0.005um")
geomArea(MET1,0.2025,999,"10A10a:min. area of MET1 must be o.2025 um2 ")
geomOffGrid(geomOutside(NOGRID,MET1),0.005,0.005,"10Ga  :MET1 must be on a 5nm grid")
saveDerived(geomSize(MET1,-1.0),"10W10b: max. width of MET1 is 2.0um.")

# VIA1
print "Checking VIA1 Rules.. "
geomAllowedWidths(VIA1,[0.26],horizontal)
geomArea(VIA1,0.0676,0.068,"11W11a:WIdth of VIA1 should be 0.26um in all sides") 
#geomWidth(VIA1,0.26,"11W11a: min. & max. size of VIA1 is 0.26um.")
#saveDerived(geomSize(VIA1,-0.13),"11W11a: min. & max. size of VIA1 is 0.26um.")
geomSpace(VIA1,0.26,0,"11S11a:Min Space between VIA1 is 0.26um ") 
saveDerived(geomAndNot(geomOverlapping(MET1,VIA1),MET1),"11E10a :Overlap of a MET1 and VIA1 is not allowed")
geomEnclose(MET1,geomAnd(MET1,VIA1),0.01,"11E10a:Min Enclosure of VIA1 by MET1 must be 0.01um")
saveDerived(geomCoincident(MET1,VIA1),"11E10a:MET1 and VIA1 should not coincide")
geomOffGrid(geomAndNot(VIA1,geomAnd(VIA1,NOGRID)),0.005,0.05,"Minimum Grid value is 5nm") 

# METAL-2
print "Checking METAL2"
geomWidth(MET2, 0.28, "12W12a : Minimum width of MET2 must be 0.28um ")
geomSpace(MET2,0.28,0,"12S12a  : Min spacing of MET2 to MET2 must be 0.28um")
geomSpace(MET2,0.60,10,10,0,"12S12b  : min. space between M2 lines with one or both M1 line width are greater than 10um must be 0.60um")
geomEnclose(MET2, VIA1, 0.01, "12E11a: min. enclosure of VIA1 by M2 >= 0.01")
geomArea(MET2, 0.2025, 9e99, "12A12a : min. area of MET2 (um2) >= 0.2025 ")
geomOffGrid(MET2, 0.005, 0.005, "12Ga:metal2 must be on a 5nm grid")
saveDerived(geomSize(MET2,-1.0),"12W12b: max. width of MET2 is 2.0um.")

#VIA2 DRC Checks
print "Check VIA2"
geomAllowedWidths(VIA2,[0.26],horizontal)
geomArea(VIA2,0.0676,0.068,"13W13a:WIdth of VIA2 should be 0.26um in all sides") 
#geomWidth(VIA2,0.26,"13W13a: min. & max. size of VIA2 is 0.26um.")
#saveDerived(geomSize(VIA2,-0.13),"13W13a: min. & max. size of VIA2 is 0.26um.")
geomSpace(VIA2,0.26,0,"13S13a: min. space between two VIA2 is 0.26um.")
saveDerived(geomAndNot(geomOverlapping(MET2,VIA2),MET2),"13E13a :Overlap of a MET2 and VIA2 is not allowed")
geomEnclose(MET2,VIA2,0.01,"13E12a: min. enclosure of VIA2 by M2 is 0.01um.") 
geomOffGrid(geomOutside(NOGRID,VIA2),0.005,0.005,"13Ga: Drawn VIA2 must conform to a 0.005um on-grid rule")

# METAL-3 (M3)
print "Checking METAL3"
geomWidth(MET3, 0.28, "14W14a : Minimum width of MET3 must be 0.28um ")
geomSpace(MET3,0.28,0,"14S14a : Min spacing of MET3 to MET3 nets must be 0.28um")
geomSpace(MET3,0.60,10,10,0,"14S14b  : min. space between M3 lines with one or both M3 line width are greater than 10um must be 0.60um")
geomEnclose(MET3,VIA2 ,0.01,"14E13a: Min Encloser of MET3 to VIA2  nets must be 0.01um")
geomArea(MET3,0.2025,999,"14A14a:min. area of MET3 must be o.2025 um2 ")
geomOffGrid(geomOutside(NOGRID,MET3),0.005,0.005,"14Ga  :MET3 must be on a 5nm grid")
saveDerived(geomSize(MET3,-1.0),"14W14b: max. width of MET3 is 2.0um.")

#VIA3 DRC Checks
print "Checking VIA3 Rules.. "
geomAllowedWidths(VIA3,[0.26],horizontal)
geomArea(VIA3,0.0676,0.068,"15W15a:WIdth of VIA3 should be 0.26um in all sides") 
#geomWidth(VIA3,0.26,"15W15a: min. & max. size of VIA3 is 0.26um.")
#saveDerived(geomSize(VIA3,-0.13),"15W15a: min. & max. size of VIA3 is 0.26um.")
geomSpace(VIA3,0.26,0,"15S15a:Min Space between VIA3 is 0.26um ") 
saveDerived(geomAndNot(geomOverlapping(MET3,VIA3),MET3),"15E15a :Overlap of a MET3 and VIA3 is not allowed")
geomEnclose(MET3,geomAnd(MET3,VIA3),0.01,"15E14a:Min Enclosure of VIA3 by MET3 must be 0.01um")
saveDerived(geomCoincident(MET3,VIA3),"15E14a:MET3 and VIA3 should not coincide")
geomOffGrid(geomAndNot(VIA3,geomAnd(VIA3,NOGRID)),0.005,0.05,"Minimum Grid value is 5nm") 

# METAL-4 (M4)
print "Checking METAL4"
geomWidth(MET4, 0.28, "16W16a : Minimum width of MET4 must be 0.28um ")
geomSpace(MET4,0.28,0,"16S16a  : Min spacing of MET4 to MET4 must be 0.28um")
geomSpace(MET4,0.60,10,10,0,"16S16b  : min. space between M4 lines with one or both M4 line width are greater than 10um must be 0.60um")
geomEnclose(MET4, VIA3, 0.01, "16E15a: min. enclosure of VIA3 by M4 >= 0.01")
geomArea(MET4, 0.2025, 9e99, "16A16a : min. area of MET4 (um2) >= 0.2025 ")
geomOffGrid(MET4, 0.005, 0.005, "16Ga:metal4 must be on a 5nm grid")
saveDerived(geomSize(MET4,-1.0),"16W16b: max. width of MET4 is 2.0um.")

#VIA4 DRC Checks
print "Check VIA4"
geomAllowedWidths(VIA4,[0.26],horizontal)
geomArea(VIA4,0.0676,0.068,"17W17a:WIdth of VIA4 should be 0.26um in all sides") 
#geomWidth(VIA4,0.26,"17W17a: min. & max. size of VIA4 is 0.26um.")
#saveDerived(geomSize(VIA4,-0.13),"17W17a: min. & max. size of VIA4 is 0.26um.")
geomSpace(VIA4,0.26,0,"17S17a: min. space between two VIA4 is 0.26um.")
saveDerived(geomAndNot(geomOverlapping(MET4,VIA4),MET4),"17E17a :Overlap of a MET4 and VIA4 is not allowed")
geomEnclose(MET4,VIA4,0.01,"17E16a: min. enclosure of VIA4 by M4 is 0.01um.") 
geomOffGrid(geomOutside(NOGRID,VIA4),0.005,0.005,"17Ga: Drawn VIA4 must conform to a 0.005um on-grid rule")

# METAL-5 (M5)
print "Checking METAL5"
geomWidth(MET5, 0.28, "18W18a    : Minimum width of MET5 must be 0.28um ")
geomSpace(MET5,0.28,0,"18S18a : Min spacing of MET5 to MET5 nets must be 0.28um")
geomSpace(MET5,0.60,10,10,0,"18S18b  : min. space between M5 lines with one or both M5 line width are greater than 10um must be 0.60um")
geomEnclose(MET5,VIA4 ,0.01,"18E17a: Min Encloser of MET5 to VIA4  nets must be 0.01um")
geomArea(MET5,0.2025,999,"18A18a:min. area of MET5 must be o.2025 um2 ")
geomOffGrid(geomOutside(NOGRID,MET5),0.005,0.005,"18Ga  :MET5 must be on a 5nm grid")
saveDerived(geomSize(MET5,-1.0),"18W18b: max. width of MET5 is 2.0um.")

#VIA5 DRC Checks
print "Checking VIA5 Rules.. "
geomAllowedWidths(VIA5,[0.74],horizontal)
geomArea(VIA5,0.5476,0.548,"19W19a:WIdth of VIA5 should be 0.74x0.74um in all sides") 
#geomWidth(VIA5,0.26,"13W13a: min. & max. size of VIA5 is 0.26um.")
#saveDerived(geomSize(VIA5,-0.13),"13W13a: min. & max. size of VIA5 is 0.26um.")
geomSpace(VIA5,0.26,0,"19S19a:Min Space between VIA5 is 0.26um ") 
saveDerived(geomAndNot(geomOverlapping(MET5,VIA5),MET5),"19E18a:Overlap of a MET5 and VIA5 is not allowed")
geomEnclose(MET5,geomAnd(MET5,VIA5),0.01,"19E18a:Min Enclosure of VIA5 by MET5 must be 0.01um")
saveDerived(geomCoincident(MET5,VIA5),"19E18a:MET5 and VIA5 should not coincide")
geomOffGrid(geomAndNot(VIA5,geomAnd(VIA5,NOGRID)),0.005,0.05,"Minimum Grid value is 5nm") 

# METAL-6 (M6)
print "Checking METAL6"
geomWidth(MET6, 0.44,"20W20a    : Minimum width of MET6 must be 0.44um ")
geomSpace(MET6,0.46,0,"20S20a  : Min spacing of MET6 to MET6 nets must be 0.46um")
geomSpace(MET6,0.60,10,10,0,"20S20b  : min. space between M6 lines with one or both M6 line width are greater than 10um must be 0.60um")
geomEnclose(MET6,VIA5 ,0.09,"20E19a: Min Encloser of MET6 to VIA5  nets must be 0.09um")
geomArea(MET6,0.5625,999,"20A20a:min. area of MET6 must be 0.5625 um2 ")
geomOffGrid(geomOutside(NOGRID,MET6),0.005,0.005,"20Ga  :MET6 must be on a 5nm grid")
saveDerived(geomSize(MET6,-3.0),"20W20b: max. width of MET6 is 6.0um.")

# Protective Overcoat Removal (POR) DRC Checks
print "Check POR"
geomWidth(POR,60,"21W21a: min. dimension of a POR for bonding pad is 60umX60um.")
geomEnclose(MET6,POR,2,"21E20a: min. enclosure of POR by M1~M6 is 2um.") 	
geomWidth(geomAnd(VIA5,POR),0.36,"POR VIA5 21W21c: min. & max. width of VIA5 is 0.36um.")
saveDerived(geomSize(geomAnd(VIA5,POR),-0.18),"POR VIA5 21W21c: min. & max. width of VIA5 is 0.36um.")
geomSpace(geomAnd(VIA5,POR),0.35,0,"POR VIA5 21S19a: min. space between two VIA5 is 0.35um.")
geomSpace(BOND,5,0,"POR 21S21a: min. space between two bonding pad is 5um.")
geomSpace(POR,9,0,"21S21b: min. space between two POR regions for bonding pad is 9um.")
saveDerived(geomAndNot(geomAndNot(POR,SEALRING),MET6),"POR 21Ra: POR must be enclosed by Top Metal")
geomOffGrid(geomOutside(NOGRID,POR),0.005,0.005,"21Ga: Drawn POR must conform to a 0.005um on-grid rule")
geomEnclose(POR,geomOr(geomOr(VIA1,VIA3),VIA5),3,"21E19a: min. enclosure of VIA1,3,5 by POR is 3um.") 
geomEnclose(POR,geomOr(VIA2,VIA4),3,"21E17a: min. enclosure of VIA2,4 by POR is 3um.") 
geomWidth(geomAnd(geomOr(geomOr(VIA1,VIA2),geomOr(VIA3,VIA4)),POR),0.26,"POR 21W21b : min. & max. width of VIA1~4 is 0.26um.")
saveDerived(geomSize(geomAnd(geomOr(geomOr(VIA1,VIA2),geomOr(VIA3,VIA4)),POR),-0.13),"POR 21W21b : min. & max. width of VIA1~4 is 0.26um.")
geomSpace(geomAnd(VIA1,POR),0.45,0,"POR 21S17a: min. space between two VIA1~4 is 0.45um.")
geomSpace(geomAnd(VIA2,POR),0.45,0,"POR 21S17a: min. space between two VIA1~4 is 0.45um.")
geomSpace(geomAnd(VIA3,POR),0.45,0,"POR 21S17a: min. space between two VIA1~4 is 0.45um.")
geomSpace(geomAnd(VIA4,POR),0.45,0,"POR 21S17a: min. space between two VIA1~4 is 0.45um.")
geomSpace(geomAnd(geomOr(VIA1,VIA3),POR),geomAnd(geomOr(VIA2,VIA4),POR),0.13,0,"POR 21S17b: min. space between VIA1,3 and VIA2,4 is 0.13um")

#BLKDNW
print "Check BLKDNW"
geomWidth(BLKWELL,0.86,"92W92a :Minimum width of BLKWELL must be 0.86um")
geomSpace(BLKWELL,0.86,0,"92S92a :Minimum Space between two BLKWELL is 0.86um")
geomEnclose(BLKWELL_IN_PWELL,geomAnd(BLKWELL_IN_PWELL,DIFF),0.30,"92E3a:Min Enclosure of DIFF by BLKWELL in PWELL must be 0.30um")
saveDerived(geomCoincident(BLKWELL_IN_PWELL,DIFF),"92E3a:BLKWELL inside PWELL and DIFF should not coincide")
saveDerived(geomAndNot(geomOverlapping(BLKWELL_IN_PWELL,DIFF),BLKWELL_IN_PWELL),"92E3a:BLKWELL inside PWELL and DIFF should not Overlap")
geomEnclose(BLKWELL_IN_SDPW,geomAnd(BLKWELL_IN_SDPW,DIFF),1.00,"92E3b:Min Enclosure of DIFF by BLKWELL in SDPW must be 1um")
saveDerived(geomCoincident(BLKWELL_IN_SDPW,DIFF),"92E3b:BLKWELL inside SDPW and DIFF should not coincide")
saveDerived(geomAndNot(geomOverlapping(BLKWELL_IN_SDPW,DIFF),BLKWELL_IN_SDPW),"92E3b:BLKWELL inside SDPW and DIFF should not Overlap") 
geomSpace(BLKWELL,DIFF,0.52,0,"92S3a :Minimum Space between  BLKWELL and a DIFF is 0.52um")
geomSpace(BLKWELL,NWELL,1.66,0,"92S2a :Minimum Space between  BLKWELL and a NWELL EDGE is 1.66um")
geomSpace(BLKWELL,SDNW,1.66,0,"92S24a :Minimum Space between  BLKWELL and a SDNW EDGE is 1.66um")
saveDerived(geomOr(geomTouching(DNW,BLKWELL),geomAnd(DNW,BLKWELL)),"92Ra:BLKWELL interact DNW is not allowed.")
geomOffGrid(geomAndNot(BLKWELL,geomAnd(BLKWELL,NOGRID)),0.005,0.005,"Minimum Grid value is 5nm") 

# Exit DRC package, freeing memory
geomEnd()
ui().winFit()
