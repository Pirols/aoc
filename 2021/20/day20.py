import numpy as np
from pathlib import Path


def enhance_image(img, algorithm, constant_val):
    inf_img = np.pad(img, (2, 2), 'constant', constant_values=(constant_val, constant_val))
    out_width = img.shape[0]+2
    out_height = img.shape[1]+2
    out_img = np.zeros((out_width, out_height), dtype=np.uint8)
    for i in range(out_width):
        for j in range(out_height):
            kernel_total = int("".join([str(inf_img[idx, jdx]) for idx in range(i, i+3) for jdx in range(j, j+3)]), 2)
            out_img[i, j] = algorithm[kernel_total]
    return out_img


if __name__ == "__main__":
    data_path = Path('20_data.txt')

    with open(data_path, mode='r') as f:
        image_enhancement_algorithm = np.array([char == '#' for char in f.readline().rstrip()], dtype=np.uint8)
        f.readline()
        image = np.array([[char == '#' for char in line.rstrip()] for line in f], dtype=np.uint8)

    # part a
    print(f"Number of lit pixels: {np.sum(enhance_image(enhance_image(image, image_enhancement_algorithm, 0), image_enhancement_algorithm, 1))}")

    # part b
    res_img = image
    for i in range(50):
        res_img = enhance_image(res_img, image_enhancement_algorithm, i % 2 != 0)
    print(f"Number of lit pixels: {np.sum(res_img)}")
