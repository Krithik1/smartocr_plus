import mss
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(bbox):
    x1, y1, x2, y2 = bbox
    width, height = x2 - x1, y2 - y1

    with mss.mss() as sct:
        monitor = {"top": y1, "left": x1, "width": width, "height": height}
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        text = pytesseract.image_to_string(img, lang='eng+hin')
        return text.strip()
