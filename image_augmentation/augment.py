import os
import cv2
from .functions import (hsv, brightness, contrast, blur, rotate_and_scale_image,
                        change_background_simple, change_background_segment)


def augment(img_load_path: str, img_save_path: str, oper: str = "brightness", **kwargs):
    """
    Load, change, and save images
    img_load_path: path to the main images
    img_save_path: path to save processed images
    oper: operation to apply ("hsv", "brightness", "contrast", "blur", "rotate_and_scale_image", "change_background_simple", "change_background_segment")
    kwargs: additional arguments for the operation
    """
    os.makedirs(img_save_path, exist_ok=True)
    
    image_paths = [
        os.path.join(img_load_path, img) for img in os.listdir(img_load_path)
        if img.endswith((".JPG", ".jpg"))
    ]

    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            continue

        if oper == "hsv":
            img_changed = hsv(img, **kwargs)
        elif oper == "brightness":
            img_changed = brightness(img, **kwargs)
        elif oper == "contrast":
            img_changed = contrast(img, **kwargs)
        elif oper == "blur":
            img_changed = blur(img, **kwargs)
        elif oper == "rotate_and_scale_image":
            img_changed = rotate_and_scale_image(img, **kwargs)
        elif oper == "change_background_simple":
            background_img = kwargs.pop("background_img", None)
            if background_img is None:
                raise ValueError("background_img must be provided for change_background_simple")
            if isinstance(background_img, str):
                background_img = cv2.imread(background_img)
            img_changed = change_background_simple(img, background_img)
        elif oper == "change_background_segment":
            background_img = kwargs.pop("background_img", None)
            if background_img is None:
                raise ValueError("background_img must be provided for change_background_segment")
            if isinstance(background_img, str):
                background_img = cv2.imread(background_img)
            img_changed = change_background_segment(img, background_img)
        else:
            raise ValueError("Operation must be one of: 'hsv', 'brightness', 'contrast', 'blur', 'rotate_and_scale_image', 'change_background_simple', 'change_background_segment'")

        img_r_path = os.path.join(img_save_path, os.path.basename(img_path))
        cv2.imwrite(img_r_path, img_changed)