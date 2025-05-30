import argparse
from PIL import Image
import os

def crop_center_square_with_padding(image, pad_ratio):
    width, height = image.size
    short_side = min(width, height)

    # Apply padding by reducing the crop area further inward
    pad = int(short_side * pad_ratio)
    crop_size = short_side - 2 * pad  # Crop area after applying padding

    # Ensure crop_size is positive
    if crop_size <= 0:
        raise ValueError("pad_ratio is too large, resulting in non-positive crop size.")

    # Compute center coordinates
    center_x, center_y = width // 2, height // 2

    # Calculate crop box (left, upper, right, lower)
    left = center_x - crop_size // 2
    upper = center_y - crop_size // 2
    right = center_x + crop_size // 2
    lower = center_y + crop_size // 2

    # Crop the image
    cropped = image.crop((left, upper, right, lower))

    return cropped

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input image')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the output image')
    parser.add_argument('--pad_ratio', type=float, default=0.0, help='Ratio of padding to be cropped from each side (e.g., 0.1 means 10% of the short side)')
    args = parser.parse_args()

    # Load input image
    image = Image.open(args.input_path)

    # Crop and apply padding
    result_image = crop_center_square_with_padding(image, args.pad_ratio)

    # Save the result
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    result_image.save(args.output_path)
    print(f"Saved cropped image to {args.output_path}")

if __name__ == '__main__':
    main()
