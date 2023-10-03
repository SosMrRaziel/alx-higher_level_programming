str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
substring = "with"
index = str.find(substring)

if index != -1:
    print(f"The index of '{substring}' in the string is: {index}")
else:
    print(f"'{substring}' not found in the string.")