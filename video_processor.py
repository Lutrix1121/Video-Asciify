import cv2
import os
from PIL import Image


def video_to_images(path, output_dir='Images'):
    """Extract frames from video and save as images."""
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        
    video = cv2.VideoCapture(path)   
    fps = video.get(cv2.CAP_PROP_FPS) 
    success, image = video.read()   
    counter = 1                  
    
    while success:
        cv2.imwrite(f"{output_dir}/Image{counter}.jpg", image)
        success, image = video.read()
        counter += 1
        
    video.release()
    return fps, (counter - 1)


def create_video_from_images(image_dir, output_path, fps, image_count):
    """Create video from processed images."""
    # Get resolution from first image
    first_image_path = f'{image_dir}/Image1.jpg'
    res = Image.open(first_image_path).size 
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(output_path, fourcc, int(fps), res)

    # Add all images to video
    for i in range(1, image_count + 1):             
        image_path = f'{image_dir}/Image{i}.jpg'
        video.write(cv2.imread(image_path))
        
    video.release()
