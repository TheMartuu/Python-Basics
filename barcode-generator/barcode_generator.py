import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

# Set barcode type
Barcode_Class = barcode.get_barcode_class("ean13")

# User input with validation for 12 digits only
my_text = str(input("Please enter 12 digits: "))

if len(my_text) != 12 or not my_text.isdigit():
    print("Error: EAN-13 requires exactly 12 numeric digits.")
    exit()

# Generate barcode 
my_barcode = Barcode_Class(my_text, writer=ImageWriter())

options = {
    "module_width": 0.35,
    "module_height": 14,
    "font_size": 0,       
    "text_distance": 0,  
    "center_text": False,
    "quiet_zone": 5
}
filename = my_barcode.save('barcode', options)

# Add text with Pillow
img = Image.open("barcode.png")
w, h = img.size

# New image with extra space below! 
new_img = Image.new("RGB", (w, h + 30), "white")
new_img.paste(img, (0, 0))

draw = ImageDraw.Draw(new_img)
font = ImageFont.load_default()

# Full text
full_text = my_barcode.get_fullcode()  #

# Centered position 
text_w, text_h = draw.textsize(full_text, font=font)

x = (w - text_w) / 2
y = h + 5

draw.text((x, y), full_text, fill="black", font=font)
new_img.save("barcode.png")

print(f"Barcode saved as barcode.png")