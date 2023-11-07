from PIL import Image, ImageDraw, ImageFont
import random
import string

# Load the source image
source_image = Image.open("path/to/source_image.jpg")

# Set the desired output directory
output_directory = "path/to/output_directory/"

# Set the font and size for the code
font_path = "path/to/font.ttf"
font_size = 30

# Set the number of copies to generate
num_copies = 1111

# Set the specific location for the code
code_location = (100, 100)  # Adjust as needed

# List to store the generated codes
codes = []

# Generate copies
for i in range(num_copies):
    # Create a copy of the source image
    new_image = source_image.copy()

    # Generate a random 5-digit code with letters and numbers
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    codes.append(code)

    # Create a drawing object
    draw = ImageDraw.Draw(new_image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Draw the code on the image
    draw.text(code_location, code, font=font, fill=(0, 0, 0))

    # Save the image with the code
    new_image.save(output_directory + f"image_{code}.jpg")

# Write the codes to a text file
with open(output_directory + "codes.txt", "w") as file:
    file.write("\n".join(codes))
