import pyfiglet

def text_to_ascii_art(text, font="standard"):
    """Converts text to ASCII art using pyfiglet.

    Args:
        text: The text to convert.
        font: The pyfiglet font to use (e.g., "standard", "banner", "slant").
              See pyfiglet's documentation for available fonts.

    Returns:
        The ASCII art representation of the text, or None if there's an error
        (e.g., invalid font).
    """
    try:
        result = pyfiglet.figlet_format(text, font=font)
        return result
    except pyfiglet.FontNotFound:
        return None  # Handle invalid font names
    except Exception as e: # Catch any other exceptions.
        print(f"An error occurred: {e}")
        return None


# Get text input from the user:
text_input = input("Enter the text to convert: ")
font_input = input("Enter the font to use (optional, default is 'standard'): ")

if not font_input: # If the user just pressed Enter.
    font_input = "standard"

ascii_art = text_to_ascii_art(text_input, font_input)

if ascii_art:
    print(ascii_art)
else:
    print(f"Error: Could not generate ASCII art. Check the font name '{font_input}'.")

# Example usage with different fonts:
print("\n--- Examples ---")
print(text_to_ascii_art("Hello", "standard"))
print(text_to_ascii_art("Python", "banner"))
print(text_to_ascii_art("ASCII", "slant"))
print(text_to_ascii_art("Error Test", "nonexistent_font")) # Example of an invalid font.

