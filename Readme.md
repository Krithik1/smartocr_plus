# SmartOCR+

SmartOCR+ is a Windows utility that lets you extract text from any part of your screen using a hotkey, and then instantly translate it, search it, define words, and recognize links or addresses in that text.

---

## ⚙️ Features

- 🧠 **OCR Extraction** — Instantly extract on-screen text via screen capture.
- 🌐 **Instant Translation** — Translate extracted text into another language.
- 🔗 **Link Recognition** — Detects and makes URLs clickable.
- 🗺️ **Address Recognition** — Converts addresses into Google Maps links.
- 🖱️ **Mouse-Selectable UI** — Simple pop-up window with clickable elements.
- 📋 **Copy to Clipboard** — Copy extracted text with one click.
- 🔍 **Google Search** — Search the full text on Google.
- 📖 **Define Word** — Look up dictionary definitions (for single-word input).
- 🔎 **Ctrl + F Search** — Find text within the extracted content.
- 🪟 **Hotkey Activation** — Triggered via `Windows + O`.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Krithik1/smartocr_plus.git
cd smartocr_plus
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download the latest version of Tesseract OCR from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki) and extract it to a folder.

Add the path to the Tesseract executable to the `PATH` environment variable.

### 4. Install Tesseract Language Data

Download the latest version of Tesseract Language Data from [Tesseract Language Data](https://github.com/tesseract-ocr/tessdata) and extract it to a folder.

Add the path to the Tesseract Language Data to the `TESSDATA_PREFIX` environment variable.

---

## 🚀 Usage

### Run the script

```bash
python main.py
```

---

## 📝 License

This project is licensed under the MIT License.
