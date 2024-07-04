'''
Final Project- CIS*6510 Cybersecurity and Defense-in-Depth
You Got a Typo: Detecting Typo-Squatting domains using Machine Learning Approach
Aditi Venkatesh -1302387
Shreya Bhoje - 1301655
This program trains a machine learning model to detect typo-squatting threats in URLs.

'''


import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from Levenshtein import distance
import numpy as np

#The dataset is loaded from 'Dataset.csv'
df = pd.read_csv('Dataset.csv') 

#Features are engineered from the URLs using CountVectorizer
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))

#Capturing character bi-grams and additional URL-based metrics
bi_grams = vectorizer.fit_transform(df['url'])


df['length_of_domain'] = df['url'].apply(len)
df['number_of_subdomains'] = df['url'].apply(lambda x: x.count('.') + 1)
df['keyboard_proximity'] = df['url'].apply(lambda x: sum([distance(c, 'a') for c in x]))
df['character_frequency'] = df['url'].apply(lambda x: sum([ord(c) for c in x]))
df['levenshtein_distance'] = df['url'].apply(lambda x: distance(x, 'legitimate'))
df['hyphen_count'] = df['url'].apply(lambda x: x.count('-'))
df['vowel_count'] = df['url'].apply(lambda x: sum([1 for c in x if c.lower() in ['a', 'e', 'i', 'o', 'u']]))
df['consonant_count'] = df['url'].apply(lambda x: sum([1 for c in x if c.isalpha() and c.lower() not in ['a', 'e', 'i', 'o', 'u']]))

#The features are combined into a feature matrix
X = np.hstack((bi_grams.toarray(), df[['length_of_domain', 'number_of_subdomains', 'keyboard_proximity',
                                        'character_frequency', 'levenshtein_distance', 'hyphen_count',
                                        'vowel_count', 'consonant_count']].values))

#The target variable 'class' is defined
y = df['class']

#The data is split into training and testing sets, and a Support Vector Machine (SVM) model with a linear kernel is trained.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_svm = SVC(kernel='linear')  
model_svm.fit(X_train, y_train)


y_pred_svm = model_svm.predict(X_test)


#The SVM model is evaluated on the test set, and metrics such as accuracy, precision, recall, and a confusion matrix are displayed.
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"Model Accuracy (SVM): {accuracy_svm}")


print("Classification Report (SVM):")
print(classification_report(y_test, y_pred_svm, zero_division=1))


print("Confusion Matrix (SVM):")
print(confusion_matrix(y_test, y_pred_svm))


#The trained SVM model and CountVectorizer vocabulary are saved using joblib files.
joblib.dump(vectorizer.vocabulary_, 'vectorizer_vocabulary1.joblib')
joblib.dump(model_svm, 'model_svm1.joblib')

