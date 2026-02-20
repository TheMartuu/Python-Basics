#1 Import barcode module and ImageWriter from barcode.writer module 
import barcode
from barcode.writer import ImageWriter

#2 Select barcode type for alphanumeric values 
Barcode_Class = barcode.get_barcode_class("ean13")

#3 Prompt user to add any string 
my_text = str(input("Please enter text: "))

#4 Convert and save string into a barcode 
#Set also render options 

my_barcode = Barcode_Class(my_text,writer=ImageWriter())

#5) Save barcode image in PNG file 
options = {
    "module_width": 0.35,
    "module_height": 14,
    "font_size": 8,
    "text_distance": 2,
    "center_text": False,
    "quiet_zone": 5
}
filename = my_barcode.save('barcode',options)
