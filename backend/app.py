from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import art
import base64
import io

app = Flask(_name_)
CORS(app)  # Enable CORS for all routes

# ASCII characters used for image conversion (from darkest to lightest)
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image):
    # Convert image to grayscale
    image = image.convert('L')
    
    # Resize image while maintaining aspect ratio
    width = 100
    aspect_ratio = image.size[1] / image.size[0]
    height = int(width * aspect_ratio * 0.5)  # * 0.5 to account for terminal character spacing
    image = image.resize((width, height))
    
    # Convert pixels to ASCII
    pixels = np.array(image)
    ascii_str = ''
    
    for row in pixels:
        for pixel in row:
            # Map pixel intensity to ASCII character
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        ascii_str += '\n'
    
    return ascii_str

@app.route('/convert/text', methods=['POST'])
def convert_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        # Convert text to ASCII art using the art library
        ascii_art = art.text2art(text)
        
        return jsonify({'ascii_art': ascii_art})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/convert/image', methods=['POST'])
def convert_image():
    try:
        # Get the image file from the request
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
            
        image_file = request.files['image']
        
        # Read and convert image
        image = Image.open(image_file)
        ascii_art = image_to_ascii(image)
        
        return jsonify({'ascii_art': ascii_art})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if _name_ == '_main_':
    app.run(debug=True, port=5000)