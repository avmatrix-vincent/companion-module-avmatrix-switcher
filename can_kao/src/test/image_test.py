from PIL import Image
import numpy as np

def print_png_rgb_values(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = np.array(img)

        height, width, _ = pixels.shape
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[y, x]
                print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
    except Exception as e:
        print(f"Error: {e}")

# 使用示例
print_png_rgb_values("res/images/delete_pressed_24x24.png")