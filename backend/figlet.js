function textToAsciiArt(text, font = 'standard') {
    return new Promise((resolve, reject) => {
      figlet(text, { font: font }, function(err, output) {
        if (err) {
          reject(err); // Reject the promise if there's an error
        } else {
          resolve(output); // Resolve the promise with the ASCII art
        }
      });
    });
  }
  
  
  // Example usage (async/await):
  async function displayAsciiArt() {
    const text = document.getElementById("textInput").value; // Get text from input field
    const font = document.getElementById("fontSelect").value; // Get font from select
  
    try {
      const asciiArt = await textToAsciiArt(text, font);
      document.getElementById("asciiArt").textContent = asciiArt; // Display in a <pre> element
    } catch (error) {
      document.getElementById("asciiArt").textContent = "Error: " + error;
      console.error("Error generating ASCII art:", error);
    }
  }
  
  
  
  // Example usage (then/catch):
  function displayAsciiArtThenCatch() {
      const text = document.getElementById("textInput").value; // Get text from input field
      const font = document.getElementById("fontSelect").value; // Get font from select
  
      textToAsciiArt(text, font)
          .then(asciiArt => {
              document.getElementById("asciiArt").textContent = asciiArt;
          })
          .catch(error => {
              document.getElementById("asciiArt").textContent = "Error: " + error;
              console.error("Error generating ASCII art:", error);
          });
  }
  
  
  // Add an event listener to a button to trigger the conversion
  document.getElementById("convertButton").addEventListener("click", displayAsciiArt); // or displayAsciiArtThenCatch
  
  
  
 