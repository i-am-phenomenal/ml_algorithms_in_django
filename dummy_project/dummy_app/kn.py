import random
import math
import json
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# PRIVATE FUNSTIONS TO GET ELEMENTS FROM DATASET


def check_if_contains_decimal(mass_value):
    if (mass_value.find(".") == -1):
        return False
    else:
        return True


def get_integer_value(mass_value):
    return mass_value.split('.')[0]


def get_mass(element):
    if 'mass' in element:
        if check_if_contains_decimal(element['mass']):
            return int(get_integer_value(element['mass']))
        else:
            return int(element['mass'])
    else:
        return 0


def get_reclat(element):
    if 'reclat' in element:
        return float(element['reclat'])
    else:
        return 0.00


def get_reclong(element):
    if 'reclong' in element:
        return float(element['reclong'])
    else:
        return 0.00


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

# ------------------ CONNECTIING TO PSQL TABLE AND LOADING SEED DATA -----------------

# connection = psycopg2.connect(database="django_database", user="postgres",
#                               password="postgres", host="127.0.0.1", port="5432")
# cursor = connection.cursor()
# json_file = open('json_dataset.txt', encoding='utf-8-sig')
# print(json_file)
# json_data = json.load(json_file)
# element = json_data[0]
# print(element)
# for element in json_data:
#     # print(element)
#     command = "INSERT INTO NASA_DATASET (NAME, ID, NAMETYPE, RECCLASS, MASS, FALL, RECLAT, RECLONG) VALUES ('%s', '%d', '%s', '%s', '%d', '%s', '%f', '%f')" % (
#         element['name'],
#         int(element['id']),
#         element['nametype'],
#         element['recclass'],
#         get_mass(element),
#         element['fall'],
#         get_reclat(element),
#         get_reclong(element))
#     # element['reclat'],
#     # element['reclong'])
#     cursor.execute(command)
# connection.commit()
# connection.close()
# for record in json_data:

# ----------------------- LOADING SEED DATA FROM ANOTHER FILE ----------------------- WIP
# def get_updated_json_dataset(json_data, recursion_counter):
#     current_element = json_data[recursion_counter]
#     current_element['id'] = recursion_counter
#     json_data[recursion_counter] = current_element
#     if recursion_counter >= len(json_data):
#         return json_data
#     else:
#         get_updated_json_dataset(json_data, (recursion_counter + 1))


# connection = psycopg2.connect(
#     database="django_database", user="postgres", password="postgres", host="127.0.0.1", port="5432"
# )
# cursor = connection.cursor()
# json_file = open('json_dataset2.txt', encoding='utf-8-sig')
# json_data = json.load(json_file)
# # updated_json_data = get_updated_json_dataset(json_data, 0) WIP
# # print(updated_json_data)

# for element in json_data:
#     print(type(element['orbit_class']))
#     print(element)
#     psql_command = "INSERT INTO ASTEROID_DATASET (H_MAG, MOID_AU, Q_AU_1, Q_AU_2, PERIOD_YR, I_DEG, PHA, ORBIT_CLASS) VALUES ('%f' ,'%f', '%f', '%f', '%f', '%f', '%c', '%s') " % (
#         # str(element['designation']),
#         element['h_mag'],
#         element['moid_au'],
#         element['q_au_1'],
#         element['q_au_2'],
#         element['period_yr'],
#         element['i_deg'],
#         element['pha'],
#         element['orbit_class']
#     )
#     cursor.execute(psql_command)

# connection.commit()
# connection.close()
