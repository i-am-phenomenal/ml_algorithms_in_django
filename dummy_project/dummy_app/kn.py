# This file acts as a utility file
import random
import math
import json
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base

# PRIVATE FUNSTIONS TO GET ELEMENTS FROM DATASET


# def get_mass(element):
#     if 'mass' in element:
#         return element['mass']
#     else:
#         return 0


# def get_reclat(element):
#     if 'reclat' in element:
#         return element['reclat']
#     else:
#         return 0.00


# def get_reclong(element):
#     if 'reclong' in element:
#         return element['reclong']
#     else:
#         return 0.00


Base = declarative_base()
# Generating Data Set


class Point:
    def __init__(self,  x_coord, y_coord, color):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color


def get_random_value_for_coord():
    return random.randrange(0, 100, 1)


def calculate_distance(current_object, iterable_object):
    x_coord_difference = (iterable_object.x_coord - current_object.x_coord)
    y_coord_difference = (iterable_object.y_coord - current_object.y_coord)
    return math.sqrt((x_coord_difference * x_coord_difference) + (y_coord_difference * y_coord_difference))


def get_object_with_relevant_data(iterator):
    x_coord = get_random_value_for_coord()
    y_coord = get_random_value_for_coord()
    color = random.choice(["Red", "Blue"])
    return Point(x_coord, y_coord, color)


# ORIGINAL DATASET
objects = []


def generate_dataset():
    for iter in range(0, 100):
        objects.append(get_object_with_relevant_data(iter))

    return objects


# FUNCTION TO GENERATE DATASET
generate_dataset()


def find_nearest_point(current_object):
    global objects
    distances = []
    for record in objects:
        distances.append(calculate_distance(current_object, record))
    for object in objects:
        current_object_distance = calculate_distance(
            current_object, object)
        if current_object_distance == min(distances):
            return object
        else:
            pass


# dummy_record = Point(1, 2, "Red")
# for obj in objects:
#     print([obj.x_coord, obj.y_coord, obj.color])
# returned_value = find_nearest_point(dummy_record)

# ------------------XXXXXXXXXXXXXXXXXXXXXXX----------------
# TRYING TO LOAD SEED DATA WHICH IS JUST A OT OF JSON DATA

# with open('json_dataset.txt') as json_data:
#     data = json.load(json_data)
#     print(data)

# custom_dictionary = {}
# json_file = open('json_dataset.txt', encoding='utf8')
# json_data = json.load(json_file)
# dataset_engine = create_engine('sqlite:///NasaDataSetDatabase.db')
# Base = declarative_base()
# Base.metadata.bind = dataset_engine
# DBSession = sessionmaker(bind=dataset_engine)
# session = DBSession()
# for element in json_data:
#     # print(element)
#     # print(element['name'])

#     dataset = NasaData(
#         name=element['name'],
#         id=element['id'],
#         nametype=element['nametype'],
#         recclass=element['recclass'],
#         mass=get_mass(element),
#         fall=element['fall'],
#         reclat=get_reclat(element),
#         reclong=get_reclong(element)
#     )
#     session.add(dataset)
#     try:
#         session.commit()
#     except IOError:
#         print("UNABLE TO SAVE DATA ")
