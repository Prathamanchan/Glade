# This file was created automatically by SWIG 1.3.27.
# Don't modify this file, modify the SWIG interface instead.

import _ui

# This file is compatible with both classic and new-style classes.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class ui(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ui, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ui, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ ui instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ui, 'this', _ui.new_ui(*args))
        _swig_setattr(self, ui, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_ui):
        try:
            if self.thisown: destroy(self)
        except: pass

    def licenseCheck(*args): return _ui.ui_licenseCheck(*args)
    def setMaxErrCount(*args): return _ui.ui_setMaxErrCount(*args)
    def maxErrCount(*args): return _ui.ui_maxErrCount(*args)
    def closeAllWindows(*args): return _ui.ui_closeAllWindows(*args)
    def loadPCell(*args): return _ui.ui_loadPCell(*args)
    def openCellView(*args): return _ui.ui_openCellView(*args)
    def closeCellView(*args): return _ui.ui_closeCellView(*args)
    def importTech(*args): return _ui.ui_importTech(*args)
    def exportTech(*args): return _ui.ui_exportTech(*args)
    def importGds2(*args): return _ui.ui_importGds2(*args)
    def exportGds2(*args): return _ui.ui_exportGds2(*args)
    def importLef(*args): return _ui.ui_importLef(*args)
    def exportLef(*args): return _ui.ui_exportLef(*args)
    def importDef(*args): return _ui.ui_importDef(*args)
    def exportDef(*args): return _ui.ui_exportDef(*args)
    def importVerilog(*args): return _ui.ui_importVerilog(*args)
    def exportVerilog(*args): return _ui.ui_exportVerilog(*args)
    def importECO(*args): return _ui.ui_importECO(*args)
    def importOasis(*args): return _ui.ui_importOasis(*args)
    def exportOasis(*args): return _ui.ui_exportOasis(*args)
    def importDxf(*args): return _ui.ui_importDxf(*args)
    def exportDxf(*args): return _ui.ui_exportDxf(*args)
    def importCDL(*args): return _ui.ui_importCDL(*args)
    def exportCDL(*args): return _ui.ui_exportCDL(*args)
    def importEdif(*args): return _ui.ui_importEdif(*args)
    def exportEdif(*args): return _ui.ui_exportEdif(*args)
    def importCds(*args): return _ui.ui_importCds(*args)
    def importLaker(*args): return _ui.ui_importLaker(*args)
    def importLaff(*args): return _ui.ui_importLaff(*args)
    def importHercules(*args): return _ui.ui_importHercules(*args)
    def importCalibre(*args): return _ui.ui_importCalibre(*args)
    def cdlFlatten(*args): return _ui.ui_cdlFlatten(*args)
    def scaleCells(*args): return _ui.ui_scaleCells(*args)
    def scaleCell(*args): return _ui.ui_scaleCell(*args)
    def biasCells(*args): return _ui.ui_biasCells(*args)
    def biasCell(*args): return _ui.ui_biasCell(*args)
    def updateCellBBox(*args): return _ui.ui_updateCellBBox(*args)
    def zoomIn(*args): return _ui.ui_zoomIn(*args)
    def zoomOut(*args): return _ui.ui_zoomOut(*args)
    def selectArea(*args): return _ui.ui_selectArea(*args)
    def deselectArea(*args): return _ui.ui_deselectArea(*args)
    def selectAll(*args): return _ui.ui_selectAll(*args)
    def deselectAll(*args): return _ui.ui_deselectAll(*args)
    def selectPoint(*args): return _ui.ui_selectPoint(*args)
    def deselectPoint(*args): return _ui.ui_deselectPoint(*args)
    def execPythonFile(*args): return _ui.ui_execPythonFile(*args)
    def addMarker(*args): return _ui.ui_addMarker(*args)
    def clearMarkers(*args): return _ui.ui_clearMarkers(*args)
    def getSelectedSet(*args): return _ui.ui_getSelectedSet(*args)
    def selectObj(*args): return _ui.ui_selectObj(*args)
    def deselectObj(*args): return _ui.ui_deselectObj(*args)
    def addSelected(*args): return _ui.ui_addSelected(*args)
    def addHilite(*args): return _ui.ui_addHilite(*args)
    def clearHilites(*args): return _ui.ui_clearHilites(*args)
    def getEditCellView(*args): return _ui.ui_getEditCellView(*args)
    def getLibByName(*args): return _ui.ui_getLibByName(*args)
    def getLibList(*args): return _ui.ui_getLibList(*args)
    def updateLibBrowser(*args): return _ui.ui_updateLibBrowser(*args)
    def updateLSW(*args): return _ui.ui_updateLSW(*args)
    def setLayerVisible(*args): return _ui.ui_setLayerVisible(*args)
    def isLayerVisible(*args): return _ui.ui_isLayerVisible(*args)
    def setLayerSelectable(*args): return _ui.ui_setLayerSelectable(*args)
    def isLayerSelectable(*args): return _ui.ui_isLayerSelectable(*args)
    def getCellList(*args): return _ui.ui_getCellList(*args)
    def createMenu(*args): return _ui.ui_createMenu(*args)
    def createAction(*args): return _ui.ui_createAction(*args)
    def createActionGroup(*args): return _ui.ui_createActionGroup(*args)
    def setBindKey(*args): return _ui.ui_setBindKey(*args)
    def createMenuItem(*args): return _ui.ui_createMenuItem(*args)
    def createIcon(*args): return _ui.ui_createIcon(*args)
    def setIcon(*args): return _ui.ui_setIcon(*args)
    def createToolBar(*args): return _ui.ui_createToolBar(*args)
    def createToolBarItem(*args): return _ui.ui_createToolBarItem(*args)
    def addSeparator(*args): return _ui.ui_addSeparator(*args)
    def createDialog(*args): return _ui.ui_createDialog(*args)
    def compareCells(*args): return _ui.ui_compareCells(*args)
    def compareCells2(*args): return _ui.ui_compareCells2(*args)
    def runLVS(*args): return _ui.ui_runLVS(*args)
    def schCheck(*args): return _ui.ui_schCheck(*args)
    def symCheck(*args): return _ui.ui_symCheck(*args)
    def uiSchCheck(*args): return _ui.ui_uiSchCheck(*args)
    def uiSymCheck(*args): return _ui.ui_uiSymCheck(*args)
    def viewCheck(*args): return _ui.ui_viewCheck(*args)
    def createCellView(*args): return _ui.ui_createCellView(*args)
    def schHNLOut(*args): return _ui.ui_schHNLOut(*args)
    def checkExtracted(*args): return _ui.ui_checkExtracted(*args)
    def closeLib(*args): return _ui.ui_closeLib(*args)
    def moveSelected(*args): return _ui.ui_moveSelected(*args)
    def copySelected(*args): return _ui.ui_copySelected(*args)
    def routeWire(*args): return _ui.ui_routeWire(*args)
    def routeTrack(*args): return _ui.ui_routeTrack(*args)
    def execCallback(*args): return _ui.ui_execCallback(*args)
    def fileNewCell(*args): return _ui.ui_fileNewCell(*args)
    def fileOpenCell(*args): return _ui.ui_fileOpenCell(*args)
    def fileSaveCell(*args): return _ui.ui_fileSaveCell(*args)
    def fileSaveCellAs(*args): return _ui.ui_fileSaveCellAs(*args)
    def fileRestoreCell(*args): return _ui.ui_fileRestoreCell(*args)
    def fileNewLib(*args): return _ui.ui_fileNewLib(*args)
    def fileOpenLib(*args): return _ui.ui_fileOpenLib(*args)
    def fileSaveLib(*args): return _ui.ui_fileSaveLib(*args)
    def fileSaveLibAs(*args): return _ui.ui_fileSaveLibAs(*args)
    def fileCloseLib(*args): return _ui.ui_fileCloseLib(*args)
    def fileDumpGraphics(*args): return _ui.ui_fileDumpGraphics(*args)
    def fileDumpSVG(*args): return _ui.ui_fileDumpSVG(*args)
    def filePrint(*args): return _ui.ui_filePrint(*args)
    def fileView(*args): return _ui.ui_fileView(*args)
    def fileExit(*args): return _ui.ui_fileExit(*args)
    def winFit(*args): return _ui.ui_winFit(*args)
    def winFitPlus(*args): return _ui.ui_winFitPlus(*args)
    def winRedraw(*args): return _ui.ui_winRedraw(*args)
    def winCancel(*args): return _ui.ui_winCancel(*args)
    def winRuler(*args): return _ui.ui_winRuler(*args)
    def winDeleteRulers(*args): return _ui.ui_winDeleteRulers(*args)
    def winPan(*args): return _ui.ui_winPan(*args)
    def winPanLeft(*args): return _ui.ui_winPanLeft(*args)
    def winPanRight(*args): return _ui.ui_winPanRight(*args)
    def winPanUp(*args): return _ui.ui_winPanUp(*args)
    def winPanDown(*args): return _ui.ui_winPanDown(*args)
    def winPan2Point(*args): return _ui.ui_winPan2Point(*args)
    def winZoomIn(*args): return _ui.ui_winZoomIn(*args)
    def winZoomOut(*args): return _ui.ui_winZoomOut(*args)
    def winZoomSelected(*args): return _ui.ui_winZoomSelected(*args)
    def winView0(*args): return _ui.ui_winView0(*args)
    def winView20(*args): return _ui.ui_winView20(*args)
    def winSelOpts(*args): return _ui.ui_winSelOpts(*args)
    def winDisplayPrefs(*args): return _ui.ui_winDisplayPrefs(*args)
    def winLastView(*args): return _ui.ui_winLastView(*args)
    def editYank(*args): return _ui.ui_editYank(*args)
    def editPaste(*args): return _ui.ui_editPaste(*args)
    def editUndo(*args): return _ui.ui_editUndo(*args)
    def editRedo(*args): return _ui.ui_editRedo(*args)
    def editCut(*args): return _ui.ui_editCut(*args)
    def editMove(*args): return _ui.ui_editMove(*args)
    def editMoveBy(*args): return _ui.ui_editMoveBy(*args)
    def editCopy(*args): return _ui.ui_editCopy(*args)
    def editStretch(*args): return _ui.ui_editStretch(*args)
    def editReshape(*args): return _ui.ui_editReshape(*args)
    def editRoundCorners(*args): return _ui.ui_editRoundCorners(*args)
    def editSelNet(*args): return _ui.ui_editSelNet(*args)
    def editSelInst(*args): return _ui.ui_editSelInst(*args)
    def editSelAll(*args): return _ui.ui_editSelAll(*args)
    def editDeselAll(*args): return _ui.ui_editDeselAll(*args)
    def editHierAscend(*args): return _ui.ui_editHierAscend(*args)
    def editHierDescend(*args): return _ui.ui_editHierDescend(*args)
    def editHierCreate(*args): return _ui.ui_editHierCreate(*args)
    def editHierFlatten(*args): return _ui.ui_editHierFlatten(*args)
    def editFind(*args): return _ui.ui_editFind(*args)
    def editRotate(*args): return _ui.ui_editRotate(*args)
    def editChangeOrient(*args): return _ui.ui_editChangeOrient(*args)
    def editMirrorX(*args): return _ui.ui_editMirrorX(*args)
    def editMirrorY(*args): return _ui.ui_editMirrorY(*args)
    def editRotate90(*args): return _ui.ui_editRotate90(*args)
    def editMoveOrigin(*args): return _ui.ui_editMoveOrigin(*args)
    def editAddFillers(*args): return _ui.ui_editAddFillers(*args)
    def editDeleteFillers(*args): return _ui.ui_editDeleteFillers(*args)
    def editReplaceViews(*args): return _ui.ui_editReplaceViews(*args)
    def editBindkeys(*args): return _ui.ui_editBindkeys(*args)
    def editInPlace(*args): return _ui.ui_editInPlace(*args)
    def editReturnOneLevel(*args): return _ui.ui_editReturnOneLevel(*args)
    def editPath2Poly(*args): return _ui.ui_editPath2Poly(*args)
    def editAddVertex(*args): return _ui.ui_editAddVertex(*args)
    def editMergeSelected(*args): return _ui.ui_editMergeSelected(*args)
    def editChop(*args): return _ui.ui_editChop(*args)
    def editAlign(*args): return _ui.ui_editAlign(*args)
    def editScale(*args): return _ui.ui_editScale(*args)
    def editBias(*args): return _ui.ui_editBias(*args)
    def editBooleans(*args): return _ui.ui_editBooleans(*args)
    def editSetNet(*args): return _ui.ui_editSetNet(*args)
    def editCreatePinsFromLabels(*args): return _ui.ui_editCreatePinsFromLabels(*args)
    def editCreateInst(*args): return _ui.ui_editCreateInst(*args)
    def editCreateLabel(*args): return _ui.ui_editCreateLabel(*args)
    def editCreatePath(*args): return _ui.ui_editCreatePath(*args)
    def editCreateMPP(*args): return _ui.ui_editCreateMPP(*args)
    def editCreatePoly(*args): return _ui.ui_editCreatePoly(*args)
    def editCreateRect(*args): return _ui.ui_editCreateRect(*args)
    def editCreateArc(*args): return _ui.ui_editCreateArc(*args)
    def editCreateEllipse(*args): return _ui.ui_editCreateEllipse(*args)
    def editCreateVia(*args): return _ui.ui_editCreateVia(*args)
    def editCreatePin(*args): return _ui.ui_editCreatePin(*args)
    def editCreateLine(*args): return _ui.ui_editCreateLine(*args)
    def editCreateWire(*args): return _ui.ui_editCreateWire(*args)
    def editCreateBus(*args): return _ui.ui_editCreateBus(*args)
    def verifyCheckOffGrid(*args): return _ui.ui_verifyCheckOffGrid(*args)
    def verifyDRCRun(*args): return _ui.ui_verifyDRCRun(*args)
    def verifyDRCView(*args): return _ui.ui_verifyDRCView(*args)
    def verifyDRCClear(*args): return _ui.ui_verifyDRCClear(*args)
    def verifyLPERun(*args): return _ui.ui_verifyLPERun(*args)
    def verifyLVSRun(*args): return _ui.ui_verifyLVSRun(*args)
    def verifyCompare(*args): return _ui.ui_verifyCompare(*args)
    def verifyTraceNet(*args): return _ui.ui_verifyTraceNet(*args)
    def verifyLayerStack(*args): return _ui.ui_verifyLayerStack(*args)
    def verifyShortTracer(*args): return _ui.ui_verifyShortTracer(*args)
    def verifyClearHighlights(*args): return _ui.ui_verifyClearHighlights(*args)
    def fpInit(*args): return _ui.ui_fpInit(*args)
    def checkOverlaps(*args): return _ui.ui_checkOverlaps(*args)
    def fpCreateRows(*args): return _ui.ui_fpCreateRows(*args)
    def fpCreateRegion(*args): return _ui.ui_fpCreateRegion(*args)
    def fpCreateGroups(*args): return _ui.ui_fpCreateGroups(*args)
    def fpPlace(*args): return _ui.ui_fpPlace(*args)
    def fpUnplace(*args): return _ui.ui_fpUnplace(*args)
    def fpGlobalRoute(*args): return _ui.ui_fpGlobalRoute(*args)
    def fpDisplayGroute(*args): return _ui.ui_fpDisplayGroute(*args)
    def fpShowCongMap(*args): return _ui.ui_fpShowCongMap(*args)
    def fpNewGroute(*args): return _ui.ui_fpNewGroute(*args)
    def fpHighLightNetTypes(*args): return _ui.ui_fpHighLightNetTypes(*args)
    def viewHierarchy(*args): return _ui.ui_viewHierarchy(*args)
    def viewLSW(*args): return _ui.ui_viewLSW(*args)
    def viewLibBrowser(*args): return _ui.ui_viewLibBrowser(*args)
    def viewStatusbar(*args): return _ui.ui_viewStatusbar(*args)
    def tiledBooleans(*args): return _ui.ui_tiledBooleans(*args)
    def showMemStats(*args): return _ui.ui_showMemStats(*args)
    def showKDTreeStats(*args): return _ui.ui_showKDTreeStats(*args)
    def checkIfEdited(*args): return _ui.ui_checkIfEdited(*args)
    def saveCellView(*args): return _ui.ui_saveCellView(*args)
    def saveLib(*args): return _ui.ui_saveLib(*args)
    def deleteCellView(*args): return _ui.ui_deleteCellView(*args)
    def renameCellView(*args): return _ui.ui_renameCellView(*args)
    def copyCell(*args): return _ui.ui_copyCell(*args)
    def copyCellView(*args): return _ui.ui_copyCellView(*args)
    def properties(*args): return _ui.ui_properties(*args)
    def copyHierCellView(*args): return _ui.ui_copyHierCellView(*args)
    def fpPlaceReadDesign(*args): return _ui.ui_fpPlaceReadDesign(*args)
    def fpPlaceReadStdout(*args): return _ui.ui_fpPlaceReadStdout(*args)
    def fpPlaceReadStderr(*args): return _ui.ui_fpPlaceReadStderr(*args)
    def lvsStarted(*args): return _ui.ui_lvsStarted(*args)
    def lvsReadErrors(*args): return _ui.ui_lvsReadErrors(*args)
    def lvsReadStdout(*args): return _ui.ui_lvsReadStdout(*args)
    def lvsReadStderr(*args): return _ui.ui_lvsReadStderr(*args)
    def shortTracer(*args): return _ui.ui_shortTracer(*args)

class uiPtr(ui):
    def __init__(self, this):
        _swig_setattr(self, ui, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ui, 'thisown', 0)
        self.__class__ = ui
_ui.ui_swigregister(uiPtr)
cvar = _ui.cvar

class polygonHole(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, polygonHole, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, polygonHole, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ polygonHole instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, polygonHole, 'this', _ui.new_polygonHole(*args))
        _swig_setattr(self, polygonHole, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_polygonHole):
        try:
            if self.thisown: destroy(self)
        except: pass

    def xpts(*args): return _ui.polygonHole_xpts(*args)
    def ypts(*args): return _ui.polygonHole_ypts(*args)
    def size(*args): return _ui.polygonHole_size(*args)

class polygonHolePtr(polygonHole):
    def __init__(self, this):
        _swig_setattr(self, polygonHole, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, polygonHole, 'thisown', 0)
        self.__class__ = polygonHole
_ui.polygonHole_swigregister(polygonHolePtr)

class dbObj(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dbObj, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dbObj, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObj instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, dbObj, 'this', _ui.new_dbObj(*args))
        _swig_setattr(self, dbObj, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_dbObj):
        try:
            if self.thisown: destroy(self)
        except: pass

    def objType(*args): return _ui.dbObj_objType(*args)
    def objName(*args): return _ui.dbObj_objName(*args)
    def offGrid(*args): return _ui.dbObj_offGrid(*args)
    def bBox(*args): return _ui.dbObj_bBox(*args)
    def qBox(*args): return _ui.dbObj_qBox(*args)
    def left(*args): return _ui.dbObj_left(*args)
    def right(*args): return _ui.dbObj_right(*args)
    def bottom(*args): return _ui.dbObj_bottom(*args)
    def top(*args): return _ui.dbObj_top(*args)
    def coord(*args): return _ui.dbObj_coord(*args)
    def setLeft(*args): return _ui.dbObj_setLeft(*args)
    def setRight(*args): return _ui.dbObj_setRight(*args)
    def setBottom(*args): return _ui.dbObj_setBottom(*args)
    def setTop(*args): return _ui.dbObj_setTop(*args)
    def isValid(*args): return _ui.dbObj_isValid(*args)
    def isInst(*args): return _ui.dbObj_isInst(*args)
    def isShape(*args): return _ui.dbObj_isShape(*args)
    def isViaInst(*args): return _ui.dbObj_isViaInst(*args)
    def isSeg(*args): return _ui.dbObj_isSeg(*args)
    def isVertex(*args): return _ui.dbObj_isVertex(*args)
    def setSpecial(*args): return _ui.dbObj_setSpecial(*args)
    def isSpecial(*args): return _ui.dbObj_isSpecial(*args)
    def dbFindProp(*args): return _ui.dbObj_dbFindProp(*args)
    def dbFindPropType(*args): return _ui.dbObj_dbFindPropType(*args)
    def dbSetPropVisible(*args): return _ui.dbObj_dbSetPropVisible(*args)
    def dbIsPropVisible(*args): return _ui.dbObj_dbIsPropVisible(*args)
    def dbAddProp(*args): return _ui.dbObj_dbAddProp(*args)
    def dbReplaceProp(*args): return _ui.dbObj_dbReplaceProp(*args)
    def dbGetStringProp(*args): return _ui.dbObj_dbGetStringProp(*args)
    def dbGetIntProp(*args): return _ui.dbObj_dbGetIntProp(*args)
    def dbGetFloatProp(*args): return _ui.dbObj_dbGetFloatProp(*args)
    def dbGetBoolProp(*args): return _ui.dbObj_dbGetBoolProp(*args)
    def dbGetOrientProp(*args): return _ui.dbObj_dbGetOrientProp(*args)
    def dbGetPropList(*args): return _ui.dbObj_dbGetPropList(*args)
    def dbSetPropList(*args): return _ui.dbObj_dbSetPropList(*args)
    def dbDeleteProp(*args): return _ui.dbObj_dbDeleteProp(*args)
    def dbGetProp(*args): return _ui.dbObj_dbGetProp(*args)
    def getNearestEdge(*args): return _ui.dbObj_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.dbObj_getNearestVertex(*args)
    def scale(*args): return _ui.dbObj_scale(*args)
    def Move(*args): return _ui.dbObj_Move(*args)
    def Copy(*args): return _ui.dbObj_Copy(*args)
    def Flatten(*args): return _ui.dbObj_Flatten(*args)
    def Stretch(*args): return _ui.dbObj_Stretch(*args)
    def transform(*args): return _ui.dbObj_transform(*args)
    def setNet(*args): return _ui.dbObj_setNet(*args)
    def getNet(*args): return _ui.dbObj_getNet(*args)
    def getNetName(*args): return _ui.dbObj_getNetName(*args)
    def layer(*args): return _ui.dbObj_layer(*args)
    def toArc(*args): return _ui.dbObj_toArc(*args)
    def toArray(*args): return _ui.dbObj_toArray(*args)
    def toCell(*args): return _ui.dbObj_toCell(*args)
    def toCellView(*args): return _ui.dbObj_toCellView(*args)
    def toEllipse(*args): return _ui.dbObj_toEllipse(*args)
    def toHSeg(*args): return _ui.dbObj_toHSeg(*args)
    def toInst(*args): return _ui.dbObj_toInst(*args)
    def toLabel(*args): return _ui.dbObj_toLabel(*args)
    def toLine(*args): return _ui.dbObj_toLine(*args)
    def toPath(*args): return _ui.dbObj_toPath(*args)
    def toPolygon(*args): return _ui.dbObj_toPolygon(*args)
    def toRectangle(*args): return _ui.dbObj_toRectangle(*args)
    def toSegment(*args): return _ui.dbObj_toSegment(*args)
    def toShape(*args): return _ui.dbObj_toShape(*args)
    def toViaInst(*args): return _ui.dbObj_toViaInst(*args)
    def toView(*args): return _ui.dbObj_toView(*args)
    def toVertex(*args): return _ui.dbObj_toVertex(*args)
    def toVSeg(*args): return _ui.dbObj_toVSeg(*args)
    def getPropList(*args): return _ui.dbObj_getPropList(*args)
    def setPropList(*args): return _ui.dbObj_setPropList(*args)

class dbObjPtr(dbObj):
    def __init__(self, this):
        _swig_setattr(self, dbObj, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dbObj, 'thisown', 0)
        self.__class__ = dbObj
_ui.dbObj_swigregister(dbObjPtr)

class propValue(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, propValue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, propValue, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ propValue instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["s"] = _ui.propValue_s_set
    __swig_getmethods__["s"] = _ui.propValue_s_get
    if _newclass:s = property(_ui.propValue_s_get, _ui.propValue_s_set)
    __swig_setmethods__["b"] = _ui.propValue_b_set
    __swig_getmethods__["b"] = _ui.propValue_b_get
    if _newclass:b = property(_ui.propValue_b_get, _ui.propValue_b_set)
    __swig_setmethods__["i"] = _ui.propValue_i_set
    __swig_getmethods__["i"] = _ui.propValue_i_get
    if _newclass:i = property(_ui.propValue_i_get, _ui.propValue_i_set)
    __swig_setmethods__["f"] = _ui.propValue_f_set
    __swig_getmethods__["f"] = _ui.propValue_f_get
    if _newclass:f = property(_ui.propValue_f_get, _ui.propValue_f_set)
    __swig_setmethods__["o"] = _ui.propValue_o_set
    __swig_getmethods__["o"] = _ui.propValue_o_get
    if _newclass:o = property(_ui.propValue_o_get, _ui.propValue_o_set)
    def __init__(self, *args):
        _swig_setattr(self, propValue, 'this', _ui.new_propValue(*args))
        _swig_setattr(self, propValue, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_propValue):
        try:
            if self.thisown: destroy(self)
        except: pass


class propValuePtr(propValue):
    def __init__(self, this):
        _swig_setattr(self, propValue, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, propValue, 'thisown', 0)
        self.__class__ = propValue
_ui.propValue_swigregister(propValuePtr)

stringType = _ui.stringType
booleanType = _ui.booleanType
integerType = _ui.integerType
floatType = _ui.floatType
listType = _ui.listType
orientType = _ui.orientType
unknownType = _ui.unknownType
class prop(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, prop, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, prop, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::prop instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_ui.delete_prop):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __init__(self, *args):
        _swig_setattr(self, prop, 'this', _ui.new_prop(*args))
        _swig_setattr(self, prop, 'thisown', 1)
    def data(*args): return _ui.prop_data(*args)
    def setData(*args): return _ui.prop_setData(*args)
    def name(*args): return _ui.prop_name(*args)
    def setName(*args): return _ui.prop_setName(*args)
    def type(*args): return _ui.prop_type(*args)
    def setType(*args): return _ui.prop_setType(*args)
    def isVisible(*args): return _ui.prop_isVisible(*args)
    def setVisible(*args): return _ui.prop_setVisible(*args)

class propPtr(prop):
    def __init__(self, this):
        _swig_setattr(self, prop, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, prop, 'thisown', 0)
        self.__class__ = prop
_ui.prop_swigregister(propPtr)

class pListItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pListItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pListItem, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::pListItem instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["next"] = _ui.pListItem_next_set
    __swig_getmethods__["next"] = _ui.pListItem_next_get
    if _newclass:next = property(_ui.pListItem_next_get, _ui.pListItem_next_set)
    __swig_setmethods__["m_Prop"] = _ui.pListItem_m_Prop_set
    __swig_getmethods__["m_Prop"] = _ui.pListItem_m_Prop_get
    if _newclass:m_Prop = property(_ui.pListItem_m_Prop_get, _ui.pListItem_m_Prop_set)
    def __init__(self, *args):
        _swig_setattr(self, pListItem, 'this', _ui.new_pListItem(*args))
        _swig_setattr(self, pListItem, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pListItem):
        try:
            if self.thisown: destroy(self)
        except: pass


class pListItemPtr(pListItem):
    def __init__(self, this):
        _swig_setattr(self, pListItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pListItem, 'thisown', 0)
        self.__class__ = pListItem
_ui.pListItem_swigregister(pListItemPtr)

class proplist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, proplist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, proplist, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::proplist instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, proplist, 'this', _ui.new_proplist(*args))
        _swig_setattr(self, proplist, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_proplist):
        try:
            if self.thisown: destroy(self)
        except: pass

    def addProp(*args): return _ui.proplist_addProp(*args)
    def replaceProp(*args): return _ui.proplist_replaceProp(*args)
    def getStringProp(*args): return _ui.proplist_getStringProp(*args)
    def getIntProp(*args): return _ui.proplist_getIntProp(*args)
    def getFloatProp(*args): return _ui.proplist_getFloatProp(*args)
    def getBoolProp(*args): return _ui.proplist_getBoolProp(*args)
    def findProp(*args): return _ui.proplist_findProp(*args)
    def getPropType(*args): return _ui.proplist_getPropType(*args)
    def setPropVisible(*args): return _ui.proplist_setPropVisible(*args)
    def isPropVisible(*args): return _ui.proplist_isPropVisible(*args)
    def getPropList(*args): return _ui.proplist_getPropList(*args)
    def setPropList(*args): return _ui.proplist_setPropList(*args)
    def deleteProp(*args): return _ui.proplist_deleteProp(*args)

class proplistPtr(proplist):
    def __init__(self, this):
        _swig_setattr(self, proplist, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, proplist, 'thisown', 0)
        self.__class__ = proplist
_ui.proplist_swigregister(proplistPtr)


copyPropList = _ui.copyPropList

deletePropList = _ui.deletePropList

deleteProp = _ui.deleteProp
class shape(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, shape, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, shape, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::shape instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, shape, 'this', _ui.new_shape(*args))
        _swig_setattr(self, shape, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_shape):
        try:
            if self.thisown: destroy(self)
        except: pass

    def layer(*args): return _ui.shape_layer(*args)
    def setSpecial(*args): return _ui.shape_setSpecial(*args)
    def isSpecial(*args): return _ui.shape_isSpecial(*args)
    def setVisited(*args): return _ui.shape_setVisited(*args)
    def wasVisited(*args): return _ui.shape_wasVisited(*args)
    def setNet(*args): return _ui.shape_setNet(*args)
    def getNet(*args): return _ui.shape_getNet(*args)
    def changeNet(*args): return _ui.shape_changeNet(*args)
    def getNetName(*args): return _ui.shape_getNetName(*args)
    def bias(*args): return _ui.shape_bias(*args)
    def getSegPts(*args): return _ui.shape_getSegPts(*args)
    def getVertexAdjPts(*args): return _ui.shape_getVertexAdjPts(*args)
    def getSegsInRect(*args): return _ui.shape_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.shape_getVertsInRect(*args)
    def nPoints(*args): return _ui.shape_nPoints(*args)
    def ptlist(*args): return _ui.shape_ptlist(*args)
    def shapeToPoly(*args): return _ui.shape_shapeToPoly(*args)
    def length(*args): return _ui.shape_length(*args)
    def area(*args): return _ui.shape_area(*args)
    def perimeter(*args): return _ui.shape_perimeter(*args)
    def ptInPoly(*args): return _ui.shape_ptInPoly(*args)
    def manhattan(*args): return _ui.shape_manhattan(*args)

class shapePtr(shape):
    def __init__(self, this):
        _swig_setattr(self, shape, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, shape, 'thisown', 0)
        self.__class__ = shape
_ui.shape_swigregister(shapePtr)

class inst(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, inst, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, inst, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::inst instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, inst, 'this', _ui.new_inst(*args))
        _swig_setattr(self, inst, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_inst):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.inst_left(*args)
    def right(*args): return _ui.inst_right(*args)
    def bottom(*args): return _ui.inst_bottom(*args)
    def top(*args): return _ui.inst_top(*args)
    def coord(*args): return _ui.inst_coord(*args)
    def offGrid(*args): return _ui.inst_offGrid(*args)
    def orient(*args): return _ui.inst_orient(*args)
    def status(*args): return _ui.inst_status(*args)
    def getPlacementStatusStr(*args): return _ui.inst_getPlacementStatusStr(*args)
    def source(*args): return _ui.inst_source(*args)
    def getPlacementSourceStr(*args): return _ui.inst_getPlacementSourceStr(*args)
    def bound(*args): return _ui.inst_bound(*args)
    def anyAngle(*args): return _ui.inst_anyAngle(*args)
    def angle(*args): return _ui.inst_angle(*args)
    def mag(*args): return _ui.inst_mag(*args)
    def libName(*args): return _ui.inst_libName(*args)
    def lib(*args): return _ui.inst_lib(*args)
    def cellName(*args): return _ui.inst_cellName(*args)
    def viewName(*args): return _ui.inst_viewName(*args)
    def instName(*args): return _ui.inst_instName(*args)
    def setMaster(*args): return _ui.inst_setMaster(*args)
    def getMaster(*args): return _ui.inst_getMaster(*args)
    def origin(*args): return _ui.inst_origin(*args)
    def bBox(*args): return _ui.inst_bBox(*args)
    def qBox(*args): return _ui.inst_qBox(*args)
    def updateBbox(*args): return _ui.inst_updateBbox(*args)
    def getBoundary(*args): return _ui.inst_getBoundary(*args)
    def objType(*args): return _ui.inst_objType(*args)
    def objName(*args): return _ui.inst_objName(*args)
    def getHPWL(*args): return _ui.inst_getHPWL(*args)
    def getNearestEdge(*args): return _ui.inst_getNearestEdge(*args)
    def transform(*args): return _ui.inst_transform(*args)
    def numRows(*args): return _ui.inst_numRows(*args)
    def numCols(*args): return _ui.inst_numCols(*args)
    def rowSpacing(*args): return _ui.inst_rowSpacing(*args)
    def colSpacing(*args): return _ui.inst_colSpacing(*args)
    def scale(*args): return _ui.inst_scale(*args)
    def Move(*args): return _ui.inst_Move(*args)
    def Copy(*args): return _ui.inst_Copy(*args)
    def Flatten(*args): return _ui.inst_Flatten(*args)
    def dbCreateInstPin(*args): return _ui.inst_dbCreateInstPin(*args)
    def dbDeleteInstPin(*args): return _ui.inst_dbDeleteInstPin(*args)
    def dbFindInstPinByName(*args): return _ui.inst_dbFindInstPinByName(*args)
    def instPins(*args): return _ui.inst_instPins(*args)
    def addInstPin(*args): return _ui.inst_addInstPin(*args)
    def getNumInstPins(*args): return _ui.inst_getNumInstPins(*args)
    def nPoints(*args): return _ui.inst_nPoints(*args)
    def ptlist(*args): return _ui.inst_ptlist(*args)
    def layer(*args): return _ui.inst_layer(*args)
    def mFactor(*args): return _ui.inst_mFactor(*args)
    def numBits(*args): return _ui.inst_numBits(*args)
    def getInstPins(*args): return _ui.inst_getInstPins(*args)

class instPtr(inst):
    def __init__(self, this):
        _swig_setattr(self, inst, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, inst, 'thisown', 0)
        self.__class__ = inst
_ui.inst_swigregister(instPtr)

class ellipse(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ellipse, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ellipse, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::ellipse instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ellipse, 'this', _ui.new_ellipse(*args))
        _swig_setattr(self, ellipse, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_ellipse):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.ellipse_left(*args)
    def right(*args): return _ui.ellipse_right(*args)
    def bottom(*args): return _ui.ellipse_bottom(*args)
    def top(*args): return _ui.ellipse_top(*args)
    def coord(*args): return _ui.ellipse_coord(*args)
    def setLeft(*args): return _ui.ellipse_setLeft(*args)
    def setRight(*args): return _ui.ellipse_setRight(*args)
    def setBottom(*args): return _ui.ellipse_setBottom(*args)
    def setTop(*args): return _ui.ellipse_setTop(*args)
    def origin(*args): return _ui.ellipse_origin(*args)
    def setOrigin(*args): return _ui.ellipse_setOrigin(*args)
    def width(*args): return _ui.ellipse_width(*args)
    def height(*args): return _ui.ellipse_height(*args)
    def qBox(*args): return _ui.ellipse_qBox(*args)
    def setXRadius(*args): return _ui.ellipse_setXRadius(*args)
    def setYRadius(*args): return _ui.ellipse_setYRadius(*args)
    def xRadius(*args): return _ui.ellipse_xRadius(*args)
    def yRadius(*args): return _ui.ellipse_yRadius(*args)
    def setNumChords(*args): return _ui.ellipse_setNumChords(*args)
    def numChords(*args): return _ui.ellipse_numChords(*args)
    def bBox(*args): return _ui.ellipse_bBox(*args)
    def objType(*args): return _ui.ellipse_objType(*args)
    def objName(*args): return _ui.ellipse_objName(*args)
    def area(*args): return _ui.ellipse_area(*args)
    def perimeter(*args): return _ui.ellipse_perimeter(*args)
    def createPolygon(*args): return _ui.ellipse_createPolygon(*args)
    def ptlist(*args): return _ui.ellipse_ptlist(*args)
    def nPoints(*args): return _ui.ellipse_nPoints(*args)
    def offGrid(*args): return _ui.ellipse_offGrid(*args)
    def manhattan(*args): return _ui.ellipse_manhattan(*args)
    def transform(*args): return _ui.ellipse_transform(*args)
    def Move(*args): return _ui.ellipse_Move(*args)
    def Copy(*args): return _ui.ellipse_Copy(*args)
    def Flatten(*args): return _ui.ellipse_Flatten(*args)
    def Stretch(*args): return _ui.ellipse_Stretch(*args)
    def bias(*args): return _ui.ellipse_bias(*args)
    def scale(*args): return _ui.ellipse_scale(*args)

class ellipsePtr(ellipse):
    def __init__(self, this):
        _swig_setattr(self, ellipse, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ellipse, 'thisown', 0)
        self.__class__ = ellipse
_ui.ellipse_swigregister(ellipsePtr)

class arc(ellipse):
    __swig_setmethods__ = {}
    for _s in [ellipse]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, arc, name, value)
    __swig_getmethods__ = {}
    for _s in [ellipse]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, arc, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::arc instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, arc, 'this', _ui.new_arc(*args))
        _swig_setattr(self, arc, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_arc):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setStartAngle(*args): return _ui.arc_setStartAngle(*args)
    def setSpanAngle(*args): return _ui.arc_setSpanAngle(*args)
    def startAngle(*args): return _ui.arc_startAngle(*args)
    def spanAngle(*args): return _ui.arc_spanAngle(*args)
    def objType(*args): return _ui.arc_objType(*args)
    def objName(*args): return _ui.arc_objName(*args)
    def area(*args): return _ui.arc_area(*args)
    def perimeter(*args): return _ui.arc_perimeter(*args)
    def createPolygon(*args): return _ui.arc_createPolygon(*args)
    def offGrid(*args): return _ui.arc_offGrid(*args)
    def manhattan(*args): return _ui.arc_manhattan(*args)
    def transform(*args): return _ui.arc_transform(*args)
    def Move(*args): return _ui.arc_Move(*args)
    def Copy(*args): return _ui.arc_Copy(*args)
    def Flatten(*args): return _ui.arc_Flatten(*args)
    def Stretch(*args): return _ui.arc_Stretch(*args)

class arcPtr(arc):
    def __init__(self, this):
        _swig_setattr(self, arc, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, arc, 'thisown', 0)
        self.__class__ = arc
_ui.arc_swigregister(arcPtr)

class array(inst):
    __swig_setmethods__ = {}
    for _s in [inst]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, array, name, value)
    __swig_getmethods__ = {}
    for _s in [inst]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, array, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::array instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, array, 'this', _ui.new_array(*args))
        _swig_setattr(self, array, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_array):
        try:
            if self.thisown: destroy(self)
        except: pass

    def numRows(*args): return _ui.array_numRows(*args)
    def numCols(*args): return _ui.array_numCols(*args)
    def rowSpacing(*args): return _ui.array_rowSpacing(*args)
    def rowXSpacing(*args): return _ui.array_rowXSpacing(*args)
    def rowYSpacing(*args): return _ui.array_rowYSpacing(*args)
    def colSpacing(*args): return _ui.array_colSpacing(*args)
    def colXSpacing(*args): return _ui.array_colXSpacing(*args)
    def colYSpacing(*args): return _ui.array_colYSpacing(*args)
    def bBox(*args): return _ui.array_bBox(*args)
    def qBox(*args): return _ui.array_qBox(*args)
    def objType(*args): return _ui.array_objType(*args)
    def objName(*args): return _ui.array_objName(*args)
    def scale(*args): return _ui.array_scale(*args)
    def Move(*args): return _ui.array_Move(*args)
    def Copy(*args): return _ui.array_Copy(*args)
    def Flatten(*args): return _ui.array_Flatten(*args)
    def offGrid(*args): return _ui.array_offGrid(*args)

class arrayPtr(array):
    def __init__(self, this):
        _swig_setattr(self, array, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, array, 'thisown', 0)
        self.__class__ = array
_ui.array_swigregister(arrayPtr)

class cell(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, cell, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, cell, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::cell instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, cell, 'this', _ui.new_cell(*args))
        _swig_setattr(self, cell, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_cell):
        try:
            if self.thisown: destroy(self)
        except: pass

    def cellViews(*args): return _ui.cell_cellViews(*args)
    def name(*args): return _ui.cell_name(*args)
    def addCellView(*args): return _ui.cell_addCellView(*args)
    def dbFindCellViewByView(*args): return _ui.cell_dbFindCellViewByView(*args)
    def objType(*args): return _ui.cell_objType(*args)
    def objName(*args): return _ui.cell_objName(*args)
    def getCellViews(*args): return _ui.cell_getCellViews(*args)

class cellPtr(cell):
    def __init__(self, this):
        _swig_setattr(self, cell, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cell, 'thisown', 0)
        self.__class__ = cell
_ui.cell_swigregister(cellPtr)

microns = _ui.microns
inches = _ui.inches
class cellView(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, cellView, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, cellView, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::cellView instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, cellView, 'this', _ui.new_cellView(*args))
        _swig_setattr(self, cellView, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_cellView):
        try:
            if self.thisown: destroy(self)
        except: pass

    def dbCreateRect(*args): return _ui.cellView_dbCreateRect(*args)
    def dbCreatePolygon(*args): return _ui.cellView_dbCreatePolygon(*args)
    def dbCreateHole(*args): return _ui.cellView_dbCreateHole(*args)
    def dbCreateInst(*args): return _ui.cellView_dbCreateInst(*args)
    def dbFindInstByName(*args): return _ui.cellView_dbFindInstByName(*args)
    def dbCreateArray(*args): return _ui.cellView_dbCreateArray(*args)
    def dbCreateLabel(*args): return _ui.cellView_dbCreateLabel(*args)
    def dbCreatePath(*args): return _ui.cellView_dbCreatePath(*args)
    def dbCreateMPP(*args): return _ui.cellView_dbCreateMPP(*args)
    def dbCreateHSeg(*args): return _ui.cellView_dbCreateHSeg(*args)
    def dbCreateVSeg(*args): return _ui.cellView_dbCreateVSeg(*args)
    def dbCreateEllipse(*args): return _ui.cellView_dbCreateEllipse(*args)
    def dbCreateCircle(*args): return _ui.cellView_dbCreateCircle(*args)
    def dbCreateArc(*args): return _ui.cellView_dbCreateArc(*args)
    def dbCreateLine(*args): return _ui.cellView_dbCreateLine(*args)
    def dbCreateNet(*args): return _ui.cellView_dbCreateNet(*args)
    def dbCreatePin(*args): return _ui.cellView_dbCreatePin(*args)
    def dbFindPinByName(*args): return _ui.cellView_dbFindPinByName(*args)
    def dbCreatePort(*args): return _ui.cellView_dbCreatePort(*args)
    def dbCreateViaInst(*args): return _ui.cellView_dbCreateViaInst(*args)
    def dbFindNetByName(*args): return _ui.cellView_dbFindNetByName(*args)
    def dbGetOverlaps(*args): return _ui.cellView_dbGetOverlaps(*args)
    def dbGetHierOverlaps(*args): return _ui.cellView_dbGetHierOverlaps(*args)
    def dbFindHierOverlaps(*args): return _ui.cellView_dbFindHierOverlaps(*args)
    def dbCreateLpp(*args): return _ui.cellView_dbCreateLpp(*args)
    def dbDeleteObj(*args): return _ui.cellView_dbDeleteObj(*args)
    def dbMergeNet(*args): return _ui.cellView_dbMergeNet(*args)
    def dbCreatePCell(*args): return _ui.cellView_dbCreatePCell(*args)
    def dbCreatePCellInst(*args): return _ui.cellView_dbCreatePCellInst(*args)
    def dbUpdatePCell(*args): return _ui.cellView_dbUpdatePCell(*args)
    def setPcell(*args): return _ui.cellView_setPcell(*args)
    def isPcell(*args): return _ui.cellView_isPcell(*args)
    def setSubMaster(*args): return _ui.cellView_setSubMaster(*args)
    def isSubMaster(*args): return _ui.cellView_isSubMaster(*args)
    def setPCellName(*args): return _ui.cellView_setPCellName(*args)
    def getPCellName(*args): return _ui.cellView_getPCellName(*args)
    def setPCellFile(*args): return _ui.cellView_setPCellFile(*args)
    def getPCellFile(*args): return _ui.cellView_getPCellFile(*args)
    def bBox(*args): return _ui.cellView_bBox(*args)
    def qBox(*args): return _ui.cellView_qBox(*args)
    def left(*args): return _ui.cellView_left(*args)
    def right(*args): return _ui.cellView_right(*args)
    def bottom(*args): return _ui.cellView_bottom(*args)
    def top(*args): return _ui.cellView_top(*args)
    def getWidth(*args): return _ui.cellView_getWidth(*args)
    def getHeight(*args): return _ui.cellView_getHeight(*args)
    def clearBbox(*args): return _ui.cellView_clearBbox(*args)
    def updateBbox(*args): return _ui.cellView_updateBbox(*args)
    def getBoundary(*args): return _ui.cellView_getBoundary(*args)
    def objType(*args): return _ui.cellView_objType(*args)
    def objName(*args): return _ui.cellView_objName(*args)
    def getNumShapes(*args): return _ui.cellView_getNumShapes(*args)
    def getInstHashTable(*args): return _ui.cellView_getInstHashTable(*args)
    def getNumInsts(*args): return _ui.cellView_getNumInsts(*args)
    def getNumViaInsts(*args): return _ui.cellView_getNumViaInsts(*args)
    def getNetHashTable(*args): return _ui.cellView_getNetHashTable(*args)
    def getNumNets(*args): return _ui.cellView_getNumNets(*args)
    def getPinHashTable(*args): return _ui.cellView_getPinHashTable(*args)
    def getNumPins(*args): return _ui.cellView_getNumPins(*args)
    def libName(*args): return _ui.cellView_libName(*args)
    def cellName(*args): return _ui.cellView_cellName(*args)
    def viewName(*args): return _ui.cellView_viewName(*args)
    def getLppList(*args): return _ui.cellView_getLppList(*args)
    def getLpp(*args): return _ui.cellView_getLpp(*args)
    def getNumLpps(*args): return _ui.cellView_getNumLpps(*args)
    def setEditable(*args): return _ui.cellView_setEditable(*args)
    def editable(*args): return _ui.cellView_editable(*args)
    def setDirty(*args): return _ui.cellView_setDirty(*args)
    def isDirty(*args): return _ui.cellView_isDirty(*args)
    def isEdited(*args): return _ui.cellView_isEdited(*args)
    def setEdited(*args): return _ui.cellView_setEdited(*args)
    def lib(*args): return _ui.cellView_lib(*args)
    def createDate(*args): return _ui.cellView_createDate(*args)
    def modDate(*args): return _ui.cellView_modDate(*args)
    def incModCount(*args): return _ui.cellView_incModCount(*args)
    def decModCount(*args): return _ui.cellView_decModCount(*args)
    def modCount(*args): return _ui.cellView_modCount(*args)
    def getNearestObj(*args): return _ui.cellView_getNearestObj(*args)
    def getNearestSeg(*args): return _ui.cellView_getNearestSeg(*args)
    def getNearestVertex(*args): return _ui.cellView_getNearestVertex(*args)
    def optimiseTrees(*args): return _ui.cellView_optimiseTrees(*args)
    def isOptimised(*args): return _ui.cellView_isOptimised(*args)
    def update(*args): return _ui.cellView_update(*args)
    def roundCorners(*args): return _ui.cellView_roundCorners(*args)
    def dbGetNLPPropList(*args): return _ui.cellView_dbGetNLPPropList(*args)
    def dbuPerUU(*args): return _ui.cellView_dbuPerUU(*args)
    def dbu(*args): return _ui.cellView_dbu(*args)
    def userUnits(*args): return _ui.cellView_userUnits(*args)
    def units(*args): return _ui.cellView_units(*args)
    def getInsts(*args): return _ui.cellView_getInsts(*args)
    def getNets(*args): return _ui.cellView_getNets(*args)
    def getPins(*args): return _ui.cellView_getPins(*args)
    def getLpps(*args): return _ui.cellView_getLpps(*args)
    def getOverlaps(*args): return _ui.cellView_getOverlaps(*args)
    def getHierOverlaps(*args): return _ui.cellView_getHierOverlaps(*args)
    def getShapes(*args): return _ui.cellView_getShapes(*args)

class cellViewPtr(cellView):
    def __init__(self, this):
        _swig_setattr(self, cellView, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cellView, 'thisown', 0)
        self.__class__ = cellView
_ui.cellView_swigregister(cellViewPtr)

class optimiseTreeTask(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, optimiseTreeTask, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, optimiseTreeTask, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ optimiseTreeTask instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, optimiseTreeTask, 'this', _ui.new_optimiseTreeTask(*args))
        _swig_setattr(self, optimiseTreeTask, 'thisown', 1)
    def run(*args): return _ui.optimiseTreeTask_run(*args)
    def __del__(self, destroy=_ui.delete_optimiseTreeTask):
        try:
            if self.thisown: destroy(self)
        except: pass


class optimiseTreeTaskPtr(optimiseTreeTask):
    def __init__(self, this):
        _swig_setattr(self, optimiseTreeTask, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, optimiseTreeTask, 'thisown', 0)
        self.__class__ = optimiseTreeTask
_ui.optimiseTreeTask_swigregister(optimiseTreeTaskPtr)

class instIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, instIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, instIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ instIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, instIterator, 'this', _ui.new_instIterator(*args))
        _swig_setattr(self, instIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_instIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.instIterator___ref__(*args)
    def value(*args): return _ui.instIterator_value(*args)
    def next(*args): return _ui.instIterator_next(*args)
    def end(*args): return _ui.instIterator_end(*args)

class instIteratorPtr(instIterator):
    def __init__(self, this):
        _swig_setattr(self, instIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, instIterator, 'thisown', 0)
        self.__class__ = instIterator
_ui.instIterator_swigregister(instIteratorPtr)

class netIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, netIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, netIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ netIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, netIterator, 'this', _ui.new_netIterator(*args))
        _swig_setattr(self, netIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_netIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.netIterator___ref__(*args)
    def value(*args): return _ui.netIterator_value(*args)
    def next(*args): return _ui.netIterator_next(*args)
    def end(*args): return _ui.netIterator_end(*args)

class netIteratorPtr(netIterator):
    def __init__(self, this):
        _swig_setattr(self, netIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, netIterator, 'thisown', 0)
        self.__class__ = netIterator
_ui.netIterator_swigregister(netIteratorPtr)

class pinIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pinIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pinIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ pinIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pinIterator, 'this', _ui.new_pinIterator(*args))
        _swig_setattr(self, pinIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pinIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.pinIterator___ref__(*args)
    def value(*args): return _ui.pinIterator_value(*args)
    def next(*args): return _ui.pinIterator_next(*args)
    def end(*args): return _ui.pinIterator_end(*args)

class pinIteratorPtr(pinIterator):
    def __init__(self, this):
        _swig_setattr(self, pinIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pinIterator, 'thisown', 0)
        self.__class__ = pinIterator
_ui.pinIterator_swigregister(pinIteratorPtr)

class lppIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lppIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lppIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ lppIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, lppIterator, 'this', _ui.new_lppIterator(*args))
        _swig_setattr(self, lppIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_lppIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.lppIterator___ref__(*args)
    def value(*args): return _ui.lppIterator_value(*args)
    def next(*args): return _ui.lppIterator_next(*args)
    def end(*args): return _ui.lppIterator_end(*args)

class lppIteratorPtr(lppIterator):
    def __init__(self, this):
        _swig_setattr(self, lppIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, lppIterator, 'thisown', 0)
        self.__class__ = lppIterator
_ui.lppIterator_swigregister(lppIteratorPtr)

class dbObjIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dbObjIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dbObjIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, dbObjIterator, 'this', _ui.new_dbObjIterator(*args))
        _swig_setattr(self, dbObjIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_dbObjIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.dbObjIterator___ref__(*args)
    def value(*args): return _ui.dbObjIterator_value(*args)
    def next(*args): return _ui.dbObjIterator_next(*args)
    def end(*args): return _ui.dbObjIterator_end(*args)

class dbObjIteratorPtr(dbObjIterator):
    def __init__(self, this):
        _swig_setattr(self, dbObjIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dbObjIterator, 'thisown', 0)
        self.__class__ = dbObjIterator
_ui.dbObjIterator_swigregister(dbObjIteratorPtr)

class shapeIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shapeIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shapeIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ shapeIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, shapeIterator, 'this', _ui.new_shapeIterator(*args))
        _swig_setattr(self, shapeIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_shapeIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.shapeIterator___ref__(*args)
    def value(*args): return _ui.shapeIterator_value(*args)
    def next(*args): return _ui.shapeIterator_next(*args)
    def end(*args): return _ui.shapeIterator_end(*args)

class shapeIteratorPtr(shapeIterator):
    def __init__(self, this):
        _swig_setattr(self, shapeIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, shapeIterator, 'thisown', 0)
        self.__class__ = shapeIterator
_ui.shapeIterator_swigregister(shapeIteratorPtr)

class Edge(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edge, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edge, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::Edge instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Edge, 'this', _ui.new_Edge(*args))
        _swig_setattr(self, Edge, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_Edge):
        try:
            if self.thisown: destroy(self)
        except: pass

    def getP0(*args): return _ui.Edge_getP0(*args)
    def getP1(*args): return _ui.Edge_getP1(*args)
    def setP0(*args): return _ui.Edge_setP0(*args)
    def setP1(*args): return _ui.Edge_setP1(*args)
    def offset(*args): return _ui.Edge_offset(*args)
    def __eq__(*args): return _ui.Edge___eq__(*args)
    def __ne__(*args): return _ui.Edge___ne__(*args)
    def length(*args): return _ui.Edge_length(*args)
    def isHorizontal(*args): return _ui.Edge_isHorizontal(*args)
    def isVertical(*args): return _ui.Edge_isVertical(*args)
    def isOrthogonal(*args): return _ui.Edge_isOrthogonal(*args)
    def isDiagonal(*args): return _ui.Edge_isDiagonal(*args)
    def deltaX(*args): return _ui.Edge_deltaX(*args)
    def deltaY(*args): return _ui.Edge_deltaY(*args)
    def contains(*args): return _ui.Edge_contains(*args)
    def crosses(*args): return _ui.Edge_crosses(*args)
    def pointToEdge(*args): return _ui.Edge_pointToEdge(*args)
    def distance(*args): return _ui.Edge_distance(*args)
    def intersects(*args): return _ui.Edge_intersects(*args)
    def intersectsAt(*args): return _ui.Edge_intersectsAt(*args)
    def isColinear(*args): return _ui.Edge_isColinear(*args)
    def parallel(*args): return _ui.Edge_parallel(*args)
    def left(*args): return _ui.Edge_left(*args)
    def nearestPoint(*args): return _ui.Edge_nearestPoint(*args)
    def normalTo(*args): return _ui.Edge_normalTo(*args)
    def projects(*args): return _ui.Edge_projects(*args)

class EdgePtr(Edge):
    def __init__(self, this):
        _swig_setattr(self, Edge, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Edge, 'thisown', 0)
        self.__class__ = Edge
_ui.Edge_swigregister(EdgePtr)

TRUNCATE = _ui.TRUNCATE
ROUNDED = _ui.ROUNDED
EXTEND = _ui.EXTEND
VAREXTEND = _ui.VAREXTEND
OCTAGONAL = _ui.OCTAGONAL
class HSeg(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, HSeg, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, HSeg, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::HSeg instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, HSeg, 'this', _ui.new_HSeg(*args))
        _swig_setattr(self, HSeg, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_HSeg):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.HSeg_left(*args)
    def right(*args): return _ui.HSeg_right(*args)
    def bottom(*args): return _ui.HSeg_bottom(*args)
    def top(*args): return _ui.HSeg_top(*args)
    def coord(*args): return _ui.HSeg_coord(*args)
    def offGrid(*args): return _ui.HSeg_offGrid(*args)
    def manhattan(*args): return _ui.HSeg_manhattan(*args)
    def setStyle(*args): return _ui.HSeg_setStyle(*args)
    def getStyle(*args): return _ui.HSeg_getStyle(*args)
    def setType(*args): return _ui.HSeg_setType(*args)
    def getType(*args): return _ui.HSeg_getType(*args)
    def getTypeStr(*args): return _ui.HSeg_getTypeStr(*args)
    def setShape(*args): return _ui.HSeg_setShape(*args)
    def getShape(*args): return _ui.HSeg_getShape(*args)
    def getShapeStr(*args): return _ui.HSeg_getShapeStr(*args)
    def orient(*args): return _ui.HSeg_orient(*args)
    def getOrientStr(*args): return _ui.HSeg_getOrientStr(*args)
    def setSpecial(*args): return _ui.HSeg_setSpecial(*args)
    def isSpecial(*args): return _ui.HSeg_isSpecial(*args)
    def setPoints(*args): return _ui.HSeg_setPoints(*args)
    def setNet(*args): return _ui.HSeg_setNet(*args)
    def getNet(*args): return _ui.HSeg_getNet(*args)
    def setIndex(*args): return _ui.HSeg_setIndex(*args)
    def index(*args): return _ui.HSeg_index(*args)
    def bBox(*args): return _ui.HSeg_bBox(*args)
    def qBox(*args): return _ui.HSeg_qBox(*args)
    def objType(*args): return _ui.HSeg_objType(*args)
    def objName(*args): return _ui.HSeg_objName(*args)
    def layer(*args): return _ui.HSeg_layer(*args)
    def width(*args): return _ui.HSeg_width(*args)
    def area(*args): return _ui.HSeg_area(*args)
    def perimeter(*args): return _ui.HSeg_perimeter(*args)
    def getFirstVertex(*args): return _ui.HSeg_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.HSeg_getLastVertex(*args)
    def extent(*args): return _ui.HSeg_extent(*args)
    def setExtent(*args): return _ui.HSeg_setExtent(*args)
    def origin(*args): return _ui.HSeg_origin(*args)
    def setOrigin(*args): return _ui.HSeg_setOrigin(*args)
    def ptInPoly(*args): return _ui.HSeg_ptInPoly(*args)
    def Move(*args): return _ui.HSeg_Move(*args)
    def Copy(*args): return _ui.HSeg_Copy(*args)
    def Flatten(*args): return _ui.HSeg_Flatten(*args)
    def getNearestEdge(*args): return _ui.HSeg_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.HSeg_getNearestVertex(*args)
    def getSegsInRect(*args): return _ui.HSeg_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.HSeg_getVertsInRect(*args)
    def transform(*args): return _ui.HSeg_transform(*args)
    def getNetName(*args): return _ui.HSeg_getNetName(*args)
    def length(*args): return _ui.HSeg_length(*args)
    def ptlist(*args): return _ui.HSeg_ptlist(*args)
    def nPoints(*args): return _ui.HSeg_nPoints(*args)
    def bias(*args): return _ui.HSeg_bias(*args)
    def scale(*args): return _ui.HSeg_scale(*args)

class HSegPtr(HSeg):
    def __init__(self, this):
        _swig_setattr(self, HSeg, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, HSeg, 'thisown', 0)
        self.__class__ = HSeg
_ui.HSeg_swigregister(HSegPtr)

class instPin(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, instPin, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, instPin, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::instPin instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, instPin, 'this', _ui.new_instPin(*args))
        _swig_setattr(self, instPin, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_instPin):
        try:
            if self.thisown: destroy(self)
        except: pass

    def objType(*args): return _ui.instPin_objType(*args)
    def objName(*args): return _ui.instPin_objName(*args)
    def setInst(*args): return _ui.instPin_setInst(*args)
    def getInst(*args): return _ui.instPin_getInst(*args)
    def setName(*args): return _ui.instPin_setName(*args)
    def getName(*args): return _ui.instPin_getName(*args)
    def setNet(*args): return _ui.instPin_setNet(*args)
    def getNet(*args): return _ui.instPin_getNet(*args)
    def setPin(*args): return _ui.instPin_setPin(*args)
    def getPin(*args): return _ui.instPin_getPin(*args)
    def setSpecial(*args): return _ui.instPin_setSpecial(*args)
    def isSpecial(*args): return _ui.instPin_isSpecial(*args)
    def setBound(*args): return _ui.instPin_setBound(*args)
    def isBound(*args): return _ui.instPin_isBound(*args)
    def setWired(*args): return _ui.instPin_setWired(*args)
    def isWired(*args): return _ui.instPin_isWired(*args)
    def getPortLoc(*args): return _ui.instPin_getPortLoc(*args)
    def getNumPorts(*args): return _ui.instPin_getNumPorts(*args)
    def isSupplyPin(*args): return _ui.instPin_isSupplyPin(*args)

class instPinPtr(instPin):
    def __init__(self, this):
        _swig_setattr(self, instPin, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, instPin, 'thisown', 0)
        self.__class__ = instPin
_ui.instPin_swigregister(instPinPtr)

normal = _ui.normal
cdlLabel = _ui.cdlLabel
pyLabel = _ui.pyLabel
maskLabel = _ui.maskLabel
instLabel = _ui.instLabel
pinLabel = _ui.pinLabel
deviceLabel = _ui.deviceLabel
deviceAnnotate = _ui.deviceAnnotate
class label(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, label, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, label, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::label instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, label, 'this', _ui.new_label(*args))
        _swig_setattr(self, label, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_label):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.label_left(*args)
    def right(*args): return _ui.label_right(*args)
    def bottom(*args): return _ui.label_bottom(*args)
    def top(*args): return _ui.label_top(*args)
    def offGrid(*args): return _ui.label_offGrid(*args)
    def manhattan(*args): return _ui.label_manhattan(*args)
    def theLabel(*args): return _ui.label_theLabel(*args)
    def height(*args): return _ui.label_height(*args)
    def width(*args): return _ui.label_width(*args)
    def orient(*args): return _ui.label_orient(*args)
    def origin(*args): return _ui.label_origin(*args)
    def type(*args): return _ui.label_type(*args)
    def align(*args): return _ui.label_align(*args)
    def overline(*args): return _ui.label_overline(*args)
    def underline(*args): return _ui.label_underline(*args)
    def strikethru(*args): return _ui.label_strikethru(*args)
    def flags(*args): return _ui.label_flags(*args)
    def bBox(*args): return _ui.label_bBox(*args)
    def qBox(*args): return _ui.label_qBox(*args)
    def textBox(*args): return _ui.label_textBox(*args)
    def objType(*args): return _ui.label_objType(*args)
    def objName(*args): return _ui.label_objName(*args)
    def nPoints(*args): return _ui.label_nPoints(*args)
    def ptlist(*args): return _ui.label_ptlist(*args)
    def getNearestEdge(*args): return _ui.label_getNearestEdge(*args)
    def transform(*args): return _ui.label_transform(*args)
    def Move(*args): return _ui.label_Move(*args)
    def Copy(*args): return _ui.label_Copy(*args)
    def Flatten(*args): return _ui.label_Flatten(*args)
    def Stretch(*args): return _ui.label_Stretch(*args)
    def bias(*args): return _ui.label_bias(*args)
    def scale(*args): return _ui.label_scale(*args)
    def getSegPts(*args): return _ui.label_getSegPts(*args)
    def getTextOrient(*args): return _ui.label_getTextOrient(*args)
    def getPresentationOffset(*args): return _ui.label_getPresentationOffset(*args)
    def length(*args): return _ui.label_length(*args)

class labelPtr(label):
    def __init__(self, this):
        _swig_setattr(self, label, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, label, 'thisown', 0)
        self.__class__ = label
_ui.label_swigregister(labelPtr)

F_HOLLOW = _ui.F_HOLLOW
F_SOLID = _ui.F_SOLID
F_STIPPLE = _ui.F_STIPPLE
F_CROSSED = _ui.F_CROSSED
F_UNKNOWN = _ui.F_UNKNOWN
T_CUT = _ui.T_CUT
T_MASTERSLICE = _ui.T_MASTERSLICE
T_ROUTING = _ui.T_ROUTING
T_BLOCKAGE = _ui.T_BLOCKAGE
T_PIN = _ui.T_PIN
T_OVERLAP = _ui.T_OVERLAP
T_WELL = _ui.T_WELL
T_DIFFUSION = _ui.T_DIFFUSION
T_POLY = _ui.T_POLY
T_IMPLANT = _ui.T_IMPLANT
T_NONE = _ui.T_NONE
LAYER_HORIZONTAL = _ui.LAYER_HORIZONTAL
LAYER_VERTICAL = _ui.LAYER_VERTICAL
class techRule(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, techRule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, techRule, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ techRule instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, techRule, 'this', _ui.new_techRule(*args))
        _swig_setattr(self, techRule, 'thisown', 1)
    def setOtherLayer(*args): return _ui.techRule_setOtherLayer(*args)
    def otherLayer(*args): return _ui.techRule_otherLayer(*args)
    def setValue(*args): return _ui.techRule_setValue(*args)
    def value(*args): return _ui.techRule_value(*args)
    def setReversed(*args): return _ui.techRule_setReversed(*args)
    def reversed(*args): return _ui.techRule_reversed(*args)
    def __del__(self, destroy=_ui.delete_techRule):
        try:
            if self.thisown: destroy(self)
        except: pass


class techRulePtr(techRule):
    def __init__(self, this):
        _swig_setattr(self, techRule, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, techRule, 'thisown', 0)
        self.__class__ = techRule
_ui.techRule_swigregister(techRulePtr)

class Layer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Layer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ Layer instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Layer, 'this', _ui.new_Layer(*args))
        _swig_setattr(self, Layer, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_Layer):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.Layer_clear(*args)
    def twoLayerRules(*args): return _ui.Layer_twoLayerRules(*args)
    def addTwoLayerRule(*args): return _ui.Layer_addTwoLayerRule(*args)
    def enclosureRules(*args): return _ui.Layer_enclosureRules(*args)
    def addEnclosureRule(*args): return _ui.Layer_addEnclosureRule(*args)
    def overlapRules(*args): return _ui.Layer_overlapRules(*args)
    def addOverlapRule(*args): return _ui.Layer_addOverlapRule(*args)
    __swig_setmethods__["m_layerNum"] = _ui.Layer_m_layerNum_set
    __swig_getmethods__["m_layerNum"] = _ui.Layer_m_layerNum_get
    if _newclass:m_layerNum = property(_ui.Layer_m_layerNum_get, _ui.Layer_m_layerNum_set)
    __swig_setmethods__["m_pLayerName"] = _ui.Layer_m_pLayerName_set
    __swig_getmethods__["m_pLayerName"] = _ui.Layer_m_pLayerName_get
    if _newclass:m_pLayerName = property(_ui.Layer_m_pLayerName_get, _ui.Layer_m_pLayerName_set)
    __swig_setmethods__["m_pPurpose"] = _ui.Layer_m_pPurpose_set
    __swig_getmethods__["m_pPurpose"] = _ui.Layer_m_pPurpose_get
    if _newclass:m_pPurpose = property(_ui.Layer_m_pPurpose_get, _ui.Layer_m_pPurpose_set)
    __swig_setmethods__["m_gdsLayer"] = _ui.Layer_m_gdsLayer_set
    __swig_getmethods__["m_gdsLayer"] = _ui.Layer_m_gdsLayer_get
    if _newclass:m_gdsLayer = property(_ui.Layer_m_gdsLayer_get, _ui.Layer_m_gdsLayer_set)
    __swig_setmethods__["m_gdsDataType"] = _ui.Layer_m_gdsDataType_set
    __swig_getmethods__["m_gdsDataType"] = _ui.Layer_m_gdsDataType_get
    if _newclass:m_gdsDataType = property(_ui.Layer_m_gdsDataType_get, _ui.Layer_m_gdsDataType_set)
    __swig_setmethods__["m_argb"] = _ui.Layer_m_argb_set
    __swig_getmethods__["m_argb"] = _ui.Layer_m_argb_get
    if _newclass:m_argb = property(_ui.Layer_m_argb_get, _ui.Layer_m_argb_set)
    __swig_setmethods__["m_lpBits"] = _ui.Layer_m_lpBits_set
    __swig_getmethods__["m_lpBits"] = _ui.Layer_m_lpBits_get
    if _newclass:m_lpBits = property(_ui.Layer_m_lpBits_get, _ui.Layer_m_lpBits_set)
    __swig_setmethods__["m_fillType"] = _ui.Layer_m_fillType_set
    __swig_getmethods__["m_fillType"] = _ui.Layer_m_fillType_get
    if _newclass:m_fillType = property(_ui.Layer_m_fillType_get, _ui.Layer_m_fillType_set)
    __swig_setmethods__["m_lineStyle"] = _ui.Layer_m_lineStyle_set
    __swig_getmethods__["m_lineStyle"] = _ui.Layer_m_lineStyle_get
    if _newclass:m_lineStyle = property(_ui.Layer_m_lineStyle_get, _ui.Layer_m_lineStyle_set)
    __swig_setmethods__["m_layerType"] = _ui.Layer_m_layerType_set
    __swig_getmethods__["m_layerType"] = _ui.Layer_m_layerType_get
    if _newclass:m_layerType = property(_ui.Layer_m_layerType_get, _ui.Layer_m_layerType_set)
    __swig_setmethods__["m_lineWidth"] = _ui.Layer_m_lineWidth_set
    __swig_getmethods__["m_lineWidth"] = _ui.Layer_m_lineWidth_get
    if _newclass:m_lineWidth = property(_ui.Layer_m_lineWidth_get, _ui.Layer_m_lineWidth_set)
    __swig_setmethods__["m_visible"] = _ui.Layer_m_visible_set
    __swig_getmethods__["m_visible"] = _ui.Layer_m_visible_get
    if _newclass:m_visible = property(_ui.Layer_m_visible_get, _ui.Layer_m_visible_set)
    __swig_setmethods__["m_selectable"] = _ui.Layer_m_selectable_set
    __swig_getmethods__["m_selectable"] = _ui.Layer_m_selectable_get
    if _newclass:m_selectable = property(_ui.Layer_m_selectable_get, _ui.Layer_m_selectable_set)
    __swig_setmethods__["m_isUsed"] = _ui.Layer_m_isUsed_set
    __swig_getmethods__["m_isUsed"] = _ui.Layer_m_isUsed_get
    if _newclass:m_isUsed = property(_ui.Layer_m_isUsed_get, _ui.Layer_m_isUsed_set)
    __swig_setmethods__["m_isActive"] = _ui.Layer_m_isActive_set
    __swig_getmethods__["m_isActive"] = _ui.Layer_m_isActive_get
    if _newclass:m_isActive = property(_ui.Layer_m_isActive_get, _ui.Layer_m_isActive_set)
    __swig_setmethods__["m_isValid"] = _ui.Layer_m_isValid_set
    __swig_getmethods__["m_isValid"] = _ui.Layer_m_isValid_get
    if _newclass:m_isValid = property(_ui.Layer_m_isValid_get, _ui.Layer_m_isValid_set)
    __swig_setmethods__["m_pFillStyle"] = _ui.Layer_m_pFillStyle_set
    __swig_getmethods__["m_pFillStyle"] = _ui.Layer_m_pFillStyle_get
    if _newclass:m_pFillStyle = property(_ui.Layer_m_pFillStyle_get, _ui.Layer_m_pFillStyle_set)
    __swig_setmethods__["m_pLineStyle"] = _ui.Layer_m_pLineStyle_set
    __swig_getmethods__["m_pLineStyle"] = _ui.Layer_m_pLineStyle_get
    if _newclass:m_pLineStyle = property(_ui.Layer_m_pLineStyle_get, _ui.Layer_m_pLineStyle_set)
    __swig_setmethods__["m_LayerWidth"] = _ui.Layer_m_LayerWidth_set
    __swig_getmethods__["m_LayerWidth"] = _ui.Layer_m_LayerWidth_get
    if _newclass:m_LayerWidth = property(_ui.Layer_m_LayerWidth_get, _ui.Layer_m_LayerWidth_set)
    __swig_setmethods__["m_LayerSpace"] = _ui.Layer_m_LayerSpace_set
    __swig_getmethods__["m_LayerSpace"] = _ui.Layer_m_LayerSpace_get
    if _newclass:m_LayerSpace = property(_ui.Layer_m_LayerSpace_get, _ui.Layer_m_LayerSpace_set)
    __swig_setmethods__["m_TwoLayerSpace"] = _ui.Layer_m_TwoLayerSpace_set
    __swig_getmethods__["m_TwoLayerSpace"] = _ui.Layer_m_TwoLayerSpace_get
    if _newclass:m_TwoLayerSpace = property(_ui.Layer_m_TwoLayerSpace_get, _ui.Layer_m_TwoLayerSpace_set)
    __swig_setmethods__["m_LayerArea"] = _ui.Layer_m_LayerArea_set
    __swig_getmethods__["m_LayerArea"] = _ui.Layer_m_LayerArea_get
    if _newclass:m_LayerArea = property(_ui.Layer_m_LayerArea_get, _ui.Layer_m_LayerArea_set)
    __swig_setmethods__["m_LayerEnc"] = _ui.Layer_m_LayerEnc_set
    __swig_getmethods__["m_LayerEnc"] = _ui.Layer_m_LayerEnc_get
    if _newclass:m_LayerEnc = property(_ui.Layer_m_LayerEnc_get, _ui.Layer_m_LayerEnc_set)
    __swig_setmethods__["m_LayerOvlp"] = _ui.Layer_m_LayerOvlp_set
    __swig_getmethods__["m_LayerOvlp"] = _ui.Layer_m_LayerOvlp_get
    if _newclass:m_LayerOvlp = property(_ui.Layer_m_LayerOvlp_get, _ui.Layer_m_LayerOvlp_set)
    __swig_setmethods__["m_pitch"] = _ui.Layer_m_pitch_set
    __swig_getmethods__["m_pitch"] = _ui.Layer_m_pitch_get
    if _newclass:m_pitch = property(_ui.Layer_m_pitch_get, _ui.Layer_m_pitch_set)
    __swig_setmethods__["m_offset"] = _ui.Layer_m_offset_set
    __swig_getmethods__["m_offset"] = _ui.Layer_m_offset_get
    if _newclass:m_offset = property(_ui.Layer_m_offset_get, _ui.Layer_m_offset_set)
    __swig_setmethods__["m_direction"] = _ui.Layer_m_direction_set
    __swig_getmethods__["m_direction"] = _ui.Layer_m_direction_get
    if _newclass:m_direction = property(_ui.Layer_m_direction_get, _ui.Layer_m_direction_set)
    __swig_setmethods__["m_resistance"] = _ui.Layer_m_resistance_set
    __swig_getmethods__["m_resistance"] = _ui.Layer_m_resistance_get
    if _newclass:m_resistance = property(_ui.Layer_m_resistance_get, _ui.Layer_m_resistance_set)
    __swig_setmethods__["m_areaCap"] = _ui.Layer_m_areaCap_set
    __swig_getmethods__["m_areaCap"] = _ui.Layer_m_areaCap_get
    if _newclass:m_areaCap = property(_ui.Layer_m_areaCap_get, _ui.Layer_m_areaCap_set)
    __swig_setmethods__["m_edgeCap"] = _ui.Layer_m_edgeCap_set
    __swig_getmethods__["m_edgeCap"] = _ui.Layer_m_edgeCap_get
    if _newclass:m_edgeCap = property(_ui.Layer_m_edgeCap_get, _ui.Layer_m_edgeCap_set)
    __swig_setmethods__["m_order"] = _ui.Layer_m_order_set
    __swig_getmethods__["m_order"] = _ui.Layer_m_order_get
    if _newclass:m_order = property(_ui.Layer_m_order_get, _ui.Layer_m_order_set)
    __swig_setmethods__["m_pPen"] = _ui.Layer_m_pPen_set
    __swig_getmethods__["m_pPen"] = _ui.Layer_m_pPen_get
    if _newclass:m_pPen = property(_ui.Layer_m_pPen_get, _ui.Layer_m_pPen_set)
    __swig_setmethods__["m_pBrush"] = _ui.Layer_m_pBrush_set
    __swig_getmethods__["m_pBrush"] = _ui.Layer_m_pBrush_get
    if _newclass:m_pBrush = property(_ui.Layer_m_pBrush_get, _ui.Layer_m_pBrush_set)
    __swig_setmethods__["m_dimFactor"] = _ui.Layer_m_dimFactor_set
    __swig_getmethods__["m_dimFactor"] = _ui.Layer_m_dimFactor_get
    if _newclass:m_dimFactor = property(_ui.Layer_m_dimFactor_get, _ui.Layer_m_dimFactor_set)
    __swig_setmethods__["m_height"] = _ui.Layer_m_height_set
    __swig_getmethods__["m_height"] = _ui.Layer_m_height_get
    if _newclass:m_height = property(_ui.Layer_m_height_get, _ui.Layer_m_height_set)
    __swig_setmethods__["m_thickness"] = _ui.Layer_m_thickness_set
    __swig_getmethods__["m_thickness"] = _ui.Layer_m_thickness_get
    if _newclass:m_thickness = property(_ui.Layer_m_thickness_get, _ui.Layer_m_thickness_set)
    __swig_setmethods__["m_epsilon"] = _ui.Layer_m_epsilon_set
    __swig_getmethods__["m_epsilon"] = _ui.Layer_m_epsilon_get
    if _newclass:m_epsilon = property(_ui.Layer_m_epsilon_get, _ui.Layer_m_epsilon_set)

class LayerPtr(Layer):
    def __init__(self, this):
        _swig_setattr(self, Layer, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Layer, 'thisown', 0)
        self.__class__ = Layer
_ui.Layer_swigregister(LayerPtr)

class library(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, library, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, library, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::library instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, library, 'this', _ui.new_library(*args))
        _swig_setattr(self, library, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_library):
        try:
            if self.thisown: destroy(self)
        except: pass

    def dbFindCellViewByName(*args): return _ui.library_dbFindCellViewByName(*args)
    def dbFindCellByName(*args): return _ui.library_dbFindCellByName(*args)
    def dbFindViewByName(*args): return _ui.library_dbFindViewByName(*args)
    def dbOpenCellView(*args): return _ui.library_dbOpenCellView(*args)
    def dbDeleteCellView(*args): return _ui.library_dbDeleteCellView(*args)
    def dbRenameCellView(*args): return _ui.library_dbRenameCellView(*args)
    def dbCopyCellView(*args): return _ui.library_dbCopyCellView(*args)
    def dbDeleteCell(*args): return _ui.library_dbDeleteCell(*args)
    def dbRenameCell(*args): return _ui.library_dbRenameCell(*args)
    def dbClose(*args): return _ui.library_dbClose(*args)
    def dbOpenLib(*args): return _ui.library_dbOpenLib(*args)
    def dbSaveLib(*args): return _ui.library_dbSaveLib(*args)
    def dbCreateView(*args): return _ui.library_dbCreateView(*args)
    def dbCreateCell(*args): return _ui.library_dbCreateCell(*args)
    def libName(*args): return _ui.library_libName(*args)
    def libPath(*args): return _ui.library_libPath(*args)
    def dbuPerUU(*args): return _ui.library_dbuPerUU(*args)
    def dbu(*args): return _ui.library_dbu(*args)
    def userUnits(*args): return _ui.library_userUnits(*args)
    def units(*args): return _ui.library_units(*args)
    def addSegParam(*args): return _ui.library_addSegParam(*args)
    def getSegParam(*args): return _ui.library_getSegParam(*args)
    def getSegParamByLayer(*args): return _ui.library_getSegParamByLayer(*args)
    def getSegIndexByLayerAndWidth(*args): return _ui.library_getSegIndexByLayerAndWidth(*args)
    def getSegIndexByLayerAndWidthAndStyle(*args): return _ui.library_getSegIndexByLayerAndWidthAndStyle(*args)
    def getSegIndexByLayer(*args): return _ui.library_getSegIndexByLayer(*args)
    def getNumSegParams(*args): return _ui.library_getNumSegParams(*args)
    def addVia(*args): return _ui.library_addVia(*args)
    def getVia(*args): return _ui.library_getVia(*args)
    def getViaByName(*args): return _ui.library_getViaByName(*args)
    def getViaIndexByName(*args): return _ui.library_getViaIndexByName(*args)
    def getViaNameByIndex(*args): return _ui.library_getViaNameByIndex(*args)
    def getNumVias(*args): return _ui.library_getNumVias(*args)
    def dbDeleteVias(*args): return _ui.library_dbDeleteVias(*args)
    def addStyle(*args): return _ui.library_addStyle(*args)
    def getStyle(*args): return _ui.library_getStyle(*args)
    def getNumStyles(*args): return _ui.library_getNumStyles(*args)
    def createNonDefRule(*args): return _ui.library_createNonDefRule(*args)
    def addNonDefRuleLayer(*args): return _ui.library_addNonDefRuleLayer(*args)
    def getNonDefRule(*args): return _ui.library_getNonDefRule(*args)
    def getNonDefRuleIndex(*args): return _ui.library_getNonDefRuleIndex(*args)
    def getNumNonDefRules(*args): return _ui.library_getNumNonDefRules(*args)
    def getNonDefRulesMap(*args): return _ui.library_getNonDefRulesMap(*args)
    def getMPPRulesMap(*args): return _ui.library_getMPPRulesMap(*args)
    def createMPPRule(*args): return _ui.library_createMPPRule(*args)
    def deleteMPPRule(*args): return _ui.library_deleteMPPRule(*args)
    def addMPPLayer(*args): return _ui.library_addMPPLayer(*args)
    def getMPPRule(*args): return _ui.library_getMPPRule(*args)
    def getNumMPPRules(*args): return _ui.library_getNumMPPRules(*args)
    def mppMaxWidth(*args): return _ui.library_mppMaxWidth(*args)
    def dbDeleteMPPs(*args): return _ui.library_dbDeleteMPPs(*args)
    def tech(*args): return _ui.library_tech(*args)
    def setDefUnits(*args): return _ui.library_setDefUnits(*args)
    def getDefUnits(*args): return _ui.library_getDefUnits(*args)
    def setLefUnits(*args): return _ui.library_setLefUnits(*args)
    def getLefUnits(*args): return _ui.library_getLefUnits(*args)
    def setDefDividerChar(*args): return _ui.library_setDefDividerChar(*args)
    def getDefDividerChar(*args): return _ui.library_getDefDividerChar(*args)
    def setDefBusBitChars(*args): return _ui.library_setDefBusBitChars(*args)
    def getDefBusBitChars(*args): return _ui.library_getDefBusBitChars(*args)
    def setLefBusBitChars(*args): return _ui.library_setLefBusBitChars(*args)
    def getLefBusBitChars(*args): return _ui.library_getLefBusBitChars(*args)
    def setVersion(*args): return _ui.library_setVersion(*args)
    def getVersion(*args): return _ui.library_getVersion(*args)
    def getCurrentVersion(*args): return _ui.library_getCurrentVersion(*args)
    __swig_setmethods__["m_curVersion"] = _ui.library_m_curVersion_set
    __swig_getmethods__["m_curVersion"] = _ui.library_m_curVersion_get
    if _newclass:m_curVersion = property(_ui.library_m_curVersion_get, _ui.library_m_curVersion_set)
    __swig_setmethods__["m_version"] = _ui.library_m_version_set
    __swig_getmethods__["m_version"] = _ui.library_m_version_get
    if _newclass:m_version = property(_ui.library_m_version_get, _ui.library_m_version_set)
    __swig_setmethods__["m_createDate"] = _ui.library_m_createDate_set
    __swig_getmethods__["m_createDate"] = _ui.library_m_createDate_get
    if _newclass:m_createDate = property(_ui.library_m_createDate_get, _ui.library_m_createDate_set)
    __swig_setmethods__["m_modDate"] = _ui.library_m_modDate_set
    __swig_getmethods__["m_modDate"] = _ui.library_m_modDate_get
    if _newclass:m_modDate = property(_ui.library_m_modDate_get, _ui.library_m_modDate_set)
    def cellNames(*args): return _ui.library_cellNames(*args)
    def viewNames(*args): return _ui.library_viewNames(*args)
    def getCells(*args): return _ui.library_getCells(*args)
    def getViews(*args): return _ui.library_getViews(*args)

class libraryPtr(library):
    def __init__(self, this):
        _swig_setattr(self, library, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, library, 'thisown', 0)
        self.__class__ = library
_ui.library_swigregister(libraryPtr)

class sort_cell_list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sort_cell_list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sort_cell_list, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ sort_cell_list instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __call__(*args): return _ui.sort_cell_list___call__(*args)
    def __init__(self, *args):
        _swig_setattr(self, sort_cell_list, 'this', _ui.new_sort_cell_list(*args))
        _swig_setattr(self, sort_cell_list, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_sort_cell_list):
        try:
            if self.thisown: destroy(self)
        except: pass


class sort_cell_listPtr(sort_cell_list):
    def __init__(self, this):
        _swig_setattr(self, sort_cell_list, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, sort_cell_list, 'thisown', 0)
        self.__class__ = sort_cell_list
_ui.sort_cell_list_swigregister(sort_cell_listPtr)

class cellIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cellIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cellIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cellIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, cellIterator, 'this', _ui.new_cellIterator(*args))
        _swig_setattr(self, cellIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_cellIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.cellIterator___ref__(*args)
    def value(*args): return _ui.cellIterator_value(*args)
    def next(*args): return _ui.cellIterator_next(*args)

class cellIteratorPtr(cellIterator):
    def __init__(self, this):
        _swig_setattr(self, cellIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cellIterator, 'thisown', 0)
        self.__class__ = cellIterator
_ui.cellIterator_swigregister(cellIteratorPtr)

class viewIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, viewIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, viewIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ viewIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, viewIterator, 'this', _ui.new_viewIterator(*args))
        _swig_setattr(self, viewIterator, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viewIterator):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ref__(*args): return _ui.viewIterator___ref__(*args)
    def value(*args): return _ui.viewIterator_value(*args)
    def next(*args): return _ui.viewIterator_next(*args)

class viewIteratorPtr(viewIterator):
    def __init__(self, this):
        _swig_setattr(self, viewIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viewIterator, 'thisown', 0)
        self.__class__ = viewIterator
_ui.viewIterator_swigregister(viewIteratorPtr)

class line(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, line, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, line, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::line instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, line, 'this', _ui.new_line(*args))
        _swig_setattr(self, line, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_line):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.line_left(*args)
    def right(*args): return _ui.line_right(*args)
    def bottom(*args): return _ui.line_bottom(*args)
    def top(*args): return _ui.line_top(*args)
    def coord(*args): return _ui.line_coord(*args)
    def setLeft(*args): return _ui.line_setLeft(*args)
    def setRight(*args): return _ui.line_setRight(*args)
    def setBottom(*args): return _ui.line_setBottom(*args)
    def setTop(*args): return _ui.line_setTop(*args)
    def setLL(*args): return _ui.line_setLL(*args)
    def setUR(*args): return _ui.line_setUR(*args)
    def getLL(*args): return _ui.line_getLL(*args)
    def getUR(*args): return _ui.line_getUR(*args)
    def offGrid(*args): return _ui.line_offGrid(*args)
    def manhattan(*args): return _ui.line_manhattan(*args)
    def setWidth(*args): return _ui.line_setWidth(*args)
    def width(*args): return _ui.line_width(*args)
    def bBox(*args): return _ui.line_bBox(*args)
    def qBox(*args): return _ui.line_qBox(*args)
    def objType(*args): return _ui.line_objType(*args)
    def objName(*args): return _ui.line_objName(*args)
    def nPoints(*args): return _ui.line_nPoints(*args)
    def bias(*args): return _ui.line_bias(*args)
    def scale(*args): return _ui.line_scale(*args)
    def ptlist(*args): return _ui.line_ptlist(*args)
    def ptInPoly(*args): return _ui.line_ptInPoly(*args)
    def ptInRect(*args): return _ui.line_ptInRect(*args)
    def length(*args): return _ui.line_length(*args)
    def getLength(*args): return _ui.line_getLength(*args)
    def transform(*args): return _ui.line_transform(*args)
    def getNearestEdge(*args): return _ui.line_getNearestEdge(*args)
    def getSegPts(*args): return _ui.line_getSegPts(*args)
    def getVertexAdjPts(*args): return _ui.line_getVertexAdjPts(*args)
    def getNearestVertex(*args): return _ui.line_getNearestVertex(*args)
    def getSegsInRect(*args): return _ui.line_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.line_getVertsInRect(*args)
    def deleteSeg(*args): return _ui.line_deleteSeg(*args)
    def getTransformPoints(*args): return _ui.line_getTransformPoints(*args)
    def at(*args): return _ui.line_at(*args)
    def getFirstVertex(*args): return _ui.line_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.line_getLastVertex(*args)
    def setLastVertex(*args): return _ui.line_setLastVertex(*args)
    def point(*args): return _ui.line_point(*args)
    def setPoint(*args): return _ui.line_setPoint(*args)
    def addPoint(*args): return _ui.line_addPoint(*args)
    def deletePoint(*args): return _ui.line_deletePoint(*args)
    def Move(*args): return _ui.line_Move(*args)
    def Copy(*args): return _ui.line_Copy(*args)
    def Flatten(*args): return _ui.line_Flatten(*args)
    def Stretch(*args): return _ui.line_Stretch(*args)
    def __getitem__(*args): return _ui.line___getitem__(*args)

class linePtr(line):
    def __init__(self, this):
        _swig_setattr(self, line, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, line, 'thisown', 0)
        self.__class__ = line
_ui.line_swigregister(linePtr)

class lpp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lpp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lpp, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::lpp instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, lpp, 'this', _ui.new_lpp(*args))
        _swig_setattr(self, lpp, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_lpp):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.lpp_clear(*args)
    def layerName(*args): return _ui.lpp_layerName(*args)
    def purpose(*args): return _ui.lpp_purpose(*args)
    def layerNum(*args): return _ui.lpp_layerNum(*args)
    def priority(*args): return _ui.lpp_priority(*args)
    def numShapes(*args): return _ui.lpp_numShapes(*args)
    def cv(*args): return _ui.lpp_cv(*args)
    def insertObj(*args): return _ui.lpp_insertObj(*args)
    def deleteObj(*args): return _ui.lpp_deleteObj(*args)
    def bBox(*args): return _ui.lpp_bBox(*args)
    def getTree(*args): return _ui.lpp_getTree(*args)
    def isOptimised(*args): return _ui.lpp_isOptimised(*args)
    def size(*args): return _ui.lpp_size(*args)
    def vmusage(*args): return _ui.lpp_vmusage(*args)
    def sizeHint(*args): return _ui.lpp_sizeHint(*args)
    def optimiseTree(*args): return _ui.lpp_optimiseTree(*args)
    def updateTree(*args): return _ui.lpp_updateTree(*args)
    def dbGetOverlaps(*args): return _ui.lpp_dbGetOverlaps(*args)
    def findOverlaps(*args): return _ui.lpp_findOverlaps(*args)
    def setFilterSize(*args): return _ui.lpp_setFilterSize(*args)
    def getOverlaps(*args): return _ui.lpp_getOverlaps(*args)

class lppPtr(lpp):
    def __init__(self, this):
        _swig_setattr(self, lpp, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, lpp, 'thisown', 0)
        self.__class__ = lpp
_ui.lpp_swigregister(lppPtr)

class objIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, objIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, objIterator, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ objIterator instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, objIterator, 'this', _ui.new_objIterator(*args))
        _swig_setattr(self, objIterator, 'thisown', 1)
    def __ref__(*args): return _ui.objIterator___ref__(*args)
    def value(*args): return _ui.objIterator_value(*args)
    def next(*args): return _ui.objIterator_next(*args)
    def end(*args): return _ui.objIterator_end(*args)
    def __del__(self, destroy=_ui.delete_objIterator):
        try:
            if self.thisown: destroy(self)
        except: pass


class objIteratorPtr(objIterator):
    def __init__(self, this):
        _swig_setattr(self, objIterator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, objIterator, 'thisown', 0)
        self.__class__ = objIterator
_ui.objIterator_swigregister(objIteratorPtr)

class mppLayer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mppLayer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mppLayer, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::mppLayer instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mppLayer, 'this', _ui.new_mppLayer(*args))
        _swig_setattr(self, mppLayer, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_mppLayer):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setWidth(*args): return _ui.mppLayer_setWidth(*args)
    def width(*args): return _ui.mppLayer_width(*args)
    def setLength(*args): return _ui.mppLayer_setLength(*args)
    def length(*args): return _ui.mppLayer_length(*args)
    def setSpace(*args): return _ui.mppLayer_setSpace(*args)
    def space(*args): return _ui.mppLayer_space(*args)
    def setBegExt(*args): return _ui.mppLayer_setBegExt(*args)
    def begExt(*args): return _ui.mppLayer_begExt(*args)
    def setEndExt(*args): return _ui.mppLayer_setEndExt(*args)
    def endExt(*args): return _ui.mppLayer_endExt(*args)
    def setLayer(*args): return _ui.mppLayer_setLayer(*args)
    def layer(*args): return _ui.mppLayer_layer(*args)

class mppLayerPtr(mppLayer):
    def __init__(self, this):
        _swig_setattr(self, mppLayer, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mppLayer, 'thisown', 0)
        self.__class__ = mppLayer
_ui.mppLayer_swigregister(mppLayerPtr)

class mppRule(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mppRule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mppRule, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::mppRule instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mppRule, 'this', _ui.new_mppRule(*args))
        _swig_setattr(self, mppRule, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_mppRule):
        try:
            if self.thisown: destroy(self)
        except: pass

    __swig_setmethods__["name"] = _ui.mppRule_name_set
    __swig_getmethods__["name"] = _ui.mppRule_name_get
    if _newclass:name = property(_ui.mppRule_name_get, _ui.mppRule_name_set)
    __swig_setmethods__["numLayers"] = _ui.mppRule_numLayers_set
    __swig_getmethods__["numLayers"] = _ui.mppRule_numLayers_get
    if _newclass:numLayers = property(_ui.mppRule_numLayers_get, _ui.mppRule_numLayers_set)
    __swig_setmethods__["layers"] = _ui.mppRule_layers_set
    __swig_getmethods__["layers"] = _ui.mppRule_layers_get
    if _newclass:layers = property(_ui.mppRule_layers_get, _ui.mppRule_layers_set)
    __swig_setmethods__["maxWidth"] = _ui.mppRule_maxWidth_set
    __swig_getmethods__["maxWidth"] = _ui.mppRule_maxWidth_get
    if _newclass:maxWidth = property(_ui.mppRule_maxWidth_get, _ui.mppRule_maxWidth_set)

class mppRulePtr(mppRule):
    def __init__(self, this):
        _swig_setattr(self, mppRule, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mppRule, 'thisown', 0)
        self.__class__ = mppRule
_ui.mppRule_swigregister(mppRulePtr)

class mpp(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, mpp, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, mpp, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::mpp instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mpp, 'this', _ui.new_mpp(*args))
        _swig_setattr(self, mpp, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_mpp):
        try:
            if self.thisown: destroy(self)
        except: pass

    def addLayer(*args): return _ui.mpp_addLayer(*args)
    def getLayer(*args): return _ui.mpp_getLayer(*args)
    def getLayers(*args): return _ui.mpp_getLayers(*args)
    def setLayers(*args): return _ui.mpp_setLayers(*args)
    def numLayers(*args): return _ui.mpp_numLayers(*args)
    def setNumLayers(*args): return _ui.mpp_setNumLayers(*args)
    def setMppRule(*args): return _ui.mpp_setMppRule(*args)
    def getMppRule(*args): return _ui.mpp_getMppRule(*args)
    def getRuleName(*args): return _ui.mpp_getRuleName(*args)
    def left(*args): return _ui.mpp_left(*args)
    def right(*args): return _ui.mpp_right(*args)
    def bottom(*args): return _ui.mpp_bottom(*args)
    def top(*args): return _ui.mpp_top(*args)
    def maxWidth(*args): return _ui.mpp_maxWidth(*args)
    def maxBegExt(*args): return _ui.mpp_maxBegExt(*args)
    def maxEndExt(*args): return _ui.mpp_maxEndExt(*args)
    def offGrid(*args): return _ui.mpp_offGrid(*args)
    def manhattan(*args): return _ui.mpp_manhattan(*args)
    def rectXLo(*args): return _ui.mpp_rectXLo(*args)
    def rectYLo(*args): return _ui.mpp_rectYLo(*args)
    def rectXHi(*args): return _ui.mpp_rectXHi(*args)
    def rectYHi(*args): return _ui.mpp_rectYHi(*args)
    def ptlist(*args): return _ui.mpp_ptlist(*args)
    def nPoints(*args): return _ui.mpp_nPoints(*args)
    def layer(*args): return _ui.mpp_layer(*args)
    def reshape(*args): return _ui.mpp_reshape(*args)
    def bBox(*args): return _ui.mpp_bBox(*args)
    def qBox(*args): return _ui.mpp_qBox(*args)
    def objType(*args): return _ui.mpp_objType(*args)
    def objName(*args): return _ui.mpp_objName(*args)
    def bias(*args): return _ui.mpp_bias(*args)
    def scale(*args): return _ui.mpp_scale(*args)
    def getSegPts(*args): return _ui.mpp_getSegPts(*args)
    def getVertexAdjPts(*args): return _ui.mpp_getVertexAdjPts(*args)
    def getNearestEdge(*args): return _ui.mpp_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.mpp_getNearestVertex(*args)
    def getSegsInRect(*args): return _ui.mpp_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.mpp_getVertsInRect(*args)
    def addVertex(*args): return _ui.mpp_addVertex(*args)
    def area(*args): return _ui.mpp_area(*args)
    def perimeter(*args): return _ui.mpp_perimeter(*args)
    def chop(*args): return _ui.mpp_chop(*args)
    def getTransformPoints(*args): return _ui.mpp_getTransformPoints(*args)
    def transform(*args): return _ui.mpp_transform(*args)
    def ptInPoly(*args): return _ui.mpp_ptInPoly(*args)
    def getFirstVertex(*args): return _ui.mpp_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.mpp_getLastVertex(*args)
    def setLastVertex(*args): return _ui.mpp_setLastVertex(*args)
    def point(*args): return _ui.mpp_point(*args)
    def setPoint(*args): return _ui.mpp_setPoint(*args)
    def createPolygon(*args): return _ui.mpp_createPolygon(*args)
    def createPolygons(*args): return _ui.mpp_createPolygons(*args)
    def addPoint(*args): return _ui.mpp_addPoint(*args)
    def deletePoint(*args): return _ui.mpp_deletePoint(*args)
    def Move(*args): return _ui.mpp_Move(*args)
    def Copy(*args): return _ui.mpp_Copy(*args)
    def Flatten(*args): return _ui.mpp_Flatten(*args)
    def Stretch(*args): return _ui.mpp_Stretch(*args)
    def compressPoints(*args): return _ui.mpp_compressPoints(*args)
    def length(*args): return _ui.mpp_length(*args)

class mppPtr(mpp):
    def __init__(self, this):
        _swig_setattr(self, mpp, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mpp, 'thisown', 0)
        self.__class__ = mpp
_ui.mpp_swigregister(mppPtr)

DB_SIGNAL = _ui.DB_SIGNAL
DB_ANALOG = _ui.DB_ANALOG
DB_CLOCK = _ui.DB_CLOCK
DB_GROUND = _ui.DB_GROUND
DB_POWER = _ui.DB_POWER
DB_RESET = _ui.DB_RESET
DB_SCAN = _ui.DB_SCAN
DB_TIEOFF = _ui.DB_TIEOFF
DB_TIEHI = _ui.DB_TIEHI
DB_TIELO = _ui.DB_TIELO
DB_DIST = _ui.DB_DIST
DB_NETLIST = _ui.DB_NETLIST
DB_TEST = _ui.DB_TEST
DB_TIMING = _ui.DB_TIMING
DB_USER = _ui.DB_USER
DB_BALANCED = _ui.DB_BALANCED
DB_STEINER = _ui.DB_STEINER
DB_TRUNK = _ui.DB_TRUNK
DB_WIREDLOGIC = _ui.DB_WIREDLOGIC
class net(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, net, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, net, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::net instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, net, 'this', _ui.new_net(*args))
        _swig_setattr(self, net, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_net):
        try:
            if self.thisown: destroy(self)
        except: pass

    def name(*args): return _ui.net_name(*args)
    def objType(*args): return _ui.net_objType(*args)
    def objName(*args): return _ui.net_objName(*args)
    def cellView(*args): return _ui.net_cellView(*args)
    def dbCreateInstPin(*args): return _ui.net_dbCreateInstPin(*args)
    def dbDeleteInstPin(*args): return _ui.net_dbDeleteInstPin(*args)
    def getHPWL(*args): return _ui.net_getHPWL(*args)
    def setUse(*args): return _ui.net_setUse(*args)
    def use(*args): return _ui.net_use(*args)
    def getUseStr(*args): return _ui.net_getUseStr(*args)
    def setSource(*args): return _ui.net_setSource(*args)
    def source(*args): return _ui.net_source(*args)
    def getSourceStr(*args): return _ui.net_getSourceStr(*args)
    def setPattern(*args): return _ui.net_setPattern(*args)
    def pattern(*args): return _ui.net_pattern(*args)
    def getPatternStr(*args): return _ui.net_getPatternStr(*args)
    def setGlobal(*args): return _ui.net_setGlobal(*args)
    def isGlobal(*args): return _ui.net_isGlobal(*args)
    def setSpecial(*args): return _ui.net_setSpecial(*args)
    def isSpecial(*args): return _ui.net_isSpecial(*args)
    def setNonDefRule(*args): return _ui.net_setNonDefRule(*args)
    def getNonDefRule(*args): return _ui.net_getNonDefRule(*args)
    def setPins(*args): return _ui.net_setPins(*args)
    def pins(*args): return _ui.net_pins(*args)
    def addPin(*args): return _ui.net_addPin(*args)
    def deletePin(*args): return _ui.net_deletePin(*args)
    def addShape(*args): return _ui.net_addShape(*args)
    def deleteShape(*args): return _ui.net_deleteShape(*args)
    def setShapes(*args): return _ui.net_setShapes(*args)
    def shapes(*args): return _ui.net_shapes(*args)
    def getNumShapes(*args): return _ui.net_getNumShapes(*args)
    def getNumInstPins(*args): return _ui.net_getNumInstPins(*args)
    def addInstPin(*args): return _ui.net_addInstPin(*args)
    def instPins(*args): return _ui.net_instPins(*args)
    def getSignals(*args): return _ui.net_getSignals(*args)
    def numBits(*args): return _ui.net_numBits(*args)
    def baseName(*args): return _ui.net_baseName(*args)
    def busBits(*args): return _ui.net_busBits(*args)
    def getShapes(*args): return _ui.net_getShapes(*args)
    def getPins(*args): return _ui.net_getPins(*args)
    def getInstPins(*args): return _ui.net_getInstPins(*args)

class netPtr(net):
    def __init__(self, this):
        _swig_setattr(self, net, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, net, 'thisown', 0)
        self.__class__ = net
_ui.net_swigregister(netPtr)

class path(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, path, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, path, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::path instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, path, 'this', _ui.new_path(*args))
        _swig_setattr(self, path, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_path):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.path_left(*args)
    def right(*args): return _ui.path_right(*args)
    def bottom(*args): return _ui.path_bottom(*args)
    def top(*args): return _ui.path_top(*args)
    def coord(*args): return _ui.path_coord(*args)
    def offGrid(*args): return _ui.path_offGrid(*args)
    def manhattan(*args): return _ui.path_manhattan(*args)
    def rectXLo(*args): return _ui.path_rectXLo(*args)
    def rectYLo(*args): return _ui.path_rectYLo(*args)
    def rectXHi(*args): return _ui.path_rectXHi(*args)
    def rectYHi(*args): return _ui.path_rectYHi(*args)
    def width(*args): return _ui.path_width(*args)
    def beginExt(*args): return _ui.path_beginExt(*args)
    def endExt(*args): return _ui.path_endExt(*args)
    def bBox(*args): return _ui.path_bBox(*args)
    def qBox(*args): return _ui.path_qBox(*args)
    def objType(*args): return _ui.path_objType(*args)
    def objName(*args): return _ui.path_objName(*args)
    def nPoints(*args): return _ui.path_nPoints(*args)
    def ptlist(*args): return _ui.path_ptlist(*args)
    def length(*args): return _ui.path_length(*args)
    def getNearestEdge(*args): return _ui.path_getNearestEdge(*args)
    def getSegPts(*args): return _ui.path_getSegPts(*args)
    def getVertexAdjPts(*args): return _ui.path_getVertexAdjPts(*args)
    def getNearestVertex(*args): return _ui.path_getNearestVertex(*args)
    def getSegsInRect(*args): return _ui.path_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.path_getVertsInRect(*args)
    def addVertex(*args): return _ui.path_addVertex(*args)
    def deleteSeg(*args): return _ui.path_deleteSeg(*args)
    def getTransformPoints(*args): return _ui.path_getTransformPoints(*args)
    def at(*args): return _ui.path_at(*args)
    def reshape(*args): return _ui.path_reshape(*args)
    def origin(*args): return _ui.path_origin(*args)
    def bias(*args): return _ui.path_bias(*args)
    def scale(*args): return _ui.path_scale(*args)
    def area(*args): return _ui.path_area(*args)
    def perimeter(*args): return _ui.path_perimeter(*args)
    def chop(*args): return _ui.path_chop(*args)
    def setStyle(*args): return _ui.path_setStyle(*args)
    def getStyle(*args): return _ui.path_getStyle(*args)
    def setType(*args): return _ui.path_setType(*args)
    def getType(*args): return _ui.path_getType(*args)
    def getTypeStr(*args): return _ui.path_getTypeStr(*args)
    def setShape(*args): return _ui.path_setShape(*args)
    def getShape(*args): return _ui.path_getShape(*args)
    def getShapeStr(*args): return _ui.path_getShapeStr(*args)
    def transform(*args): return _ui.path_transform(*args)
    def ptInPoly(*args): return _ui.path_ptInPoly(*args)
    def getFirstVertex(*args): return _ui.path_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.path_getLastVertex(*args)
    def setLastVertex(*args): return _ui.path_setLastVertex(*args)
    def point(*args): return _ui.path_point(*args)
    def setPoint(*args): return _ui.path_setPoint(*args)
    def createPolygon(*args): return _ui.path_createPolygon(*args)
    def addPoint(*args): return _ui.path_addPoint(*args)
    def deletePoint(*args): return _ui.path_deletePoint(*args)
    def Move(*args): return _ui.path_Move(*args)
    def Copy(*args): return _ui.path_Copy(*args)
    def Flatten(*args): return _ui.path_Flatten(*args)
    def Stretch(*args): return _ui.path_Stretch(*args)
    def compressPoints(*args): return _ui.path_compressPoints(*args)
    def shapeToPoly(*args): return _ui.path_shapeToPoly(*args)
    def __getitem__(*args): return _ui.path___getitem__(*args)

class pathPtr(path):
    def __init__(self, this):
        _swig_setattr(self, path, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, path, 'thisown', 0)
        self.__class__ = path
_ui.path_swigregister(pathPtr)

DB_PIN_INPUT = _ui.DB_PIN_INPUT
DB_PIN_OUTPUT = _ui.DB_PIN_OUTPUT
DB_PIN_INOUT = _ui.DB_PIN_INOUT
DB_PIN_FEEDTHRU = _ui.DB_PIN_FEEDTHRU
DB_PIN_TRISTATE = _ui.DB_PIN_TRISTATE
DB_PIN_UNKNOWN = _ui.DB_PIN_UNKNOWN
DB_PIN_SIGNAL = _ui.DB_PIN_SIGNAL
DB_PIN_ANALOG = _ui.DB_PIN_ANALOG
DB_PIN_CLOCK = _ui.DB_PIN_CLOCK
DB_PIN_GROUND = _ui.DB_PIN_GROUND
DB_PIN_POWER = _ui.DB_PIN_POWER
DB_PIN_RESET = _ui.DB_PIN_RESET
DB_PIN_SCAN = _ui.DB_PIN_SCAN
DB_PIN_TIEOFF = _ui.DB_PIN_TIEOFF
DB_PIN_TIEHI = _ui.DB_PIN_TIEHI
DB_PIN_TIELO = _ui.DB_PIN_TIELO
DB_PIN_ABUTMENT = _ui.DB_PIN_ABUTMENT
DB_PIN_RING = _ui.DB_PIN_RING
DB_PIN_FEED = _ui.DB_PIN_FEED
class pin(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pin, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pin, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::pin instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pin, 'this', _ui.new_pin(*args))
        _swig_setattr(self, pin, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pin):
        try:
            if self.thisown: destroy(self)
        except: pass

    def name(*args): return _ui.pin_name(*args)
    def setUse(*args): return _ui.pin_setUse(*args)
    def use(*args): return _ui.pin_use(*args)
    def getUseStr(*args): return _ui.pin_getUseStr(*args)
    def setDir(*args): return _ui.pin_setDir(*args)
    def dir(*args): return _ui.pin_dir(*args)
    def getDirStr(*args): return _ui.pin_getDirStr(*args)
    def setShape(*args): return _ui.pin_setShape(*args)
    def getShape(*args): return _ui.pin_getShape(*args)
    def getShapeStr(*args): return _ui.pin_getShapeStr(*args)
    def setNet(*args): return _ui.pin_setNet(*args)
    def getNet(*args): return _ui.pin_getNet(*args)
    def getNetName(*args): return _ui.pin_getNetName(*args)
    def objType(*args): return _ui.pin_objType(*args)
    def objName(*args): return _ui.pin_objName(*args)
    def ports(*args): return _ui.pin_ports(*args)
    def setPorts(*args): return _ui.pin_setPorts(*args)
    def getNumPorts(*args): return _ui.pin_getNumPorts(*args)
    def addPort(*args): return _ui.pin_addPort(*args)
    def deletePort(*args): return _ui.pin_deletePort(*args)
    def setBits(*args): return _ui.pin_setBits(*args)
    def bits(*args): return _ui.pin_bits(*args)
    def getPorts(*args): return _ui.pin_getPorts(*args)

class pinPtr(pin):
    def __init__(self, this):
        _swig_setattr(self, pin, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pin, 'thisown', 0)
        self.__class__ = pin
_ui.pin_swigregister(pinPtr)

class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ Point instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Point, 'this', _ui.new_Point(*args))
        _swig_setattr(self, Point, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_Point):
        try:
            if self.thisown: destroy(self)
        except: pass

    def getX(*args): return _ui.Point_getX(*args)
    def getY(*args): return _ui.Point_getY(*args)
    def setX(*args): return _ui.Point_setX(*args)
    def setY(*args): return _ui.Point_setY(*args)
    def set(*args): return _ui.Point_set(*args)
    def __eq__(*args): return _ui.Point___eq__(*args)
    def __ne__(*args): return _ui.Point___ne__(*args)
    def __lt__(*args): return _ui.Point___lt__(*args)
    def __gt__(*args): return _ui.Point___gt__(*args)
    def __add__(*args): return _ui.Point___add__(*args)
    def __imul__(*args): return _ui.Point___imul__(*args)
    def __sub__(*args): return _ui.Point___sub__(*args)
    def __iadd__(*args): return _ui.Point___iadd__(*args)
    def __isub__(*args): return _ui.Point___isub__(*args)
    def offset(*args): return _ui.Point_offset(*args)
    __swig_setmethods__["x"] = _ui.Point_x_set
    __swig_getmethods__["x"] = _ui.Point_x_get
    if _newclass:x = property(_ui.Point_x_get, _ui.Point_x_set)
    __swig_setmethods__["y"] = _ui.Point_y_set
    __swig_getmethods__["y"] = _ui.Point_y_get
    if _newclass:y = property(_ui.Point_y_get, _ui.Point_y_set)

class PointPtr(Point):
    def __init__(self, this):
        _swig_setattr(self, Point, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Point, 'thisown', 0)
        self.__class__ = Point
_ui.Point_swigregister(PointPtr)

class pointList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pointList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pointList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::pointList instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pointList, 'this', _ui.new_pointList(*args))
        _swig_setattr(self, pointList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pointList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __eq__(*args): return _ui.pointList___eq__(*args)
    def __ne__(*args): return _ui.pointList___ne__(*args)
    def __lt__(*args): return _ui.pointList___lt__(*args)
    def setPtlist(*args): return _ui.pointList_setPtlist(*args)
    def points(*args): return _ui.pointList_points(*args)
    def append(*args): return _ui.pointList_append(*args)
    def at(*args): return _ui.pointList_at(*args)
    def numPts(*args): return _ui.pointList_numPts(*args)
    def bBox(*args): return _ui.pointList_bBox(*args)
    def area(*args): return _ui.pointList_area(*args)
    def perimeter(*args): return _ui.pointList_perimeter(*args)
    def transform(*args): return _ui.pointList_transform(*args)
    def scale(*args): return _ui.pointList_scale(*args)
    def compressPoints(*args): return _ui.pointList_compressPoints(*args)
    def setFirstVertex(*args): return _ui.pointList_setFirstVertex(*args)
    def isSelfIntersecting(*args): return _ui.pointList_isSelfIntersecting(*args)
    def overlaps(*args): return _ui.pointList_overlaps(*args)
    def contains(*args): return _ui.pointList_contains(*args)
    def intersectsAt(*args): return _ui.pointList_intersectsAt(*args)
    def isOrthogonal(*args): return _ui.pointList_isOrthogonal(*args)
    def vmusage(*args): return _ui.pointList_vmusage(*args)
    def ptlist(*args): return _ui.pointList_ptlist(*args)
    def __getitem__(*args): return _ui.pointList___getitem__(*args)

class pointListPtr(pointList):
    def __init__(self, this):
        _swig_setattr(self, pointList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pointList, 'thisown', 0)
        self.__class__ = pointList
_ui.pointList_swigregister(pointListPtr)

class polygon(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, polygon, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, polygon, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::polygon instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, polygon, 'this', _ui.new_polygon(*args))
        _swig_setattr(self, polygon, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_polygon):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.polygon_left(*args)
    def right(*args): return _ui.polygon_right(*args)
    def bottom(*args): return _ui.polygon_bottom(*args)
    def top(*args): return _ui.polygon_top(*args)
    def coord(*args): return _ui.polygon_coord(*args)
    def offGrid(*args): return _ui.polygon_offGrid(*args)
    def manhattan(*args): return _ui.polygon_manhattan(*args)
    def ptlist(*args): return _ui.polygon_ptlist(*args)
    def pointlist(*args): return _ui.polygon_pointlist(*args)
    def reshape(*args): return _ui.polygon_reshape(*args)
    def qBox(*args): return _ui.polygon_qBox(*args)
    def bBox(*args): return _ui.polygon_bBox(*args)
    def objType(*args): return _ui.polygon_objType(*args)
    def objName(*args): return _ui.polygon_objName(*args)
    def bias(*args): return _ui.polygon_bias(*args)
    def scale(*args): return _ui.polygon_scale(*args)
    def getNearestEdge(*args): return _ui.polygon_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.polygon_getNearestVertex(*args)
    def getSegPts(*args): return _ui.polygon_getSegPts(*args)
    def getVertexAdjPts(*args): return _ui.polygon_getVertexAdjPts(*args)
    def getSegsInRect(*args): return _ui.polygon_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.polygon_getVertsInRect(*args)
    def ptInPoly(*args): return _ui.polygon_ptInPoly(*args)
    def addVertex(*args): return _ui.polygon_addVertex(*args)
    def area(*args): return _ui.polygon_area(*args)
    def perimeter(*args): return _ui.polygon_perimeter(*args)
    def nPoints(*args): return _ui.polygon_nPoints(*args)
    def getTransformPoints(*args): return _ui.polygon_getTransformPoints(*args)
    def transform(*args): return _ui.polygon_transform(*args)
    def getFirstVertex(*args): return _ui.polygon_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.polygon_getLastVertex(*args)
    def Move(*args): return _ui.polygon_Move(*args)
    def Copy(*args): return _ui.polygon_Copy(*args)
    def Flatten(*args): return _ui.polygon_Flatten(*args)
    def Stretch(*args): return _ui.polygon_Stretch(*args)
    def compressPoints(*args): return _ui.polygon_compressPoints(*args)
    def setFirstVertex(*args): return _ui.polygon_setFirstVertex(*args)
    def shapeToPoly(*args): return _ui.polygon_shapeToPoly(*args)
    def length(*args): return _ui.polygon_length(*args)
    def selfIntersecting(*args): return _ui.polygon_selfIntersecting(*args)
    def at(*args): return _ui.polygon_at(*args)
    def isOrthogonal(*args): return _ui.polygon_isOrthogonal(*args)
    def __getitem__(*args): return _ui.polygon___getitem__(*args)

class polygonPtr(polygon):
    def __init__(self, this):
        _swig_setattr(self, polygon, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, polygon, 'thisown', 0)
        self.__class__ = polygon
_ui.polygon_swigregister(polygonPtr)

class Rect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rect, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ Rect instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_ui.delete_Rect):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.Rect_left(*args)
    def right(*args): return _ui.Rect_right(*args)
    def bottom(*args): return _ui.Rect_bottom(*args)
    def top(*args): return _ui.Rect_top(*args)
    def getXLo(*args): return _ui.Rect_getXLo(*args)
    def getXHi(*args): return _ui.Rect_getXHi(*args)
    def getYLo(*args): return _ui.Rect_getYLo(*args)
    def getYHi(*args): return _ui.Rect_getYHi(*args)
    def coord(*args): return _ui.Rect_coord(*args)
    def otherCoord(*args): return _ui.Rect_otherCoord(*args)
    def getLL(*args): return _ui.Rect_getLL(*args)
    def getLR(*args): return _ui.Rect_getLR(*args)
    def getUR(*args): return _ui.Rect_getUR(*args)
    def getUL(*args): return _ui.Rect_getUL(*args)
    def setLeft(*args): return _ui.Rect_setLeft(*args)
    def setRight(*args): return _ui.Rect_setRight(*args)
    def setBottom(*args): return _ui.Rect_setBottom(*args)
    def setTop(*args): return _ui.Rect_setTop(*args)
    def setXLo(*args): return _ui.Rect_setXLo(*args)
    def setXHi(*args): return _ui.Rect_setXHi(*args)
    def setYLo(*args): return _ui.Rect_setYLo(*args)
    def setYHi(*args): return _ui.Rect_setYHi(*args)
    def set(*args): return _ui.Rect_set(*args)
    def invalidate(*args): return _ui.Rect_invalidate(*args)
    def isNull(*args): return _ui.Rect_isNull(*args)
    def getQRect(*args): return _ui.Rect_getQRect(*args)
    def at(*args): return _ui.Rect_at(*args)
    def edge(*args): return _ui.Rect_edge(*args)
    def getEdge(*args): return _ui.Rect_getEdge(*args)
    def __eq__(*args): return _ui.Rect___eq__(*args)
    def __ne__(*args): return _ui.Rect___ne__(*args)
    def __lt__(*args): return _ui.Rect___lt__(*args)
    def __gt__(*args): return _ui.Rect___gt__(*args)
    def __iadd__(*args): return _ui.Rect___iadd__(*args)
    def __init__(self, *args):
        _swig_setattr(self, Rect, 'this', _ui.new_Rect(*args))
        _swig_setattr(self, Rect, 'thisown', 1)
    def scale(*args): return _ui.Rect_scale(*args)
    def bias(*args): return _ui.Rect_bias(*args)
    def offset(*args): return _ui.Rect_offset(*args)
    def moveTo(*args): return _ui.Rect_moveTo(*args)
    def width(*args): return _ui.Rect_width(*args)
    def height(*args): return _ui.Rect_height(*args)
    def centre(*args): return _ui.Rect_centre(*args)
    def isSquare(*args): return _ui.Rect_isSquare(*args)
    def normalise(*args): return _ui.Rect_normalise(*args)
    def transform(*args): return _ui.Rect_transform(*args)
    def swapxy(*args): return _ui.Rect_swapxy(*args)
    def unionWith(*args): return _ui.Rect_unionWith(*args)
    def intersectsWith(*args): return _ui.Rect_intersectsWith(*args)
    def touchOrOverlaps(*args): return _ui.Rect_touchOrOverlaps(*args)
    def overlaps(*args): return _ui.Rect_overlaps(*args)
    def touch(*args): return _ui.Rect_touch(*args)
    def contains(*args): return _ui.Rect_contains(*args)
    __swig_setmethods__["m_coords"] = _ui.Rect_m_coords_set
    __swig_getmethods__["m_coords"] = _ui.Rect_m_coords_get
    if _newclass:m_coords = property(_ui.Rect_m_coords_get, _ui.Rect_m_coords_set)

class RectPtr(Rect):
    def __init__(self, this):
        _swig_setattr(self, Rect, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Rect, 'thisown', 0)
        self.__class__ = Rect
_ui.Rect_swigregister(RectPtr)

class rectangle(shape):
    __swig_setmethods__ = {}
    for _s in [shape]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, rectangle, name, value)
    __swig_getmethods__ = {}
    for _s in [shape]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, rectangle, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::rectangle instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, rectangle, 'this', _ui.new_rectangle(*args))
        _swig_setattr(self, rectangle, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_rectangle):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.rectangle_left(*args)
    def right(*args): return _ui.rectangle_right(*args)
    def bottom(*args): return _ui.rectangle_bottom(*args)
    def top(*args): return _ui.rectangle_top(*args)
    def coord(*args): return _ui.rectangle_coord(*args)
    def setLeft(*args): return _ui.rectangle_setLeft(*args)
    def setRight(*args): return _ui.rectangle_setRight(*args)
    def setBottom(*args): return _ui.rectangle_setBottom(*args)
    def setTop(*args): return _ui.rectangle_setTop(*args)
    def width(*args): return _ui.rectangle_width(*args)
    def height(*args): return _ui.rectangle_height(*args)
    def origin(*args): return _ui.rectangle_origin(*args)
    def qBox(*args): return _ui.rectangle_qBox(*args)
    def bBox(*args): return _ui.rectangle_bBox(*args)
    def objType(*args): return _ui.rectangle_objType(*args)
    def objName(*args): return _ui.rectangle_objName(*args)
    def centre(*args): return _ui.rectangle_centre(*args)
    def __eq__(*args): return _ui.rectangle___eq__(*args)
    def __ne__(*args): return _ui.rectangle___ne__(*args)
    def __lt__(*args): return _ui.rectangle___lt__(*args)
    def __gt__(*args): return _ui.rectangle___gt__(*args)
    def transform(*args): return _ui.rectangle_transform(*args)
    def length(*args): return _ui.rectangle_length(*args)
    def nPoints(*args): return _ui.rectangle_nPoints(*args)
    def ptlist(*args): return _ui.rectangle_ptlist(*args)
    def coords(*args): return _ui.rectangle_coords(*args)
    def shapeToPoly(*args): return _ui.rectangle_shapeToPoly(*args)
    def area(*args): return _ui.rectangle_area(*args)
    def perimeter(*args): return _ui.rectangle_perimeter(*args)
    def offGrid(*args): return _ui.rectangle_offGrid(*args)
    def manhattan(*args): return _ui.rectangle_manhattan(*args)
    def bias(*args): return _ui.rectangle_bias(*args)
    def scale(*args): return _ui.rectangle_scale(*args)
    def getNearestEdge(*args): return _ui.rectangle_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.rectangle_getNearestVertex(*args)
    def getSegPts(*args): return _ui.rectangle_getSegPts(*args)
    def getSegsInRect(*args): return _ui.rectangle_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.rectangle_getVertsInRect(*args)
    def getVertexAdjPts(*args): return _ui.rectangle_getVertexAdjPts(*args)
    def ptInPoly(*args): return _ui.rectangle_ptInPoly(*args)
    def Move(*args): return _ui.rectangle_Move(*args)
    def Copy(*args): return _ui.rectangle_Copy(*args)
    def Flatten(*args): return _ui.rectangle_Flatten(*args)
    def Stretch(*args): return _ui.rectangle_Stretch(*args)

class rectanglePtr(rectangle):
    def __init__(self, this):
        _swig_setattr(self, rectangle, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, rectangle, 'thisown', 0)
        self.__class__ = rectangle
_ui.rectangle_swigregister(rectanglePtr)

class segment(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, segment, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, segment, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::segment instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, segment, 'this', _ui.new_segment(*args))
        _swig_setattr(self, segment, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_segment):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ne__(*args): return _ui.segment___ne__(*args)
    def __eq__(*args): return _ui.segment___eq__(*args)
    def null(*args): return _ui.segment_null(*args)
    def getEdge(*args): return _ui.segment_getEdge(*args)
    def length(*args): return _ui.segment_length(*args)
    def DistanceToPoint(*args): return _ui.segment_DistanceToPoint(*args)
    def NearestPoint(*args): return _ui.segment_NearestPoint(*args)
    def objType(*args): return _ui.segment_objType(*args)
    def objName(*args): return _ui.segment_objName(*args)
    def SetObj(*args): return _ui.segment_SetObj(*args)
    def GetObj(*args): return _ui.segment_GetObj(*args)
    def isXseg(*args): return _ui.segment_isXseg(*args)
    def isYseg(*args): return _ui.segment_isYseg(*args)
    def isDiag(*args): return _ui.segment_isDiag(*args)
    def isManhattan(*args): return _ui.segment_isManhattan(*args)
    def bBox(*args): return _ui.segment_bBox(*args)
    def qBox(*args): return _ui.segment_qBox(*args)
    def normalise(*args): return _ui.segment_normalise(*args)
    def segInRect(*args): return _ui.segment_segInRect(*args)
    def transform(*args): return _ui.segment_transform(*args)
    def Move(*args): return _ui.segment_Move(*args)
    def Copy(*args): return _ui.segment_Copy(*args)
    __swig_setmethods__["p0"] = _ui.segment_p0_set
    __swig_getmethods__["p0"] = _ui.segment_p0_get
    if _newclass:p0 = property(_ui.segment_p0_get, _ui.segment_p0_set)
    __swig_setmethods__["p1"] = _ui.segment_p1_set
    __swig_getmethods__["p1"] = _ui.segment_p1_get
    if _newclass:p1 = property(_ui.segment_p1_get, _ui.segment_p1_set)

class segmentPtr(segment):
    def __init__(self, this):
        _swig_setattr(self, segment, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, segment, 'thisown', 0)
        self.__class__ = segment
_ui.segment_swigregister(segmentPtr)

class dbSegParam(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dbSegParam, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dbSegParam, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::dbSegParam instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, dbSegParam, 'this', _ui.new_dbSegParam(*args))
        _swig_setattr(self, dbSegParam, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_dbSegParam):
        try:
            if self.thisown: destroy(self)
        except: pass

    def layer(*args): return _ui.dbSegParam_layer(*args)
    def setLayer(*args): return _ui.dbSegParam_setLayer(*args)
    def lib(*args): return _ui.dbSegParam_lib(*args)
    def width(*args): return _ui.dbSegParam_width(*args)
    def setWidth(*args): return _ui.dbSegParam_setWidth(*args)
    def beginExt(*args): return _ui.dbSegParam_beginExt(*args)
    def setBeginExt(*args): return _ui.dbSegParam_setBeginExt(*args)
    def endExt(*args): return _ui.dbSegParam_endExt(*args)
    def setEndExt(*args): return _ui.dbSegParam_setEndExt(*args)
    def style(*args): return _ui.dbSegParam_style(*args)
    def setStyle(*args): return _ui.dbSegParam_setStyle(*args)

class dbSegParamPtr(dbSegParam):
    def __init__(self, this):
        _swig_setattr(self, dbSegParam, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dbSegParam, 'thisown', 0)
        self.__class__ = dbSegParam
_ui.dbSegParam_swigregister(dbSegParamPtr)

class signal(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, signal, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, signal, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::signal instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, signal, 'this', _ui.new_signal(*args))
        _swig_setattr(self, signal, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_signal):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setName(*args): return _ui.signal_setName(*args)
    def name(*args): return _ui.signal_name(*args)
    def setNet(*args): return _ui.signal_setNet(*args)
    def net(*args): return _ui.signal_net(*args)
    def objType(*args): return _ui.signal_objType(*args)
    def objName(*args): return _ui.signal_objName(*args)

class signalPtr(signal):
    def __init__(self, this):
        _swig_setattr(self, signal, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, signal, 'thisown', 0)
        self.__class__ = signal
_ui.signal_swigregister(signalPtr)

TECH_LINELENGTH = _ui.TECH_LINELENGTH
TECH_MAX_LAYERS = _ui.TECH_MAX_LAYERS
TECH_MAX_SYS_LAYERS = _ui.TECH_MAX_SYS_LAYERS
TECH_NONSELECT_LAYERS = _ui.TECH_NONSELECT_LAYERS
TECH_BACKGROUND_LAYER = _ui.TECH_BACKGROUND_LAYER
TECH_INSTANCE_LAYER = _ui.TECH_INSTANCE_LAYER
TECH_VIAINST_LAYER = _ui.TECH_VIAINST_LAYER
TECH_CURSOR_LAYER = _ui.TECH_CURSOR_LAYER
TECH_AXES_LAYER = _ui.TECH_AXES_LAYER
TECH_MAJORGRID_LAYER = _ui.TECH_MAJORGRID_LAYER
TECH_MINORGRID_LAYER = _ui.TECH_MINORGRID_LAYER
TECH_SELECT_LAYER = _ui.TECH_SELECT_LAYER
TECH_FLIGHTLINE_LAYER = _ui.TECH_FLIGHTLINE_LAYER
TECH_TEXT_LAYER = _ui.TECH_TEXT_LAYER
TECH_PIN_LAYER = _ui.TECH_PIN_LAYER
TECH_WIRE_LAYER = _ui.TECH_WIRE_LAYER
TECH_DEVICE_LAYER = _ui.TECH_DEVICE_LAYER
TECH_MARKER_LAYER = _ui.TECH_MARKER_LAYER
TECH_ROW_LAYER = _ui.TECH_ROW_LAYER
TECH_REGION_LAYER = _ui.TECH_REGION_LAYER
TECH_PRBOUNDARY_LAYER = _ui.TECH_PRBOUNDARY_LAYER
TECH_MPP_LAYER = _ui.TECH_MPP_LAYER
TECH_ANNOTATE9_LAYER = _ui.TECH_ANNOTATE9_LAYER
TECH_ANNOTATE8_LAYER = _ui.TECH_ANNOTATE8_LAYER
TECH_ANNOTATE7_LAYER = _ui.TECH_ANNOTATE7_LAYER
TECH_ANNOTATE6_LAYER = _ui.TECH_ANNOTATE6_LAYER
TECH_ANNOTATE5_LAYER = _ui.TECH_ANNOTATE5_LAYER
TECH_ANNOTATE4_LAYER = _ui.TECH_ANNOTATE4_LAYER
TECH_ANNOTATE3_LAYER = _ui.TECH_ANNOTATE3_LAYER
TECH_ANNOTATE2_LAYER = _ui.TECH_ANNOTATE2_LAYER
TECH_ANNOTATE1_LAYER = _ui.TECH_ANNOTATE1_LAYER
TECH_ANNOTATE_LAYER = _ui.TECH_ANNOTATE_LAYER
TECH_Y9_LAYER = _ui.TECH_Y9_LAYER
TECH_Y8_LAYER = _ui.TECH_Y8_LAYER
TECH_Y7_LAYER = _ui.TECH_Y7_LAYER
TECH_Y6_LAYER = _ui.TECH_Y6_LAYER
TECH_Y5_LAYER = _ui.TECH_Y5_LAYER
TECH_Y4_LAYER = _ui.TECH_Y4_LAYER
TECH_Y3_LAYER = _ui.TECH_Y3_LAYER
TECH_Y2_LAYER = _ui.TECH_Y2_LAYER
TECH_Y1_LAYER = _ui.TECH_Y1_LAYER
TECH_Y0_LAYER = _ui.TECH_Y0_LAYER
TECH_MAX_USER_LAYERS = _ui.TECH_MAX_USER_LAYERS
TECH_MAX_SELECT_LAYERS = _ui.TECH_MAX_SELECT_LAYERS
class techFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, techFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, techFile, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::techFile instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, techFile, 'this', _ui.new_techFile(*args))
        _swig_setattr(self, techFile, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_techFile):
        try:
            if self.thisown: destroy(self)
        except: pass

    def techLoad(*args): return _ui.techFile_techLoad(*args)
    def techSave(*args): return _ui.techFile_techSave(*args)
    def setupDefaultLayers(*args): return _ui.techFile_setupDefaultLayers(*args)
    def setupDefaultStipples(*args): return _ui.techFile_setupDefaultStipples(*args)
    def setupDefaultLineStyles(*args): return _ui.techFile_setupDefaultLineStyles(*args)
    def layerTable(*args): return _ui.techFile_layerTable(*args)
    def lib(*args): return _ui.techFile_lib(*args)
    def isSelectable(*args): return _ui.techFile_isSelectable(*args)
    def selectable(*args): return _ui.techFile_selectable(*args)
    def isVisible(*args): return _ui.techFile_isVisible(*args)
    def visible(*args): return _ui.techFile_visible(*args)
    def isUsed(*args): return _ui.techFile_isUsed(*args)
    def setUsed(*args): return _ui.techFile_setUsed(*args)
    def isActive(*args): return _ui.techFile_isActive(*args)
    def setActive(*args): return _ui.techFile_setActive(*args)
    def setAllInactive(*args): return _ui.techFile_setAllInactive(*args)
    def isValid(*args): return _ui.techFile_isValid(*args)
    def setValid(*args): return _ui.techFile_setValid(*args)
    def getPen(*args): return _ui.techFile_getPen(*args)
    def setPen(*args): return _ui.techFile_setPen(*args)
    def getBrush(*args): return _ui.techFile_getBrush(*args)
    def setBrush(*args): return _ui.techFile_setBrush(*args)
    def color(*args): return _ui.techFile_color(*args)
    def getDimColor(*args): return _ui.techFile_getDimColor(*args)
    def setLayerName(*args): return _ui.techFile_setLayerName(*args)
    def getLayerName(*args): return _ui.techFile_getLayerName(*args)
    def setLayerPurpose(*args): return _ui.techFile_setLayerPurpose(*args)
    def getLayerPurpose(*args): return _ui.techFile_getLayerPurpose(*args)
    def getLayerPurposePair(*args): return _ui.techFile_getLayerPurposePair(*args)
    def setLayerGdsLayer(*args): return _ui.techFile_setLayerGdsLayer(*args)
    def getLayerGdsLayer(*args): return _ui.techFile_getLayerGdsLayer(*args)
    def setLayerDataType(*args): return _ui.techFile_setLayerDataType(*args)
    def getLayerDataType(*args): return _ui.techFile_getLayerDataType(*args)
    def getLayerNum(*args): return _ui.techFile_getLayerNum(*args)
    def getNextFreeSlot(*args): return _ui.techFile_getNextFreeSlot(*args)
    def createLayer(*args): return _ui.techFile_createLayer(*args)
    def deleteLayer(*args): return _ui.techFile_deleteLayer(*args)
    def setLayerType(*args): return _ui.techFile_setLayerType(*args)
    def getLayerType(*args): return _ui.techFile_getLayerType(*args)
    def getLayerTypeAsStr(*args): return _ui.techFile_getLayerTypeAsStr(*args)
    def getNumRoutingLayers(*args): return _ui.techFile_getNumRoutingLayers(*args)
    def getRoutingLayer(*args): return _ui.techFile_getRoutingLayer(*args)
    def getNumObsLayers(*args): return _ui.techFile_getNumObsLayers(*args)
    def getObsLayer(*args): return _ui.techFile_getObsLayer(*args)
    def getNumPinLayers(*args): return _ui.techFile_getNumPinLayers(*args)
    def getPinLayer(*args): return _ui.techFile_getPinLayer(*args)
    def setLayerWidth(*args): return _ui.techFile_setLayerWidth(*args)
    def getLayerWidth(*args): return _ui.techFile_getLayerWidth(*args)
    def setLayerSpacing(*args): return _ui.techFile_setLayerSpacing(*args)
    def getLayerSpacing(*args): return _ui.techFile_getLayerSpacing(*args)
    def set2LayerSpacing(*args): return _ui.techFile_set2LayerSpacing(*args)
    def get2LayerSpacing(*args): return _ui.techFile_get2LayerSpacing(*args)
    def layerSpacingRules(*args): return _ui.techFile_layerSpacingRules(*args)
    def setLayerEnc(*args): return _ui.techFile_setLayerEnc(*args)
    def getLayerEnc(*args): return _ui.techFile_getLayerEnc(*args)
    def enclosureRules(*args): return _ui.techFile_enclosureRules(*args)
    def setLayerOvlp(*args): return _ui.techFile_setLayerOvlp(*args)
    def getLayerOvlp(*args): return _ui.techFile_getLayerOvlp(*args)
    def overlapRules(*args): return _ui.techFile_overlapRules(*args)
    def setLayerArea(*args): return _ui.techFile_setLayerArea(*args)
    def getLayerArea(*args): return _ui.techFile_getLayerArea(*args)
    def setLayerPitch(*args): return _ui.techFile_setLayerPitch(*args)
    def getLayerPitch(*args): return _ui.techFile_getLayerPitch(*args)
    def setLayerOffset(*args): return _ui.techFile_setLayerOffset(*args)
    def getLayerOffset(*args): return _ui.techFile_getLayerOffset(*args)
    def setLayerDir(*args): return _ui.techFile_setLayerDir(*args)
    def getLayerDir(*args): return _ui.techFile_getLayerDir(*args)
    def getLayerDirAsStr(*args): return _ui.techFile_getLayerDirAsStr(*args)
    def setLayerResistance(*args): return _ui.techFile_setLayerResistance(*args)
    def getLayerResistance(*args): return _ui.techFile_getLayerResistance(*args)
    def setLayerAreaCap(*args): return _ui.techFile_setLayerAreaCap(*args)
    def getLayerAreaCap(*args): return _ui.techFile_getLayerAreaCap(*args)
    def setLayerEdgeCap(*args): return _ui.techFile_setLayerEdgeCap(*args)
    def getLayerEdgeCap(*args): return _ui.techFile_getLayerEdgeCap(*args)
    def getLayerUp(*args): return _ui.techFile_getLayerUp(*args)
    def getLayerDown(*args): return _ui.techFile_getLayerDown(*args)
    def setLayerByOrder(*args): return _ui.techFile_setLayerByOrder(*args)
    def getLayerByOrder(*args): return _ui.techFile_getLayerByOrder(*args)
    def getLayerOrder(*args): return _ui.techFile_getLayerOrder(*args)
    def changeLayerOrder(*args): return _ui.techFile_changeLayerOrder(*args)
    def getLineStyle(*args): return _ui.techFile_getLineStyle(*args)
    def setLineStyle(*args): return _ui.techFile_setLineStyle(*args)
    def getLineWidth(*args): return _ui.techFile_getLineWidth(*args)
    def setLineWidth(*args): return _ui.techFile_setLineWidth(*args)
    def getFillPattern(*args): return _ui.techFile_getFillPattern(*args)
    def setFillPattern(*args): return _ui.techFile_setFillPattern(*args)
    def getFillName(*args): return _ui.techFile_getFillName(*args)
    def getFillType(*args): return _ui.techFile_getFillType(*args)
    def changeFillStyle(*args): return _ui.techFile_changeFillStyle(*args)
    def setFillType(*args): return _ui.techFile_setFillType(*args)
    def setCurrentLayer(*args): return _ui.techFile_setCurrentLayer(*args)
    def getCurrentLayer(*args): return _ui.techFile_getCurrentLayer(*args)
    def setStippleTable(*args): return _ui.techFile_setStippleTable(*args)
    def getStippleTable(*args): return _ui.techFile_getStippleTable(*args)
    def addStipple(*args): return _ui.techFile_addStipple(*args)
    def setStipple(*args): return _ui.techFile_setStipple(*args)
    def setStippleName(*args): return _ui.techFile_setStippleName(*args)
    def setStippleType(*args): return _ui.techFile_setStippleType(*args)
    def setCrossFillPattern(*args): return _ui.techFile_setCrossFillPattern(*args)
    def getNumStipples(*args): return _ui.techFile_getNumStipples(*args)
    def getStipple(*args): return _ui.techFile_getStipple(*args)
    def setLineTable(*args): return _ui.techFile_setLineTable(*args)
    def getLineTable(*args): return _ui.techFile_getLineTable(*args)
    def addLine(*args): return _ui.techFile_addLine(*args)
    def setLine(*args): return _ui.techFile_setLine(*args)
    def getLineName(*args): return _ui.techFile_getLineName(*args)
    def getNumLines(*args): return _ui.techFile_getNumLines(*args)
    def setLayerDimFactor(*args): return _ui.techFile_setLayerDimFactor(*args)
    def getLayerDimFactor(*args): return _ui.techFile_getLayerDimFactor(*args)
    def setDimFactor(*args): return _ui.techFile_setDimFactor(*args)
    def getDimFactor(*args): return _ui.techFile_getDimFactor(*args)
    def getLayer(*args): return _ui.techFile_getLayer(*args)
    def setLayer(*args): return _ui.techFile_setLayer(*args)
    def getLayerHeight(*args): return _ui.techFile_getLayerHeight(*args)
    def setLayerHeight(*args): return _ui.techFile_setLayerHeight(*args)
    def getLayerThickness(*args): return _ui.techFile_getLayerThickness(*args)
    def setLayerThickness(*args): return _ui.techFile_setLayerThickness(*args)
    def getLayerEpsilon(*args): return _ui.techFile_getLayerEpsilon(*args)
    def setLayerEpsilon(*args): return _ui.techFile_setLayerEpsilon(*args)
    def isMetal(*args): return _ui.techFile_isMetal(*args)
    def isVia(*args): return _ui.techFile_isVia(*args)
    def setMfgGrid(*args): return _ui.techFile_setMfgGrid(*args)
    def mfgGrid(*args): return _ui.techFile_mfgGrid(*args)

class techFilePtr(techFile):
    def __init__(self, this):
        _swig_setattr(self, techFile, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, techFile, 'thisown', 0)
        self.__class__ = techFile
_ui.techFile_swigregister(techFilePtr)

class transform(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, transform, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, transform, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::transform instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_ui.delete_transform):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __init__(self, *args):
        _swig_setattr(self, transform, 'this', _ui.new_transform(*args))
        _swig_setattr(self, transform, 'thisown', 1)
    def __eq__(*args): return _ui.transform___eq__(*args)
    def __ne__(*args): return _ui.transform___ne__(*args)
    def __lt__(*args): return _ui.transform___lt__(*args)
    def __imul__(*args): return _ui.transform___imul__(*args)
    def invert(*args): return _ui.transform_invert(*args)
    def inverseTransformRect(*args): return _ui.transform_inverseTransformRect(*args)
    def inverseTransformPoint(*args): return _ui.transform_inverseTransformPoint(*args)
    def transformRect(*args): return _ui.transform_transformRect(*args)
    def transformPoint(*args): return _ui.transform_transformPoint(*args)
    def transformPointList(*args): return _ui.transform_transformPointList(*args)
    def setOrient(*args): return _ui.transform_setOrient(*args)
    def getOrient(*args): return _ui.transform_getOrient(*args)
    def setOrigin(*args): return _ui.transform_setOrigin(*args)
    def getOrigin(*args): return _ui.transform_getOrigin(*args)
    def setMag(*args): return _ui.transform_setMag(*args)
    def isXYSwapped(*args): return _ui.transform_isXYSwapped(*args)
    def name(*args): return _ui.transform_name(*args)
    def setT11(*args): return _ui.transform_setT11(*args)
    def T11(*args): return _ui.transform_T11(*args)
    def setT12(*args): return _ui.transform_setT12(*args)
    def T12(*args): return _ui.transform_T12(*args)
    def setT21(*args): return _ui.transform_setT21(*args)
    def T21(*args): return _ui.transform_T21(*args)
    def setT22(*args): return _ui.transform_setT22(*args)
    def T22(*args): return _ui.transform_T22(*args)
    def setT31(*args): return _ui.transform_setT31(*args)
    def T31(*args): return _ui.transform_T31(*args)
    def setT32(*args): return _ui.transform_setT32(*args)
    def T32(*args): return _ui.transform_T32(*args)
    def isNull(*args): return _ui.transform_isNull(*args)

class transformPtr(transform):
    def __init__(self, this):
        _swig_setattr(self, transform, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, transform, 'thisown', 0)
        self.__class__ = transform
_ui.transform_swigregister(transformPtr)

PI = _ui.PI
class transform64(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, transform64, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, transform64, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::transform64 instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_ui.delete_transform64):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __init__(self, *args):
        _swig_setattr(self, transform64, 'this', _ui.new_transform64(*args))
        _swig_setattr(self, transform64, 'thisown', 1)
    def __eq__(*args): return _ui.transform64___eq__(*args)
    def __ne__(*args): return _ui.transform64___ne__(*args)
    def __lt__(*args): return _ui.transform64___lt__(*args)
    def __imul__(*args): return _ui.transform64___imul__(*args)
    def invert(*args): return _ui.transform64_invert(*args)
    def inverseTransformRect(*args): return _ui.transform64_inverseTransformRect(*args)
    def inverseTransformPoint(*args): return _ui.transform64_inverseTransformPoint(*args)
    def transformRect(*args): return _ui.transform64_transformRect(*args)
    def transformPoint(*args): return _ui.transform64_transformPoint(*args)
    def transformPointList(*args): return _ui.transform64_transformPointList(*args)
    def setOrient(*args): return _ui.transform64_setOrient(*args)
    def getOrient(*args): return _ui.transform64_getOrient(*args)
    def setOrigin(*args): return _ui.transform64_setOrigin(*args)
    def getOrigin(*args): return _ui.transform64_getOrigin(*args)
    def setMag(*args): return _ui.transform64_setMag(*args)
    def isXYSwapped(*args): return _ui.transform64_isXYSwapped(*args)
    def name(*args): return _ui.transform64_name(*args)
    def setT11(*args): return _ui.transform64_setT11(*args)
    def T11(*args): return _ui.transform64_T11(*args)
    def setT12(*args): return _ui.transform64_setT12(*args)
    def T12(*args): return _ui.transform64_T12(*args)
    def setT21(*args): return _ui.transform64_setT21(*args)
    def T21(*args): return _ui.transform64_T21(*args)
    def setT22(*args): return _ui.transform64_setT22(*args)
    def T22(*args): return _ui.transform64_T22(*args)
    def setT31(*args): return _ui.transform64_setT31(*args)
    def T31(*args): return _ui.transform64_T31(*args)
    def setT32(*args): return _ui.transform64_setT32(*args)
    def T32(*args): return _ui.transform64_T32(*args)
    def isNull(*args): return _ui.transform64_isNull(*args)

class transform64Ptr(transform64):
    def __init__(self, this):
        _swig_setattr(self, transform64, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, transform64, 'thisown', 0)
        self.__class__ = transform64
_ui.transform64_swigregister(transform64Ptr)

class Trapezoid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trapezoid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trapezoid, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ Trapezoid instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Trapezoid, 'this', _ui.new_Trapezoid(*args))
        _swig_setattr(self, Trapezoid, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_Trapezoid):
        try:
            if self.thisown: destroy(self)
        except: pass

    def at(*args): return _ui.Trapezoid_at(*args)
    def edge(*args): return _ui.Trapezoid_edge(*args)
    def left(*args): return _ui.Trapezoid_left(*args)
    def right(*args): return _ui.Trapezoid_right(*args)
    def bottom(*args): return _ui.Trapezoid_bottom(*args)
    def top(*args): return _ui.Trapezoid_top(*args)
    def setXlo(*args): return _ui.Trapezoid_setXlo(*args)
    def setXhi(*args): return _ui.Trapezoid_setXhi(*args)
    def setYlo1(*args): return _ui.Trapezoid_setYlo1(*args)
    def setYhi1(*args): return _ui.Trapezoid_setYhi1(*args)
    def setYlo2(*args): return _ui.Trapezoid_setYlo2(*args)
    def setYhi2(*args): return _ui.Trapezoid_setYhi2(*args)
    def getLL(*args): return _ui.Trapezoid_getLL(*args)
    def getLR(*args): return _ui.Trapezoid_getLR(*args)
    def getUR(*args): return _ui.Trapezoid_getUR(*args)
    def getUL(*args): return _ui.Trapezoid_getUL(*args)
    def width(*args): return _ui.Trapezoid_width(*args)
    def height(*args): return _ui.Trapezoid_height(*args)
    def origin(*args): return _ui.Trapezoid_origin(*args)
    def bBox(*args): return _ui.Trapezoid_bBox(*args)
    def qBox(*args): return _ui.Trapezoid_qBox(*args)
    def centre(*args): return _ui.Trapezoid_centre(*args)
    def invalidate(*args): return _ui.Trapezoid_invalidate(*args)
    def isNull(*args): return _ui.Trapezoid_isNull(*args)
    def __eq__(*args): return _ui.Trapezoid___eq__(*args)
    def __ne__(*args): return _ui.Trapezoid___ne__(*args)
    def __lt__(*args): return _ui.Trapezoid___lt__(*args)
    def __gt__(*args): return _ui.Trapezoid___gt__(*args)
    def transform(*args): return _ui.Trapezoid_transform(*args)
    def touchOrOverlaps(*args): return _ui.Trapezoid_touchOrOverlaps(*args)
    def overlaps(*args): return _ui.Trapezoid_overlaps(*args)
    def unionWith(*args): return _ui.Trapezoid_unionWith(*args)
    def intersects(*args): return _ui.Trapezoid_intersects(*args)
    def ptInPoly(*args): return _ui.Trapezoid_ptInPoly(*args)
    def nPoints(*args): return _ui.Trapezoid_nPoints(*args)
    def ptlist(*args): return _ui.Trapezoid_ptlist(*args)
    def coords(*args): return _ui.Trapezoid_coords(*args)
    def area(*args): return _ui.Trapezoid_area(*args)
    def perimeter(*args): return _ui.Trapezoid_perimeter(*args)
    def offGrid(*args): return _ui.Trapezoid_offGrid(*args)
    def manhattan(*args): return _ui.Trapezoid_manhattan(*args)

class TrapezoidPtr(Trapezoid):
    def __init__(self, this):
        _swig_setattr(self, Trapezoid, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Trapezoid, 'thisown', 0)
        self.__class__ = Trapezoid
_ui.Trapezoid_swigregister(TrapezoidPtr)

UNKNOWN = _ui.UNKNOWN
CELLVIEW = _ui.CELLVIEW
CELL = _ui.CELL
VIEW = _ui.VIEW
INST = _ui.INST
RECTANGLE = _ui.RECTANGLE
TEXT = _ui.TEXT
ARRAY = _ui.ARRAY
PATH = _ui.PATH
POLYGON = _ui.POLYGON
VIAINST = _ui.VIAINST
NET = _ui.NET
PIN = _ui.PIN
SEGMENT = _ui.SEGMENT
LINE = _ui.LINE
VERTEX = _ui.VERTEX
HSEG = _ui.HSEG
VSEG = _ui.VSEG
ELLIPSE = _ui.ELLIPSE
ARC = _ui.ARC
MPP = _ui.MPP
SIGNAL = _ui.SIGNAL
INSTPIN = _ui.INSTPIN
R0 = _ui.R0
R90 = _ui.R90
R180 = _ui.R180
R270 = _ui.R270
MX = _ui.MX
MXR90 = _ui.MXR90
MY = _ui.MY
MYR90 = _ui.MYR90
DB_UNPLACED = _ui.DB_UNPLACED
DB_PLACED = _ui.DB_PLACED
DB_FIXED = _ui.DB_FIXED
DB_COVER = _ui.DB_COVER
DB_UNKNOWN = _ui.DB_UNKNOWN
DB_SRC_NONE = _ui.DB_SRC_NONE
DB_SRC_NETLIST = _ui.DB_SRC_NETLIST
DB_SRC_DIST = _ui.DB_SRC_DIST
DB_SRC_USER = _ui.DB_SRC_USER
DB_SRC_TIMING = _ui.DB_SRC_TIMING
DB_RING = _ui.DB_RING
DB_PADRING = _ui.DB_PADRING
DB_BLOCKRING = _ui.DB_BLOCKRING
DB_STRIPE = _ui.DB_STRIPE
DB_FOLLOWPIN = _ui.DB_FOLLOWPIN
DB_IOWIRE = _ui.DB_IOWIRE
DB_COREWIRE = _ui.DB_COREWIRE
DB_BLOCKWIRE = _ui.DB_BLOCKWIRE
DB_BLOCKAGEWIRE = _ui.DB_BLOCKAGEWIRE
DB_FILLWIRE = _ui.DB_FILLWIRE
DB_DRCFILL = _ui.DB_DRCFILL
DB_ROUTEDWIRE = _ui.DB_ROUTEDWIRE
DB_FIXEDWIRE = _ui.DB_FIXEDWIRE
DB_COVERWIRE = _ui.DB_COVERWIRE
DB_NOSHIELD = _ui.DB_NOSHIELD
DB_TRUNCATED = _ui.DB_TRUNCATED
DB_ROUND = _ui.DB_ROUND
DB_EXTENDED = _ui.DB_EXTENDED
DB_VAREXTEND = _ui.DB_VAREXTEND
DB_OCTAGONAL = _ui.DB_OCTAGONAL
topLeft = _ui.topLeft
centreLeft = _ui.centreLeft
bottomLeft = _ui.bottomLeft
topCentre = _ui.topCentre
centreCentre = _ui.centreCentre
bottomCentre = _ui.bottomCentre
topRight = _ui.topRight
centreRight = _ui.centreRight
bottomRight = _ui.bottomRight
NUM_RECORDS = _ui.NUM_RECORDS
GDS_HEADER = _ui.GDS_HEADER
GDS_BGNLIB = _ui.GDS_BGNLIB
GDS_LIBNAME = _ui.GDS_LIBNAME
GDS_UNITS = _ui.GDS_UNITS
GDS_ENDLIB = _ui.GDS_ENDLIB
GDS_BGNSTR = _ui.GDS_BGNSTR
GDS_STRNAME = _ui.GDS_STRNAME
GDS_ENDSTR = _ui.GDS_ENDSTR
GDS_BOUNDARY = _ui.GDS_BOUNDARY
GDS_PATH = _ui.GDS_PATH
GDS_SREF = _ui.GDS_SREF
GDS_AREF = _ui.GDS_AREF
GDS_TEXT = _ui.GDS_TEXT
GDS_LAYER = _ui.GDS_LAYER
GDS_DATATYPE = _ui.GDS_DATATYPE
GDS_WIDTH = _ui.GDS_WIDTH
GDS_XY = _ui.GDS_XY
GDS_ENDEL = _ui.GDS_ENDEL
GDS_SNAME = _ui.GDS_SNAME
GDS_COLROW = _ui.GDS_COLROW
GDS_TEXTNODE = _ui.GDS_TEXTNODE
GDS_NODE = _ui.GDS_NODE
GDS_TEXTTYPE = _ui.GDS_TEXTTYPE
GDS_PRESENTATION = _ui.GDS_PRESENTATION
GDS_SPACING = _ui.GDS_SPACING
GDS_STRING = _ui.GDS_STRING
GDS_STRANS = _ui.GDS_STRANS
GDS_MAG = _ui.GDS_MAG
GDS_ANGLE = _ui.GDS_ANGLE
GDS_UINTEGER = _ui.GDS_UINTEGER
GDS_USTRING = _ui.GDS_USTRING
GDS_REFLIBS = _ui.GDS_REFLIBS
GDS_FONTS = _ui.GDS_FONTS
GDS_PATHTYPE = _ui.GDS_PATHTYPE
GDS_GENERATIONS = _ui.GDS_GENERATIONS
GDS_ATTRTABLE = _ui.GDS_ATTRTABLE
GDS_STYPTABLE = _ui.GDS_STYPTABLE
GDS_STRTYPE = _ui.GDS_STRTYPE
GDS_ELFLAGS = _ui.GDS_ELFLAGS
GDS_ELKEY = _ui.GDS_ELKEY
GDS_LINKTYPE = _ui.GDS_LINKTYPE
GDS_LINKKEYS = _ui.GDS_LINKKEYS
GDS_NODETYPE = _ui.GDS_NODETYPE
GDS_PROPATTR = _ui.GDS_PROPATTR
GDS_PROPVALUE = _ui.GDS_PROPVALUE
GDS_BOX = _ui.GDS_BOX
GDS_BOXTYPE = _ui.GDS_BOXTYPE
GDS_PLEX = _ui.GDS_PLEX
GDS_BGNEXTN = _ui.GDS_BGNEXTN
GDS_ENDEXTN = _ui.GDS_ENDEXTN
GDS_TAPENUM = _ui.GDS_TAPENUM
GDS_TAPECODE = _ui.GDS_TAPECODE
GDS_STRCLASS = _ui.GDS_STRCLASS
GDS_RESERVED = _ui.GDS_RESERVED
GDS_FORMAT = _ui.GDS_FORMAT
GDS_MASK = _ui.GDS_MASK
GDS_ENDMASKS = _ui.GDS_ENDMASKS
GDS_LIBDIRSIZE = _ui.GDS_LIBDIRSIZE
GDS_SRFNAME = _ui.GDS_SRFNAME
GDS_LIBSECUR = _ui.GDS_LIBSECUR
GDS_BORDER = _ui.GDS_BORDER
GDS_SOFTFENCE = _ui.GDS_SOFTFENCE
GDS_HARDFENCE = _ui.GDS_HARDFENCE
GDS_SOFTWIRE = _ui.GDS_SOFTWIRE
GDS_HARDWIRE = _ui.GDS_HARDWIRE
GDS_PATHPORT = _ui.GDS_PATHPORT
GDS_NODEPORT = _ui.GDS_NODEPORT
GDS_USERCONSTRAINT = _ui.GDS_USERCONSTRAINT
GDS_SPACER_ERROR = _ui.GDS_SPACER_ERROR
GDS_CONTACT = _ui.GDS_CONTACT
path2rect = _ui.path2rect
path2hvseg = _ui.path2hvseg
path2path = _ui.path2path
allLayers = _ui.allLayers
techLayers = _ui.techLayers
singleLayer = _ui.singleLayer
class db_size(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, db_size, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, db_size, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ db_size instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, db_size, 'this', _ui.new_db_size(*args))
        _swig_setattr(self, db_size, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_db_size):
        try:
            if self.thisown: destroy(self)
        except: pass

    def width(*args): return _ui.db_size_width(*args)
    def height(*args): return _ui.db_size_height(*args)
    def setWidth(*args): return _ui.db_size_setWidth(*args)
    def setHeight(*args): return _ui.db_size_setHeight(*args)

class db_sizePtr(db_size):
    def __init__(self, this):
        _swig_setattr(self, db_size, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, db_size, 'thisown', 0)
        self.__class__ = db_size
_ui.db_size_swigregister(db_sizePtr)

MAX_MSG_LENGTH = _ui.MAX_MSG_LENGTH
class db(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, db, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, db, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ db instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, db, 'this', _ui.new_db(*args))
        _swig_setattr(self, db, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_db):
        try:
            if self.thisown: destroy(self)
        except: pass

    __swig_getmethods__["useOpenGL"] = lambda x: _ui.db_useOpenGL
    if _newclass:useOpenGL = staticmethod(_ui.db_useOpenGL)
    __swig_getmethods__["getLibList"] = lambda x: _ui.db_getLibList
    if _newclass:getLibList = staticmethod(_ui.db_getLibList)
    __swig_getmethods__["getNumLibs"] = lambda x: _ui.db_getNumLibs
    if _newclass:getNumLibs = staticmethod(_ui.db_getNumLibs)
    __swig_getmethods__["addLib"] = lambda x: _ui.db_addLib
    if _newclass:addLib = staticmethod(_ui.db_addLib)
    __swig_getmethods__["deleteLib"] = lambda x: _ui.db_deleteLib
    if _newclass:deleteLib = staticmethod(_ui.db_deleteLib)
    __swig_getmethods__["getLibByName"] = lambda x: _ui.db_getLibByName
    if _newclass:getLibByName = staticmethod(_ui.db_getLibByName)
    __swig_getmethods__["createLib"] = lambda x: _ui.db_createLib
    if _newclass:createLib = staticmethod(_ui.db_createLib)
    __swig_getmethods__["setLog"] = lambda x: _ui.db_setLog
    if _newclass:setLog = staticmethod(_ui.db_setLog)
    __swig_getmethods__["setLogNoPrompt"] = lambda x: _ui.db_setLogNoPrompt
    if _newclass:setLogNoPrompt = staticmethod(_ui.db_setLogNoPrompt)
    __swig_getmethods__["setCellView"] = lambda x: _ui.db_setCellView
    if _newclass:setCellView = staticmethod(_ui.db_setCellView)
    __swig_getmethods__["getCellView"] = lambda x: _ui.db_getCellView
    if _newclass:getCellView = staticmethod(_ui.db_getCellView)
    __swig_getmethods__["setRotateLabels"] = lambda x: _ui.db_setRotateLabels
    if _newclass:setRotateLabels = staticmethod(_ui.db_setRotateLabels)
    __swig_getmethods__["getRotateLabels"] = lambda x: _ui.db_getRotateLabels
    if _newclass:getRotateLabels = staticmethod(_ui.db_getRotateLabels)
    __swig_getmethods__["error"] = lambda x: _ui.db_error
    if _newclass:error = staticmethod(_ui.db_error)
    __swig_getmethods__["errorNoPrompt"] = lambda x: _ui.db_errorNoPrompt
    if _newclass:errorNoPrompt = staticmethod(_ui.db_errorNoPrompt)
    __swig_getmethods__["warn"] = lambda x: _ui.db_warn
    if _newclass:warn = staticmethod(_ui.db_warn)
    __swig_getmethods__["warnNoPrompt"] = lambda x: _ui.db_warnNoPrompt
    if _newclass:warnNoPrompt = staticmethod(_ui.db_warnNoPrompt)
    __swig_getmethods__["info"] = lambda x: _ui.db_info
    if _newclass:info = staticmethod(_ui.db_info)
    __swig_getmethods__["infoNoPrompt"] = lambda x: _ui.db_infoNoPrompt
    if _newclass:infoNoPrompt = staticmethod(_ui.db_infoNoPrompt)
    __swig_getmethods__["msg"] = lambda x: _ui.db_msg
    if _newclass:msg = staticmethod(_ui.db_msg)
    __swig_getmethods__["msgNoPrompt"] = lambda x: _ui.db_msgNoPrompt
    if _newclass:msgNoPrompt = staticmethod(_ui.db_msgNoPrompt)
    __swig_getmethods__["startTimer"] = lambda x: _ui.db_startTimer
    if _newclass:startTimer = staticmethod(_ui.db_startTimer)
    __swig_getmethods__["getElapsed"] = lambda x: _ui.db_getElapsed
    if _newclass:getElapsed = staticmethod(_ui.db_getElapsed)
    __swig_getmethods__["maxErrCount"] = lambda x: _ui.db_maxErrCount
    if _newclass:maxErrCount = staticmethod(_ui.db_maxErrCount)
    __swig_getmethods__["setMaxErrCount"] = lambda x: _ui.db_setMaxErrCount
    if _newclass:setMaxErrCount = staticmethod(_ui.db_setMaxErrCount)

class dbPtr(db):
    def __init__(self, this):
        _swig_setattr(self, db, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, db, 'thisown', 0)
        self.__class__ = db
_ui.db_swigregister(dbPtr)

db_useOpenGL = _ui.db_useOpenGL

db_getLibList = _ui.db_getLibList

db_getNumLibs = _ui.db_getNumLibs

db_addLib = _ui.db_addLib

db_deleteLib = _ui.db_deleteLib

db_getLibByName = _ui.db_getLibByName

db_createLib = _ui.db_createLib

db_setLog = _ui.db_setLog

db_setLogNoPrompt = _ui.db_setLogNoPrompt

db_setCellView = _ui.db_setCellView

db_getCellView = _ui.db_getCellView

db_setRotateLabels = _ui.db_setRotateLabels

db_getRotateLabels = _ui.db_getRotateLabels

db_error = _ui.db_error

db_errorNoPrompt = _ui.db_errorNoPrompt

db_warn = _ui.db_warn

db_warnNoPrompt = _ui.db_warnNoPrompt

db_info = _ui.db_info

db_infoNoPrompt = _ui.db_infoNoPrompt

db_msg = _ui.db_msg

db_msgNoPrompt = _ui.db_msgNoPrompt

db_startTimer = _ui.db_startTimer

db_getElapsed = _ui.db_getElapsed

db_maxErrCount = _ui.db_maxErrCount

db_setMaxErrCount = _ui.db_setMaxErrCount


getOrient = _ui.getOrient

getDEFOrient = _ui.getDEFOrient

setOrient = _ui.setOrient

orientToDegrees = _ui.orientToDegrees

getPresentation = _ui.getPresentation

setPresentation = _ui.setPresentation

translateAlign = _ui.translateAlign

translateRotation = _ui.translateRotation

translateOrientation = _ui.translateOrientation

db_DateTime = _ui.db_DateTime

dbStrdup = _ui.dbStrdup

dbRound = _ui.dbRound

areaPolygon = _ui.areaPolygon

compressPathPoints = _ui.compressPathPoints

overlaps = _ui.overlaps

checkCCW = _ui.checkCCW

stretchPolyPts = _ui.stretchPolyPts

shortLyrName = _ui.shortLyrName

getPCellArgs = _ui.getPCellArgs

parseNLPFormatString = _ui.parseNLPFormatString

pyEvalString = _ui.pyEvalString

sizePoly = _ui.sizePoly

getPropAsFloat = _ui.getPropAsFloat

busbits = _ui.busbits

makeSpiceName = _ui.makeSpiceName

createSpiceName = _ui.createSpiceName

makePCellName = _ui.makePCellName
class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::Vector instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Vector, 'this', _ui.new_Vector(*args))
        _swig_setattr(self, Vector, 'thisown', 1)
    def setX(*args): return _ui.Vector_setX(*args)
    def setY(*args): return _ui.Vector_setY(*args)
    def __add__(*args): return _ui.Vector___add__(*args)
    def __iadd__(*args): return _ui.Vector___iadd__(*args)
    def __sub__(*args): return _ui.Vector___sub__(*args)
    def __isub__(*args): return _ui.Vector___isub__(*args)
    def __mul__(*args): return _ui.Vector___mul__(*args)
    def __imul__(*args): return _ui.Vector___imul__(*args)
    def __div__(*args): return _ui.Vector___div__(*args)
    def __idiv__(*args): return _ui.Vector___idiv__(*args)
    def dotProduct(*args): return _ui.Vector_dotProduct(*args)
    def normal(*args): return _ui.Vector_normal(*args)
    def distance(*args): return _ui.Vector_distance(*args)
    __swig_setmethods__["x"] = _ui.Vector_x_set
    __swig_getmethods__["x"] = _ui.Vector_x_get
    if _newclass:x = property(_ui.Vector_x_get, _ui.Vector_x_set)
    __swig_setmethods__["y"] = _ui.Vector_y_set
    __swig_getmethods__["y"] = _ui.Vector_y_get
    if _newclass:y = property(_ui.Vector_y_get, _ui.Vector_y_set)
    def __del__(self, destroy=_ui.delete_Vector):
        try:
            if self.thisown: destroy(self)
        except: pass


class VectorPtr(Vector):
    def __init__(self, this):
        _swig_setattr(self, Vector, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Vector, 'thisown', 0)
        self.__class__ = Vector
_ui.Vector_swigregister(VectorPtr)

compressPoints = _ui.compressPoints

setFirstVertex = _ui.setFirstVertex

ptInPoly = _ui.ptInPoly

contains = _ui.contains

clip = _ui.clip

createPolygon = _ui.createPolygon

stretchPathPts = _ui.stretchPathPts

getInstAttribute = _ui.getInstAttribute

getCellAttribute = _ui.getCellAttribute

parseNLPLabel = _ui.parseNLPLabel

roundPoly = _ui.roundPoly

class vertex(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, vertex, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, vertex, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::vertex instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vertex, 'this', _ui.new_vertex(*args))
        _swig_setattr(self, vertex, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_vertex):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __ne__(*args): return _ui.vertex___ne__(*args)
    def __eq__(*args): return _ui.vertex___eq__(*args)
    def null(*args): return _ui.vertex_null(*args)
    def objType(*args): return _ui.vertex_objType(*args)
    def objName(*args): return _ui.vertex_objName(*args)
    def SetObj(*args): return _ui.vertex_SetObj(*args)
    def GetObj(*args): return _ui.vertex_GetObj(*args)
    def getPoint(*args): return _ui.vertex_getPoint(*args)
    def bBox(*args): return _ui.vertex_bBox(*args)
    def qBox(*args): return _ui.vertex_qBox(*args)
    def Move(*args): return _ui.vertex_Move(*args)
    def Copy(*args): return _ui.vertex_Copy(*args)
    def transform(*args): return _ui.vertex_transform(*args)
    def x(*args): return _ui.vertex_x(*args)
    def y(*args): return _ui.vertex_y(*args)
    def setX(*args): return _ui.vertex_setX(*args)
    def setY(*args): return _ui.vertex_setY(*args)
    __swig_setmethods__["p"] = _ui.vertex_p_set
    __swig_getmethods__["p"] = _ui.vertex_p_get
    if _newclass:p = property(_ui.vertex_p_get, _ui.vertex_p_set)

class vertexPtr(vertex):
    def __init__(self, this):
        _swig_setattr(self, vertex, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vertex, 'thisown', 0)
        self.__class__ = vertex
_ui.vertex_swigregister(vertexPtr)

class viaLayer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, viaLayer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, viaLayer, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::viaLayer instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["layer"] = _ui.viaLayer_layer_set
    __swig_getmethods__["layer"] = _ui.viaLayer_layer_get
    if _newclass:layer = property(_ui.viaLayer_layer_get, _ui.viaLayer_layer_set)
    __swig_setmethods__["geom"] = _ui.viaLayer_geom_set
    __swig_getmethods__["geom"] = _ui.viaLayer_geom_get
    if _newclass:geom = property(_ui.viaLayer_geom_get, _ui.viaLayer_geom_set)
    __swig_setmethods__["next"] = _ui.viaLayer_next_set
    __swig_getmethods__["next"] = _ui.viaLayer_next_get
    if _newclass:next = property(_ui.viaLayer_next_get, _ui.viaLayer_next_set)
    def __init__(self, *args):
        _swig_setattr(self, viaLayer, 'this', _ui.new_viaLayer(*args))
        _swig_setattr(self, viaLayer, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viaLayer):
        try:
            if self.thisown: destroy(self)
        except: pass


class viaLayerPtr(viaLayer):
    def __init__(self, this):
        _swig_setattr(self, viaLayer, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viaLayer, 'thisown', 0)
        self.__class__ = viaLayer
_ui.viaLayer_swigregister(viaLayerPtr)

class via(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, via, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, via, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::via instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, via, 'this', _ui.new_via(*args))
        _swig_setattr(self, via, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_via):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setViaName(*args): return _ui.via_setViaName(*args)
    def getViaName(*args): return _ui.via_getViaName(*args)
    def getViaLayerList(*args): return _ui.via_getViaLayerList(*args)
    def setViaLayerList(*args): return _ui.via_setViaLayerList(*args)
    def getNumLayers(*args): return _ui.via_getNumLayers(*args)
    def getFirstLayer(*args): return _ui.via_getFirstLayer(*args)
    def getLastLayer(*args): return _ui.via_getLastLayer(*args)
    def getCutLayer(*args): return _ui.via_getCutLayer(*args)
    def setViaDefault(*args): return _ui.via_setViaDefault(*args)
    def getViaDefault(*args): return _ui.via_getViaDefault(*args)
    def setSpecial(*args): return _ui.via_setSpecial(*args)
    def getSpecial(*args): return _ui.via_getSpecial(*args)
    def setNonDefaultName(*args): return _ui.via_setNonDefaultName(*args)
    def getNonDefaultName(*args): return _ui.via_getNonDefaultName(*args)
    def setRuleName(*args): return _ui.via_setRuleName(*args)
    def getRuleName(*args): return _ui.via_getRuleName(*args)
    def addViaLayer(*args): return _ui.via_addViaLayer(*args)
    def getOtherViaLayer(*args): return _ui.via_getOtherViaLayer(*args)
    def lib(*args): return _ui.via_lib(*args)
    def bBox(*args): return _ui.via_bBox(*args)
    def qBox(*args): return _ui.via_qBox(*args)
    def setResistance(*args): return _ui.via_setResistance(*args)
    def getResistance(*args): return _ui.via_getResistance(*args)
    def setPattern(*args): return _ui.via_setPattern(*args)
    def getPattern(*args): return _ui.via_getPattern(*args)

class viaPtr(via):
    def __init__(self, this):
        _swig_setattr(self, via, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, via, 'thisown', 0)
        self.__class__ = via
_ui.via_swigregister(viaPtr)

class viaInst(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, viaInst, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, viaInst, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::viaInst instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, viaInst, 'this', _ui.new_viaInst(*args))
        _swig_setattr(self, viaInst, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viaInst):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.viaInst_left(*args)
    def right(*args): return _ui.viaInst_right(*args)
    def bottom(*args): return _ui.viaInst_bottom(*args)
    def top(*args): return _ui.viaInst_top(*args)
    def coord(*args): return _ui.viaInst_coord(*args)
    def offGrid(*args): return _ui.viaInst_offGrid(*args)
    def setStyle(*args): return _ui.viaInst_setStyle(*args)
    def getStyle(*args): return _ui.viaInst_getStyle(*args)
    def setType(*args): return _ui.viaInst_setType(*args)
    def getType(*args): return _ui.viaInst_getType(*args)
    def getTypeStr(*args): return _ui.viaInst_getTypeStr(*args)
    def setShape(*args): return _ui.viaInst_setShape(*args)
    def getShape(*args): return _ui.viaInst_getShape(*args)
    def getShapeStr(*args): return _ui.viaInst_getShapeStr(*args)
    def orient(*args): return _ui.viaInst_orient(*args)
    def getOrientStr(*args): return _ui.viaInst_getOrientStr(*args)
    def setSpecial(*args): return _ui.viaInst_setSpecial(*args)
    def isSpecial(*args): return _ui.viaInst_isSpecial(*args)
    def setNet(*args): return _ui.viaInst_setNet(*args)
    def getNet(*args): return _ui.viaInst_getNet(*args)
    def getNetName(*args): return _ui.viaInst_getNetName(*args)
    def bBox(*args): return _ui.viaInst_bBox(*args)
    def qBox(*args): return _ui.viaInst_qBox(*args)
    def getLowerLayer(*args): return _ui.viaInst_getLowerLayer(*args)
    def getCutLayer(*args): return _ui.viaInst_getCutLayer(*args)
    def getUpperLayer(*args): return _ui.viaInst_getUpperLayer(*args)
    def objType(*args): return _ui.viaInst_objType(*args)
    def objName(*args): return _ui.viaInst_objName(*args)
    def nPoints(*args): return _ui.viaInst_nPoints(*args)
    def ptlist(*args): return _ui.viaInst_ptlist(*args)
    def layer(*args): return _ui.viaInst_layer(*args)
    def getNearestEdge(*args): return _ui.viaInst_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.viaInst_getNearestVertex(*args)
    def getViaIndex(*args): return _ui.viaInst_getViaIndex(*args)
    def setViaIndex(*args): return _ui.viaInst_setViaIndex(*args)
    def getVia(*args): return _ui.viaInst_getVia(*args)
    def origin(*args): return _ui.viaInst_origin(*args)
    def isDefault(*args): return _ui.viaInst_isDefault(*args)
    def dbPrint(*args): return _ui.viaInst_dbPrint(*args)
    def Move(*args): return _ui.viaInst_Move(*args)
    def Copy(*args): return _ui.viaInst_Copy(*args)
    def Flatten(*args): return _ui.viaInst_Flatten(*args)
    def Stretch(*args): return _ui.viaInst_Stretch(*args)
    def transform(*args): return _ui.viaInst_transform(*args)
    def bias(*args): return _ui.viaInst_bias(*args)
    def scale(*args): return _ui.viaInst_scale(*args)
    def manhattan(*args): return _ui.viaInst_manhattan(*args)

class viaInstPtr(viaInst):
    def __init__(self, this):
        _swig_setattr(self, viaInst, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viaInst, 'thisown', 0)
        self.__class__ = viaInst
_ui.viaInst_swigregister(viaInstPtr)

maskLayout = _ui.maskLayout
schematic = _ui.schematic
symbol = _ui.symbol
abstract = _ui.abstract
autoLayout = _ui.autoLayout
verilog = _ui.verilog
class view(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, view, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, view, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::view instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, view, 'this', _ui.new_view(*args))
        _swig_setattr(self, view, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_view):
        try:
            if self.thisown: destroy(self)
        except: pass

    def cellViews(*args): return _ui.view_cellViews(*args)
    def name(*args): return _ui.view_name(*args)
    def setViewType(*args): return _ui.view_setViewType(*args)
    def viewType(*args): return _ui.view_viewType(*args)
    def getViewTypeAsString(*args): return _ui.view_getViewTypeAsString(*args)
    def addCellView(*args): return _ui.view_addCellView(*args)
    def dbFindCellViewByCell(*args): return _ui.view_dbFindCellViewByCell(*args)
    def objType(*args): return _ui.view_objType(*args)
    def objName(*args): return _ui.view_objName(*args)
    def getCellViews(*args): return _ui.view_getCellViews(*args)

class viewPtr(view):
    def __init__(self, this):
        _swig_setattr(self, view, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, view, 'thisown', 0)
        self.__class__ = view
_ui.view_swigregister(viewPtr)

class VSeg(dbObj):
    __swig_setmethods__ = {}
    for _s in [dbObj]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, VSeg, name, value)
    __swig_getmethods__ = {}
    for _s in [dbObj]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, VSeg, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ cdb::VSeg instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, VSeg, 'this', _ui.new_VSeg(*args))
        _swig_setattr(self, VSeg, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_VSeg):
        try:
            if self.thisown: destroy(self)
        except: pass

    def left(*args): return _ui.VSeg_left(*args)
    def right(*args): return _ui.VSeg_right(*args)
    def bottom(*args): return _ui.VSeg_bottom(*args)
    def top(*args): return _ui.VSeg_top(*args)
    def coord(*args): return _ui.VSeg_coord(*args)
    def offGrid(*args): return _ui.VSeg_offGrid(*args)
    def manhattan(*args): return _ui.VSeg_manhattan(*args)
    def setStyle(*args): return _ui.VSeg_setStyle(*args)
    def getStyle(*args): return _ui.VSeg_getStyle(*args)
    def setType(*args): return _ui.VSeg_setType(*args)
    def getType(*args): return _ui.VSeg_getType(*args)
    def getTypeStr(*args): return _ui.VSeg_getTypeStr(*args)
    def setShape(*args): return _ui.VSeg_setShape(*args)
    def getShape(*args): return _ui.VSeg_getShape(*args)
    def getShapeStr(*args): return _ui.VSeg_getShapeStr(*args)
    def orient(*args): return _ui.VSeg_orient(*args)
    def getOrientStr(*args): return _ui.VSeg_getOrientStr(*args)
    def setSpecial(*args): return _ui.VSeg_setSpecial(*args)
    def isSpecial(*args): return _ui.VSeg_isSpecial(*args)
    def setPoints(*args): return _ui.VSeg_setPoints(*args)
    def setNet(*args): return _ui.VSeg_setNet(*args)
    def getNet(*args): return _ui.VSeg_getNet(*args)
    def setIndex(*args): return _ui.VSeg_setIndex(*args)
    def index(*args): return _ui.VSeg_index(*args)
    def bBox(*args): return _ui.VSeg_bBox(*args)
    def qBox(*args): return _ui.VSeg_qBox(*args)
    def objType(*args): return _ui.VSeg_objType(*args)
    def objName(*args): return _ui.VSeg_objName(*args)
    def layer(*args): return _ui.VSeg_layer(*args)
    def width(*args): return _ui.VSeg_width(*args)
    def area(*args): return _ui.VSeg_area(*args)
    def perimeter(*args): return _ui.VSeg_perimeter(*args)
    def getFirstVertex(*args): return _ui.VSeg_getFirstVertex(*args)
    def getLastVertex(*args): return _ui.VSeg_getLastVertex(*args)
    def extent(*args): return _ui.VSeg_extent(*args)
    def setExtent(*args): return _ui.VSeg_setExtent(*args)
    def origin(*args): return _ui.VSeg_origin(*args)
    def setOrigin(*args): return _ui.VSeg_setOrigin(*args)
    def ptInPoly(*args): return _ui.VSeg_ptInPoly(*args)
    def Move(*args): return _ui.VSeg_Move(*args)
    def Copy(*args): return _ui.VSeg_Copy(*args)
    def Flatten(*args): return _ui.VSeg_Flatten(*args)
    def getNearestEdge(*args): return _ui.VSeg_getNearestEdge(*args)
    def getNearestVertex(*args): return _ui.VSeg_getNearestVertex(*args)
    def getSegsInRect(*args): return _ui.VSeg_getSegsInRect(*args)
    def getVertsInRect(*args): return _ui.VSeg_getVertsInRect(*args)
    def transform(*args): return _ui.VSeg_transform(*args)
    def getNetName(*args): return _ui.VSeg_getNetName(*args)
    def length(*args): return _ui.VSeg_length(*args)
    def ptlist(*args): return _ui.VSeg_ptlist(*args)
    def nPoints(*args): return _ui.VSeg_nPoints(*args)
    def bias(*args): return _ui.VSeg_bias(*args)
    def scale(*args): return _ui.VSeg_scale(*args)

class VSegPtr(VSeg):
    def __init__(self, this):
        _swig_setattr(self, VSeg, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, VSeg, 'thisown', 0)
        self.__class__ = VSeg
_ui.VSeg_swigregister(VSegPtr)


drcInit = _ui.drcInit

geomBegin = _ui.geomBegin

drcUnInit = _ui.drcUnInit

geomEnd = _ui.geomEnd

geomAddShape = _ui.geomAddShape

geomAddShapes = _ui.geomAddShapes

geomStartPoly = _ui.geomStartPoly

geomAddPoly = _ui.geomAddPoly

geomMerge = _ui.geomMerge

geomNot = _ui.geomNot

geomConnect = _ui.geomConnect

geomOr = _ui.geomOr

geomSelectOr = _ui.geomSelectOr

geomAndNot = _ui.geomAndNot

geomXor = _ui.geomXor

geomTouching = _ui.geomTouching

geomOverlapping = _ui.geomOverlapping

geomInside = _ui.geomInside

geomContains = _ui.geomContains

geomOutside = _ui.geomOutside

geomAvoiding = _ui.geomAvoiding

geomButting = _ui.geomButting

geomCoincident = _ui.geomCoincident

geomEmpty = _ui.geomEmpty

geomHoles = _ui.geomHoles

geomNoHoles = _ui.geomNoHoles

geomGetNon90 = _ui.geomGetNon90

geomGetNon45 = _ui.geomGetNon45

geomGetRectangles = _ui.geomGetRectangles

geomGetPolygons = _ui.geomGetPolygons

setExtViewName = _ui.setExtViewName

saveInterconnect = _ui.saveInterconnect

extractTFT = _ui.extractTFT

extractDevice = _ui.extractDevice

extractMosCap = _ui.extractMosCap

extractDio = _ui.extractDio

extractBjt = _ui.extractBjt

extractParasitic = _ui.extractParasitic

extractParasitic2 = _ui.extractParasitic2

extractParasitic3 = _ui.extractParasitic3

geomReportMarkers = _ui.geomReportMarkers

geomGetCount = _ui.geomGetCount

geomGetTotalCount = _ui.geomGetTotalCount

geomNumShapes = _ui.geomNumShapes
class arcList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, arcList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, arcList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::arc > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, arcList, 'this', _ui.new_arcList(*args))
        _swig_setattr(self, arcList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_arcList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.arcList_clear(*args)
    def size(*args): return _ui.arcList_size(*args)
    def isEmpty(*args): return _ui.arcList_isEmpty(*args)
    def member(*args): return _ui.arcList_member(*args)
    def prepend(*args): return _ui.arcList_prepend(*args)
    def append(*args): return _ui.arcList_append(*args)
    def concat(*args): return _ui.arcList_concat(*args)
    def remove(*args): return _ui.arcList_remove(*args)
    def pop(*args): return _ui.arcList_pop(*args)
    def first(*args): return _ui.arcList_first(*args)
    def next(*args): return _ui.arcList_next(*args)
    def peek(*args): return _ui.arcList_peek(*args)
    def last(*args): return _ui.arcList_last(*args)
    def sort(*args): return _ui.arcList_sort(*args)
    def reverse(*args): return _ui.arcList_reverse(*args)

class arcListPtr(arcList):
    def __init__(self, this):
        _swig_setattr(self, arcList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, arcList, 'thisown', 0)
        self.__class__ = arcList
_ui.arcList_swigregister(arcListPtr)
none = cvar.none
samenet = cvar.samenet
diffnet = cvar.diffnet
vertical = cvar.vertical
horizontal = cvar.horizontal
diagonal = cvar.diagonal
project = cvar.project
parallel = cvar.parallel
abut = cvar.abut
not_equal = cvar.not_equal
equal = cvar.equal
greater = cvar.greater
edges = cvar.edges
output_only = cvar.output_only
opposite = cvar.opposite

geomGetShapes = _ui.geomGetShapes

geomGetRawShapes = _ui.geomGetRawShapes

geomGetEdges = _ui.geomGetEdges

geomLabel = _ui.geomLabel

geomAnd = _ui.geomAnd

geomSize = _ui.geomSize

geomTrapezoid = _ui.geomTrapezoid

geomGetTexted = _ui.geomGetTexted

geomSetText = _ui.geomSetText

geomBkgnd = _ui.geomBkgnd

geomErase = _ui.geomErase

saveDerived = _ui.saveDerived

extractMOS = _ui.extractMOS

extractRes = _ui.extractRes

extractParasitic3D = _ui.extractParasitic3D

geomWidth = _ui.geomWidth

geomAllowedWidths = _ui.geomAllowedWidths

geomLength = _ui.geomLength

geomSpace = _ui.geomSpace

geomSpace2 = _ui.geomSpace2

geomAllowedSpaces = _ui.geomAllowedSpaces

geom2DSpace = _ui.geom2DSpace

geomNotch = _ui.geomNotch

geomMargin = _ui.geomMargin

geomLineEnd = _ui.geomLineEnd

geomPitch = _ui.geomPitch

geomOverlap = _ui.geomOverlap

geomEnclose = _ui.geomEnclose

geomEnclose2 = _ui.geomEnclose2

geomAllowedEncs = _ui.geomAllowedEncs

geomExtension = _ui.geomExtension

geomArea = _ui.geomArea

geomAreaIn = _ui.geomAreaIn

geomOffGrid = _ui.geomOffGrid

geomAdjLength = _ui.geomAdjLength

geomAllowedSize = _ui.geomAllowedSize

geomMaxDensity = _ui.geomMaxDensity

geomMinDensity = _ui.geomMinDensity

class arrayList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, arrayList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, arrayList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::array > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, arrayList, 'this', _ui.new_arrayList(*args))
        _swig_setattr(self, arrayList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_arrayList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.arrayList_clear(*args)
    def size(*args): return _ui.arrayList_size(*args)
    def isEmpty(*args): return _ui.arrayList_isEmpty(*args)
    def member(*args): return _ui.arrayList_member(*args)
    def prepend(*args): return _ui.arrayList_prepend(*args)
    def append(*args): return _ui.arrayList_append(*args)
    def concat(*args): return _ui.arrayList_concat(*args)
    def remove(*args): return _ui.arrayList_remove(*args)
    def pop(*args): return _ui.arrayList_pop(*args)
    def first(*args): return _ui.arrayList_first(*args)
    def next(*args): return _ui.arrayList_next(*args)
    def peek(*args): return _ui.arrayList_peek(*args)
    def last(*args): return _ui.arrayList_last(*args)
    def sort(*args): return _ui.arrayList_sort(*args)
    def reverse(*args): return _ui.arrayList_reverse(*args)

class arrayListPtr(arrayList):
    def __init__(self, this):
        _swig_setattr(self, arrayList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, arrayList, 'thisown', 0)
        self.__class__ = arrayList
_ui.arrayList_swigregister(arrayListPtr)

class cellViewList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cellViewList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cellViewList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::cellView > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, cellViewList, 'this', _ui.new_cellViewList(*args))
        _swig_setattr(self, cellViewList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_cellViewList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.cellViewList_clear(*args)
    def size(*args): return _ui.cellViewList_size(*args)
    def isEmpty(*args): return _ui.cellViewList_isEmpty(*args)
    def member(*args): return _ui.cellViewList_member(*args)
    def prepend(*args): return _ui.cellViewList_prepend(*args)
    def append(*args): return _ui.cellViewList_append(*args)
    def concat(*args): return _ui.cellViewList_concat(*args)
    def remove(*args): return _ui.cellViewList_remove(*args)
    def pop(*args): return _ui.cellViewList_pop(*args)
    def first(*args): return _ui.cellViewList_first(*args)
    def next(*args): return _ui.cellViewList_next(*args)
    def peek(*args): return _ui.cellViewList_peek(*args)
    def last(*args): return _ui.cellViewList_last(*args)
    def sort(*args): return _ui.cellViewList_sort(*args)
    def reverse(*args): return _ui.cellViewList_reverse(*args)

class cellViewListPtr(cellViewList):
    def __init__(self, this):
        _swig_setattr(self, cellViewList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cellViewList, 'thisown', 0)
        self.__class__ = cellViewList
_ui.cellViewList_swigregister(cellViewListPtr)

class cellList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cellList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cellList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::cell > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, cellList, 'this', _ui.new_cellList(*args))
        _swig_setattr(self, cellList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_cellList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.cellList_clear(*args)
    def size(*args): return _ui.cellList_size(*args)
    def isEmpty(*args): return _ui.cellList_isEmpty(*args)
    def member(*args): return _ui.cellList_member(*args)
    def prepend(*args): return _ui.cellList_prepend(*args)
    def append(*args): return _ui.cellList_append(*args)
    def concat(*args): return _ui.cellList_concat(*args)
    def remove(*args): return _ui.cellList_remove(*args)
    def pop(*args): return _ui.cellList_pop(*args)
    def first(*args): return _ui.cellList_first(*args)
    def next(*args): return _ui.cellList_next(*args)
    def peek(*args): return _ui.cellList_peek(*args)
    def last(*args): return _ui.cellList_last(*args)
    def sort(*args): return _ui.cellList_sort(*args)
    def reverse(*args): return _ui.cellList_reverse(*args)

class cellListPtr(cellList):
    def __init__(self, this):
        _swig_setattr(self, cellList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cellList, 'thisown', 0)
        self.__class__ = cellList
_ui.cellList_swigregister(cellListPtr)

class lppList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lppList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lppList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::lpp > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, lppList, 'this', _ui.new_lppList(*args))
        _swig_setattr(self, lppList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_lppList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.lppList_clear(*args)
    def size(*args): return _ui.lppList_size(*args)
    def isEmpty(*args): return _ui.lppList_isEmpty(*args)
    def member(*args): return _ui.lppList_member(*args)
    def prepend(*args): return _ui.lppList_prepend(*args)
    def append(*args): return _ui.lppList_append(*args)
    def concat(*args): return _ui.lppList_concat(*args)
    def remove(*args): return _ui.lppList_remove(*args)
    def pop(*args): return _ui.lppList_pop(*args)
    def first(*args): return _ui.lppList_first(*args)
    def next(*args): return _ui.lppList_next(*args)
    def peek(*args): return _ui.lppList_peek(*args)
    def last(*args): return _ui.lppList_last(*args)
    def sort(*args): return _ui.lppList_sort(*args)
    def reverse(*args): return _ui.lppList_reverse(*args)

class lppListPtr(lppList):
    def __init__(self, this):
        _swig_setattr(self, lppList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, lppList, 'thisown', 0)
        self.__class__ = lppList
_ui.lppList_swigregister(lppListPtr)

class objList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, objList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, objList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<dbObj > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, objList, 'this', _ui.new_objList(*args))
        _swig_setattr(self, objList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_objList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.objList_clear(*args)
    def size(*args): return _ui.objList_size(*args)
    def isEmpty(*args): return _ui.objList_isEmpty(*args)
    def member(*args): return _ui.objList_member(*args)
    def prepend(*args): return _ui.objList_prepend(*args)
    def append(*args): return _ui.objList_append(*args)
    def concat(*args): return _ui.objList_concat(*args)
    def remove(*args): return _ui.objList_remove(*args)
    def pop(*args): return _ui.objList_pop(*args)
    def first(*args): return _ui.objList_first(*args)
    def next(*args): return _ui.objList_next(*args)
    def peek(*args): return _ui.objList_peek(*args)
    def last(*args): return _ui.objList_last(*args)
    def sort(*args): return _ui.objList_sort(*args)
    def reverse(*args): return _ui.objList_reverse(*args)

class objListPtr(objList):
    def __init__(self, this):
        _swig_setattr(self, objList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, objList, 'thisown', 0)
        self.__class__ = objList
_ui.objList_swigregister(objListPtr)

class ellipseList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ellipseList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ellipseList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::ellipse > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ellipseList, 'this', _ui.new_ellipseList(*args))
        _swig_setattr(self, ellipseList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_ellipseList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.ellipseList_clear(*args)
    def size(*args): return _ui.ellipseList_size(*args)
    def isEmpty(*args): return _ui.ellipseList_isEmpty(*args)
    def member(*args): return _ui.ellipseList_member(*args)
    def prepend(*args): return _ui.ellipseList_prepend(*args)
    def append(*args): return _ui.ellipseList_append(*args)
    def concat(*args): return _ui.ellipseList_concat(*args)
    def remove(*args): return _ui.ellipseList_remove(*args)
    def pop(*args): return _ui.ellipseList_pop(*args)
    def first(*args): return _ui.ellipseList_first(*args)
    def next(*args): return _ui.ellipseList_next(*args)
    def peek(*args): return _ui.ellipseList_peek(*args)
    def last(*args): return _ui.ellipseList_last(*args)
    def sort(*args): return _ui.ellipseList_sort(*args)
    def reverse(*args): return _ui.ellipseList_reverse(*args)

class ellipseListPtr(ellipseList):
    def __init__(self, this):
        _swig_setattr(self, ellipseList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ellipseList, 'thisown', 0)
        self.__class__ = ellipseList
_ui.ellipseList_swigregister(ellipseListPtr)

class dbHierObjList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dbHierObjList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dbHierObjList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::dbHierObj > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, dbHierObjList, 'this', _ui.new_dbHierObjList(*args))
        _swig_setattr(self, dbHierObjList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_dbHierObjList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.dbHierObjList_clear(*args)
    def size(*args): return _ui.dbHierObjList_size(*args)
    def isEmpty(*args): return _ui.dbHierObjList_isEmpty(*args)
    def member(*args): return _ui.dbHierObjList_member(*args)
    def prepend(*args): return _ui.dbHierObjList_prepend(*args)
    def append(*args): return _ui.dbHierObjList_append(*args)
    def concat(*args): return _ui.dbHierObjList_concat(*args)
    def remove(*args): return _ui.dbHierObjList_remove(*args)
    def pop(*args): return _ui.dbHierObjList_pop(*args)
    def first(*args): return _ui.dbHierObjList_first(*args)
    def next(*args): return _ui.dbHierObjList_next(*args)
    def peek(*args): return _ui.dbHierObjList_peek(*args)
    def last(*args): return _ui.dbHierObjList_last(*args)
    def sort(*args): return _ui.dbHierObjList_sort(*args)
    def reverse(*args): return _ui.dbHierObjList_reverse(*args)

class dbHierObjListPtr(dbHierObjList):
    def __init__(self, this):
        _swig_setattr(self, dbHierObjList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dbHierObjList, 'thisown', 0)
        self.__class__ = dbHierObjList
_ui.dbHierObjList_swigregister(dbHierObjListPtr)

class hsegList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hsegList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hsegList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::HSeg > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, hsegList, 'this', _ui.new_hsegList(*args))
        _swig_setattr(self, hsegList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_hsegList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.hsegList_clear(*args)
    def size(*args): return _ui.hsegList_size(*args)
    def isEmpty(*args): return _ui.hsegList_isEmpty(*args)
    def member(*args): return _ui.hsegList_member(*args)
    def prepend(*args): return _ui.hsegList_prepend(*args)
    def append(*args): return _ui.hsegList_append(*args)
    def concat(*args): return _ui.hsegList_concat(*args)
    def remove(*args): return _ui.hsegList_remove(*args)
    def pop(*args): return _ui.hsegList_pop(*args)
    def first(*args): return _ui.hsegList_first(*args)
    def next(*args): return _ui.hsegList_next(*args)
    def peek(*args): return _ui.hsegList_peek(*args)
    def last(*args): return _ui.hsegList_last(*args)
    def sort(*args): return _ui.hsegList_sort(*args)
    def reverse(*args): return _ui.hsegList_reverse(*args)

class hsegListPtr(hsegList):
    def __init__(self, this):
        _swig_setattr(self, hsegList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, hsegList, 'thisown', 0)
        self.__class__ = hsegList
_ui.hsegList_swigregister(hsegListPtr)

class instList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, instList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, instList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::inst > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, instList, 'this', _ui.new_instList(*args))
        _swig_setattr(self, instList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_instList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.instList_clear(*args)
    def size(*args): return _ui.instList_size(*args)
    def isEmpty(*args): return _ui.instList_isEmpty(*args)
    def member(*args): return _ui.instList_member(*args)
    def prepend(*args): return _ui.instList_prepend(*args)
    def append(*args): return _ui.instList_append(*args)
    def concat(*args): return _ui.instList_concat(*args)
    def remove(*args): return _ui.instList_remove(*args)
    def pop(*args): return _ui.instList_pop(*args)
    def first(*args): return _ui.instList_first(*args)
    def next(*args): return _ui.instList_next(*args)
    def peek(*args): return _ui.instList_peek(*args)
    def last(*args): return _ui.instList_last(*args)
    def sort(*args): return _ui.instList_sort(*args)
    def reverse(*args): return _ui.instList_reverse(*args)

class instListPtr(instList):
    def __init__(self, this):
        _swig_setattr(self, instList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, instList, 'thisown', 0)
        self.__class__ = instList
_ui.instList_swigregister(instListPtr)

class instPinList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, instPinList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, instPinList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::instPin > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, instPinList, 'this', _ui.new_instPinList(*args))
        _swig_setattr(self, instPinList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_instPinList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.instPinList_clear(*args)
    def size(*args): return _ui.instPinList_size(*args)
    def isEmpty(*args): return _ui.instPinList_isEmpty(*args)
    def member(*args): return _ui.instPinList_member(*args)
    def prepend(*args): return _ui.instPinList_prepend(*args)
    def append(*args): return _ui.instPinList_append(*args)
    def concat(*args): return _ui.instPinList_concat(*args)
    def remove(*args): return _ui.instPinList_remove(*args)
    def pop(*args): return _ui.instPinList_pop(*args)
    def first(*args): return _ui.instPinList_first(*args)
    def next(*args): return _ui.instPinList_next(*args)
    def peek(*args): return _ui.instPinList_peek(*args)
    def last(*args): return _ui.instPinList_last(*args)
    def sort(*args): return _ui.instPinList_sort(*args)
    def reverse(*args): return _ui.instPinList_reverse(*args)

class instPinListPtr(instPinList):
    def __init__(self, this):
        _swig_setattr(self, instPinList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, instPinList, 'thisown', 0)
        self.__class__ = instPinList
_ui.instPinList_swigregister(instPinListPtr)

class labelList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, labelList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, labelList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::label > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, labelList, 'this', _ui.new_labelList(*args))
        _swig_setattr(self, labelList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_labelList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.labelList_clear(*args)
    def size(*args): return _ui.labelList_size(*args)
    def isEmpty(*args): return _ui.labelList_isEmpty(*args)
    def member(*args): return _ui.labelList_member(*args)
    def prepend(*args): return _ui.labelList_prepend(*args)
    def append(*args): return _ui.labelList_append(*args)
    def concat(*args): return _ui.labelList_concat(*args)
    def remove(*args): return _ui.labelList_remove(*args)
    def pop(*args): return _ui.labelList_pop(*args)
    def first(*args): return _ui.labelList_first(*args)
    def next(*args): return _ui.labelList_next(*args)
    def peek(*args): return _ui.labelList_peek(*args)
    def last(*args): return _ui.labelList_last(*args)
    def sort(*args): return _ui.labelList_sort(*args)
    def reverse(*args): return _ui.labelList_reverse(*args)

class labelListPtr(labelList):
    def __init__(self, this):
        _swig_setattr(self, labelList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, labelList, 'thisown', 0)
        self.__class__ = labelList
_ui.labelList_swigregister(labelListPtr)

class libList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, libList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, libList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::library > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, libList, 'this', _ui.new_libList(*args))
        _swig_setattr(self, libList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_libList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.libList_clear(*args)
    def size(*args): return _ui.libList_size(*args)
    def isEmpty(*args): return _ui.libList_isEmpty(*args)
    def member(*args): return _ui.libList_member(*args)
    def prepend(*args): return _ui.libList_prepend(*args)
    def append(*args): return _ui.libList_append(*args)
    def concat(*args): return _ui.libList_concat(*args)
    def remove(*args): return _ui.libList_remove(*args)
    def pop(*args): return _ui.libList_pop(*args)
    def first(*args): return _ui.libList_first(*args)
    def next(*args): return _ui.libList_next(*args)
    def peek(*args): return _ui.libList_peek(*args)
    def last(*args): return _ui.libList_last(*args)
    def sort(*args): return _ui.libList_sort(*args)
    def reverse(*args): return _ui.libList_reverse(*args)

class libListPtr(libList):
    def __init__(self, this):
        _swig_setattr(self, libList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, libList, 'thisown', 0)
        self.__class__ = libList
_ui.libList_swigregister(libListPtr)

class mppList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mppList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mppList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::mpp > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mppList, 'this', _ui.new_mppList(*args))
        _swig_setattr(self, mppList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_mppList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.mppList_clear(*args)
    def size(*args): return _ui.mppList_size(*args)
    def isEmpty(*args): return _ui.mppList_isEmpty(*args)
    def member(*args): return _ui.mppList_member(*args)
    def prepend(*args): return _ui.mppList_prepend(*args)
    def append(*args): return _ui.mppList_append(*args)
    def concat(*args): return _ui.mppList_concat(*args)
    def remove(*args): return _ui.mppList_remove(*args)
    def pop(*args): return _ui.mppList_pop(*args)
    def first(*args): return _ui.mppList_first(*args)
    def next(*args): return _ui.mppList_next(*args)
    def peek(*args): return _ui.mppList_peek(*args)
    def last(*args): return _ui.mppList_last(*args)
    def sort(*args): return _ui.mppList_sort(*args)
    def reverse(*args): return _ui.mppList_reverse(*args)

class mppListPtr(mppList):
    def __init__(self, this):
        _swig_setattr(self, mppList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mppList, 'thisown', 0)
        self.__class__ = mppList
_ui.mppList_swigregister(mppListPtr)

class netList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, netList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, netList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::net > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, netList, 'this', _ui.new_netList(*args))
        _swig_setattr(self, netList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_netList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.netList_clear(*args)
    def size(*args): return _ui.netList_size(*args)
    def isEmpty(*args): return _ui.netList_isEmpty(*args)
    def member(*args): return _ui.netList_member(*args)
    def prepend(*args): return _ui.netList_prepend(*args)
    def append(*args): return _ui.netList_append(*args)
    def concat(*args): return _ui.netList_concat(*args)
    def remove(*args): return _ui.netList_remove(*args)
    def pop(*args): return _ui.netList_pop(*args)
    def first(*args): return _ui.netList_first(*args)
    def next(*args): return _ui.netList_next(*args)
    def peek(*args): return _ui.netList_peek(*args)
    def last(*args): return _ui.netList_last(*args)
    def sort(*args): return _ui.netList_sort(*args)
    def reverse(*args): return _ui.netList_reverse(*args)

class netListPtr(netList):
    def __init__(self, this):
        _swig_setattr(self, netList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, netList, 'thisown', 0)
        self.__class__ = netList
_ui.netList_swigregister(netListPtr)

class pathList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pathList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pathList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::path > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pathList, 'this', _ui.new_pathList(*args))
        _swig_setattr(self, pathList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pathList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.pathList_clear(*args)
    def size(*args): return _ui.pathList_size(*args)
    def isEmpty(*args): return _ui.pathList_isEmpty(*args)
    def member(*args): return _ui.pathList_member(*args)
    def prepend(*args): return _ui.pathList_prepend(*args)
    def append(*args): return _ui.pathList_append(*args)
    def concat(*args): return _ui.pathList_concat(*args)
    def remove(*args): return _ui.pathList_remove(*args)
    def pop(*args): return _ui.pathList_pop(*args)
    def first(*args): return _ui.pathList_first(*args)
    def next(*args): return _ui.pathList_next(*args)
    def peek(*args): return _ui.pathList_peek(*args)
    def last(*args): return _ui.pathList_last(*args)
    def sort(*args): return _ui.pathList_sort(*args)
    def reverse(*args): return _ui.pathList_reverse(*args)

class pathListPtr(pathList):
    def __init__(self, this):
        _swig_setattr(self, pathList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pathList, 'thisown', 0)
        self.__class__ = pathList
_ui.pathList_swigregister(pathListPtr)

class pinList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pinList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pinList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::pin > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pinList, 'this', _ui.new_pinList(*args))
        _swig_setattr(self, pinList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_pinList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.pinList_clear(*args)
    def size(*args): return _ui.pinList_size(*args)
    def isEmpty(*args): return _ui.pinList_isEmpty(*args)
    def member(*args): return _ui.pinList_member(*args)
    def prepend(*args): return _ui.pinList_prepend(*args)
    def append(*args): return _ui.pinList_append(*args)
    def concat(*args): return _ui.pinList_concat(*args)
    def remove(*args): return _ui.pinList_remove(*args)
    def pop(*args): return _ui.pinList_pop(*args)
    def first(*args): return _ui.pinList_first(*args)
    def next(*args): return _ui.pinList_next(*args)
    def peek(*args): return _ui.pinList_peek(*args)
    def last(*args): return _ui.pinList_last(*args)
    def sort(*args): return _ui.pinList_sort(*args)
    def reverse(*args): return _ui.pinList_reverse(*args)

class pinListPtr(pinList):
    def __init__(self, this):
        _swig_setattr(self, pinList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pinList, 'thisown', 0)
        self.__class__ = pinList
_ui.pinList_swigregister(pinListPtr)

class polyList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, polyList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, polyList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::polygon > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, polyList, 'this', _ui.new_polyList(*args))
        _swig_setattr(self, polyList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_polyList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.polyList_clear(*args)
    def size(*args): return _ui.polyList_size(*args)
    def isEmpty(*args): return _ui.polyList_isEmpty(*args)
    def member(*args): return _ui.polyList_member(*args)
    def prepend(*args): return _ui.polyList_prepend(*args)
    def append(*args): return _ui.polyList_append(*args)
    def concat(*args): return _ui.polyList_concat(*args)
    def remove(*args): return _ui.polyList_remove(*args)
    def pop(*args): return _ui.polyList_pop(*args)
    def first(*args): return _ui.polyList_first(*args)
    def next(*args): return _ui.polyList_next(*args)
    def peek(*args): return _ui.polyList_peek(*args)
    def last(*args): return _ui.polyList_last(*args)
    def sort(*args): return _ui.polyList_sort(*args)
    def reverse(*args): return _ui.polyList_reverse(*args)

class polyListPtr(polyList):
    def __init__(self, this):
        _swig_setattr(self, polyList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, polyList, 'thisown', 0)
        self.__class__ = polyList
_ui.polyList_swigregister(polyListPtr)

class rectList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rectList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rectList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::rectangle > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, rectList, 'this', _ui.new_rectList(*args))
        _swig_setattr(self, rectList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_rectList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.rectList_clear(*args)
    def size(*args): return _ui.rectList_size(*args)
    def isEmpty(*args): return _ui.rectList_isEmpty(*args)
    def member(*args): return _ui.rectList_member(*args)
    def prepend(*args): return _ui.rectList_prepend(*args)
    def append(*args): return _ui.rectList_append(*args)
    def concat(*args): return _ui.rectList_concat(*args)
    def remove(*args): return _ui.rectList_remove(*args)
    def pop(*args): return _ui.rectList_pop(*args)
    def first(*args): return _ui.rectList_first(*args)
    def next(*args): return _ui.rectList_next(*args)
    def peek(*args): return _ui.rectList_peek(*args)
    def last(*args): return _ui.rectList_last(*args)
    def sort(*args): return _ui.rectList_sort(*args)
    def reverse(*args): return _ui.rectList_reverse(*args)

class rectListPtr(rectList):
    def __init__(self, this):
        _swig_setattr(self, rectList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, rectList, 'thisown', 0)
        self.__class__ = rectList
_ui.rectList_swigregister(rectListPtr)

class shapeList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shapeList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shapeList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::shape > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, shapeList, 'this', _ui.new_shapeList(*args))
        _swig_setattr(self, shapeList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_shapeList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.shapeList_clear(*args)
    def size(*args): return _ui.shapeList_size(*args)
    def isEmpty(*args): return _ui.shapeList_isEmpty(*args)
    def member(*args): return _ui.shapeList_member(*args)
    def prepend(*args): return _ui.shapeList_prepend(*args)
    def append(*args): return _ui.shapeList_append(*args)
    def concat(*args): return _ui.shapeList_concat(*args)
    def remove(*args): return _ui.shapeList_remove(*args)
    def pop(*args): return _ui.shapeList_pop(*args)
    def first(*args): return _ui.shapeList_first(*args)
    def next(*args): return _ui.shapeList_next(*args)
    def peek(*args): return _ui.shapeList_peek(*args)
    def last(*args): return _ui.shapeList_last(*args)
    def sort(*args): return _ui.shapeList_sort(*args)
    def reverse(*args): return _ui.shapeList_reverse(*args)

class shapeListPtr(shapeList):
    def __init__(self, this):
        _swig_setattr(self, shapeList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, shapeList, 'thisown', 0)
        self.__class__ = shapeList
_ui.shapeList_swigregister(shapeListPtr)

class signalList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, signalList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, signalList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::signal > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, signalList, 'this', _ui.new_signalList(*args))
        _swig_setattr(self, signalList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_signalList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.signalList_clear(*args)
    def size(*args): return _ui.signalList_size(*args)
    def isEmpty(*args): return _ui.signalList_isEmpty(*args)
    def member(*args): return _ui.signalList_member(*args)
    def prepend(*args): return _ui.signalList_prepend(*args)
    def append(*args): return _ui.signalList_append(*args)
    def concat(*args): return _ui.signalList_concat(*args)
    def remove(*args): return _ui.signalList_remove(*args)
    def pop(*args): return _ui.signalList_pop(*args)
    def first(*args): return _ui.signalList_first(*args)
    def next(*args): return _ui.signalList_next(*args)
    def peek(*args): return _ui.signalList_peek(*args)
    def last(*args): return _ui.signalList_last(*args)
    def sort(*args): return _ui.signalList_sort(*args)
    def reverse(*args): return _ui.signalList_reverse(*args)

class signalListPtr(signalList):
    def __init__(self, this):
        _swig_setattr(self, signalList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, signalList, 'thisown', 0)
        self.__class__ = signalList
_ui.signalList_swigregister(signalListPtr)

class viaList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, viaList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, viaList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::via > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, viaList, 'this', _ui.new_viaList(*args))
        _swig_setattr(self, viaList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viaList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.viaList_clear(*args)
    def size(*args): return _ui.viaList_size(*args)
    def isEmpty(*args): return _ui.viaList_isEmpty(*args)
    def member(*args): return _ui.viaList_member(*args)
    def prepend(*args): return _ui.viaList_prepend(*args)
    def append(*args): return _ui.viaList_append(*args)
    def concat(*args): return _ui.viaList_concat(*args)
    def remove(*args): return _ui.viaList_remove(*args)
    def pop(*args): return _ui.viaList_pop(*args)
    def first(*args): return _ui.viaList_first(*args)
    def next(*args): return _ui.viaList_next(*args)
    def peek(*args): return _ui.viaList_peek(*args)
    def last(*args): return _ui.viaList_last(*args)
    def sort(*args): return _ui.viaList_sort(*args)
    def reverse(*args): return _ui.viaList_reverse(*args)

class viaListPtr(viaList):
    def __init__(self, this):
        _swig_setattr(self, viaList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viaList, 'thisown', 0)
        self.__class__ = viaList
_ui.viaList_swigregister(viaListPtr)

class viaInstList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, viaInstList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, viaInstList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::viaInst > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, viaInstList, 'this', _ui.new_viaInstList(*args))
        _swig_setattr(self, viaInstList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viaInstList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.viaInstList_clear(*args)
    def size(*args): return _ui.viaInstList_size(*args)
    def isEmpty(*args): return _ui.viaInstList_isEmpty(*args)
    def member(*args): return _ui.viaInstList_member(*args)
    def prepend(*args): return _ui.viaInstList_prepend(*args)
    def append(*args): return _ui.viaInstList_append(*args)
    def concat(*args): return _ui.viaInstList_concat(*args)
    def remove(*args): return _ui.viaInstList_remove(*args)
    def pop(*args): return _ui.viaInstList_pop(*args)
    def first(*args): return _ui.viaInstList_first(*args)
    def next(*args): return _ui.viaInstList_next(*args)
    def peek(*args): return _ui.viaInstList_peek(*args)
    def last(*args): return _ui.viaInstList_last(*args)
    def sort(*args): return _ui.viaInstList_sort(*args)
    def reverse(*args): return _ui.viaInstList_reverse(*args)

class viaInstListPtr(viaInstList):
    def __init__(self, this):
        _swig_setattr(self, viaInstList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viaInstList, 'thisown', 0)
        self.__class__ = viaInstList
_ui.viaInstList_swigregister(viaInstListPtr)

class viewList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, viewList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, viewList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::view > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, viewList, 'this', _ui.new_viewList(*args))
        _swig_setattr(self, viewList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_viewList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.viewList_clear(*args)
    def size(*args): return _ui.viewList_size(*args)
    def isEmpty(*args): return _ui.viewList_isEmpty(*args)
    def member(*args): return _ui.viewList_member(*args)
    def prepend(*args): return _ui.viewList_prepend(*args)
    def append(*args): return _ui.viewList_append(*args)
    def concat(*args): return _ui.viewList_concat(*args)
    def remove(*args): return _ui.viewList_remove(*args)
    def pop(*args): return _ui.viewList_pop(*args)
    def first(*args): return _ui.viewList_first(*args)
    def next(*args): return _ui.viewList_next(*args)
    def peek(*args): return _ui.viewList_peek(*args)
    def last(*args): return _ui.viewList_last(*args)
    def sort(*args): return _ui.viewList_sort(*args)
    def reverse(*args): return _ui.viewList_reverse(*args)

class viewListPtr(viewList):
    def __init__(self, this):
        _swig_setattr(self, viewList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, viewList, 'thisown', 0)
        self.__class__ = viewList
_ui.viewList_swigregister(viewListPtr)

class vsegList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vsegList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vsegList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ dbObjList<cdb::VSeg > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vsegList, 'this', _ui.new_vsegList(*args))
        _swig_setattr(self, vsegList, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_vsegList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def clear(*args): return _ui.vsegList_clear(*args)
    def size(*args): return _ui.vsegList_size(*args)
    def isEmpty(*args): return _ui.vsegList_isEmpty(*args)
    def member(*args): return _ui.vsegList_member(*args)
    def prepend(*args): return _ui.vsegList_prepend(*args)
    def append(*args): return _ui.vsegList_append(*args)
    def concat(*args): return _ui.vsegList_concat(*args)
    def remove(*args): return _ui.vsegList_remove(*args)
    def pop(*args): return _ui.vsegList_pop(*args)
    def first(*args): return _ui.vsegList_first(*args)
    def next(*args): return _ui.vsegList_next(*args)
    def peek(*args): return _ui.vsegList_peek(*args)
    def last(*args): return _ui.vsegList_last(*args)
    def sort(*args): return _ui.vsegList_sort(*args)
    def reverse(*args): return _ui.vsegList_reverse(*args)

class vsegListPtr(vsegList):
    def __init__(self, this):
        _swig_setattr(self, vsegList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vsegList, 'thisown', 0)
        self.__class__ = vsegList
_ui.vsegList_swigregister(vsegListPtr)

class intarray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intarray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intarray, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ intarray instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, intarray, 'this', _ui.new_intarray(*args))
        _swig_setattr(self, intarray, 'thisown', 1)
    def __del__(self, destroy=_ui.delete_intarray):
        try:
            if self.thisown: destroy(self)
        except: pass

    def __getitem__(*args): return _ui.intarray___getitem__(*args)
    def __setitem__(*args): return _ui.intarray___setitem__(*args)
    def cast(*args): return _ui.intarray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _ui.intarray_frompointer
    if _newclass:frompointer = staticmethod(_ui.intarray_frompointer)

class intarrayPtr(intarray):
    def __init__(self, this):
        _swig_setattr(self, intarray, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, intarray, 'thisown', 0)
        self.__class__ = intarray
_ui.intarray_swigregister(intarrayPtr)

intarray_frompointer = _ui.intarray_frompointer

def getSelectedSet() :
  result = []
  objs = cvar.uiptr.getSelectedSet()
  obj = objs.first()
  while obj :
    result.append(obj)
    obj = objs.next()
  return result

def selectObj(obj) :
  cvar.uiptr.selectObj(obj)

def addSelected(obj) :
  cvar.uiptr.addSelected(obj)

def getEditCellView() :
  return cvar.uiptr.getEditCellView()

def getLibByName(name) :
  return cvar.dbptr.getLibByName(name)

def deleteObj(obj) :
	cvar.uiptr.deselectObj(obj)
	cv = cvar.uiptr.getEditCellView()
	cv.dbDeleteObj(obj, True, True)

def getLibList() :
  result = []
  libs = cvar.uiptr.getLibList()
  lib = libs.first()
  while lib :
    result.append(lib)
    lib = libs.next()
  return result

def getCellList() :
  result = []
  cells = cvar.uiptr.getCellList()
  cv = cells.first()
  while cv :
    result.append(cv)
    cv = cells.next()
  return result



