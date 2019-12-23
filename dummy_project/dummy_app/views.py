from django.shortcuts import render
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from .schema import KNClassification, KNValuesForm
from .kn import generate_dataset, find_nearest_point, Point
from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.views.decorators.csrf import csrf_exempt
from .database import Database


# CUSTOM AND PRIVATE FUNCTIONS GO HERE
def insert_kn_data_into_database(returned_values):
    kn_engine = create_engine('sqlite:///KNClassificationDatabase.db')
    Base = declarative_base()
    Base.metadata.bind = kn_engine
    DBSession = sessionmaker(bind=kn_engine)
    session = DBSession()
    kn_data = KNClassification(
        prediction=returned_values["prediction"],
        name_in_dataset=returned_values["name_in_dataset"],
        kn_score=returned_values["kn_score"]
    )
    session.add(kn_data)
    try:
        session.commit()
        session.close()
    except IOError:
        print("THERE WAS AN ERROR WHILE TRYING TO SAVE DATA, PLEASE LOOK INTO IT !!!!")


def get_values_for_kn_data():
    kn_engine = create_engine('sqlite:///KNClassificationDatabase.db')
    Base = declarative_base()
    Base.metadata.bind = kn_engine
    DBSession = sessionmaker(bind=kn_engine)
    session = DBSession()
    try:
        all_records = session.query(KNClassification).all()
        session.close()
        return all_records
    except IOError:
        print("SOMETHING WENT WRONG. PLEASE HAVE A LOOK !!!!")


def home(request):
    return render(request, "home.html")


def custom_kn_algorithm(request):
    return render(request, "custom_kn_algorithm.html", {})


def kn_algo(request):
    x_coord = 0
    y_coord = 0
    if request.method == 'POST':
        form = KNValuesForm(request.POST)
        print(form, "++++++++++++++++++")
        if form.is_valid():
            x_coord = form.cleaned_data.get("x_coord")
            y_coord = form.cleaned_data.get("y_coord")
    dataset = generate_dataset()
    current_object = Point(x_coord, y_coord, "")
    prediction = find_nearest_point(current_object)

    return render(request, "custom_kn_algorithm.html", {})


def algo1(request):
    # This is the KN Classification Algo
    records = []
    if request.method == 'POST':
        form = KNValuesForm(request.POST)
        if form.is_valid():
            value_1 = form.cleaned_data.get("kn_value1")
            value_2 = form.cleaned_data.get("kn_value2")
            value_3 = form.cleaned_data.get("kn_value3")
            value_4 = form.cleaned_data.get("kn_value4")
    iris_dataset = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris_dataset["data"], iris_dataset["target"], random_state=0)

    kn = KNeighborsClassifier(n_neighbors=1)
    kn.fit(x_train, y_train)
    # x_new = np.array([[5, 2.9, 1, 0.2]])
    x_new = np.array([[value_1, value_2, value_3, value_4]])
    print(" X NEW ", x_new)
    prediction = kn.predict(x_new)
    returned_values = {"prediction": prediction[0],
                       "name_in_dataset": iris_dataset["target_names"][prediction][0],
                       "kn_score": kn.score(x_test, y_test)}
    insert_kn_data_into_database(returned_values)
    records = get_values_for_kn_data()
    dict_list = []
    for record in records:
        dict_list.append(convert_to_dictionary(record))
    return render(request, "algo1.html", {"objects": dict_list})


def decision_tree(request):
    # dataset_engine = create_engine('sqlite:///NasaDataSetDatabase.db')
    # Base = declarative_base()
    # Base.metadata.bind = dataset_engine
    # DBSession = sessionmaker(bind=dataset_engine)
    # session = DBSession()
    # try:
    #     all_records = session.query(NasaData).all()
    #     session.close()
    #     print(all_records, "@@@@@@@@@@@@@@@@@@@@@@@@@")
    # except IOError:
    #     print("UNABLE TO FETCH DATA")
    # col_names = ['pregnant', 'glucose', 'bp', 'skin',
    #              'insulin', 'bmi', 'pedigree', 'age', 'label']
    # pima = pd.read_csv("C:/practice Programs/diabetes.csv",
    #                    header=None, names=col_names)
    # pima.head()
    # feature_cols = ['pregnant', 'insulin', 'bmi',
    #                 'age', 'glucose', 'bp', 'pedigree']
    # x = pima[feature_cols]
    # y = pima.label
    # x_train, x_test, y_train, y_test = train_test_split(
    #     x, y, test_size=0.3, random_state=1)
    # clf = DecisionTreeClassifier()

    # clf = clf.fit(x_train, y_train)
    # y_pred = clf.predict(x_test)
    # accuracy = metrics.accuracy_score(y_test, y_pred)
    return render(request, "home.html")

# API functions for react native frontend start here


def index(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request, 'food/index.html', context)

# Rest API endpoint


def get_rest_list(request):
    """
        Return JSON list of all the data
    """
    if request.method == "GET":
        rest_list = Restaurant.objects.order_by('-pub_date')
        serializer = RestaurantSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)


# PRIVATE FUNCTIONS START HERE


def convert_to_dictionary(record):
    return {"prediction": record.prediction[0],
            "name_in_dataset": record.name_in_dataset,
            "kn_score": record.kn_score,
            "id": record.id
            }
