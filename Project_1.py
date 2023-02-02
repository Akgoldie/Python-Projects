from PIL import Image
import qrcode
#link="https://github.com/Akgoldie"
link=input("Enter the link: ")
#file_name="Github_Account.png"
file_name=input("Enter the File name: ")
image_save=qrcode.make(link)
image_save.save(file_name)
img = Image.open(file_name)
img.show()
