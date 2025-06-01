import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
from docx import Document

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def extract_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_text_from_image(path):
    return pytesseract.image_to_string(Image.open(path))

def load_data(file):
    ext = file.name.split('.')[-1].lower()
    if ext in ['csv']:
        return pd.read_csv(file)
    elif ext in ['xlsx']:
        return pd.read_excel(file)
    elif ext in ['txt']:
        return extract_text_from_txt(file)
    elif ext in ['pdf']:
        return extract_text_from_pdf(file)
    elif ext in ['docx']:
        return extract_text_from_docx(file)
    elif ext in ['jpg', 'jpeg', 'png']:
        return extract_text_from_image(file)
    else:
        return "Unsupported file format."
