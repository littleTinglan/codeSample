import maya.cmds as mc
import sys
import os

# UI
def UI():

    # Check if the window already existed, delete the window if it previously existed

    if mc.window('faceRigTool', exists=True):
        mc.deleteUI('faceRigTool')

    # Create a window
    mc.window('faceRigTool')
    mc.columnLayout(w=450, h=300)
    mc.frameLayout(l='Auto Face Rig Tool', w=450, h=300)
    #mc.setParent('..')
    # step 1
    # Name the character
    mc.textFieldGrp('charName', label='Step 1: Character Name:')
    # step 2 - Adjust joints positions
    mc.text(label='Step 2: Align all joints with your character', al = 'center')
    # step 3 - Create joints
    mc.button(w=200,label='Step 3: Create Joints', command='createJnt()')
    # step 4 - Create Rig
    mc.button(label='Step 4: Create Rig', command='createRig()')
    # step 5 - Bind face
    mc.text(label='Step 5: Bind face')
    # step 6 - Attach blendshapes
    mc.button(label='Step 6: Attach blend shapes', command='attachBlendShapes()')
    mc.showWindow('faceRigTool')


UI()

#This function will create floating joints for user to position around the model
def createJnt():
    charName = mc.textFieldGrp('charName', query=True, text=True)
    #create joint chain 
    mc.joint(name='c_' + charName + '_neck_joint_bind')
    mc.joint(name='c_' + charName + '_head_joint_bind', position=(0, 5, 1))
    mc.joint(name='c_' + charName + '_headTop_joint', position=(0, 10, 1))
    mc.joint(name='c_' + charName + '_headAim_joint_end', position=(0, 10, 5))
    mc.joint(name='c_' + charName + '_jaw_joint_bind', position=(0, 5, 2))
    mc.joint(name='c_' + charName + '_jawAim_joint_end', position=(0, 5, 5))
    mc.select('c_*')
    mc.parent(world=True)

    mc.setAttr('c_' + charName + '_neck_joint_bind.translateX', lock=True)
    mc.setAttr('c_' + charName + '_neck_joint_bind.translateY', lock=True)
    mc.setAttr('c_' + charName + '_neck_joint_bind.translateZ', lock=True)
    mc.setAttr('c_' + charName + '_head_joint_bind.translateX', lock=True)
    mc.setAttr('c_' + charName + '_headTop_joint.translateX', lock=True)
    mc.setAttr('c_' + charName + '_headAim_joint_end.translateX', lock=True)
    mc.setAttr('c_' + charName + '_jaw_joint_bind.translateX', lock=True)
    mc.setAttr('c_' + charName + '_jawAim_joint_end.translateX', lock=True)

    #Create a text curve specify the name of the joint for each joint 
    mc.textCurves(text='NECK', name='Temp_neckText')
    mc.setAttr('Temp_neckTextShape.rotateY', 90)
    mc.setAttr('Temp_neckTextShape.template', 1)
    mc.parent('Temp_neckTextShape', 'c_' + charName + '_neck_joint_bind')

    mc.textCurves(text='HEAD', name='Temp_headText')
    mc.setAttr('Temp_headTextShape.rotateY', 90)
    mc.setAttr('Temp_headTextShape.translateY', 5)
    mc.setAttr('Temp_headTextShape.translateZ', 1)
    mc.setAttr('Temp_headTextShape.template', 1)
    mc.parent('Temp_headTextShape', 'c_' + charName + '_head_joint_bind')

    mc.textCurves(text='HEAD_TOP', name='Temp_headTopText')
    mc.setAttr('Temp_headTopTextShape.rotateY', 90)
    mc.setAttr('Temp_headTopTextShape.translateY', 10)
    mc.setAttr('Temp_headTopTextShape.translateZ', 1)
    mc.setAttr('Temp_headTopTextShape.template', 1)
    mc.parent('Temp_headTopTextShape', 'c_' + charName + '_headTop_joint')

    mc.textCurves(text='HEAD_AIM', name='Temp_headAimText')
    mc.setAttr('Temp_headAimTextShape.rotateY', 90)
    mc.setAttr('Temp_headAimTextShape.translateY', 10)
    mc.setAttr('Temp_headAimTextShape.translateZ', 5)
    mc.setAttr('Temp_headAimTextShape.template', 1)
    mc.parent('Temp_headAimTextShape', 'c_' + charName + '_headAim_joint_end')

    mc.textCurves(text='JAW', name='Temp_jawText')
    mc.setAttr('Temp_jawTextShape.rotateY', 90)
    mc.setAttr('Temp_jawTextShape.translateY', 5)
    mc.setAttr('Temp_jawTextShape.translateZ', 2)
    mc.setAttr('Temp_jawTextShape.template', 1)
    mc.parent('Temp_jawTextShape', 'c_' + charName + '_jaw_joint_bind')

    mc.textCurves(text='JAW_AIM', name='Temp_jawAimText')
    mc.setAttr('Temp_jawAimTextShape.rotateY', 90)
    mc.setAttr('Temp_jawAimTextShape.translateY', 5)
    mc.setAttr('Temp_jawAimTextShape.translateZ', 5)
    mc.setAttr('Temp_jawAimTextShape.template', 1)
    mc.parent('Temp_jawAimTextShape', 'c_' + charName + '_jawAim_joint_end')
    sys.stdout.write('skeleton complete')

#This function will create a controller latter used in the CreateRig step 
def createController(ctrlName, charName, alignment):
    #Create the limit box
    mc.nurbsSquare(name=charName + '_' + ctrlName + '_limitBox')
    mc.setAttr(charName + '_' + ctrlName + '_limitBox.scaleX', 2.5)
    mc.setAttr(charName + '_' + ctrlName + '_limitBox.scaleY', 2.5)
    mc.makeIdentity(apply=True, scale=True)
    mc.setAttr('top' + charName + '_' + ctrlName + '_limitBox.template', True)
    mc.setAttr('left' + charName + '_' + ctrlName + '_limitBox.template', True)
    mc.setAttr('bottom' + charName + '_' + ctrlName+ '_limitBox.template', True)
    mc.setAttr('right' + charName + '_' + ctrlName+ '_limitBox.template', True)
    
    #Create handle
    ctrlHandleName = charName + '_' + ctrlName + '_ctrl'
    mc.circle(name=ctrlHandleName)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.scaleX', .2)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.scaleY', .2)
    mc.makeIdentity(apply=True, scale=True)
    
    #Limit the handle transform so that it will be only moving within the box
    mc.transformLimits(tx=(-1, 1), etx=(True, True))
    mc.transformLimits(tx=(-1, 1), ety=(True, True))
    #Lock rotation, scale and translate on Z-axis 
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.translateZ', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.rotateX', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.rotateY', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.rotateZ', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.scaleX', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.scaleY', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.scaleZ', lock=True, keyable=False, channelBox=False)
    mc.setAttr(charName + '_' + ctrlName + '_ctrl.visibility', lock=True, keyable=False, channelBox=False)

    #alignment
    if alignment == 'center':
        colorYellow(ctrlHandleName)
    elif alignment == 'right':
        colorRed(ctrlHandleName)
    else:
        colorBlue(ctrlHandleName)

    mc.textCurves(text=ctrlName, name=charName + '_' + ctrlName + '_label_')
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.translateX', -1.2)
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.translateY', 1.3)
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.scaleX', .5)
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.scaleY', .5)
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.scaleZ', .5)
    mc.setAttr(charName + '_' + ctrlName + '_label_Shape.template', True)
    mc.parent(charName + '_' + ctrlName + '_ctrl', charName + '_' + ctrlName + '_label_Shape', charName + '_' + ctrlName + '_limitBox')

#Helper functions for CreateControllers
def colorYellow(ctrl):
    mc.select(ctrl)
    mc.pickWalk(direction='down')
    mc.setAttr(ctrl + '.overrideEnabled', 1)
    mc.setAttr(ctrl + '.overrideColor', 17)

def colorBlue(ctrl):
    mc.select(ctrl)
    mc.pickWalk(direction='down')
    mc.setAttr(ctrl + '.overrideEnabled', 1)
    mc.setAttr(ctrl + '.overrideColor', 6)

def colorRed(ctrl):
    mc.select(ctrl)
    mc.pickWalk(direction='down')
    mc.setAttr(ctrl + '.overrideEnabled', 1)
    mc.setAttr(ctrl + '.overrideColor', 13)

#After user adjusted the floating joints, create a rig
def createRig():
    charName = mc.textFieldGrp('charName', query=True, text=True)
    mc.setAttr('c_' + charName + '_neck_joint_bind.translateX', lock=False)
    mc.setAttr('c_' + charName + '_neck_joint_bind.translateY', lock=False)
    mc.setAttr('c_' + charName + '_neck_joint_bind.translateZ', lock=False)
    mc.setAttr('c_' + charName + '_head_joint_bind.translateX', lock=False)
    mc.setAttr('c_' + charName + '_headTop_joint.translateX', lock=False)
    mc.setAttr('c_' + charName + '_headAim_joint_end.translateX', lock=False)
    mc.setAttr('c_' + charName + '_jaw_joint_bind.translateX', lock=False)
    mc.setAttr('c_' + charName + '_jawAim_joint_end.translateX', lock=False)

    #Constrains
    mc.aimConstraint('c_' + charName + '_head_joint_bind', 'c_' + charName + '_neck_joint_bind', name='Temp_NeckConst')
    mc.aimConstraint('c_' + charName + '_headTop_joint', 'c_' + charName + '_head_joint_bind', name='Temp_HeadConst')
    mc.aimConstraint('c_' + charName + '_headAim_joint_end', 'c_' + charName + '_headTop_joint', name='Temp_headTopConst')
    mc.aimConstraint('c_' + charName + '_headTop_joint', 'c_' + charName + '_headAim_joint_end', name='Temp_headAimConst', aimVector=(-1, 0, 0))
    mc.aimConstraint('c_' + charName + '_jawAim_joint_end', 'c_' + charName + '_jaw_joint_bind', name='Temp_jawConst')
    mc.aimConstraint('c_' + charName + '_jaw_joint_bind', 'c_' + charName + '_jawAim_joint_end', name='Temp_jawAimConst', aimVector=(-1, 0, 0))

    #Parent the joints
    mc.parent('c_' + charName + '_head_joint_bind', 'c_' + charName + '_neck_joint_bind')
    mc.parent('c_' + charName + '_headTop_joint', 'c_' + charName + '_head_joint_bind')
    mc.parent('c_' + charName + '_headAim_joint_end', 'c_' + charName + '_jaw_joint_bind', 'c_' + charName + '_headTop_joint')
    mc.parent('c_' + charName + '_jawAim_joint_end', 'c_' + charName + '_jaw_joint_bind')
    mc.delete('Temp_*')
    mc.select(all=True)
    mc.select(deselect=True)

    #Create Controllers
    createController('L_Eye_Blink', charName, 'left')
    mc.setAttr(charName + '_L_Eye_Blink_limitBox.translateX', 11)
    mc.setAttr(charName + '_L_Eye_Blink_limitBox.translateY', 4.3)
    mc.setAttr(charName + '_L_Eye_Blink_limitBox.scaleX', .5)
    mc.setAttr(charName + '_L_Eye_Blink_limitBox.scaleY', .5)
    mc.setAttr(charName + '_L_Eye_Blink_limitBox.scaleZ', .5)

    createController('R_Eye_Blink', charName, 'right')
    mc.setAttr(charName + '_R_Eye_Blink_limitBox.translateX', 9)
    mc.setAttr(charName + '_R_Eye_Blink_limitBox.translateY', 4.3)
    mc.setAttr(charName + '_R_Eye_Blink_limitBox.scaleX', .5)
    mc.setAttr(charName + '_R_Eye_Blink_limitBox.scaleY', .5)
    mc.setAttr(charName + '_R_Eye_Blink_limitBox.scaleZ', .5)

    createController('L_Mouth', charName, 'left')
    mc.setAttr(charName + '_L_Mouth_limitBox.translateX', 11)
    mc.setAttr(charName + '_L_Mouth_limitBox.translateY', 5.9)
    mc.setAttr(charName + '_L_Mouth_limitBox.scaleX', .5)
    mc.setAttr(charName + '_L_Mouth_limitBox.scaleY', .5)
    mc.setAttr(charName + '_L_Mouth_limitBox.scaleZ', .5)

    createController('R_Mouth', charName, 'right')
    mc.setAttr(charName + '_R_Mouth_limitBox.translateX', 9)
    mc.setAttr(charName + '_R_Mouth_limitBox.translateY', 5.9)
    mc.setAttr(charName + '_R_Mouth_limitBox.scaleX', .5)
    mc.setAttr(charName + '_R_Mouth_limitBox.scaleY', .5)
    mc.setAttr(charName + '_R_Mouth_limitBox.scaleZ', .5)

    createController('L_Eye', charName, 'left')
    mc.setAttr(charName + '_L_Eye_limitBox.translateX', 11)
    mc.setAttr(charName + '_L_Eye_limitBox.translateY', 7.5)
    mc.setAttr(charName + '_L_Eye_limitBox.scaleX', .5)
    mc.setAttr(charName + '_L_Eye_limitBox.scaleY', .5)
    mc.setAttr(charName + '_L_Eye_limitBox.scaleZ', .5)

    createController('R_Eye', charName, 'right')
    mc.setAttr(charName + '_R_Eye_limitBox.translateX', 9)
    mc.setAttr(charName + '_R_Eye_limitBox.translateY', 7.5)
    mc.setAttr(charName + '_R_Eye_limitBox.scaleX', .5)
    mc.setAttr(charName + '_R_Eye_limitBox.scaleY', .5)
    mc.setAttr(charName + '_R_Eye_limitBox.scaleZ', .5)

    createController('L_Brow', charName, 'left')
    mc.setAttr(charName + '_L_Brow_limitBox.translateX', 11)
    mc.setAttr(charName + '_L_Brow_limitBox.translateY', 9.1)
    mc.setAttr(charName + '_L_Brow_limitBox.scaleX', .5)
    mc.setAttr(charName + '_L_Brow_limitBox.scaleY', .5)
    mc.setAttr(charName + '_L_Brow_limitBox.scaleZ', .5)
    #mc.addAttr(shortName='L_In_in_out', longName='LeftInInOut', defaultValue=0.0, minValue=0.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='L_In_Up_Down', longName='LeftInUpDown', defaultValue=0.0, minValue=-1.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='L_Mid_Up_Down', longName='LeftMidUpDown', defaultValue=0.0, minValue=-1.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='L_Out_Up_Down', longName='LeftOutUpDown', defaultValue=0.0,  minValue=-1.0, maxValue=1, hidden=False, keyable=True)

    createController('R_Brow', charName, 'right')
    mc.setAttr(charName + '_R_Brow_limitBox.translateX', 9)
    mc.setAttr(charName + '_R_Brow_limitBox.translateY', 9.1)
    mc.setAttr(charName + '_R_Brow_limitBox.scaleX', .5)
    mc.setAttr(charName + '_R_Brow_limitBox.scaleY', .5)
    mc.setAttr(charName + '_R_Brow_limitBox.scaleZ', .5)
    #mc.addAttr(shortName='R_In_in_out', longName='RightInInOut', defaultValue=0.0,  minValue=0.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='R_In_Up_Down', longName='RightInUpDown', defaultValue=0.0, minValue=-1.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='R_Mid_Up_Down', longName='RightMidUpDown', defaultValue=0.0, minValue=-1.0, maxValue=1, hidden=False, keyable=True)
    mc.addAttr(shortName='R_Out_Up_Down', longName='RightOutUpDown', defaultValue=0.0, minValue=-1.0, maxValue=1, hidden=False, keyable=True)

    #Parent all the controllers
    mc.curve(name=charName + '_MasterFaceCtrl', degree=1, point=[(1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0), (1, 1, 0)])
    mc.setAttr(charName + '_MasterFaceCtrl.translateX', 10)
    mc.setAttr(charName + '_MasterFaceCtrl.translateY', 6.5)
    mc.setAttr(charName + '_MasterFaceCtrl.scaleX', 2)
    mc.setAttr(charName + '_MasterFaceCtrl.scaleY', 4.5)
    mc.makeIdentity(apply=True, translate=True, scale=True)
    mc.textCurves(text=charName, name=charName + '_label_')
    mc.setAttr(charName + '_label_Shape.translateX', 8.2)
    mc.setAttr(charName + '_label_Shape.translateY', 10.1)
    mc.setAttr(charName + '_label_Shape.template', True)
    mc.parent(charName + '_label_Shape', charName + '_R_Brow_limitBox', charName + '_L_Brow_limitBox', charName + '_R_Eye_limitBox', charName + '_L_Eye_limitBox', charName + '_L_Mouth_limitBox', charName + '_R_Mouth_limitBox', charName + '_L_Eye_Blink_limitBox', charName + '_R_Eye_Blink_limitBox')
    mc.select('c_' + charName + '_neck_joint_bind')
    mc.makeIdentity(apply=True, r=True, t=True, s=True)
    mc.parentConstraint('c_' + charName + '_headTop_joint', 'hair', maintainOffset=True)
    mc.parentConstraint('c_' + charName + '_headTop_joint', 'eyes', maintainOffset=True)
    mc.parentConstraint('c_' + charName + '_headTop_joint', 'upper_jaw_geo', maintainOffset=True)
    mc.parentConstraint('c_' + charName + '_jawAim_joint_end', 'lower_jaw_geo', maintainOffset=True)
    mc.select('face')
    mc.deformer(type='wrap')

    #Connect the controllers for eyeballs with the geometry
    mc.setDrivenKeyframe('L_eye_geo.rotateY', currentDriver=charName + '_L_Eye_ctrl.translateX', driverValue=0, value=0)
    mc.setDrivenKeyframe('L_eye_geo.rotateY', currentDriver=charName + '_L_Eye_ctrl.translateX', driverValue=1, value=45)
    mc.setDrivenKeyframe('L_eye_geo.rotateY', currentDriver=charName + '_L_Eye_ctrl.translateX', driverValue=-1, value=-45)

    mc.setDrivenKeyframe('L_eye_geo.rotateX', currentDriver=charName + '_L_Eye_ctrl.translateY', driverValue=0, value=0)
    mc.setDrivenKeyframe('L_eye_geo.rotateX', currentDriver=charName + '_L_Eye_ctrl.translateY', driverValue=1, value=45)
    mc.setDrivenKeyframe('L_eye_geo.rotateX', currentDriver=charName + '_L_Eye_ctrl.translateY', driverValue=-1, value=-45)

    mc.setDrivenKeyframe('R_eye_geo.rotateY', currentDriver=charName + '_R_Eye_ctrl.translateX', driverValue=0, value=0)
    mc.setDrivenKeyframe('R_eye_geo.rotateY', currentDriver=charName + '_R_Eye_ctrl.translateX', driverValue=1, value=45)
    mc.setDrivenKeyframe('R_eye_geo.rotateY', currentDriver=charName + '_R_Eye_ctrl.translateX', driverValue=-1, value=-45)

    mc.setDrivenKeyframe('R_eye_geo.rotateX', currentDriver=charName + '_R_Eye_ctrl.translateY ', driverValue=0, value=0)
    mc.setDrivenKeyframe('R_eye_geo.rotateX', currentDriver=charName + '_R_Eye_ctrl.translateY', driverValue=1, value=45)
    mc.setDrivenKeyframe('R_eye_geo.rotateX', currentDriver=charName + '_R_Eye_ctrl.translateY', driverValue=-1, value=-45)

#Attach blendshapes to the base head
def attachBlendShapes():
    charName = mc.textFieldGrp('charName', query=True, text=True)
    #read in all the blendshapes from folder
    path = mc.workspace(query=True, rootDirectory=True) + 'blendShapes/'
    listBlendShapes = os.listdir(path)
    
    #attach to the base head
    mc.select('face')
    mc.blendShape(name='faceBlendShapes')
    count = 0
    for bs in listBlendShapes:
        geoName = bs.split('.')
        geoName = geoName[0]
        blendPart = bs.split('_')
        blendPart = blendPart[1]
        mc.file(path + bs, applyTo=None, i=True, defaultNamespace=True)
        mc.blendShape('faceBlendShapes', edit=True, target=('face', count, geoName, 1.0))
        
        #Blendshapes for mouth
        if blendPart == 'Mouth':
            #connect the blendshapes with the controller
            mc.select(charName + '_L_Mouth_ctrl')
            if geoName == 'L_Mouth_CornerDown':
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerDown', currentDriver=charName + '_L_Mouth_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerDown', currentDriver=charName + '_L_Mouth_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'L_Mouth_CornerUp':
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerUp', currentDriver=charName + '_L_Mouth_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerUp' , currentDriver=charName + '_L_Mouth_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'L_Mouth_CornerIn':
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerIn', currentDriver=charName + '_L_Mouth_ctrl.translateX', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerIn', currentDriver=charName + '_L_Mouth_ctrl.translateX', driverValue=-1, value=1)
            elif geoName == 'L_Mouth_CornerOut':
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerOut', currentDriver=charName + '_L_Mouth_ctrl.translateX', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Mouth_CornerOut', currentDriver=charName + '_L_Mouth_ctrl.translateX', driverValue=1, value=1)
            mc.select(charName + '_R_Mouth_ctrl')
            if geoName == 'R_Mouth_CornerDown':
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerDown', currentDriver=charName + '_R_Mouth_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerDown', currentDriver=charName + '_R_Mouth_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'R_Mouth_CornerUp':
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerUp', currentDriver=charName + '_R_Mouth_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerUp', currentDriver=charName + '_R_Mouth_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'R_Mouth_CornerIn':
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerIn', currentDriver=charName + '_R_Mouth_ctrl.translateX', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerIn', currentDriver=charName + '_R_Mouth_ctrl.translateX', driverValue=-1, value=1)
            elif geoName == 'R_Mouth_CornerOut':
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerOut', currentDriver=charName + '_R_Mouth_ctrl.translateX', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Mouth_CornerOut', currentDriver=charName + '_R_Mouth_ctrl.translateX', driverValue=1, value=1)
            else:
                mc.addAttr(longName=geoName, defaultValue=0.0, minValue=0.0, maxValue=1.0, hidden=False, keyable=True)
        
        #Blendshapes for Eyebrows 
        if geoName == 'L_Brow*':
            mc.select(charName + '_L_Brow_ctrl')
            if geoName == 'L_Brow_OutUp':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutUp', currentDriver=charName + '_L_Brow_ctrl.LeftOutUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutUp', currentDriver=charName + '_L_Brow_ctrl.LeftOutUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'L_Brow_OutDown':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutDown', currentDriver=charName + '_L_Brow_ctrl.LeftOutUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutDown', currentDriver=charName + '_L_Brow_ctrl.LeftOutUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_OutDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=-1, value=1)
                   
            if geoName == 'L_Brow_MidUp':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidUp', currentDriver=charName + '_L_Brow_ctrl.LeftMidUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidUp', currentDriver=charName + '_L_Brow_ctrl.LeftMidUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'L_Brow_MidDown':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidDown', currentDriver=charName + '_L_Brow_ctrl.LeftMidUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidDown', currentDriver=charName + '_L_Brow_ctrl.LeftMidUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_MidDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=-1, value=1)

            if geoName == 'L_Brow_InUp':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InUp', currentDriver=charName + '_L_Brow_ctrl.LeftInUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InUp', currentDriver=charName + '_L_Brow_ctrl.LeftInUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InUp', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'L_Brow_InDown':
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InDown', currentDriver=charName + '_L_Brow_ctrl.LeftInUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InDown', currentDriver=charName + '_L_Brow_ctrl.LeftInUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=0,value=0)
                mc.setDrivenKeyframe('faceBlendShapes.L_Brow_InDown', currentDriver=charName + '_L_Brow_ctrl.translateY', driverValue=-1,value=1)
            else:
                mc.addAttr(longName=geoName, defaultValue=0.0, minValue=0.0, maxValue=1.0,  keyable=True)
        if geoName == 'R_Brow*':
            mc.select(charName + '_R_Brow_ctrl')
            if geoName == 'R_Brow_OutUp':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutUp', currentDriver=charName + '_R_Brow_ctrl.RightOutUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutUp', currentDriver=charName + '_R_Brow_ctrl.RightOutUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'R_Brow_OutDown':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutDown', currentDriver=charName + '_R_Brow_ctrl.RightOutUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutDown', currentDriver=charName + '_R_Brow_ctrl.RightOutUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_OutDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'R_Brow_MidUp':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidUp', currentDriver=charName + '_R_Brow_ctrl.RightMidUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidUp', currentDriver=charName + '_R_Brow_ctrl.RightMidUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'R_Brow_MidDown':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidDown', currentDriver=charName + '_R_Brow_ctrl.RightMidUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidDown', currentDriver=charName + '_R_Brow_ctrl.RightMidUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_MidDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'R_Brow_InUp':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InUp', currentDriver=charName + '_R_Brow_ctrl.RightInUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InUp', currentDriver=charName + '_R_Brow_ctrl.RightInUpDown', driverValue=1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InUp', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=1, value=1)
            elif geoName == 'R_Brow_InDown':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InDown', currentDriver=charName + '_R_Brow_ctrl.RightInUpDown', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InDown', currentDriver=charName + '_R_Brow_ctrl.RightInUpDown', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InDown', currentDriver=charName + '_R_Brow_ctrl.translateY', driverValue=-1, value=1)
            elif geoName == 'R_Brow_InIn':
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InIn', currentDriver=charName + '_R_Brow_ctrl.RightInInOut', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InIn', currentDriver=charName + '_R_Brow_ctrl.RightInInOut', driverValue=-1, value=1)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InIn', currentDriver=charName + '_R_Brow_ctrl.translateX', driverValue=0, value=0)
                mc.setDrivenKeyframe('faceBlendShapes.R_Brow_InIn', currentDriver=charName + '_R_Brow_ctrl.translateX', driverValue=-1, value=1)
            else:
                mc.addAttr(longName=geoName, defaultValue=0.0, minValue=0.0, maxValue=1.0, hidden=False, keyable=True)

        #Blendshapes for eye blink
        mc.select(charName + '_R_Eye_Blink_ctrl')
        if geoName == 'R_Eye_Blink':
            mc.setDrivenKeyframe('faceBlendShapes.R_Eye_Blink', currentDriver=charName + '_R_Eye_Blink_ctrl.translateY', driverValue=0, value=0)
            mc.setDrivenKeyframe('faceBlendShapes.R_Eye_Blink', currentDriver=charName + '_R_Eye_Blink_ctrl.translateY', driverValue=-1, value=1)
        else:
            mc.addAttr(longName=geoName, defaultValue=0.0, minValue=0.0, maxValue=1.0, hidden=False, keyable=True)

        mc.select(charName + '_L_Eye_Blink_ctrl')
        if geoName == 'L_Eye_Blink':
            mc.setDrivenKeyframe('faceBlendShapes.L_Eye_Blink', currentDriver=charName + '_L_Eye_Blink_ctrl.translateY', driverValue=0, value=0)
            mc.setDrivenKeyframe('faceBlendShapes.L_Eye_Blink', currentDriver=charName + '_L_Eye_Blink_ctrl.translateY', driverValue=-1, value=1)
        else:
            mc.addAttr(longName=geoName, defaultValue=0.0, minValue=0.0, maxValue=1.0, hidden=False, keyable=True, )
        print geoName
        count = count + 1
        mc.delete(geoName)
