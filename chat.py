import mcpi.minecraft as minecraft
import mcpi.block as block
import time


if __name__ == "__main__":

    time.sleep(5)
    world = minecraft.Minecraft.create()

    print "Minecraft"
    world.postToChat("Bienvenue dans le monde Minecraft !")

    time.sleep(5)

    end = False


    playerPos = world.player.getPos()
    world.postToChat("Position : x=" + str(playerPos.x) + ", y=" + str(playerPos.y) + ", z=" + str(playerPos.z))

    time.sleep(5)


    while(end == False):
       a = 0
