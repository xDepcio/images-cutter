from PIL import Image
import os
import sys
import argparse


def get_images(sub_dir):
    file_names = os.listdir(f'sources/{sub_dir}')
    return file_names


def check_pixel_in_final_box(pixels, start_x, end_x, start_y, end_y, x, y):
    return x >= start_x and x <= end_x and y >= start_y and y <= end_y


def format_image(image, start_x, end_x, start_y, end_y):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            if not check_pixel_in_final_box(
                    pixels=pixels,
                    start_x=start_x, end_x=end_x,
                    start_y=start_y, end_y=end_y, x=x, y=y
            ):
                pixels[x, y] = (r, g, b, 0)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'type', type=str, help="cards type (spells, dungeons, heroes)")
    parser.add_argument('start_x', type=int, help="starting pixel x pos")
    parser.add_argument('start_y', type=int, help="starting pixel y pos")
    parser.add_argument('end_x', type=int, help="ending pixel x pos")
    parser.add_argument('end_y', type=int, help="ending pixel y pos")
    args = parser.parse_args()

    images_names = get_images(args.type)
    for image_name in images_names:
        img = Image.open(f'sources/{args.type}/{image_name}')
        format_image(img, args.start_x, args.end_x, args.start_y, args.end_y)
        img.save(f"outputs/{args.type}/{image_name}")


if __name__ == '__main__':
    main(sys.argv)


# Pixels for different images types (start_x, start_y, end_x, end_y):
# (114, 236, 607, 674) - spell card
# (78, 231, 667, 654) - hero card
