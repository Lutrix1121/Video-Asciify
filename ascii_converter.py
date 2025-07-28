def ascii_conversion(bw_image, ascii_string=None):
    """Convert grayscale image to ASCII characters."""
    if ascii_string is None:
        ascii_string = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@", "&"]
    
    pixels = bw_image.getdata()      
    ascii_image_list = []         
    
    for pixel in pixels:          
        ascii_converted = int((pixel * len(ascii_string)) / 256) 
        ascii_image_list.append(ascii_string[ascii_converted]) 
        
    return ascii_image_list 


def get_default_ascii_chars():
    """Return the default ASCII character set for conversion."""
    return [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@", "&"]
