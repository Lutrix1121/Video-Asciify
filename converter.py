import imgkit
import os
from video_processor import video_to_images, create_video_from_images
from image_processor import get_image, pixelate_image, grayscale_image, get_color_data
from ascii_converter import ascii_conversion, get_default_ascii_chars
from html_generator import create_ascii_html
from file_manager import create_directories, cleanup_directories


def conversion(video_path, output_video='final_video.mp4',progress_callback=None):
    """
    Convert video to ASCII art video.
    
    Args:
        video_path (str): Path to input video file
        output_video (str): Path for output video file
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    wkhtmltoimage_path = os.path.join(current_dir, 'wkhtmltoimage.exe')
    # Configuration for imgkit
    config = imgkit.config(wkhtmltoimage=wkhtmltoimage_path)  
    
    # Get ASCII character set
    ascii_string = get_default_ascii_chars()
    
    # Step 1: Extract frames from video
    print("Extracting frames from video...")
    fps, number_images = video_to_images(video_path)
    
    # Step 2: Create working directories
    directories = ['HtmlImages', 'TextImages']
    create_directories(directories)

    # Step 3: Process each frame
    print(f"Processing {number_images} frames...")
    for i in range(1, number_images + 1):
        # Load and resize image
        image = get_image(f'Images/Image{i}.jpg')
        
        # Create pixelated version
        right_size_image = pixelate_image(image)
        
        # Convert to grayscale
        bw_image = grayscale_image(right_size_image)
        
        # Convert to ASCII
        converted_list = ascii_conversion(bw_image, ascii_string)
        
        # Get color data
        color_list = get_color_data(right_size_image)
        
        # Generate HTML with colored ASCII
        html_path = create_ascii_html(converted_list, right_size_image, color_list, i)
        
        # Convert HTML to image
        output_image_path = f'TextImages/Image{i}.jpg'
        imgkit.from_file(html_path, output_image_path, config=config)
        
        progress = (i / number_images) * 100
        if progress_callback:
            progress_callback(i, number_images, progress)

        # Progress indicator
        print(f"{i}/{number_images}")

    # Step 4: Create final video
    print("Creating final video...")
    create_video_from_images('TextImages', output_video, fps, number_images)
    
    # Step 5: Cleanup
    print("Cleaning up temporary files...")
    cleanup_directories(['Images', 'HtmlImages', 'TextImages'])
    
    print(f"Conversion complete! Output saved as: {output_video}")


