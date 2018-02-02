from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10

for outer in range(5):
    brokenWall.append([])
    for inner in range(10):
        chunk = brokenBlock()
        brokenWall[outer].append(chunk)
for row in reversed(brokenWall):
    for chunk in row:
        mc.setBlock(x, y, z, chunk)
        z += 1
    y += 1
    z = pos.x