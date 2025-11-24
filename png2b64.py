import base64

def png_to_base64(png_path, output_txt_path=None):
    """
    Convert a PNG file to a Base64 string.
    Optionally save the Base64 string to a .txt file.
    """
    with open(png_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    if output_txt_path:
        with open(output_txt_path, "w") as txt_file:
            txt_file.write(encoded)

    return encoded


def base64_to_png(base64_str, output_png_path):
    """
    Convert a Base64 string back into a PNG file.
    """
    img_data = base64.b64decode(base64_str)
    with open(output_png_path, "wb") as png_file:
        png_file.write(img_data)


if __name__ == "__main__":
    # Example usage:

    # 1) Convert PNG to Base64
    b64 = png_to_base64("C:\\Users\\joaom\\Desktop\\IMG_20240517.jpg", "C:\\Users\\joaom\\Desktop\\encoded.txt")
    print("Base64 output saved to encoded.txt")

    # 2) Convert Base64 back to PNG
    with open("C:\\Users\\joaom\\Desktop\\encoded.txt", "r") as f:
        b64_str = f.read()

    base64_to_png(b64_str, "C:\\Users\\joaom\\Desktop\\decoded.png")
    print("PNG restored as decoded.png")
