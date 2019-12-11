#The name of the file on my local system is kn.py 
# I need to keep that in mind in case of  any discrepancies.
import random
import math
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
