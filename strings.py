'''
name = "Python Tutorial"

print(name)
print(name[0])
print(name[-2])
print(name[0:2])
print(name[:2])
print(name[7:])


name1 = "Python"
name2 = "Tutorial"
name3 = 24
print(name1 + " " + name2 + " " + str(name3))

name = "Python Tutorial"

print("P" in name)
print("o" not in name)
print("rial" in name)


name = "python tutorial"

print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())  #first letter of the string is capitalized and the rest are in lowercase


name = "python tutorial"
print(name.find("l"))
print(name.find("th"))
print(name.find("z"))
print(name.find("t", 4))

print("------")
print(name.find("t"))
print(name.rfind("t"))

print("------")
print(name.index("t"))  #find() and index() are similar but index() raises an error if the substring is not found, while find() returns -1.
print(name.rindex("t"))


name = "python tutorial"

print(name.center(20))
print(name.center(20, "*"))
print(name.rjust(20))

name = "       python tutorial------"
print(name)
print(name.strip())
print(name.rstrip("-"))


name = "python tutorial"

print(name.startswith("py"))
print(name.startswith("th"))
print(name.startswith("th", 2))

print(name.endswith("al"))



name = "python tutorial"
print(name)
print(name.replace(" ", "_"))
print(name)


x = 'abc'
y = 'def'

print(x.join(y))
print(" ".join(y))

name = ["python", "tutorial", "is", "awesome"]
print(name)
print(" ".join(name))

'''

name = "python tutorial"
print(name.split())