
pip install image_augmentation

from image_augmentation import augment


img_load_path = "/content/drive/MyDrive/Ai_Lab"
img_save_path = "/content/drive/MyDrive/Ai_Lab"
augment(
    img_load_path=img_load_path,
    img_save_path=img_save_path,
    operation="brightness",
    operation="add",
    value=100
)

