"""
Simple qrcode generator function, which takes either a text or a url as a redirect location
"""

import qrcode


def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qr001.png')


url = input('Enter your text or url:\n')

generate_qr_code(url)