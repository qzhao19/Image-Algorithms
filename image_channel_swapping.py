import numpy as np

def BGR2RGB(image):
    """
    """
    if not isinstance(image, np.ndarray):
        raise ValueError('Image data type is not ndarray')

    b = image[:, :, 0].copy()
    g = image[:, :, 1].copy()
    r = image[:, :, 2].copy()

    # BGR => RGB
    image[:, :, 0] = r
    image[:, :, 1] = g
    image[:, :, 2] = b

    return image
