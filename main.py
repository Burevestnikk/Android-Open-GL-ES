import numpy as np
import os

vertices = []
polygons = []

def round_number(string_number):
    if "\n" in string_number:
        string_number = string_number.replace("\n", "")
    if "." in string_number:
        parts = string_number.split(".")
        if len(parts[1]) > 5:
            return parts[0] + "." + parts[1][:5] 
    return string_number

with open('car.obj') as f:
    for line in f:
        if line.startswith('v '):
            vertex = list(map(round_number, line[2:].split())) 
            vertices.append(vertex)
        elif line.startswith('f '):
            indices = line[2:].split()
            polygon = np.array([int(index.split('/')[0])-1 for index in indices])
            polygons.append(polygon)

for polygon in polygons:
    with open('data.txt', 'a') as file:
        file.write(str(polygon))
