# Resume

Easily tailor your resume for different companies and roles.

## Getting Started

### Dependencies

- Windows 11
- Python 3.x (download from [python.org](https://www.python.org/downloads/))
- TeX Live
- VS Code
- LaTeX Workshop from VS Code Marketplace
- Remote Development from VS Code Marketplace

### Setting Up the Environment

1. **Create a virtual environment**:
   - Open your terminal or command prompt.
   - Navigate to your project directory.
   - Run:
     ```
     python -m venv venv
     ```
     This will create a directory named `venv` in your project directory, which contains the virtual environment.

2. **Activate the virtual environment**:
   - In PowerShell:
     ```
     .\venv\Scripts\activate
     ```
   - In Command Prompt:
     ```
     venv\Scripts\activate.bat
     ```
   Once activated, your command prompt will indicate that you are in the virtual environment (e.g., your prompt might change to `(venv)`).

3. **Install dependencies**:
   - Run:
     ```
     pip install -r requirements.txt
     ```
     This will install all the Python packages listed in `requirements.txt`, which are required for the project.

### Generating Resume

1. Edit `data.json` with your personal information.
2. Run `json_to_tex.py` to generate your resume.
3. If you need the resume and cover letter combined in a single document, run `merge_pdfs.py`, or `pdf_to_docx.py` for a word document.

## Acknowledgments

- [Omar Roldan](https://www.overleaf.com/latex/templates/cv-developer/rdycxzvvnvcc)

