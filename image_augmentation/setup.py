from setuptools import setup, find_packages

setup(
    name="image_augmentation",  
    version="0.1.0",  
    author="Erfan Shakouri",  
    author_email="",  
    description="A simple image augmentation library using OpenCV and YOLO", 
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/ErfanShakouri/AI_Image_Augmentation_lib",  
    packages=find_packages(),  
    install_requires=[
        "numpy>=1.19.0",
        "opencv-python>=4.5.0",
        "ultralytics>=8.0.0",       
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)