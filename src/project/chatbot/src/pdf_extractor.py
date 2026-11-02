from pypdf import PdfReader


def extract_pdf_text(path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        path (str): The path to the PDF file."""
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]

    return "\n".join(pages).strip()

if __name__ == "__main__":
    pdf_path = "src\\project\\chatbot\\data\\circulars\\circ01.pdf"  # Replace with your PDF file path
    extracted_text = extract_pdf_text(pdf_path)
    print(extracted_text)