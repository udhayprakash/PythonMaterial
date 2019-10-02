import pyqrcode


def generate_qr():
    link_to_post = "https://udhayprakash.blogspot.com/"
    url = pyqrcode.create(link_to_post)
    url.png('url.png', scale=8)
    print("Printing QR code")
    print(url.terminal())


generate_qr()

# future Ref: https://pythonhosted.org/PyQRCode/index.html
