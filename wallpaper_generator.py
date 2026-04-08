#!/usr/bin/env python3
"""
Automatic Wallpaper Generator
Creates customized wallpapers with gradients, patterns, and text.
"""

import os
import random
import argparse
from datetime import datetime

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: The 'Pillow' library is not installed.")
    print("Please install it by running:\n")
    print("    pip install -r requirements.txt\n")
    print("Or directly:\n")
    print("    pip install Pillow\n")
    raise SystemExit(1)


class WallpaperGenerator:
    """Generate custom wallpapers with various designs."""
    
    def __init__(self, width=1920, height=1080):
        """
        Initialize the wallpaper generator.
        
        Args:
            width: Width of the wallpaper in pixels
            height: Height of the wallpaper in pixels
        """
        self.width = width
        self.height = height
        
    def create_gradient(self, color1, color2, direction='horizontal'):
        """
        Create a gradient background.
        
        Args:
            color1: Starting color (R, G, B)
            color2: Ending color (R, G, B)
            direction: 'horizontal', 'vertical', or 'diagonal'
        
        Returns:
            PIL Image with gradient
        """
        image = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        if direction == 'horizontal':
            for x in range(self.width):
                ratio = x / self.width
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                draw.line([(x, 0), (x, self.height)], fill=(r, g, b))
        elif direction == 'vertical':
            for y in range(self.height):
                ratio = y / self.height
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        else:  # diagonal
            for y in range(self.height):
                for x in range(self.width):
                    ratio = (x + y) / (self.width + self.height)
                    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                    draw.point((x, y), fill=(r, g, b))
        
        return image
    
    def add_geometric_pattern(self, image, pattern_type='circles'):
        """
        Add geometric patterns to the wallpaper.
        
        Args:
            image: Base PIL Image
            pattern_type: Type of pattern ('circles', 'squares', 'triangles')
        
        Returns:
            PIL Image with patterns
        """
        draw = ImageDraw.Draw(image, 'RGBA')
        
        if pattern_type == 'circles':
            for _ in range(20):
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                radius = random.randint(50, 200)
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(30, 80)
                )
                draw.ellipse([x - radius, y - radius, x + radius, y + radius],
                           fill=color)
        
        elif pattern_type == 'squares':
            for _ in range(15):
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                size = random.randint(50, 150)
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(30, 80)
                )
                draw.rectangle([x, y, x + size, y + size], fill=color)
        
        elif pattern_type == 'triangles':
            for _ in range(15):
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                size = random.randint(50, 150)
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(30, 80)
                )
                points = [
                    (x, y),
                    (x + size, y),
                    (x + size // 2, y + size)
                ]
                draw.polygon(points, fill=color)
        
        return image
    
    def add_text(self, image, text, font_size=60, color=(255, 255, 255)):
        """
        Add text to the wallpaper.
        
        Args:
            image: Base PIL Image
            text: Text to add
            font_size: Font size
            color: Text color (R, G, B)
        
        Returns:
            PIL Image with text
        """
        draw = ImageDraw.Draw(image)
        
        try:
            # Try to use a system font
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Calculate text position (centered)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        position = ((self.width - text_width) // 2, (self.height - text_height) // 2)
        
        # Add shadow for better readability
        shadow_offset = 3
        draw.text((position[0] + shadow_offset, position[1] + shadow_offset),
                 text, font=font, fill=(0, 0, 0, 128))
        draw.text(position, text, font=font, fill=color)
        
        return image
    
    def generate_random_wallpaper(self, text=None, output_path=None):
        """
        Generate a random wallpaper with various designs.
        
        Args:
            text: Optional text to add to wallpaper
            output_path: Path to save the wallpaper
        
        Returns:
            PIL Image
        """
        # Random color schemes
        color_schemes = [
            [(33, 150, 243), (30, 136, 229)],  # Blue
            [(156, 39, 176), (123, 31, 162)],  # Purple
            [(255, 87, 34), (244, 67, 54)],    # Red-Orange
            [(76, 175, 80), (67, 160, 71)],    # Green
            [(255, 193, 7), (255, 160, 0)],    # Amber
            [(0, 188, 212), (0, 172, 193)],    # Cyan
            [(233, 30, 99), (216, 27, 96)],    # Pink
        ]
        
        # Choose random colors and direction
        colors = random.choice(color_schemes)
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])
        
        # Create gradient background
        image = self.create_gradient(colors[0], colors[1], direction)
        
        # Add geometric pattern
        pattern_type = random.choice(['circles', 'squares', 'triangles'])
        image = self.add_geometric_pattern(image, pattern_type)
        
        # Add text if provided
        if text:
            image = self.add_text(image, text)
        
        # Save if output path provided
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            image.save(output_path, 'PNG')
            print(f"Wallpaper saved to: {output_path}")
        
        return image
    
    def generate_custom_wallpaper(self, color1, color2, pattern_type, text=None, output_path=None):
        """
        Generate a custom wallpaper with specific parameters.
        
        Args:
            color1: Starting color tuple (R, G, B)
            color2: Ending color tuple (R, G, B)
            pattern_type: Type of pattern ('circles', 'squares', 'triangles', or 'none')
            text: Optional text to add
            output_path: Path to save the wallpaper
        
        Returns:
            PIL Image
        """
        # Create gradient background
        image = self.create_gradient(color1, color2, 'diagonal')
        
        # Add pattern if requested
        if pattern_type != 'none':
            image = self.add_geometric_pattern(image, pattern_type)
        
        # Add text if provided
        if text:
            image = self.add_text(image, text)
        
        # Save if output path provided
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            image.save(output_path, 'PNG')
            print(f"Wallpaper saved to: {output_path}")
        
        return image


def main():
    """Main function to run the wallpaper generator from command line."""
    parser = argparse.ArgumentParser(description='Generate custom wallpapers automatically')
    parser.add_argument('--width', type=int, default=1920, help='Width of wallpaper (default: 1920)')
    parser.add_argument('--height', type=int, default=1080, help='Height of wallpaper (default: 1080)')
    parser.add_argument('--text', type=str, help='Text to display on wallpaper')
    parser.add_argument('--output', type=str, default='wallpaper.png', help='Output file path')
    parser.add_argument('--random', action='store_true', help='Generate random wallpaper')
    parser.add_argument('--count', type=int, default=1, help='Number of wallpapers to generate (with --random)')
    
    args = parser.parse_args()
    
    generator = WallpaperGenerator(args.width, args.height)
    
    if args.random:
        # Generate multiple random wallpapers
        for i in range(args.count):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_name = f"wallpaper_{timestamp}_{i}.png" if args.count > 1 else args.output
            generator.generate_random_wallpaper(text=args.text, output_path=output_name)
    else:
        # Generate a single random wallpaper
        generator.generate_random_wallpaper(text=args.text, output_path=args.output)
    
    print("Wallpaper generation complete!")


if __name__ == '__main__':
    main()
