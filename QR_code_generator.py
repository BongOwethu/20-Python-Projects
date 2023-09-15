# install all libaries needed using pip qrcode Image in powershell
# create a function that collects a text and converts it to a qr
# save the qr code as an image
# run the function

import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color ='black', back_color='white')
    img.save('qrimg001.png')

url = input('Enter the url: ')    
generate_qrcode(url)

# After runnying the code you need to go to your root folder and see the image created
# don't forget to chang the image number in image.save('qrimageX.png') togenerate code

