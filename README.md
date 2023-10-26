README
This repository contains a Python script for generating copies of an image with random 5-character codes and saving the modified images to an output directory. It also creates a text file that stores the generated codes. This README provides an overview of how to use the code and its components.

Requirements
Python 3.x
Pillow (PIL) library
You can install it using pip install Pillow
Usage
Clone or download this repository to your local machine.

Make sure you have the required dependencies installed.

Replace "path/to/source_image.jpg" with the path to your source image. The source image should be a valid image file (e.g., JPEG).

Set the desired output directory by changing "path/to/output_directory/" to the directory where you want to save the modified images and the codes file.

Specify the font file path and font size as follows:

font_path: Set the path to the TrueType font file you want to use for the code.
font_size: Adjust the font size as needed.
Set the number of copies you want to generate by modifying the num_copies variable. In the provided code, it's set to 1111, but you can change it to any desired number.

Customize the code placement by adjusting the code_location variable. The values (100, 100) indicate the (x, y) coordinates on the image where the code will be placed. Modify these coordinates as necessary.