/*
Final Project- CIS*6510 Cybersecurity and Defense-in-Depth
You Got a Typo: Detecting Typo-Squatting domains using Machine Learning Approach
Aditi Venkatesh -1302387
Shreya Bhoje - 1301655
*/

// Function to check the entered URL for typosquat using the Flask API
function checkURL() {
  // Get references to HTML elements by their IDs
  const urlInput = document.getElementById('urlInput');
  const resultParagraph = document.getElementById('result');

  // Retrieve the value entered in the URL input field
  const url = urlInput.value;

  // Check if a URL is provided; if not, display a message and exit the function
  if (!url) {
    resultParagraph.textContent = 'Please enter a URL.';
    return;
  }

  // Make a POST request to the Flask API for typosquat prediction
  fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url: url })
  })
  .then(response => response.json())
  .then(data => {
    // Handle the prediction result
    if (data.prediction_knn === "bad") {
      alert('This URL may be a typosquat!');
    } else {
      alert('This URL appears to be legitimate.');
    }
  })
  .catch(error => {
    // Log and handle errors, and update the result paragraph with an error message
    console.error('Error:', error);
    resultParagraph.textContent = 'An error occurred while checking the URL.';
  });
}
