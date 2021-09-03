from mcpi import block
from mcpi import minecraft

mc = minecraft.Minecraft.create()
pos = (-100, 0, -100)
second_pos = (100, 0, 100)
mc.setBlock(*pos, block.STONE.id)
mc.setBlocks(*pos, *second_pos, block.AIR.id, 0)


def clean_area(x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)


def create_golem(x, y, z):
    mc.setBlock(x, y, z, 42)
    mc.setBlock(x, y + 1, z, 42)
    mc.setBlock(x + 1, y + 1, z, 42)
    mc.setBlock(x - 1, y + 1, z, 42)
    mc.setBlock(x, y + 2, z, 91)


create_golem(*pos)

# for i in range(0, 1000):
#     create_golem(5, 5, 5)


# mc.setBlocks(-3, 1, 26, 11, 62, 7, 1)
# blocks = mc.getBlocks(0, 3, 0, -1, 4, -1)
# for block in blocks:
#     print(int(block))
#
# mc.setBlocks(100, 100, 100, 160, 160, 160, block.Block(0, 0))
