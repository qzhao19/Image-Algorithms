import numpy as np

def BGR2GRAY(image):
    """Transform a bgr image to a gray image. Grayscale is a kind of image luminance 
    expression method and is calculated by the following formula: 
    Y = 0.2126*R + 0.7152*G + 0.0722*B

    Args:
        image: uint8 ndarray data 
    """
    if not isinstance(image, np.ndarray):
        raise ValueError('Image data type is not ndarray')

    image = image.astype(np.float)

    b = image[:, :, 0].copy()
    g = image[:, :, 1].copy()
    r = image[:, :, 2].copy()

    image_out = 0.2126*r + 0.7152*g + 0.0722*b
    image_out = image_out.astype(np.uint8)

    return image_out