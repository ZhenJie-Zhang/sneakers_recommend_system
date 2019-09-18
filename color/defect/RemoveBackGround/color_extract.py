# from PIL import Image
# from webcolors import rgb_to_hex, rgb_to_name, CSS3_NAMES_TO_HEX
#
# image = Image.open("test.jpg")
# color_list = image.getcolors(image.size[0]*image.size[1])
# color_list.sort(reverse=True)
# print(color_list)
#
# for CSS3_NAME, COLOR_HEX in CSS3_NAMES_TO_HEX.items():
#     print(COLOR_HEX, CSS3_NAME, sep="\t")
# print(len(CSS3_NAMES_TO_HEX))

# for count, col in color_list:
#     print(count, rgb_to_hex(col), sep="\t", end="\t")
    # try:
    #     print(rgb_to_name(col))
    #
    # except ValueError:
    #     print(None)

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)

fig, ax = plt.subplots(figsize=(12, 10))

for i, name in enumerate(sorted_names):
    print(name)

