import numpy as np
from PIL import Image
from mcpi import minecraft

mc = minecraft.Minecraft.create()
image = Image.open('claptrap.png')


def draw_image(image_obj):
    img_array = np.asarray(image_obj)
    for i in range(0, img_array.shape[0]):
        for j in range(0, img_array.shape[1]):
            print(img_array[i, j])
            pix = img_array[i, j]
            if pix == 0:
                mc.setBlock(j, img_array.shape[0] - i, 0, 0)  # (x, y, z, тип блока, подтип блока)
            if pix == 1:
                mc.setBlock(j, img_array.shape[0] - i, 0, 251, 14)  # (x, y, z, тип блока, подтип блока)
            if pix == 2:
                mc.setBlock(j, img_array.shape[0] - i, 0, 251, 15)  # (x, y, z, тип блока, подтип блока)
            if pix == 3:
                mc.setBlock(j, img_array.shape[0] - i, 0, 251, 1)  # (x, y, z, тип блока, подтип блока)
            if pix == 4:
                mc.setBlock(j, img_array.shape[0] - i, 0, 251, 4)  # (x, y, z, тип блока, подтип блока)
            if pix == 5:
                mc.setBlock(j, img_array.shape[0] - i, 0, 251, 3)  # (x, y, z, тип блока, подтип блока)


draw_image(image)
