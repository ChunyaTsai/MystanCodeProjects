"""
File: blur.py
Name: Chunya Tsai
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    將每格pixel的RGB改為相鄰pixel的平均RGB以達到模糊化的效果
    :param img: 原圖
    :return: 模糊化的原圖
    """
    # Todo: create a new blank img that is as big as the original one

    new_img = SimpleImage.blank(img.width, img.height)
    # loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            pixel_new_img = new_img.get_pixel(x, y)

            # belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # get pixel at the top-left corner of the image.
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x, y + 1)
                pixel2 = img.get_pixel(x + 1, y + 1)
                pixel3 = img.get_pixel(x + 1, y)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red) // 4
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green) // 4
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4

            elif x == img.width-1 and y == 0:
                # get pixel at the top-right corner of the image.
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y)
                pixel2 = img.get_pixel(x - 1, y + 1)
                pixel3 = img.get_pixel(x, y + 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red) // 4
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green) // 4
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4

            elif x == 0 and y == img.height-1:
                # get pixel at the bottom-left corner of the image
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x + 1, y)
                pixel2 = img.get_pixel(x + 1, y - 1)
                pixel3 = img.get_pixel(x, y - 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red) // 4
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green) // 4
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4

            elif x == img.width-1 and y == img.height-1:
                # get pixel at the bottom-right corner of the image
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y)
                pixel2 = img.get_pixel(x - 1, y - 1)
                pixel3 = img.get_pixel(x, y - 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red) // 4
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green) // 4
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
 
            elif img.width-1 > x > 0 == y:
                # get top edge's pixels (without two corners)
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y)
                pixel2 = img.get_pixel(x - 1, y + 1)
                pixel3 = img.get_pixel(x, y + 1)
                pixel4 = img.get_pixel(x + 1, y)
                pixel5 = img.get_pixel(x + 1, y + 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6

            elif 0 < x < img.width-1 and y == img.height-1:
                # get bottom edge's pixels (without two corners)
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x - 1, y)
                pixel4 = img.get_pixel(x + 1, y - 1)
                pixel5 = img.get_pixel(x + 1, y)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6

            elif x == 0 < y < img.height-1:
                # get left edge's pixels (without two corners)
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x, y - 1)
                pixel2 = img.get_pixel(x + 1, y - 1)
                pixel3 = img.get_pixel(x + 1, y)
                pixel4 = img.get_pixel(x, y + 1)
                pixel5 = img.get_pixel(x + 1, y + 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6

            elif x == img.width-1 and 0 < y < img.height-1:
                # # get right edge's pixels (without two corners)
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x - 1, y)
                pixel4 = img.get_pixel(x - 1, y + 1)
                pixel5 = img.get_pixel(x, y + 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6

            else:
                # Inner pixels.
                pixel0 = img.get_pixel(x, y)
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel5 = img.get_pixel(x + 1, y)
                pixel6 = img.get_pixel(x - 1, y + 1)
                pixel7 = img.get_pixel(x, y + 1)
                pixel8 = img.get_pixel(x + 1, y + 1)

                pixel_new_img.red = (pixel0.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red + pixel7.red + pixel8.red) // 9
                pixel_new_img.green = (pixel0.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green + pixel7.green + pixel8.green) // 9
                pixel_new_img.blue = (pixel0.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue + pixel7.blue + pixel8.blue) // 9

    return new_img


def main():
    """
    印出原圖(路徑: images/smiley-face.png)及模糊化的原圖
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(3):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
