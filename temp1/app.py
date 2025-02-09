from flask import Flask, request, jsonify, render_template
import pyfiglet

app = Flask(__name__)

def text_to_ascii_art(text, font="standard"):
    """Converts text to ASCII art using pyfiglet."""
    try:
        result = pyfiglet.figlet_format(text, font=font)
        return result
    except pyfiglet.FontNotFound:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    """Receives text input from the frontend and returns ASCII art."""
    data = request.json
    text = data.get("text", "")
    font = data.get("font", "standard")

    ascii_art = text_to_ascii_art(text, font)
    
    if ascii_art:
        return jsonify({"ascii": ascii_art})
    else:
        return jsonify({"error": f"Could not generate ASCII art with font '{font}'"}), 400

if __name__ == "__main__":
    app.run(debug=True)
