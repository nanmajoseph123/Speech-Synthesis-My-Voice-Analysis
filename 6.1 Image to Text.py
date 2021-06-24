# pytesseract is used to convert the image to text string
import pytesseract

# PIL is used to import an image
from PIL import Image
img = Image.open('Text2.jpg')

print(img) # Gives complete details of image i.e format dimension size etc

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'
# Converts the image into result and saves it into result
result = pytesseract.image_to_string(img)
# Write the text into a text file and save
with open('SRHTest.txt', mode='w') as file:
    file.write(result)
    print(result)


