from django.shortcuts import render
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


def home(request):
    return render(request, "home.html")


def algo1(request):
    iris_dataset = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris_dataset["data"], iris_dataset["target"], random_state=0)

    kn = KNeighborsClassifier(n_neighbors=1)
    kn.fit(x_train, y_train)

    x_new = np.array([[5, 2.9, 1, 0.2]])
    prediction = kn.predict(x_new)
    returned_values = {"prediction": prediction,
                       "name_in_dataset": iris_dataset["target_names"][prediction],
                       "kn_score": kn.score(x_test, y_test)}
    print(returned_values, "RETURNED VALUES 11111111")
    return render(request, "algo1.html", returned_values)


def decision_tree(request):
    col_names = ['pregnant', 'glucose', 'bp', 'skin',
                 'insulin', 'bmi', 'pedigree', 'age', 'label']
    pima = pd.read_csv("C:/practice Programs/diabetes.csv",
                       header=None, names=col_names)
    pima.head()
    feature_cols = ['pregnant', 'insulin', 'bmi',
                    'age', 'glucose', 'bp', 'pedigree']
    x = pima[feature_cols]
    y = pima.label
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1)
    # print(x_train)
    # print(y_train)
    print(x_test)
    # print(y_test)
    clf = DecisionTreeClassifier()

    clf = clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(accuracy, '22222222222222222222222')
    return render(request, "home.html")
