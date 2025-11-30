import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1, error_correction=
qr.constants.ERROR_CORRECT_H, box_size=10, border=5)

qr.add_data("https://bing.com")
qr.make(fit=True)
img =qr.make_image(fill_color="GREEN",back_color="Lightblue")
img.save("QRSearchengineBing.png")
