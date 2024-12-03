function displayFilename() {
// Get the selected file input
const fileInput = document.getElementById('file');
// Get the filename of the selected file
const filename = fileInput.files.length > 0 ? fileInput.files[0].name : '';

// Display the filename below the buttons
const filenameDisplay = document.getElementById('filename-display');
if (filename) {
    filenameDisplay.textContent = "Selected file: " + filename;
} else {
    filenameDisplay.textContent = '';
}
}

