# 📌 Is script ka use 3 PDF files ko ek single file mein merge karne ke liye hota hai.

import PyPDF2

# 👇 Sabhi input PDFs ko open karo (binary read mode mein)
# you can add more file as file 4, 5, 6 in that manner you can do
with open('HIGHSCHOOL.pdf', 'rb') as file1, \
     open('INTERMEDIATE.pdf', 'rb') as file2, \
     open('Degree.pdf', 'rb') as file3:

    # 📚 Har file ke liye reader object banao
    pdf_reader1 = PyPDF2.PdfReader(file1)
    pdf_reader2 = PyPDF2.PdfReader(file2)
    pdf_reader3 = PyPDF2.PdfReader(file3)

    # 📝 Output ke liye writer object banao
    pdf_writer = PyPDF2.PdfWriter()

    # 📥 Sabhi pages ko ek-ek karke add karo writer mein
    for page in pdf_reader1.pages:
        pdf_writer.add_page(page)

    for page in pdf_reader2.pages:
        pdf_writer.add_page(page)

    for page in pdf_reader3.pages:
        pdf_writer.add_page(page)

    # 🗃️ Final merged PDF save karo
    with open('fileKaMergeHoneKeBadName.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)

print("✅ PDFs merged successfully!")
