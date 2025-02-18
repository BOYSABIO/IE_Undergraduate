from pathlib import Path
import json


# Read data as a string and convert to a Python object.
path = Path('JSON_FILES/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features'] 

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # loop through the list containing data about each earthquake
    mags.append(mag)

print(mags[:10])
