import maya.cmds as mc

sel = mc.ls(sl = True)
sel = sel[0]
mc.duplicate(sel, name = 'dupObj')
mc.setAttr('dupObj.sx' , -1)
mc.duplicate('baseHead', name = 'dupBaseHead')
mc.setAttr('dupBaseHead.sx', -1)
mc.blendShape('dupObj', 'dupBaseHead', n = 'mirrorBlendShape')
mc.select('baseHead', 'dupBaseHead')
mc.CreateWrap()
mc.setAttr('mirrorBlendShape.dubObj', 1)
mc.duplicate('baseHead', name = 'newHead')
mc.setAttr('newHead.ty', -25)