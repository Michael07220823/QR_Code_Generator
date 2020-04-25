# QR_Code_Generator

## Install package
`pip install qrcode[pil]`

## Usage
First - bash or cmd<br>
`qr "Hello world !" > output/Hello_world.png`<br>
  
Second - Python<br>
<pre><code>
import qrcode

qr = qrcode.make("https://pypi.org/project/qrcode/")
qr.save("qrcode.png")
</code></pre>

Second-2 - Python<br>
<pre><code>
import qrcode

content = 'https://pypi.org/project/qrcode/'

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

qr.add_data(content)
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")

img.save("output/qrcode.png")
</code></pre>

Second-3 - Python<br>
<pre><code>
import qrcode
import qrcode.image.svg

content = "Hello world !"
factory = qrcode.image.svg.SvgFillImage

img = qrcode.make(content, image_factory=factory)

img.save("output/Hello_world.svg")
</code></pre>

-----------
### Reference
* [qrcode](https://pypi.org/project/qrcode/)
