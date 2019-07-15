#------------QR Code Reader--------------#
#----------------stu.edu-----------------#

from PIL import Image
from pyzbar.pyzbar import decode

try:
    data = decode(Image.open('center_middle_v2.png'))
    print(str(data[0][0]).strip('b').strip("'"))

except IndexError:
    print('Something went wrong with the QR code.')
