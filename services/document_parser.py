from pathlib import Path

from pypdf import PdfReader
from docx import Document


def parse_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def parse_docx(file_path: str) -> str:
    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


def parse_txt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def parse_markdown(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def parse_document(file_path: str) -> str:
    """
    Parse PDF, DOCX, TXT, or Markdown files.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".pdf":
        return parse_pdf(file_path)

    if extension == ".docx":
        return parse_docx(file_path)

    if extension == ".txt":
        return parse_txt(file_path)

    if extension in [".md", ".markdown"]:
        return parse_markdown(file_path)

    raise ValueError(
        f"Unsupported file type: {extension}"
    )