from PIL import Image

def convert_to_16bit_style_pixel_art(image_path, output_path, pixel_size=128, palette_size=64):
    # Load and resize down (simulate sprite size)
    img = Image.open(image_path)
    img_small = img.resize((pixel_size, pixel_size), resample=Image.BILINEAR)

    # Simulate 16-bit color reduction
    img_small = img_small.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

    # Upscale to make blocky but crisp
    upscale_factor = img.size[0] // pixel_size
    img_pixel_art = img_small.resize(img.size, Image.NEAREST)

    # Save and show
    img_pixel_art.save(output_path)
    img_pixel_art.show()

# Your image path
image_path = r"C:\Users\home\Downloads\2025-07-16 at 00.21.23_c531f33c.jpg"
output_path = r"C:\Users\home\Downloads\pixel_art_16bit_style.png"

convert_to_16bit_style_pixel_art(image_path, output_path, pixel_size=128, palette_size=64)