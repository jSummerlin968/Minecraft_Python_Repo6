from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


level = range(0, 50)

for item in level:
    y = y - 1
    if mc.getBlock(x, y, z) == 56:
        mc.postToChat("A diamond ore is " + str(pos.y - y) + " blocks below you.")
        break
    else:
        mc.postToChat("There is no diamond below you.")
    