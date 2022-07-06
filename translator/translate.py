from googletrans import Translator

def translate(text: str) -> str:
    translator = Translator()
    output = translator.translate(text=text, dest="es")
    return output.text
