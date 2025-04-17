# PdfToSpeech

Converts PDF documents to MP3 audio files using gTTS or pyttsx3.

## Installation

```bash
git clone https://github.com/krisarmstrong/pdf-to-speech
cd pdf-to-speech
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python pdf_to_speech.py input.pdf output.mp3 --engine gtts --verbose
```

- `input_file`: Input PDF file.
- `output_file`: Output MP3 file.
- `--engine`: Text-to-speech engine (gtts or pyttsx3, default: gtts).
- `-v, --verbose`: Enable verbose logging.
- `--logfile`: Log file path (default: pdf_to_speech.log).

## Files

- `pdf_to_speech.py`: Main script.
- `version_bumper.py`: Version management tool.
- `tests/test_pdf_to_speech.py`: Pytest suite.
- `requirements.txt`: Dependencies.
- `CHANGELOG.md`: Version history.
- `LICENSE`: MIT License.
- `CONTRIBUTING.md`: Contribution guidelines.
- `CODE_OF_CONDUCT.md`: Contributor Covenant.

## GitHub Setup

```bash
gh repo create pdf-to-speech --public --source=. --remote=origin
git init
git add .
git commit -m "Initial commit: PdfToSpeech v1.0.1"
git tag v1.0.1
git push origin main --tags
```

## Contributing

See CONTRIBUTING.md for details.

## License

MIT License. See LICENSE for details.