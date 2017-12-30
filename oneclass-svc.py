## Training one-class SVM for normal HTTP traffic classification
##

import pandas as pd
import numpy as np


def cvs_process(csv_file, target_value):
    # Function to clean cvs from NaN,
    # transform features into labels using LabelEncoder
    # and select features by choosing those which differ
    #
    # It returns transformed dataframe object and target list with target_values
    #
    from sklearn.preprocessing import LabelEncoder

    # change NaN into integer
    data=csv_file.fillna('na')

    class_le = LabelEncoder()
    size=data.shape
    translbl = pd.DataFrame()
    feature_list = []

    for i in range(0, size[1]):
        translbl = class_le.fit_transform(data.values[:,i].astype(str))
        data.values[:,i]=translbl
        if not translbl.sum() == 0:
            feature_list.insert(i,i)

    return(data,[target_value for col in range(size[0])], feature_list)

csv_file_train = pd.read_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-train.csv', dtype=str)
csv_file_test1 = pd.read_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-test.csv', dtype=str)
csv_file_test2 = pd.read_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqanom-test.csv', dtype=str)

[data_train,target_train, feature_list] = cvs_process(csv_file_train,0)
[data_test1,target_test1] = cvs_process(csv_file_test1,0)
[data_test2,target_test2] = cvs_process(csv_file_test2,1)

data_test = pd.DataFrame(pd.concat([data_test1,data_test2], ignore_index=True))
target_test = pd.DataFrame(pd.concat([target_test1,target_test2], ignore_index=True))


## Model selection using Grid Search with OneClassSVM model
##
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.svm import OneClassSVM
from sklearn.model_selection import GridSearchCV

pipe_svc = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=2)),
            ('clf', OneClassSVM(random_state=1))])

param_grid = [{'clf__nu': np.linspace(0.01, 0.99, 99),
               'clf__kernel': ['linear']},
                 {'clf__nu': np.linspace(0.01, 0.99, 99),
                  'clf__gamma': np.logspace(-9, 3, 13),
                  'clf__kernel': ['rbf']}]

gs = GridSearchCV(estimator=pipe_svc,
                  param_grid=param_grid,
                  scoring='accuracy',
                  cv=10,
                  n_jobs=-1)
gs = gs.fit(data_train.iloc[:,feature_list], target_train)

print(gs.best_score_)       # prints the score of the optimal hyperparameters
print(gs.best_params_)      # prints the hyperparameters


# Applying the hyperparameters to the test set
clf = gs.best_estimator_
clf.fit(data_train.iloc[:,feature_list], target_train)           # fitting
print('Test accuracy: %.3f' % clf.score(data_test.iloc[:,feature_list], target_test))    #score for the testset
