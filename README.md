You Got a Typo: Detecting Typo-Squatting Domains using Machine Learning
Introduction
Typo-squatting is a cybersecurity threat that leverages human error and inexpensive domain registrations to divert genuine traffic from legitimate domains. It is often used for phishing attacks, redirecting users to competitors' sites, or spreading malicious content. Despite numerous awareness initiatives, the number of victims continues to rise due to the exploitation of human oversight.

In this project, we have developed a browser extension that detects potentially typo-squatted domains using a machine learning model, allowing users to verify the legitimacy of the URLs they type in their browser.

Approach
We implemented a machine learning model to detect typo-squatting domains. The model uses features such as bi-grams, domain length, number of subdomains, keyboard proximity, character frequency, Levenshtein distance, hyphen count, vowel count, and consonant count to classify URLs.

Methodology
The project is designed as a Google Chrome browser extension that integrates with a Python/Flask backend. Here are the main steps:

Data Collection: We collected legitimate domains from Similarweb.com and potentially typo-squatted domains generated using DNS Twist.
Feature Extraction: Extracted bi-grams and additional URL-based features to create a feature matrix.
Model Training: Trained a Support Vector Machine (SVM) model on the collected data.
Integration: Integrated the trained model into a Flask application that interacts with the Chrome extension.
Prediction: The extension sends the user-entered URL to the Flask server, which predicts whether the URL is legitimate or a typo-squat.
Results
The SVM model achieved high accuracy in detecting typo-squatted domains. The performance was evaluated using precision, recall, F1-score, and a confusion matrix. The extension successfully alerts users when a potentially dangerous URL is detected.

Future Work
Future improvements could include implementing multimodal analysis that uses both the URL and web page content to detect typo-squatting. Additionally, integrating the extension with organizational security products like Intrusion Detection Systems (IDS) and Firewalls could enhance threat detection and response.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/you-got-a-typo.git
cd you-got-a-typo
Train the model (if not already trained):
bash
Copy code
python train_model.py
Run the Flask server:
bash
Copy code
python backend.py
Load the Chrome extension:
Open Chrome and navigate to chrome://extensions/.
Enable "Developer mode".
Click "Load unpacked" and select the chrome_extension directory.
Usage
Enter a URL in the Chrome extension's input field. The extension will check the URL and alert you if it detects a typo-squatting domain.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.

Acknowledgements
DNS Twist for generating typo-squatted domain names.
Similarweb for providing legitimate domain data.
University of Guelph for supporting this research project.
Contact
For any questions or suggestions, please open an issue on GitHub or contact the project maintainers.

