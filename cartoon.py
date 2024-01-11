import cv2
import os
import numpy as np

def display(image_path):
    img = cv2.imread(image_path)

    path = r'/Users/vinithreddy/projects/cartoonify-and-pencilskecth/static'
    if not os.path.exists(path):
        os.makedirs(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(os.path.join(path, 'cartoon.jpg'), cartoon)
    cv2.imwrite(os.path.join(path, 'image.jpg'), img)
    cv2.imwrite(os.path.join(path, 'gray.jpg'), gray)
    cv2.imwrite(os.path.join(path, 'edges.jpg'), edges)
    cv2.imwrite(os.path.join(path, 'color.jpg'), color)

    img_invert = cv2.bitwise_not(gray)
    gray_blur = cv2.GaussianBlur(gray, (25, 25), 0)
    pencil = cv2.divide(gray, gray_blur, scale=250.0)
    cv2.imwrite(os.path.join(path, 'gaussianblur.jpg'), gray_blur)
    cv2.imwrite(os.path.join(path, 'inverted.jpg'), img_invert)
    cv2.imwrite(os.path.join(path, 'pencil.jpg'), pencil)

    # Return the file paths of the processed images
    return {
        'cartoon': 'static/cartoon.jpg',
        'original': 'static/image.jpg',
        'gray': 'static/gray.jpg',
        'edges': 'static/edges.jpg',
        'color': 'static/color.jpg',
        'gaussianblur': 'static/gaussianblur.jpg',
        'inverted': 'static/inverted.jpg',
        'pencil': 'static/pencil.jpg'
    }
