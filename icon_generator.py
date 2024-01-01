from PIL import Image, ImageDraw, ImageFont
import random
import textwrap

def create_icon_with_text(text, file_path):
    # Constants
    width, height = 32, 32  # Image dimensions
    background_alpha = 128  # Alpha value for the background
    font_size = 9           # Font size (may need adjustment)
    max_line_length = 8     # Max characters per line

    # Generate a random background color with alpha = 128
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), background_alpha)

    # Create an image with the specified background color
    image = Image.new("RGBA", (width, height), bg_color)

    # Determine a contrasting text color
    text_color = (255, 255, 255) if sum(bg_color[:3]) / 3 < 128 else (0, 0, 0)

    # Prepare to draw on the image
    draw = ImageDraw.Draw(image)
    try:
        # A simple small font
        font = ImageFont.truetype("smalle.otf", font_size)
    except IOError:
        # Default to a simpler font if the preferred one is not available
        font = ImageFont.load_default()

    # Split text into multiple lines if necessary
    lines = textwrap.wrap(text, width=max_line_length)

    # Calculate text height to center it vertically
    text_height = sum(font.getsize(line)[1] for line in lines)
    y_start = (height - text_height) // 2

    # Draw each line of text
    y = y_start
    for line in lines:
        text_width, line_height = font.getsize(line)
        x = (width - text_width) // 2
        x = round(x)  # Ensure x is an integer for pixel-perfect alignment
        y = round(y)  # Ensure y is rounded to the nearest pixel
        draw.text((x, y), line, fill=text_color, font=font, align="left")
        y += line_height

    # Save the image
    image.save(file_path)

# Script execution starts here
if __name__ == "__main__":
    user_text = input("Enter the text for the icon: ")
    file_name = input("Enter the filename for the icon (without extension): ")
    file_path = f".\{file_name}.png"

    create_icon_with_text(user_text, file_path)
    print(f"Icon created and saved as {file_path}")
