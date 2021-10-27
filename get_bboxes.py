import collections
import json
import sys

def flatten(x):
    """Return a flattened copy of array x"""
    # https://stackoverflow.com/a/2158522/3347737
    if isinstance(x, collections.abc.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

data = json.load(sys.stdin)

def get_bbox(f):
    coords = flatten(f["geometry"]["coordinates"])
    lng = coords[::2]
    lat = coords[1::2]
    bbox = [min(lng), min(lat), max(lng), max(lat)]
    props = dict(f["properties"])
    props["bbox"] = bbox
    return props

result = [get_bbox(f) for f in data["features"]]

print(json.dumps(result))

