import keyboard
import time
from smart_ocr.region_selector import select_region
from smart_ocr.ocr_engine import extract_text, initialize_ocr
from smart_ocr.gui import show_popup

def main():
    print("SmartOCR+ running... Press Windows+O to start.")
    initialize_ocr()

    def handle_hotkey():
        time.sleep(0.2)
        bbox = select_region()
        if not bbox:
            return
        x1, y1, x2, y2 = bbox
        if x2 - x1 < 5 or y2 - y1 < 5:  # You can adjust the minimum size
            print("[SmartOCR+] Ignored too-small region.")
            return
        text = extract_text(bbox)
        show_popup(text)

    keyboard.add_hotkey("windows+o", handle_hotkey)
    keyboard.wait("esc")  # Exit with ESC
    
if __name__ == "__main__":
    main()
