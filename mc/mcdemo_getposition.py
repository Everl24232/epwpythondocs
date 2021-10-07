#Everleigh Pierce
#mc demo pos

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.getTilePos()

pos = mc.player.getTilePos()
mc.postToChat(pos)
mc.postToChat("Your x position: " + str(pos.x))
mc.postToChat("Your y position: " + str(pos.y))
mc.postToChat("Your z position: " + str(pos.z))