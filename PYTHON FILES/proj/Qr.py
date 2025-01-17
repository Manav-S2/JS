'''import qrcode as qr

img = qr.make('https://www.google.com/')

img.save('google.png')
'''

import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10, border = 4)

qr.add_data("https://www.google.com")
qr.make(fit=True)

img = qr.make_image(fill_color = '#000', back_color = '#fff`6')

img.save('google.jpg')