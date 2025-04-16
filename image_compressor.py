# 📌 Is script ka use image compress karne ke liye hota hai.
# 🎯 Target ye hai ki image 20 KB se kam na ho aur 50 KB se zyada bhi na ho.

from PIL import Image
import os

# 👇 Function jo image compress karta hai
def compress_image(input_path, output_path, min_size_kb=20, max_size_kb=50, target_dimensions=(200, 230)):
    # 🖼️ Image open karo
    img = Image.open(input_path)
    
    # 📏 Resize karo image ko given dimensions ke andar rakhte hue
    img.thumbnail(target_dimensions, Image.LANCZOS)

    quality = 91  # Start mein image ki quality
    step = 2      # Kitna quality badhaye/ghataye har step pe
    enlarge_factor = 1.03  # Agar image choti ho jaye to thoda bada karne ka factor

    for i in range(20):  # Max 20 attempts tak try karega
        # 📸 Compress karke save karo image
        img.save(output_path, format='JPEG', quality=quality, optimize=True)

        # 🔍 Check karo size
        current_size_kb = os.path.getsize(output_path) / 1024

        # ✅ Agar size sahi hai to done!
        if min_size_kb <= current_size_kb <= max_size_kb:
            print(f"✅ Compression successful. Final size: {current_size_kb:.2f} KB.")
            return

        # 📉 Agar size zyada hai to quality kam karo
        elif current_size_kb > max_size_kb:
            quality -= step
            quality = max(quality, 10)  # Quality minimum 10 tak hi jaaye

        # 📈 Agar size bahut kam hai to enlarge ya quality badhao
        elif current_size_kb < min_size_kb:
            if quality < 95:
                quality += step
            else:
                new_width = int(img.width * enlarge_factor)
                new_height = int(img.height * enlarge_factor)
                img = img.resize((new_width, new_height), Image.LANCZOS)

    print("⚠️ Unable to meet size requirements without compromising quality or size.")

# 👇 Input/output file ke path
input_image_path = 'signatureAnmol.jpg'
output_image_path = 'signatureAnmol_compressed.jpg'

# 🛠️ Function call
compress_image(input_image_path, output_image_path)
