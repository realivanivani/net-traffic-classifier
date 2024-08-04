## Training one-class SVM for normal HTTP traffic classification
##

import pandas as pd
import numpy as np
import os


path = '/Users/ivanivani/Documents/python/net_traffic_classifier/net-traffic-classifier'

csv_file_train = pd.read_csv(os.path.join(path,'reqnorm-train.csv'), dtype=str)
csv_file_test = pd.read_csv(os.path.join(path,'reqnorm-test.csv'), dtype=str)
csv_file_outliers = pd.read_csv(os.path.join(path,'reqanom-test.csv'), dtype=str)

size_train=np.size(csv_file_train,0)
size_test=np.size(csv_file_test,0)
size_outlier=np.size(csv_file_outliers,0)

data = pd.DataFrame()
data = pd.concat([csv_file_train,csv_file_test], ignore_index=True)
data = pd.concat([data,csv_file_outliers], ignore_index=True)


# change NaN into string
data=data.fillna('na')

size=data.shape
relevant_features = []

for i in range(0, size[1]):
    uniques = data.apply(lambda x: x.nunique())
    if  uniques[i] != 1:
        relevant_features.insert(i,str(i))
new_data = data[relevant_features].apply(lambda x: ' '.join(x),axis=1)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
new_data=vectorizer.fit_transform(new_data.values)
print(new_data.shape)

data_train = new_data[:size_train,:]
data_test = new_data[size_train:size_test,:]
data_outliers = new_data[size_test:,:]


print('Done importing cvs and Tfidf vectorizing')

print('Relevant features:', relevant_features)

## Using simple OneClassSVM model
## example taken from scikit.learn webpage

# fit the model
from sklearn.svm import OneClassSVM
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from pprint import pprint
from time import time
import logging
from sklearn.metrics import make_scorer

print('\nStart fitting..')

# # from scikit-learn webpage, Sample pipeline for text feature extraction and evaluation
# pipeline = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', OneClassSVM()),
# ])
#
# param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
#
# parameters = [{'clf__C': param_range,
#                'clf__kernel': ['linear']},
#                  {'clf__C': param_range,
#                   'clf__gamma': param_range,
#                   'clf__kernel': ['rbf']}]
#
# scorer = make_scorer(roc_auc_score, pos_label=0)         # defining scorer
#
# # find the best parameters for both the feature extraction and the
# # classifier
# grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, scoring=scorer)
#
# print("Performing grid search...")
# print("pipeline:", [name for name, _ in pipeline.steps])
# print("parameters:")
# print(parameters)
# t0 = time()
# grid_search.fit(data_train)
# print("done in %0.3fs" % (time() - t0))
# print()
#
# print("Best score: %0.3f" % grid_search.best_score_)
# print("Best parameters set:")
# best_parameters = grid_search.best_estimator_.get_params()
# for param_name in sorted(parameters.keys()):
#         print("\t%s: %r" % (param_name, best_parameters[param_name]))
#

clf = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(data_train)

print('Done fitting\n\nTesting..')
y_pred_train = clf.predict(data_train)
y_pred_test = clf.predict(data_test)
y_pred_outliers = clf.predict(data_outliers)
n_corr_train = y_pred_train[y_pred_train == 1].size
#print(n_corr_train)
n_corr_test = y_pred_test[y_pred_test == 1].size
#print(n_corr_test)
n_corr_outliers = y_pred_outliers[y_pred_outliers == -1].size
#print(n_corr_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
print(n_error_test)

## Performance metrics
print('\nPrecision metrics')

prec = (n_corr_test / (n_corr_test + n_error_outliers))         # precision
recall = (n_corr_test / (n_error_outliers + n_corr_test))       # recall
f1_score = 2*(prec*recall/(prec+recall))                        # f1 score

positive_detection = (n_corr_outliers / size_outlier)           # TP / TP + FN
false_detection = (n_error_test / size_test)                    # FP / FP + TN

# using my own definitions
print('\nPrecision: %.3f' % prec)
print('\nRecall: %.3f' % recall)
print('\nF1: %.3f' % f1_score)

# ROC AUC (Positive_detection / false_detection)
print('\nPositive detection: %.3f' % positive_detection)
print('\nFalse detection: %.3f' % false_detection)
