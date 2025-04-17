#!/usr/bin/env python3
"""
Tests for PdfToSpeech.
"""
import os
import pytest
from pdf_to_speech import __version__, extract_pdf_text
from PyPDF2 import PdfWriter, PdfReader

@pytest.fixture
def pdf_file(tmp_path):
    """Create a temporary PDF file."""
    pdf_path = tmp_path / "test.pdf"
    output_path = tmp_path / "test.mp3"
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    writer.pages[0].add_text("Test content")
    with open(pdf_path, "wb") as f:
        writer.write(f)
    return pdf_path, output_path

def test_version() -> None:
    """Test version format."""
    assert __version__ == "1.0.1"

def test_extract_pdf_text(pdf_file) -> None:
    """Test extracting text from a PDF."""
    pdf_path, _ = pdf_file
    text = extract_pdf_text(str(pdf_path))
    assert "Test content" in text

def test_extract_pdf_text_invalid_file() -> None:
    """Test extracting text from an invalid PDF."""
    with pytest.raises(FileNotFoundError):
        extract_pdf_text("nonexistent.pdf")