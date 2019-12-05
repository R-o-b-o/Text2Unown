from PIL import Image


text = input("Enter text to be unowned: ").upper().replace(" ", "_")
imageSizes = []

for char in text:
    with Image.open(f"unown/{char}.png") as charImage:
        imageSizes.append(charImage.size)

textImage = Image.new("RGBA", (sum([x[0] for x in imageSizes]), 60))

offset = 0
for char in text:
    with Image.open(f"unown/{char}.png") as charImage:
        textImage.paste(charImage, (offset, 0))
        offset += charImage.size[0]

textImage.save("out.png")
