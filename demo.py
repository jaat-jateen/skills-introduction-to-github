#!/usr/bin/env python3
"""
Demo script to showcase the wallpaper generator capabilities
Generates several example wallpapers with different styles
"""

import os
from wallpaper_generator import WallpaperGenerator


def main():
    """Generate demo wallpapers."""
    print("Wallpaper Generator Demo")
    print("=" * 50)
    
    # Create output directory
    output_dir = "demo_wallpapers"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize generator
    generator = WallpaperGenerator(1280, 720)
    
    # Demo 1: Simple gradient
    print("\n1. Generating blue gradient wallpaper...")
    generator.generate_custom_wallpaper(
        color1=(33, 150, 243),
        color2=(30, 136, 229),
        pattern_type='none',
        output_path=f"{output_dir}/01_blue_gradient.png"
    )
    
    # Demo 2: Gradient with circles
    print("2. Generating purple wallpaper with circles...")
    generator.generate_custom_wallpaper(
        color1=(156, 39, 176),
        color2=(123, 31, 162),
        pattern_type='circles',
        output_path=f"{output_dir}/02_purple_circles.png"
    )
    
    # Demo 3: Gradient with squares and text
    print("3. Generating green wallpaper with squares and text...")
    generator.generate_custom_wallpaper(
        color1=(76, 175, 80),
        color2=(67, 160, 71),
        pattern_type='squares',
        text="Hello World",
        output_path=f"{output_dir}/03_green_squares_text.png"
    )
    
    # Demo 4: Gradient with triangles and text
    print("4. Generating orange wallpaper with triangles and text...")
    generator.generate_custom_wallpaper(
        color1=(255, 87, 34),
        color2=(244, 67, 54),
        pattern_type='triangles',
        text="Be Creative",
        output_path=f"{output_dir}/04_orange_triangles_text.png"
    )
    
    # Demo 5: Random wallpapers
    print("5. Generating 3 random wallpapers...")
    for i in range(3):
        generator.generate_random_wallpaper(
            text=f"Random #{i+1}",
            output_path=f"{output_dir}/05_random_{i+1}.png"
        )
    
    print("\n" + "=" * 50)
    print(f"Demo complete! Check the '{output_dir}' folder for results.")
    print(f"Generated 7 example wallpapers.")


if __name__ == '__main__':
    main()
