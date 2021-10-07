#Everleigh Pierce
#mc demo place block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.getTilePos()

pos = mc.player.getTilePos()
mc.postToChat(pos)
mc.setBlock(pos.x, pos.y-1, pos.z, 1)