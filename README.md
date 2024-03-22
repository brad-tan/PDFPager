# PDF Page Insertion Script

This Python script adds a blank page after each existing page within a PDF document.  This facilitates easier note-taking, especially when using an iPad with digital writing tools.

**Key Uses**

* **Handwritten Notes:** Add space for comfortable handwritten notes directly within the PDF on an iPad.
* **Study Material:** Insert extra pages for working out problems, taking notes on lectures, or expanding on key concepts.
* **Creative Projects:** Provides additional space for sketches, brainstorming, or mind-mapping alongside content in the PDF.

**Prerequisites**

* Python 3 (https://www.python.org/)
* PyPDF2 library: Install using `pip install pypdf2`

**Usage**

1. Save this script as a `.py` file (e.g., `add_blank_pages.py`)
2. Run the script from your terminal, providing the input PDF filename as an argument:

   ```bash
    python3 add_blank_pages.py input_file.pdf
