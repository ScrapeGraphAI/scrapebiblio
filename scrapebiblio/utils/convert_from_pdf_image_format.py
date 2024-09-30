import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    """
    Estrae il testo da un'immagine utilizzando Tesseract OCR.

    Args:
        image_path (str): Il percorso del file immagine.

    Returns:
        str: Il testo estratto dall'immagine.
    """
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
        return text
