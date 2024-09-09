import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

# Data to encode
data = "https://maps.app.goo.gl/LNLPkJEHJKsqwfQ8A"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box
    border=4,  # thickness of the border (boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(back_color=(38,38,38), fill_color=(255, 255, 255))

# Save the image
img.save("qrcode.png")
print("saved")


