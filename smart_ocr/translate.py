from deep_translator import GoogleTranslator
from langdetect import detect

def translate_text(text, target_lang='en'):
    try:
        source_lang = detect(text)
        if source_lang == target_lang:
            return None

        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"[Translation Error] Google Translator failed: {e}")
        return None
