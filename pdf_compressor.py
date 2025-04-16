# 📌 Is script ka use PDF file ka size kam karne ke liye hota hai.
# 🛠️ Iske liye system mein Ghostscript installed hona chahiye (gs command).

import os
import subprocess

# 👇 Yeh function PDF compress karta hai
def compress_pdf(input_path, output_path, quality='screen'):
    command = [
        'gs',  # Ghostscript command
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS=/{quality}',  # Quality level: screen, ebook, printer
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',  # Output file ka path
        input_path  # Input file ka path
    ]
    
    # ⚙️ Command run karo
    subprocess.run(command, check=True)

    # 📊 Size check aur print karo
    print(f"✅ Compressed PDF saved as '{output_path}'")
    print(f"📦 Original size: {os.path.getsize(input_path)/1024:.2f} KB")
    print(f"📉 Compressed size: {os.path.getsize(output_path)/1024:.2f} KB")

# ✅ Yahan se function call ho raha hai (input/output file ke path ke saath)
input_pdf_path = "input.pdf"
output_pdf_path = "output.pdf"

# ✨ Quality levels: screen < ebook < printer < prepress < default
compress_pdf(input_pdf_path, output_pdf_path, quality='ebook')
