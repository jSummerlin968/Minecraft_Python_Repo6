from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

blocks = [1, 7, 9, 11, 14, 15, 17, 22, 30, 46, 49, 57, 58, 79, 82, 89, 246, 87, 321, 156]

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x, y, z, random.choice(blocks))