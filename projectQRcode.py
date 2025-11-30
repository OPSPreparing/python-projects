import qrcode as qr
# from qrcode import image, PilImage
# from PIL import Image
img = qr.make("https://google.com")
img.save("QRSearchengine.png")
