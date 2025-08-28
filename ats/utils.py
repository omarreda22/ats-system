import re

from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def safe_search(pattern, text, flags=0):
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else None


def extract_recommendations(result: str):
    # 1) Try to grab the Recommendations block (up to next ALL-CAPS-ish header or end)
    rec_block = safe_search(
        r"(?ims)(?:^|\n)Recommendations?\s*:\s*(.*?)(?=\n[A-Z][^\n]{0,60}:\s*$|\Z)",
        result,
    )
    # 2) If no explicit header, just scan the whole text for bullet/numbered items
    if not rec_block:
        rec_block = result

    # 3) Find bullet/numbered items (captures wrapped lines until next bullet)
    items = re.findall(
        r"^\s*(?:\d+[\.)]|\*|-|•)\s+(.*?)(?=(?:\n\s*(?:\d+[\.)]|\*|-|•)\s+)|\Z)",
        rec_block,
        flags=re.M | re.S,
    )

    # 4) Clean: remove markdown **bold**, collapse spaces, trim bullet chars
    cleaned = []
    for it in items:
        it = re.sub(r"\*\*(.*?)\*\*", r"\1", it)  # remove **bold**
        it = re.sub(r"\s+", " ", it).strip(" -• ")  # normalize spaces & trim
        cleaned.append(it.strip())
    return cleaned
