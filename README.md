![WIP](https://img.shields.io/badge/status-work--in--progress-yellow)

# 🦖 Chrome Dino for Pico

A minimalist clone of the Chrome Dino game, built for the Raspberry Pi Pico microcontroller and ST7735 OLED display. Assets are preprocessed on PC using Python, then rendered on Pico with MicroPython.

![Alt Text](assets/preview.gif)

---
## 🔧 Hardware requirements

- Raspberry Pi Pico (or compatible MicroPython board)
- ST7735 OLED Display (or similar)
- Computer with Python 3 for preprocessing game assets.

---
## 🚀 How to use

### 1. Connect Display to Pico

Wire up your ST7735 display to the Pico.

### 2. Prepare Assets

Place black-and-white `.png` sprite files into the `assets/` directory (or use the defaults), and run:

```bash
python parser/png_to_pixels.py
```

This will generate `pico/sprites.py`, containing pixel data in a format optimized for rendering on Pico.

### 3. Upload Code to Pico

Use a tool like Thonny, rshell, or ampy to upload all files from `pico/` directory to your microcontroller's filesystem.

### 4. Launch the Game

If using Raspberry Pi Pico, code in `main.py` will auto-run on boot.
Otherwise, run main.py manually.

---
## 🧠 Credits
- Based on the original **Chrome Dino** game by Google.
- Display driver based on the work of [GuyCarver](https://github.com/GuyCarver), author of the original ST7735 MicroPython driver.
