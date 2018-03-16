"""
Program takes a block id from the user and replaces the list with those ids.
Comes with three build templates.
Coded by Joseph Summerlin
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#imports minecraft and gets the user's coordinates.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
#tower gets the user's choice for their block and inputs value into variable "Mainblock", which is included into a precreated list. Then 'tower' places each block in the list.
def tower(x, y, z, tower):
    mainblock = int(input("Please input what block you want. Please enter block ID, not block name. "))
    #When input is given, block names are not accepted. The program will only accept block ids.
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
    #List must be read in reverse for the build to be properly placed.
    for depth in reversed(tower):
        for height in depth:
            for block in height:
                mc. setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ
             
# 'igloo' gets input for one block and inputs the value into the variable 'mainblock' which is used in a precreated list. 'igloo' then places each block in the precreated list. 
def igloo(x, y, z, build1):
    mainblock = int(input("Please input what block you want. Please enter the block id, not name. "))
    #When input is given, block names are not accepted. The program will only accept block ids.
    build1 = [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, mainblock, 0, 0, 0], [0, 0, 0, mainblock, 0, 0, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]],
             [[0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]],
             [[0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, 0, mainblock, 0, mainblock, 0, 0], [0, mainblock, 0, 0, 0, mainblock, 0], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [mainblock, 0, 0, 0, 0, 0, mainblock], [0, mainblock, 0, 0, 0, mainblock, 0], [0, 0, mainblock, mainblock, mainblock, 0, 0]]]
    startingX = x
    startingY = y
    startingZ = z
    #List must be read in reverse for build to be properly placed.
    for depth in reversed(build1):
        for height in depth:
            for block in height:
                mc.setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ
# 'simplehouse' gets three values from the user and inputs them into 'mainblock' (Note that roof and mainblock have switched roles), 'roof', and 'frame'. 'simplehouse' then places every block in the precreated list.
def simplehouse(x, y, z, simplehouse):
    #When input is given, block names are not accepted. The program will only accept block ids.
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
    #List must be read in reverse for build to be properly placed.
    for depth in reversed(simplehouse):
        for height in depth:
            for block in height:
                mc.setBlock(x, y, z, block)
                x += 1
            z += 1
            x = startingX
        y += 1
        z = startingZ
#gets users choice on which build they want. options are from 'igloo', 'tower', or 'simplehouse'.
choice = input("What build do you want? Choose from igloo, tower, or simplehouse (enter as written). ")
if choice == "igloo":
    #if igloo is chosen, 'igloo' is run and a message is posted to chat.
    igloo(x, y, z, igloo)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors not included).")
elif choice == "simplehouse":
    #if simplehouse is chosen, 'simplehouse' is run and a message is posted to chat.
    simplehouse(x, y, z, simplehouse)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors not included).")
elif choice == "tower":
    #if tower is chosen, 'tower' is run and a message is posted to chat.
    tower(x, y, z, tower)
    mc.postToChat("Thank you for using 'GENERIC BUILD TEMPLATE' (Doors and floors [and sometimes ladders] not included). ")

else:
    #Input must be EXACTLY as shown, or else the program will not accept the choice.
    mc.postToChat("That is not a choice or you've entered the choice wrong. Please enter exactly as shown.")