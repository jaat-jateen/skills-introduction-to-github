# Wallpaper Generator

Automatically generate beautiful, customized wallpapers with gradients, geometric patterns, and text.

## Features

- **Multiple Resolution Support**: Generate wallpapers in any resolution (default: 1920x1080)
- **Gradient Backgrounds**: Beautiful gradient backgrounds with multiple color schemes
- **Geometric Patterns**: Choose from circles, squares, or triangles
- **Custom Text**: Add personalized text to your wallpapers
- **Random Generation**: Create unique wallpapers with random designs
- **Batch Generation**: Generate multiple wallpapers at once

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Generate a Random Wallpaper

```bash
python3 wallpaper_generator.py --random
```

This will create a `wallpaper.png` file with a random design.

### Add Custom Text

```bash
python3 wallpaper_generator.py --random --text "Hello World"
```

### Generate Multiple Wallpapers

```bash
python3 wallpaper_generator.py --random --count 5 --text "My Design"
```

This will create 5 different wallpapers with timestamps in their filenames.

### Custom Resolution

```bash
python3 wallpaper_generator.py --random --width 2560 --height 1440
```

Generate a wallpaper for 2K displays.

### Specify Output File

```bash
python3 wallpaper_generator.py --random --output my_wallpaper.png
```

## Examples

### Example 1: Simple Gradient Wallpaper
```bash
python3 wallpaper_generator.py --random --output examples/gradient.png
```

### Example 2: Wallpaper with Text
```bash
python3 wallpaper_generator.py --random --text "Stay Creative" --output examples/creative.png
```

### Example 3: 4K Wallpaper
```bash
python3 wallpaper_generator.py --random --width 3840 --height 2160 --output examples/4k.png
```

### Example 4: Mobile Wallpaper
```bash
python3 wallpaper_generator.py --random --width 1080 --height 1920 --output examples/mobile.png
```

## Command Line Options

- `--width`: Width of the wallpaper in pixels (default: 1920)
- `--height`: Height of the wallpaper in pixels (default: 1080)
- `--text`: Custom text to display on the wallpaper
- `--output`: Output file path (default: wallpaper.png)
- `--random`: Generate a random wallpaper design
- `--count`: Number of wallpapers to generate (use with --random)

## Color Schemes

The generator includes several pre-defined color schemes:
- Blue tones
- Purple tones
- Red-Orange tones
- Green tones
- Amber/Yellow tones
- Cyan tones
- Pink tones

Each wallpaper randomly selects a color scheme and pattern type for unique results.

## Pattern Types

- **Circles**: Overlapping semi-transparent circles
- **Squares**: Random squares with varying opacity
- **Triangles**: Geometric triangle patterns

## Using as a Python Module

You can also use the wallpaper generator in your own Python scripts:

```python
from wallpaper_generator import WallpaperGenerator

# Create generator
generator = WallpaperGenerator(width=1920, height=1080)

# Generate random wallpaper
generator.generate_random_wallpaper(
    text="My Custom Text",
    output_path="my_wallpaper.png"
)

# Generate custom wallpaper
generator.generate_custom_wallpaper(
    color1=(33, 150, 243),  # Blue
    color2=(30, 136, 229),   # Darker blue
    pattern_type='circles',
    text="Custom Design",
    output_path="custom.png"
)
```

## Tips

1. **For Desktop Backgrounds**: Use your screen's native resolution
2. **For Mobile Devices**: Use portrait orientation (e.g., 1080x1920)
3. **Batch Generation**: Generate multiple wallpapers and pick your favorite
4. **Custom Text**: Keep text short for better visibility

## Troubleshooting

### Issue: "No module named 'PIL'"
**Solution**: Install Pillow: `pip install Pillow`

### Issue: Text not showing correctly
**Solution**: The generator will use system fonts if available, otherwise defaults to basic fonts

### Issue: Colors look different on different monitors
**Solution**: This is normal due to monitor calibration. Adjust your monitor settings or try different color schemes

## License

This project is licensed under the MIT License - see the LICENSE file for details.
