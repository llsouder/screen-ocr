try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
     """
     This function will handle the core OCR processing of images.
     """
     text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
     return text

print(ocr_core('images/ocr_example_1.png'))
print(ocr_core('images/food.jpg'))
print(ocr_core('images/atc.png'))
