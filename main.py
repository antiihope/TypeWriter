text = "a soul that does not know, and a mind that never rests".replace(". ", ".\n\n")


import os
import time
import random
import PIL
from PIL import Image, ImageDraw, ImageFont

width, height = 540, 256
fontsize = 12
font = ImageFont.truetype("monospace\MonospaceBold.ttf", fontsize)
fontsizee = 15
fonte = ImageFont.truetype("monospace\MonospaceBold.ttf", fontsize)


def endFrame(current_text, frames, n=2, nF=1):
    for i in range(n):
        current_img = Image.new("RGB", (width, height), "black")
        # create a draw object
        draw = ImageDraw.Draw(current_img)
        # draw the text on the image
        draw.text((10, height / 4), current_text + "|", font=fonte, fill="#0bc50b")
        # add the image to the list
        for i in range(nF):
            frames.append(current_img)
        frames.append(current_img)
        current_img = Image.new("RGB", (width, height), "black")
        # create a draw object
        draw = ImageDraw.Draw(current_img)
        # draw the text on the image
        draw.text((10, height / 4), current_text + "", font=fonte, fill="#0bc50b")
        # add the image to the list
        for i in range(nF):
            frames.append(current_img)
    return frames


def blink(current_text, frames, n=2, nF=1):
    for i in range(n):
        current_img = Image.new("RGB", (width, height), "black")
        # create a draw object
        draw = ImageDraw.Draw(current_img)
        # draw the text on the image
        draw.text((10, height / 4), current_text + "_", font=fonte, fill="#0bc50b")
        # add the image to the list
        for i in range(nF):
            frames.append(current_img)
        current_img = Image.new("RGB", (width, height), "black")
        # create a draw object
        draw = ImageDraw.Draw(current_img)
        # draw the text on the image
        draw.text((10, height / 4), current_text + "", font=fonte, fill="#0bc50b")
        # add the image to the list
        for i in range(nF):
            frames.append(current_img)
    return frames


def typewriter(text, color="black", speed=0.05):
    """
    This function will make a typewriter effect on the text
    """

    # get the size of the text
    # make a gif
    frames = []
    letters = list(text)
    current_text = ""
    for letter in letters:
        current_text += letter
        # create a new image
        current_img = Image.new("RGB", (width, height), "black")
        # create a draw object
        draw = ImageDraw.Draw(current_img)
        # draw the text on the image
        draw.text((10, height / 4), current_text, font=font, fill="#0bc50b")
        # add the image to the list
        frames.append(current_img)
        # frames = endFrame(current_text, frames, 1, 1)
        # frames = blink(current_text, frames, 1, 1)

    # create a new image
    frames = endFrame(current_text, frames, 5, 2)
    # save the gif
    frames[0].save(
        "typewriter.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        special_args=["-loop", "0"],
        loop=0,
    )


typewriter(text)

# open the gif
os.system("typewriter.gif")


# def main():
#     # get the text
#     text = input("Enter the text: ")
#     # get the font
#     font = input("Enter the font: ")
#     # get the color
#     color = input("Enter the color: ")
#     # get the speed
#     speed = int(input("Enter the speed: "))
#     # make the typewriter effect
#     typewriter(text, font, color, speed)
