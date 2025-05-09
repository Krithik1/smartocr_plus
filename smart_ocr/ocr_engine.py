import mss
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def initialize_ocr():
    dummy_img = Image.new("L", (100, 30))
    pytesseract.image_to_string(dummy_img, lang='eng+hin')

def extract_text(bbox):
    x1, y1, x2, y2 = bbox
    width, height = x2 - x1, y2 - y1

    with mss.mss() as sct:
        monitor = {"top": y1, "left": x1, "width": width, "height": height}
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        img = img.convert("L")
        img = img.filter(ImageFilter.SHARPEN)
        img = ImageEnhance.Contrast(img).enhance(2)
        
        text = pytesseract.image_to_string(img, lang='eng+hin')
        return text.strip()
