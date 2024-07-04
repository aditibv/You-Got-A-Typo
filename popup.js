/*Final Project- CIS*6510 Cybersecurity and Defense-in-Depth
You Got a Typo: Detecting Typo-Squatting domains using Machine Learning Approach
Aditi Venkatesh -1302387
Shreya Bhoje - 1301655
*/

// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
  
  // Attach a click event listener to the 'checkButton' element
  document.getElementById('checkButton').addEventListener('click', function() {
    
    // Query the active tab in the current window
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      // Get the URL of the active tab
      var url = tabs[0].url;
      
      // Call the checkTyposquat function with the retrieved URL
      checkTyposquat(url);
    });
  });
});

// Function to check for typosquat using the Flask API
function checkTyposquat(url) {
  console.log("Checking typosquat for URL:", url);

  // Make a POST request to the Flask API for typosquat prediction
  fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      // Display an alert based on the prediction result
      if (data.prediction_knn === "bad") {
        alert('This URL may be a typosquat!');
      } else {
        alert('This URL appears to be legitimate.');
      }
    })
    .catch(error => console.error('Error:', error));
}
