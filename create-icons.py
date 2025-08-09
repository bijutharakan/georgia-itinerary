#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import io

def create_icon(size):
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw gradient circle (simplified - just using solid color)
    # Using average of the gradient colors
    circle_color = (135, 203, 119, 255)  # Green from gradient
    draw.ellipse([0, 0, size-1, size-1], fill=circle_color)
    
    # Draw a second circle with yellow tint
    overlay = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    draw_overlay.ellipse([0, 0, size-1, size-1], fill=(255, 217, 61, 128))
    img = Image.alpha_composite(img, overlay)
    
    # Add the Lari symbol (using a simple L for now)
    draw = ImageDraw.Draw(img)
    try:
        # Try to use a nice font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size=int(size * 0.5))
    except:
        font = ImageFont.load_default()
    
    # Draw the Georgian Lari symbol (₾) - using 'L' as fallback
    text = "₾"
    # Get text bbox for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) / 2, (size - text_height) / 2 - bbox[1])
    
    draw.text(position, text, fill=(255, 255, 255, 255), font=font)
    
    return img

# Create both icon sizes
try:
    # Create 192x192 icon
    icon_192 = create_icon(192)
    icon_192.save('icon-192.png', 'PNG')
    print("Created icon-192.png")
    
    # Create 512x512 icon
    icon_512 = create_icon(512)
    icon_512.save('icon-512.png', 'PNG')
    print("Created icon-512.png")
    
    print("Icons created successfully!")
except ImportError:
    print("Pillow library not installed. Install with: pip3 install Pillow")
except Exception as e:
    print(f"Error creating icons: {e}")