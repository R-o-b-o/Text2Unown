from PIL import Image
import argparse

def text2unown(text, unownFilepath, outFilepath, scale):

    imageSizes = []

    for char in text:
        with Image.open(f"{unownFilepath}/{char}.png") as charImage:
            imageSizes.append(charImage.size)

    textImage = Image.new("RGBA", (sum([x[0] for x in imageSizes]), max([x[1] for x in imageSizes])))

    offset = 0
    for char in text:
        with Image.open(f"{unownFilepath}/{char}.png") as charImage:
            textImage.paste(charImage, (offset, textImage.size[1] - charImage.size[1]))
            offset += charImage.size[0]

    textImage.thumbnail((textImage.size[0] * scale, textImage.size[1] * scale))
    textImage.save(outFilepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', "--text", required=True,
        help = "The input text to be unowned")
    parser.add_argument('-u', "--unown-filepath", default="unown-high",
        help = "Location of the unown images")
    parser.add_argument('-o', "--output", default="out.png",
        help = "Filepath to the output image")
    parser.add_argument('-s', "--scale", default=1, type=float,
        help = "How much to scale the image")

    args = vars(parser.parse_args())
    text2unown(args["text"].lower().replace(" ", "_"), args["unown_filepath"], args["output"], args["scale"])