import os
from PIL import Image
import pillow_avif  # required to enable AVIF support

"""
Script to convert PNG files into a better low-size AVIF file.
This can be useful for easier storage of photos, which can be the main problem.
"""

# ----------- SETTINGS -----------
input_folder = ""               # folder with your PNGs
output_folder = ""              # folder to save AVIF images
max_width = 1280                # resize target (e.g., 1280 px wide)
max_height = 720                # optional limit (keeps aspect ratio)
avif_quality = 55               # 30–60 is a good range for photos
# --------------------------------

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if not (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg") or file.lower().endswith(".png")):
        continue

    input_path = os.path.join(input_folder, file)
    output_name = os.path.splitext(file)[0] + ".avif"
    output_path = os.path.join(output_folder, output_name)

    with Image.open(input_path) as img:

        # Keep the correct image orientation
        orientation = img.getexif().get(274)
        if orientation == 3:  # upside down
            img = img.rotate(180, expand=True)
        elif orientation == 6:  # rotated 90 CW
            img = img.rotate(90, expand=True)
        elif orientation == 8:  # rotated 270 CW
            img = img.rotate(-90, expand=True)

        # Convert to RGB if it's PNG with alpha (AVIF supports alpha, but RGB is usually smaller)
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")

        # Resize
        img.thumbnail((max_width, max_height), Image.LANCZOS)

        # Save as AVIF
        img.save(
            output_path,
            format="AVIF",
            quality=avif_quality,
            chroma_subsampling="420",   # best for small size
            lossless=True               # lossy AVIF is smallest
        )

    print(f"Saved: {output_path}")

print("Done converting all image files.")
