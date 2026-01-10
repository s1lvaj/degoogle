import os
from PIL import Image
import pillow_avif  # required to enable AVIF support

"""
Script to convert PNG files into a better low-size file.
This can be useful for easier storage of photos, which can be the main problem.
"""

def convert_images(
        new_type,
        input_folder,
        output_folder,
        max_width=None,  # max_width=1280 is a good width example
        max_height=None,  # max_height=720 is a good height example
        quality=None  # 30–60 is a good range for photos, like 55
        ):
    """
    Convert images to a new type.
    
    :param new_type: Description
    :param input_folder: Description
    :param output_folder: Description
    :param max_width: Description
    :param max_height: Description
    :param quality: Description

    :return: None.
    """
    
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if not (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg") or file.lower().endswith(".png")):
            continue

        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0] + "." + new_type
        output_path = os.path.join(output_folder, output_name)

        with Image.open(input_path) as img:

            # Keep the correct image orientation
            orientation = img.getexif().get(274)
            print(f"Update Orientation: {orientation}")
            if orientation == 3:  # upside down
                img = img.rotate(180, expand=True)
            elif orientation == 6:  # rotated 90 CW
                img = img.rotate(90, expand=True)
            elif orientation == 8:  # rotated 270 CW
                img = img.rotate(-90, expand=True)

            # Resize
            if (max_width is not None) and (max_height is not None):
                img.thumbnail((max_width, max_height), Image.LANCZOS)

            # Save as new type
            if quality is not None:
                img.save(
                    output_path,
                    format=new_type.upper(),
                    quality=quality,
                    chroma_subsampling="420",   # best for small size
                    lossless=True               # lossy AVIF is smallest
                )
            else:
                img.save(
                    output_path,
                    format=new_type.upper()
                )

        print(f"Saved: {output_path}")
    return


if __name__ == '__main__':
    FOLDER = os.path.dirname(os.path.realpath(__file__))
    convert_images('webp', FOLDER, FOLDER, max_width=1280, max_height=720)
    print("Done converting all image files.")