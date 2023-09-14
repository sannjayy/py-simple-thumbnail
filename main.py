from PIL import Image, ImageDraw, ImageFont

def generate_thumbnail_with_text(width, height, background_color, text, text_color, font_path, output_file):
    # Create a new image with the specified dimensions and background color
    image = Image.new('RGB', (width, height), background_color)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Load a font (you can customize the font size and style)
    font = ImageFont.truetype(font_path, size=73)
    
    # Calculate text size and position
    # text_width, text_height = 10.10, 10.23
    text_width = width * 0.8
    text_height = height * 0.8
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw the text on the image
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image to the specified output file
    image.save(output_file)

if __name__ == "__main__":
    # Thumbnail dimensions
    width = 1600
    height = 840
    
    # Background color (RGB tuple)
    background_color = (238, 255, 204, 1)  # Light Green
    
    # Text to be added
    text = "Extracting text from a PDF \n-with Python!"
    
    # Text color (RGB tuple)
    # text_color = (90, 80, 80, 1)  # Gray
    text_color = (40, 98, 252, 1)  # Blue
    
    # Font file path (you need to specify the path to a TrueType font file)
    font_path = "Poppins/Poppins-Bold.ttf"
    
    # Output file path
    output_file = "thumbnail.png"
    
    # Generate the thumbnail with text
    generate_thumbnail_with_text(width, height, background_color, text, text_color, font_path, output_file)
    print(f"Thumbnail with text generated: {output_file}")
