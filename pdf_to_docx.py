# pdf_to_docx.py
# This script converts a PDF resume to a DOCX file using the pdf2docx library.
# It preserves layout, text, images, and tables where possible.
# Installation: pip install pdf2docx
# Usage: python pdf_to_docx.py input.pdf output.docx

from pdf2docx import Converter
import sys

def convert_pdf_to_docx(pdf_path, docx_path):
    """
    Convert a PDF file to a DOCX file.
    
    Args:
    pdf_path (str): Path to the input PDF file.
    docx_path (str): Path to the output DOCX file.
    """
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print(f"Conversion completed: {pdf_path} -> {docx_path}")

if __name__ == "__main__":
    pdf_file = "resume.pdf"
    docx_file = "resume.docx"
    
    try:
        convert_pdf_to_docx(pdf_file, docx_file)
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)