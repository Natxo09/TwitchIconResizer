# Twitch Icon Resizer

This Python script allows users to resize an image to predefined sizes and save the resized images in a dedicated folder. The script uses the PIL library to handle image operations and `tkinter` for the file selection dialog.

## Features

- **Select an image**: Open a dialog to select an image file to resize.
- **Resize images**: Automatically resize the image to 18x18, 36x36, and 72x72 pixels.
- **Save images**: Creates a new folder named after the image file and saves the resized images in that folder.

## Prerequisites

Before you run this script, make sure you have Python and PIL (Pillow) installed on your system. You can install Pillow using pip if it's not already installed:

```bash
pip install Pillow
