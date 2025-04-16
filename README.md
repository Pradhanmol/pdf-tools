# 🧰 PDF & Image Compression + PDF Merger Tools

This repository provides 3 handy Python scripts for:

- 📄 **PDF Compression** using Ghostscript
- 📁 **PDF Merging** using PyPDF2
- 🖼️ **Image Compression** using PIL (Pillow)

These scripts are beginner-friendly and can be run both **locally** and on **Google Colab** for quick file processing.

---

## 🚀 Features

- Lightweight & easy to set up
- Virtual environment friendly
- Supports automation / batch processing
- Google Colab compatible for zero-installation use

---

## 📦 Requirements

- Python 3.7+
- [Ghostscript](https://www.ghostscript.com/download.html) (for PDF compression)
- pip packages:
  - `PyPDF2`
  - `Pillow`

---

## 🧑‍💻 Local Setup (Step-by-Step)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/pdf-tools.git
cd pdf-tools

2️⃣ Create and activate a virtual environment (optional but recommended)
# Create a virtual environment
python -m venv env

# Activate it
# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt
If requirements.txt is not present, install manually:
pip install PyPDF2 Pillow

☁️ Run on Google Colab (No Install Required)
📥 STEP 1: Upload Files
Use this code in a Colab cell to upload your files:
from google.colab import files
uploaded = files.upload()

Select your PDF/image files when prompted.

▶️ STEP 2: Run Script
Paste and run the script after uploading files:

📤 STEP 3: Download Output File
To download the output file after processing, use:
from google.colab import files
files.download("output_filename.pdf")  # Replace with your actual output file

🔗 Open in Google Colab

PDF Merger in Colab
Image Compressor in Colab
