# Icon Generator Script

## Overview
This Python script generates simple icons with custom text. It creates a 32x32 PNG image with a randomly colored background and centers the user-provided text in a contrasting color.

## Requirements
- Python 3.x
- Pillow library (PIL fork)

## Installation
1. Ensure you have Python installed.
2. Install the Pillow library:
   ```bash
   pip install Pillow
   ```

## Usage
Run the script in a Python environment. You will be prompted to enter the text for the icon and a filename (without the extension). The script will generate an icon with your text and save it as a PNG file in the current directory.

### Example
```bash
python icon_generator.py
```

Input:
```
Enter the text for the icon: Hello
Enter the filename for the icon (without extension): example
```

Output:
```
Icon created and saved as .\example.png
```

## Features
- Generates a 32x32 icon with customizable text.
- Randomly colored background with adjustable alpha.
- Auto-adjusts text color for better visibility.
- Wraps text to fit the icon's dimensions.
- Customizable font size and line length.

## Customization
You can modify the following parameters in the script:
- `width`, `height`: Dimensions of the icon.
- `background_alpha`: Alpha value of the background color.
- `font_size`: Size of the text font.
- `max_line_length`: Maximum number of characters per line.

## Note
- The script uses `smalle.otf` font. If it's not available, it defaults to a basic font. Make sure the font file is in the script's directory or update the script with the path to your font file.