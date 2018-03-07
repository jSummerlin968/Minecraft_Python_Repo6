from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

def tower(x, y, z, tower):
    mainblock = int(input("Please input what block you want. Please enter block ID, not block name. "))
    
    tower = [[[0, mainblock, 0, mainblock, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, 0, 0, 0, 0, 0, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, 0, 0, 0, 0, 0, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, mainblock, 0, mainblock, 0]],
             [[0, mainblock, mainblock, mainblock, mainblock, mainblock, 0], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, 0, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [0, mainblock, mainblock, mainblock, mainblock, mainblock, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, mainblock, mainblock, mainblock, mainblock, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, mainblock, mainblock, mainblock, mainblock, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]]]
    startingX = x
    startingY = y
    startingZ = z
    for depth in reversed(tower):
        for height in depth:
            for block in height:
                mc. setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ
             
def igloo(x, y, z, build1):
    mainblock = int(input("Please input what block you want. Please enter the block id, not name. "))
    
    build1 = [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, mainblock, 0, 0, 0], [0, 0, 0, mainblock, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]],
             [[0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]],
             [[0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]]]
    startingX = x
    startingY = y
    startingZ = z
    for depth in reversed(build1):
        for height in depth:
            for block in height:
                mc.setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ

def simplehouse(x, y, z, simplehouse):
    
    mainblock = int(input("Please input what block you want for the roof. Please enter a block id, not name. "))
    roof = int(input("Please input what block you want for the mainblock. Please enter a block id, not name. "))
    frame = int(input("Please input what block you want for the frame. Please enter a block id, not name. "))
    simplehouse = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, mainblock, mainblock, mainblock, 0, 0, 0], [0, 0, 0, mainblock, mainblock, mainblock, 0, 0, 0], [0, 0, 0, mainblock, mainblock, mainblock, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock], [mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock, mainblock]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, frame, frame, frame, frame, frame, frame, frame, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, frame, frame, frame, frame, frame, frame, frame, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, frame, roof, 64, roof, 64, roof, frame, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, frame, roof, 64, roof, 64, roof, frame, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, roof, 0, 0, 0, 0, 0, roof, 0], [0, frame, roof, roof, roof, roof, roof, frame, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]]
    startingX = x
    startingY = y
    startingZ = z
    for depth in reversed(simplehouse):
        for height in depth:
            for block in height:
                mc.setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ
choice = input("What build do you want? Choose from igloo, tower, or simplehouse (enter as written). ")
if choice == "igloo":
    igloo(x, y, z, igloo)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors not included).")
elif choice == "simplehouse":
    simplehouse(x, y, z, simplehouse)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors not included).")
elif choice == "tower":
    tower(x, y, z, tower)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors not included). ")
else:
    mc.postToChat("That is not a choice or you've entered the choice wrong. Please enter exactly as shown.")