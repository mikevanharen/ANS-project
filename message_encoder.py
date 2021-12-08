from PIL import Image
import numpy as np

secret = "Hello, World"
bin_secret_list = []

# convert secret string to byte string
for letter in secret:
    ASCII = ord(letter)
    bin_secret_list.append(format(ASCII, '08b'))
bin_secret = ''.join(bin_secret_list)
bin_secret += "00000000"

image = Image.open('beemovie.png')
img = np.array(image)

# encode secret byte string in the red color of the image
i = 0
for row in img:
    for col in row:
        if i < len(bin_secret):
            R = col[0]
            col[0] = int(format(R, '08b')[:-1] + bin_secret[i], 2)
            i += 1

save_image = Image.fromarray(img)
save_image.save('encoded_beemovie.png')