x  = {"name": "Alice", "age": 30, "city": "New York"}
print(x)

print(x["name"])

print(len(x))

x["marks"] = 31
print(x)

x.pop("marks")
print(x)

'''
x.clear()
print(x)

'''
print(x.keys())
print(x.values())
print(x.items())
