import os


def create_ascii_html(ascii_list, image, color_data, image_pos, output_dir='HtmlImages'):
    """Generate HTML file with colored ASCII art."""
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        
    html_path = f'{output_dir}/Html{image_pos}.html'
    
    with open(html_path, "w") as file:
        # Write HTML header
        file.write("""<!DOCTYPE html>
<html>
   <body style='background-color:black'>
   <pre style='display: inline-block; border-width: 4px 6px; border-color: black; border-style: solid; background-color:black; font-size: 32px ;font-face: Montserrat;font-weight: bold;line-height:60%'>""")

        width, height = image.size
        counter = 0
        
        # Write ASCII characters with colors
        for char in ascii_list:
            color_hex = '%02x%02x%02x' % color_data[counter] 
            counter += 1
            
            if (counter % width) != 0:             
                file.write(f"<span style=\"color: #{color_hex}\">{char}</span>")  
            else:
                file.write("<br />") 
                
        # Write HTML footer
        file.write("""</pre></body>
</html>""")
    
    return html_path


def get_html_template():
    """Return the HTML template structure."""
    return {
        'header': """<!DOCTYPE html>
<html>
   <body style='background-color:black'>
   <pre style='display: inline-block; border-width: 4px 6px; border-color: black; border-style: solid; background-color:black; font-size: 32px ;font-face: Montserrat;font-weight: bold;line-height:60%'>""",
        'footer': """</pre></body>
</html>"""
    }
