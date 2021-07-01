import json

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
d = json.loads(a_string)

# Make json Prettier
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

print(d)
print(type(d))
print(d.keys())
print(pretty(d))

l1 = [2, 3, 5]
l2 = [6, 1,10]

l3 = [x1 + x2 for (x1, x2) in list(zip(l1, l2))]
print(l3)