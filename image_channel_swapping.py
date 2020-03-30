import numpy as np

def BGR2RGB(img_in):
    """
    """
    if not isinstance(img_in, np.ndarray):
        raise ValueError('Image data type is not ndarray')

    img = img_in.copy()    

    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # BGR => RGB
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img
