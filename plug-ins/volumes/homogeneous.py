import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

kPluginNodeName = "MitsubaHomogeneousParticipatingMedium"
kPluginNodeClassify = "shader/volume"
kPluginNodeId = OpenMaya.MTypeId(0x87005)

class homogeneous(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mMaterial = OpenMaya.MObject()

        mUseSigmaAS = OpenMaya.MObject()
        mSigmaA = OpenMaya.MObject()
        mSigmaS = OpenMaya.MObject()

        mUserSigmaTAlbedo = OpenMaya.MObject()
        mSigmaT = OpenMaya.MObject()
        mAlbedo = OpenMaya.MObject()

        mScale = OpenMaya.MObject()

        mPhaseFunction = OpenMaya.MObject()
        mPhaseFunctionHGG = OpenMaya.MObject()
        mPhaseFunctionMicroFlakeStdDev = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == homogeneous.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( homogeneous.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter

def nodeCreator():
    return homogeneous()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        homogeneous.mMaterial = eAttr.create("material", "mat")
        eAttr.setKeyable(1) 
        eAttr.setStorable(1)
        eAttr.setReadable(1)
        eAttr.setWritable(1)

        Materials = ["Apple",
            "Cream",
            "Skimmilk",
            "Spectralon",
            "Chicken1",
            "Ketchup",
            "Skin1",
            "Wholemilk",
            "Chicken2",
            "Potato",
            "Skin2",
            "Lowfat Milk",
            "Reduced Milk",
            "Regular Milk",
            "Espresso",
            "Mint Mocha Coffee",
            "Lowfat Soy Milk",
            "Regular Soy Milk",
            "Lowfat Chocolate Milk",
            "Regular Chocolate Milk",
            "Coke",
            "Pepsi Sprite", 
            "Gatorade",
            "Chardonnay",
            "White Zinfandel",
            "Merlot",
            "Budweiser Beer",
            "Coors Light Beer",
            "Clorox",
            "Apple Juice",
            "Cranberry Juice",
            "Grape Juice",
            "Ruby Grapefruit Juice",
            "White Grapefruit Juice",
            "Shampoo",
            "Strawberry Shampoo",
            "Head & Shoulders Shampoo",
            "Lemon Tea Powder",
            "Orange Juice Powder",
            "Pink Lemonade Powder",
            "Cappuccino Powder",
            "Salt Powder",
            "Sugar Powder",
            "Suisse Mocha"
        ]

        for i in range(len(Materials)):
            eAttr.addField(Materials[i], i)

        # Default to Skin1
        eAttr.setDefault(6)

        homogeneous.mUseSigmaAS = nAttr.create("useSigmaAS","sas", OpenMaya.MFnNumericData.kBoolean, False)
        nAttr.setKeyable(0) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        homogeneous.mSigmaA = nAttr.createColor("sigmaA", "sa")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        homogeneous.mSigmaS = nAttr.createColor("sigmaS", "ss")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        homogeneous.mUserSigmaTAlbedo = nAttr.create("useSigmaTAlbedo","sta", OpenMaya.MFnNumericData.kBoolean, False)
        nAttr.setKeyable(0) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        homogeneous.mSigmaT = nAttr.createColor("sigmaT", "st")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        homogeneous.mAlbedo = nAttr.createColor("albedo", "a")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        homogeneous.mScale = nAttr.create("scale","s", OpenMaya.MFnNumericData.kFloat, 1.0)
        nAttr.setKeyable(0) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        homogeneous.mPhaseFunction = eAttr.create("phaseFunction", "pf")
        eAttr.setKeyable(1) 
        eAttr.setStorable(1)
        eAttr.setReadable(1)
        eAttr.setWritable(1)

        PhaseFunctions = ["Isotropic",
            "Henyey-Greenstein",
            "Rayleigh",
            "Kajiya-Kay",
            "Micro-Flake"
        ]

        for i in range(len(PhaseFunctions)):
            eAttr.addField(PhaseFunctions[i], i)

        # Default to Isotropic
        eAttr.setDefault(0)

        homogeneous.mPhaseFunctionHGG = nAttr.create("phaseFunctionHGG","pfhgg", OpenMaya.MFnNumericData.kFloat, 0.0)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        homogeneous.mPhaseFunctionMicroFlakeStdDev = nAttr.create("phaseFunctionMFSD","pfmfsd", OpenMaya.MFnNumericData.kFloat, 0.05)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        homogeneous.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)

    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        homogeneous.addAttribute(homogeneous.mMaterial)

        homogeneous.addAttribute(homogeneous.mUseSigmaAS)
        homogeneous.addAttribute(homogeneous.mSigmaA)
        homogeneous.addAttribute(homogeneous.mSigmaS)

        homogeneous.addAttribute(homogeneous.mUserSigmaTAlbedo)
        homogeneous.addAttribute(homogeneous.mSigmaT)
        homogeneous.addAttribute(homogeneous.mAlbedo)

        homogeneous.addAttribute(homogeneous.mScale)

        homogeneous.addAttribute(homogeneous.mPhaseFunction)
        homogeneous.addAttribute(homogeneous.mPhaseFunctionHGG)
        homogeneous.addAttribute(homogeneous.mPhaseFunctionMicroFlakeStdDev)

        homogeneous.addAttribute(homogeneous.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    '''
    try:
        homogeneous.attributeAffects (homogeneous.mSigmaA, homogeneous.mOutColor)
        homogeneous.attributeAffects (homogeneous.mUseSigmaAS, homogeneous.mUserSigmaTAlbedo)
        homogeneous.attributeAffects (homogeneous.mUserSigmaTAlbedo, homogeneous.mUseSigmaAS)
    except:
        sys.stderr.write("Failed in setting attributeAffects\n")
        raise
    '''

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, kPluginNodeId, nodeCreator, 
                    nodeInitializer, OpenMayaMPx.MPxNode.kDependNode, kPluginNodeClassify )
    except:
        sys.stderr.write( "Failed to register node: %s" % kPluginNodeName )
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( kPluginNodeId )
    except:
        sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeName )
        raise
