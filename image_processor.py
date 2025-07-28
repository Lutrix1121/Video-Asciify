from PIL import Image, ImageOps


def get_image(image_path, resize_factor=1.05):
    """Load and slightly resize image."""
    initial_image = Image.open(image_path)   
    width, height = initial_image.size                 
    initial_image = initial_image.resize((round(width * resize_factor), height)) 
    return initial_image    


def pixelate_image(image, final_width=200):
    """Resize image to create pixelated effect."""
    width, height = image.size                 
    final_height = int((height * final_width) / width)  
    image = image.resize((final_width, final_height)) 
    return image


def grayscale_image(image):
    """Convert image to grayscale."""
    image_bw = ImageOps.grayscale(image) 
    return image_bw


def get_color_data(image):
    """Extract RGB color data from image pixels."""
    pixels = image.getdata()  # Creates a list with the RGB value for each pixel
    return pixels
