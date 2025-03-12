# Image Augmentation Library

![Python](https://img.shields.io/badge/python-3.6%2B-blue)

A Python library for image augmentation using OpenCV and YOLO. This library provides a variety of functions to manipulate images, such as adjusting HSV values, brightness, contrast, applying blur, rotating/scaling, and changing backgrounds using object detection and segmentation.

## Features

- **HSV Adjustment:** Modify hue, saturation, and value of images.
- **Brightness Adjustment:** Add or subtract brightness from images.
- **Contrast Adjustment:** Increase or decrease image contrast using gamma correction.
- **Blur Filter:** Apply Gaussian blur with adaptive kernel size.
- **Rotate and Scale:** Rotate and scale images with adjustable parameters.
- **Background Change (Simple):** Use YOLOv8 bounding box detection to replace the background of detected objects (e.g., persons).
- **Background Change (Segmentation):** Use YOLOv8 segmentation to precisely replace the background of detected objects.
- **Batch Processing:** Apply augmentations to all images in a directory and save the results.

## Installation

You can install the `image_augmentation` library via pip:

```bash
pip install image_augmentation
```

### Prerequisites

Ensure you have the following dependencies installed:
- Python 3.6 or higher
- `numpy>=1.19.0`
- `opencv-python>=4.5.0`
- `ultralytics>=8.0.0` (for YOLOv8 models)

You can install all dependencies automatically when you install the package via pip.

## Usage

The library provides a main function `augment` that can apply various operations to a directory of images. Below are some examples of how to use the library:

### Example 1: Increase Brightness

Increase the brightness of all images in a directory by adding a value of 100:

```python
from image_augmentation import augment

augment(
    img_load_path="/path/to/input",
    img_save_path="/path/to/output",
    oper="brightness",
    operation="add",
    value=100
)
```


## Available Operations

The `augment` function supports the following operations:

| Operation                  | Description                                      | Required Parameters                             |
|----------------------------|--------------------------------------------------|------------------------------------------------|
| `hsv`                     | Adjust HSV values (hue, saturation, value)      | `hue`, `saturation`, `value`                   |
| `brightness`              | Adjust brightness (add or subtract)             | `operation` ("add" or "subtract"), `value`     |
| `contrast`                | Adjust contrast using gamma correction          | `gamma` (float)                                |
| `blur`                    | Apply Gaussian blur with adaptive kernel size   | `threshold`, `high_th`, `low_th`               |
| `rotate_and_scale`        | Rotate and scale images                         | `rotation_amount_degree`, `scale_factor`       |
| `change_background_simple`| Replace background using YOLO bounding boxes    | `background_img` (path or numpy array)         |
| `change_background_segment`| Replace background using YOLO segmentation     | `background_img` (path or numpy array)         |

## Project Structure

```
image_augmentation/
│
├── image_augmentation/       # Main package directory
│   ├── __init__.py           # Package initialization
│   ├── functions.py          # Core augmentation functions
│   ├── augment.py            # Main augment function for batch processing
│
├── tests/                    # Test directory (optional)
│   ├── test.py  # Unit tests
│
├── setup.py                  # Setup script for installation
├── README.md                 # Project documentation
```



## Acknowledgments

- This library uses [OpenCV](https://opencv.org/) for image processing.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) is used for object detection and segmentation.
- Thanks to the open-source community for providing tools and inspiration.

