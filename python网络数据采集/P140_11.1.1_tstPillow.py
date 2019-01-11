from PIL import Image,ImageFilter

img = Image.open('IMG_20150412_103036.jpg')
blurry_img = img.filter(ImageFilter.GaussianBlur)
blurry_img.save('GaussianBlur_IMG.jpg')
blurry_img.show()