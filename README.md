# Video Asciify

A Python application that downloads YouTube videos and converts them into ASCII art videos with preserved colors and motion.

## Features

- **YouTube Video Download**: Download videos directly from YouTube URLs
- **ASCII Art Conversion**: Convert video frames to colored ASCII art
- **Video Recreation**: Generate a new video file with ASCII art frames
- **GUI Interface**: User-friendly tkinter-based interface
- **Color Preservation**: Maintains original video colors in ASCII output

## How It Works

1. **Download**: Downloads YouTube videos using `pytubefix`
2. **Frame Extraction**: Extracts individual frames from the video
3. **ASCII Conversion**: Converts each frame to ASCII art using character mapping
4. **Color Mapping**: Preserves original colors by mapping RGB values to ASCII characters
5. **HTML Generation**: Creates colored HTML representations of each frame
6. **Image Rendering**: Converts HTML to images using `wkhtmltoimage`
7. **Video Reconstruction**: Combines ASCII art images back into a video

## Prerequisites

### Required Software
- Python 3.x
- `wkhtmltoimage` executable (for HTML to image conversion)

### Python Dependencies
```
pip install pillow opencv-python imgkit pytubefix
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/video-asciify.git
   cd video-asciify
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install wkhtmltoimage**:
   - **Windows**: Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
   - **macOS**: `brew install wkhtmltopdf`
   - **Linux**: `sudo apt-get install wkhtmltopdf`

4. **Configure wkhtmltoimage path**:
   Update the path in `Conversion.py` line 69:
   ```python
   config = imgkit.config(wkhtmltoimage=r'path/to/wkhtmltoimage')
   ```
   Don't need to change anything if the wkhtmltoimage is in the same folder as the program

## Usage

### GUI Application

1. **Run the main application**:
   ```bash
   python Video_Asciify.py
   ```

2. **Follow the GUI steps**:
   - Paste a YouTube video URL
   - Click "Download video" and select save directory
   - Click "Show latest video file" to confirm the download
   - Click "Start asciify" to begin conversion
   - Wait for processing to complete

### Programmatic Usage

```python
import Conversion

# Convert a local video file to ASCII art video
Conversion.conversion('path/to/your/video.mp4')
```

## File Structure

```
video-asciify/
├── Video_Asciify.py    # Main GUI application
├── Download.py         # YouTube video download functionality
├── Conversion.py       # ASCII art conversion logic
├── globals.py          # Global variables for state management
└── README.md          # This file
```

## Configuration

### ASCII Character Set
Modify the ASCII characters used for conversion in `Conversion.py`:
```python
ascii_string = [" ",".",":","-","=","+","*","#","%","@","&"]
```

### Output Resolution
Adjust the pixelation level by changing `final_width` in the `pixelate_image` function:
```python
def pixelate_image(image, final_width = 200):  # Lower = more pixelated
```

## Output

The application generates:
- `final_video.mp4`: The ASCII art version of your input video
- Temporary directories (automatically cleaned up):
  - `Images/`: Extracted video frames
  - `HtmlImages/`: HTML representations of ASCII frames
  - `TextImages/`: Rendered ASCII art images

## Limitations

- Processing time depends on video length and resolution
- Large videos may require significant disk space during processing
- Requires `wkhtmltoimage` for HTML rendering
- ASCII output resolution is limited for optimal viewing

## Troubleshooting

### Common Issues

1. **"wkhtmltoimage not found"**:
   - Ensure wkhtmltoimage is installed and path is correctly configured

2. **"Permission denied" errors**:
   - Check write permissions in the working directory

3. **Memory issues with large videos**:
   - Try shorter videos or reduce the `final_width` parameter

4. **YouTube download fails**:
   - Verify the video URL is accessible and not age-restricted

## Dependencies

- `PIL (Pillow)`: Image processing
- `opencv-python`: Video processing
- `imgkit`: HTML to image conversion
- `pytubefix`: YouTube video downloading
- `tkinter`: GUI framework (usually included with Python)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [GNU General Public License v3.0](LICENSE).

## Acknowledgments

- ASCII art conversion algorithm inspired by traditional text-based art techniques
- Uses `pytubefix` for reliable YouTube video downloading
- Built with Python's extensive image processing libraries

---

**Note**: This tool is for educational and personal use. Please respect YouTube's Terms of Service and copyright laws when downloading videos.
