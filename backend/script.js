function convertTextToAscii() {
    const text = document.getElementById('textInput').value;
    // This is a simple demonstration - you would need to implement actual ASCII art conversion
    const asciiArt = text.split('').map(char => char + ' ').join('');
    document.getElementById('asciiOutput').textContent = asciiArt;
}

function convertImageToAscii() {
    const fileInput = document.getElementById('imageInput');
    if (fileInput.files && fileInput.files[0]) {
        // This is where you would implement actual image to ASCII conversion
        document.getElementById('asciiOutput').textContent = 'Image conversion would happen here...';
    } else {
        alert('Please select an image first.');
    }

}
async function convertTextToAscii() {
const text = document.getElementById('textInput').value;
if (!text.trim()) {
    alert('Please enter some text first.');
    return;
}

try {
    const response = await fetch('http://localhost:5000/convert/text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    if (data.error) {
        throw new Error(data.error);
    }

    document.getElementById('asciiOutput').textContent = data.ascii_art;
} catch (error) {
    alert('Error converting text: ' + error.message);
}
}

async function convertImageToAscii() {
const fileInput = document.getElementById('imageInput');
if (!fileInput.files || !fileInput.files[0]) {
    alert('Please select an image first.');
    return;
}

const formData = new FormData();
formData.append('image', fileInput.files[0]);

try {
    const response = await fetch('http://localhost:5000/convert/image', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (data.error) {
        throw new Error(data.error);
    }

    document.getElementById('asciiOutput').textContent = data.ascii_art;
} catch (error) {
    alert('Error converting image: ' + error.message);
}
}

