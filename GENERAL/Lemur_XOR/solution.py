from PIL import Image
from pwn import *

img1 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")

img2 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")

x = xor(img1.tobytes(), img2.tobytes())

print(img1.size, img2.size)
Image.frombytes("RGB", (582 , 327), x).save("result.png")
