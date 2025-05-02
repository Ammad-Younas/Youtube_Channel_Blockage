# Channel Blocker

A Python-based tool that automatically closes browser tabs when it detects specific channel names or content based on screenshots.

## Features

- Automatically monitors browser tabs
- Uses image recognition to detect specific channel names/content
- Configurable detection threshold
- Runs in the background with minimal system impact

## Requirements

- Python 3.x
- Required Python packages:
  - pyautogui
  - keyboard
  - opencv-python (cv2)
  - numpy

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install pyautogui keyboard opencv-python numpy
   ```
3. Create a `_internal/TARGETS` folder in the project directory
4. Add screenshots of the channel names/content you want to block in the TARGETS folder

## Usage

1. Place screenshots of the channel names or content you want to block in the `_internal/TARGETS` folder
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will start monitoring and automatically close any tabs that match the target images

## Configuration

You can modify the following parameters in `main.py`:

- `CHECK_INTERVAL`: Time interval between checks (in seconds)
- `THRESHOLD`: Image matching threshold (0.0 to 1.0)
- `TARGET_FOLDER`: Location of target images

## Notes

- The script supports various image formats: PNG, JPG, JPEG, BMP, TIFF, and WEBP
- Make sure the screenshots are clear and representative of what you want to block
- The script runs continuously until manually stopped
- Use Ctrl+C to stop the script

## Disclaimer

This tool is provided as-is. Use it responsibly and in accordance with applicable laws and terms of service.
