import qrcode
import qrcode.image.svg

content = "Hello world !"
factory = qrcode.image.svg.SvgFillImage

img = qrcode.make(content, image_factory=factory)

img.save("output/Hello world.svg")