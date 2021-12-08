from PIL import Image
import numpy as np

img = np.array(Image.open('encoded_beemovie.png'))

# Extract message out of the red color of the image
secret = []
for row in img:
    for col in row:
        R = col[0]
        secret.append(format(R, '08b')[-1])
message = ''.join(secret)

i = 0
test_list = []
# Convert the byte string to a string of characters
while i < len(message):
    letter = chr(int(message[i:i + 8], 2))
    if int(message[i:i + 8], 2) == 0:
        break
    test_list.append(letter)
    i += 8
    print(letter, end="")
