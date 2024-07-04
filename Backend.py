'''
Final Project- CIS*6510 Cybersecurity and Defense-in-Depth
You Got a Typo: Detecting Typo-Squatting domains using Machine Learning Approach
Aditi Venkatesh -1302387
Shreya Bhoje - 1301655
This Flask program serves as the backend for a browser extension designed to detect typo-squatting threats in URLs.

'''


from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from Levenshtein import distance
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


model_svm = joblib.load('model_svm1.joblib')
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))

vectorizer.vocabulary_ = joblib.load('vectorizer_vocabulary1.joblib')

def predict_svm(url):
    try:
        # Feature extraction
        bi_grams = vectorizer.transform([url])
        additional_features = np.array([
            len(url),
            url.count('.') + 1,
            sum([distance(c, 'a') for c in url]),
            sum([ord(c) for c in url]),
            distance(url, 'legitimate'),
            url.count('-'),
            sum([1 for c in url if c.lower() in ['a', 'e', 'i', 'o', 'u']]),
            sum([1 for c in url if c.isalpha() and c.lower() not in ['a', 'e', 'i', 'o', 'u']])
        ]).reshape(1, -1)

        X = np.hstack((bi_grams.toarray(), additional_features))

        prediction_svm = model_svm.predict(X)
        return (prediction_svm)  

    except Exception as e:
        return str(e)

@app.route('/predict', methods=['POST'])
def predict_svm_route():
    try:
        data = request.get_json(force=True)
        print(data)
        url = data['url']
        print(url)
        prediction_svm1 = predict_svm(url)
        prediction_svm = ' '.join(prediction_svm1)
        print(prediction_svm)
        return jsonify({'prediction_knn': prediction_svm}), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({'error': str(e)})
   

def main():
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()
